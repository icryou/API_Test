#coding=utf-8
import requests
import unittest


class Test_categories_list(unittest.TestCase):
    u'''专项列表页'''
    def setUp(self):
        self.base_url="base_url"
        self.cookies=dict(cookies_are='cookies')

    def test_check_status_code_and_json(self):
        u'''检查专项列表返回的status_code和json检验'''
        resp=requests.get(self.base_url,cookies=self.cookies)
        self.assertEqual(resp.status_code,200)
        self.assertIn('"id":40907',resp.content)



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
