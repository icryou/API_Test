__author__ = 'zengyue'
#coding=utf-8

import unittest
import requests

class Test_Modify_nickname(unittest.TestCase):
    u'''修改昵称'''
    def setUp(self):
        self.base_url="http://www.yuantiku.com/iphone/gkyy/categories?deep=true&filter=smart&level=0"
        self.cookies=dict(cookies_are='Hm_lvt_75f573cdde0823f3daac2bac99f1eb2c=1417419666,1419232105; __utmt=1; __utma=57468450.1028443361.1417161200.1433480524.1433491187.41; __utmb=57468450.13.10.1433491187; __utmc=57468450; __utmz=57468450.1419319083.14.2.utmcsr=mail.fenbi.com|utmccn=(referral)|utmcmd=referral|utmcct=/cgi-bin/mail_spam; sid=7964259505720484889; sess="IkTf9cWhoioccschDsUG3OaoU7DsG4HXw0MwhEhn7egrkDCL3H58cRA1x2F0conmg+hGJc3VBQX7xqqr1mpwOA=="; userid=421; persistent="mWBB9cgSWXmTM5lCISWLj0YmiXpOzkINCyMYgYqm/qDZU3pXrM7C/nxfhmIoSa9aFsQwkKApMo7GI2Nss/JeRA=="')

    def test_check_nickname(self):
        u'''验证修改后的nickname返回是否正确'''
        self.base_url="http://www.yuantiku.com/iphone/chuzhong/users/info/settings"
        resp=requests.post(self.base_url,data={"nickname":"helloer"},cookies=self.cookies)
        self.assertEqual(resp.status_code,200)
        self.assertIn("helloer",resp.content)


    def tearDown(self):
        self.cookies.clear()

if __name__ == '__main__':
    unittest.main()
