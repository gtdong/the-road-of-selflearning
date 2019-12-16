import  unittest
from testcases import test_baiduAPI
from testdatas import  conf_common

# from lib.htmlreport import HTMLTestRunner
# from lib.htmlreport import HTMLTestRunnerOrigin as HTMLTestRunner
from lib.htmlreport import HTMLTestReportEN as HTMLTestRunner


class MoudleTestSuite():

    def __init__(self,suite=None):
        self.suite = suite

    def suiteAPI(self):
        '''
        suite carete method: loadTestsFromTestCase
        :return suite
        '''
        self.suite = unittest.TestLoader().loadTestsFromTestCase(test_baiduAPI.APITestCase)
        return self.suite


    def discoverysuiteAPI(self,filedir=None):
        '''
        suite carete method: discover
        :param filedir:
        :return:
        '''
        self.filedir = filedir
        self.suite = unittest.TestLoader.discover(self.filedir)





class GenerateReport():


    def __init__(self,suite):
        self.suite =suite


    def createreport(self) -> None:

        with (open(conf_common.reportobject["reportfilepath"], 'wb')) as fp:
            runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                verbosity= conf_common.reportobject["verbosity"],
                title=conf_common.reportobject["title"],
                description=conf_common.reportobject["description"]
            )

            runner.run(self.suite)

    def checkreport(self):
        '''
        校验已生成新的Html报告
        :return:
        '''
        pass


