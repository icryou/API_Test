__author__ = 'zengyue'
#coding=utf-8

import unittest
import requests

class Test_Modify_nickname(unittest.TestCase):
    u'''修改昵称'''
    def setUp(self):
        self.base_url="base_url"
        self.cookies=dict(cookies_are='cookies')

    def test_check_nickname(self):
        u'''验证修改后的nickname返回是否正确'''
        self.base_url="base_url"
        resp=requests.post(self.base_url,data={"nickname":"helloer"},cookies=self.cookies)
        self.assertEqual(resp.status_code,200)
        self.assertIn("helloer",resp.content)


    def tearDown(self):
        self.cookies.clear()

if __name__ == '__main__':
    unittest.main()
