__author__ = 'zengyue'
#coding=utf-8

import unittest
import requests
import json

class Test_Submit_exercise(unittest.TestCase):
    u'''提交试卷练习'''
    def setUp(self):
        self.base_url="http://www.yuantiku.com/iphone/gkyy/categories?deep=true&filter=smart&level=0"
        self.cookies=dict(cookies_are='Hm_lvt_75f573cdde0823f3daac2bac99f1eb2c=1417419666,1419232105; __utmt=1; __utma=57468450.1028443361.1417161200.1433480524.1433491187.41; __utmb=57468450.13.10.1433491187; __utmc=57468450; __utmz=57468450.1419319083.14.2.utmcsr=mail.fenbi.com|utmccn=(referral)|utmcmd=referral|utmcct=/cgi-bin/mail_spam; sid=7964259505720484889; sess="IkTf9cWhoioccschDsUG3OaoU7DsG4HXw0MwhEhn7egrkDCL3H58cRA1x2F0conmg+hGJc3VBQX7xqqr1mpwOA=="; userid=421; persistent="mWBB9cgSWXmTM5lCISWLj0YmiXpOzkINCyMYgYqm/qDZU3pXrM7C/nxfhmIoSa9aFsQwkKApMo7GI2Nss/JeRA=="')

    def test_check_status_code_and_json(self):
        u'''检查提交试卷后返回的status_code和json校验'''
        self.base_url="http://yuantiku.com/android/gkyw/exercises?paper"
        resp=requests.post(self.base_url,data={'paperId':'67799','type':'1'},cookies=self.cookies)
        s=resp.text[6:15]
        data={"userAnswers":{"0":{"answer":{"choice":"1","type":201},"flag":0,"questionId":1553709,"questionIndex":0,"time":5},"1":{"answer":{"choice":"1","type":201},"flag":0,"questionId":1553711,"questionIndex":1,"time":1},"2":{"answer":{"type":201},"flag":0,"questionId":1553719,"questionIndex":2,"time":3}}}
        data["id"] = int(s)
        data["treeId"] = 75
        data["status"] = 3
        self.base_url="http://yuantiku.com/android/gkyw/exercises/" + s + "/submit/incr"
        resp=requests.post(self.base_url,data=json.dumps(data),cookies=self.cookies)
        self.assertIn("2015年普通高等学校招生全国统一考试（广东卷）：语文",resp.content)

    def tearDown(self):
        self.cookies.clear()

if __name__ == '__main__':
    unittest.main()