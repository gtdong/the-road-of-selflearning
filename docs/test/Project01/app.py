
from testsuites import suiteday01




if __name__== '__main__':

    # 生成测试套件
    do_test =suiteday01.GenerateReport(suiteday01.MoudleTestSuite().suiteAPI())
    #  运行测试套件中的用例
    do_test.createreport()