1  环境准备 unitest,httptestrunner,邮箱账号
2  运行方式: 
   用
   报告文件路径是在testdatas/conf_common里面配置的,
   默认是windows的,如果你的电脑操作系统是其他的需要把路径修改.
    例如  tmp_reports\\robert_report
    改成  tmp_reports/robert_report
3  报告模板怎么修改?
   1  在testsuites文件夹中,
    修改前 from lib.htmlreport import HTMLTestRunner
    修改后 from lib.htmlreport import HTMLTestRunnerEN as HTMLTestRunner