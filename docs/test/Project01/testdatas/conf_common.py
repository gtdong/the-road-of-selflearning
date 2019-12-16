import time
url_baiduAPI="https://www.baidu.com/"
url_baiduAPI_http="http://www.baidu.com/"

url_luffyAPI="http://www.luffy.com"


http_header ={
    "User-Agent:":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}




now_time = time.strftime("%Y-%m-%d %H_%M_%S")

# 测试报告存放的位置
reportobject = {
    "title" :"测试学科--测试开发 ",
    "verbosity":3,  # 日志打印详细级别  数值越高越详细，默认是1  [1,2,3]
    "description" : '这是unittest综合实战',
    "reportfilepath": ('tmp_reports\\robert_report' + now_time + '.html')
}

