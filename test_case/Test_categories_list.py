#coding=utf-8
import requests
import unittest


class Test_categories_list(unittest.TestCase):
    u'''专项列表页'''
    def setUp(self):
        self.base_url="http://www.yuantiku.com/iphone/gkyy/categories?deep=true&filter=smart&level=0"
        self.cookies=dict(cookies_are='Hm_lvt_75f573cdde0823f3daac2bac99f1eb2c=1417419666,1419232105; __utmt=1; __utma=57468450.1028443361.1417161200.1433480524.1433491187.41; __utmb=57468450.13.10.1433491187; __utmc=57468450; __utmz=57468450.1419319083.14.2.utmcsr=mail.fenbi.com|utmccn=(referral)|utmcmd=referral|utmcct=/cgi-bin/mail_spam; sid=7964259505720484889; sess="IkTf9cWhoioccschDsUG3OaoU7DsG4HXw0MwhEhn7egrkDCL3H58cRA1x2F0conmg+hGJc3VBQX7xqqr1mpwOA=="; userid=421; persistent="mWBB9cgSWXmTM5lCISWLj0YmiXpOzkINCyMYgYqm/qDZU3pXrM7C/nxfhmIoSa9aFsQwkKApMo7GI2Nss/JeRA=="')

    def test_check_status_code_and_json(self):
        u'''检查专项列表返回的status_code和json检验'''
        resp=requests.get(self.base_url,cookies=self.cookies)
        self.assertEqual(resp.status_code,200)
        self.assertIn('"id":40907',resp.content)



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()