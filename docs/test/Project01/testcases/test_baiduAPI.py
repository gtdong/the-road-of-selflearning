import unittest
import requests
import json

from testdatas.conf_common import url_baiduAPI,url_baiduAPI,url_baiduAPI_http,http_header



class APITestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getsuccess(self):
        """
                验证get请求http协议成功
        """

        tmp_response = requests.get(url=url_baiduAPI,timeout=3)
        print(tmp_response.status_code)

        self.assertEqual(200,tmp_response.status_code)


    def test_getsuccesshttp(self):
        u"""验证get请求http协议成功
        """

        tmp_response = requests.get(url=url_baiduAPI_http,timeout=3)
        print(tmp_response.status_code)
        self.assertEqual(200,tmp_response.status_code)

    def test_isupper(self):
        u"""是不是空
        :return:
        """
        self.assertIsNotNone(None)

    def test01(self):
        u'''测试登录用例，账号：xx 密码xx'''
        print ("执行测试用例01")

    def test03(self):
        u'''测试登搜索用例，关键词：xxx'''
        print ("执行测试用例03")

    def testChinese(self):
        u'''验证None是不是空'''
        self.assertEqual("",None,"None 不是空")







