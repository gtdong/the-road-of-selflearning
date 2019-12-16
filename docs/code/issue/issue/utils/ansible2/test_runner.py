# coding: utf-8

from utils.ansible2.runner import AdHocRunner, CommandRunner, PlayBookRunner
from utils.ansible2.inventory import Inventory


def TestAdHocRunner():
    """
     以yml的形式 执行多个命令
    :return:
    """
    host_data = [
        {
            "hostname": "10.0.0.143",
            "ip": "10.0.0.143",
            "port": 22
        },
    ] #主机列表
    inventory = Inventory(host_data) #动态生成主机配置信息
    runner = AdHocRunner(inventory)
    # dest = "/opt/mysql/world.sh"

    tasks = [
        # {"action": {"module": "ping"}, "name": "run_whoami"},
        {"action": {"module": "replace", "args": 'path=/tmp/a.txt regexp="^(ac.*)" replace="#\\1"'},
         "name": "down nginx"}
        # {"action": {"module": "shell", "args": "free -m | awk 'NR\=\=2{printf \"%.2f\", $3*100/$2 }'"}, "name": "get_mem_usage"},
        # {"action": {"module": "shell", "args": "df -h | awk '$NF\=\=\"/\"{printf \"%s\", $5}'"}, "name": "get_disk_usage"},
        # {"action": {"module": "copy", "args": "src=/home/python/Desktop/3358.cnf dest=/opt/mysql/my3358.cnf mode=0777"}, "name": "send_file"},
        # {"action": {"module": "copy", "args": "src=/home/python/Desktop/deploy.sh dest=/opt/mysql/deploy.sh mode=0777"}, "name": "send_file"},
        # {"action": {"module": "command", "args": "sh /opt/mysql/hello.sh"}, "name": "execute_file"},
        # {"action": {"module": "shell", "args": "sudo sh /opt/mysql/deploy.sh"}, "name": "execute_file"},
        # {"action": {"module": "lineinfile", "args": "dest=/opt/mysql/hello.sh line=hello1 regexp=echo state=present"}, "name": "modify_file"},
        # {"action": {"module": "lineinfile", "args": "dest=/opt/mysql/world.sh line="" regexp=echo state=present"}, "name": "modify_file"},
        # {"action": {"module": "lineinfile", "args": "dest=%s line=sun regexp=echo state=present" % dest}, "name": "modify_file"},
        # {"action": {"module": "shell", "args": "lineinfile dest=/opt/mysql/hello.sh regexp=hello insertafter=#echo line=hello world"}, "name": "modify_file"},

        # {"action": {"module": "shell", "args": "grep 'cpu ' /proc/stat | awk '{usage\=($2+$4)*100/($2+$4+$5)} END {print usage}'"}, "name": "get_cpu_usage"},
    ]
    ret = runner.run(tasks)
    print(ret.results_summary)
    print(ret.results_raw)


def TestCommandRunner():
    """
    执行单个命令，返回结果
    :return:
    """

    host_data = [
        {
            "hostname": "10.211.55.19", #key值
            "ip": "10.211.55.19",
            "port": 22,
            "username": "root",
        },
    ]
    inventory = Inventory(host_data)  #重新组成虚拟组
    runner = CommandRunner(inventory)

    res = runner.execute('pwd')
    # print(res.results_command)
    print(res.results_raw,type(res.results_raw))
    # res.results_raw



def TestPlayBookRunner():
    """
    执行playbook
    :return:
    """
    host_data = [
        {
            "hostname": "10.211.55.19",
            "ip": "10.211.55.19",
            "port": 22,
            "username": "root",
        },
    ]
    inventory = Inventory(host_data)
    runner = PlayBookRunner(inventory).run("/Users/derekwang/test")
    print(runner)


if __name__ == "__main__":
    # TestAdHocRunner()
    TestCommandRunner()
    # TestPlayBookRunner()
