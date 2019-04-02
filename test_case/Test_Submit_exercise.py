__author__ = 'zengyue'
#coding=utf-8

import unittest
import requests
import json

class Test_Submit_exercise(unittest.TestCase):
    u'''提交试卷练习'''
    def setUp(self):
        self.base_url="base_url"
        self.cookies=dict(cookies_are='cookies')

    def test_check_status_code_and_json(self):
        u'''检查提交试卷后返回的status_code和json校验'''
        self.base_url="base_url"
        resp=requests.post(self.base_url,data={'paperId':'67799','type':'1'},cookies=self.cookies)
        s=resp.text[6:15]
        data={"userAnswers":{"0":{"answer":{"choice":"1","type":1233242},"flag":0,"questionId":3426234531245,"questionIndex":0,"time":5},"1":{"answer":{"choice":"1","type":201},"flag":0,"questionId":1553711,"questionIndex":1,"time":1},"2":{"answer":{"type":201},"flag":0,"questionId":155371324234129,"questionIndex":2,"time":3}}}
        data["id"] = int(s)
        data["treeId"] = 75
        data["status"] = 3
        self.base_url="base_url"
        resp=requests.post(self.base_url,data=json.dumps(data),cookies=self.cookies)
        self.assertIn("2015年普通高等学校招生全国统一考试（广东卷）：语文",resp.content)

    def tearDown(self):
        self.cookies.clear()

if __name__ == '__main__':
    unittest.main()
