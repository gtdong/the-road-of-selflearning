from utils.ansible2.runner import AdHocRunner, CommandRunner, PlayBookRunner
from utils.ansible2.inventory import Inventory

def ansible_adhoc_helper(hostlist,tasks):
    host_data=[{"hostname":h.hostip,"ip":h.hostip,"port":h.ssh_port} for h in hostlist]
    inventory = Inventory(host_data)  # 动态生成主机配置信息
    runner = AdHocRunner(inventory)
    ret = runner.run(tasks)
    return ret.results_raw
