#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import importlib
from lib.config.conf import settings
import importlib
import traceback
class PluginsManager():
    '''
    读取配置文件中的配置
    '''
    def __init__(self,hostname=None):
        self.plugins_dict = settings.PLUGINS_DICT
        self.mode = settings.MODE
        self.hostname = hostname
        self.debug = settings.DEBUG
        if self.mode == 'ssh':
            self.ssh_hostname = settings.SSH_HOSTNAME
            self.ssh_port = settings.SSH_PORT
            self.ssh_user = settings.SSH_USER
            # self.ssh_hostname = settings.SSH_HOSTNAME
            self.ssh_pwd = settings.SSH_PWD

    def execute(self):
        response = {}
        for k,v in self.plugins_dict.items():
            ret = {"status":None,"data":None}
            try:
                module_path, cls_name = v.rsplit('.',1)
                module = importlib.import_module(module_path)
                cls = getattr(module,cls_name)
                res = cls().process(self.cmd_run,self.debug)
                ret['status'] = 10000
                ret['data'] = res
            except Exception as e:
                ret['status'] = 10001
                ret['data'] = "%s 采集 %s 出错， 错误信息是：%s" % (self.hostname if self.hostname else 'agent',k,traceback.format_exc())
            response[k] = ret
        return response

    def cmd_run(self,cmd):
        if self.mode == 'agent':
            import subprocess
            res = subprocess.getoutput(cmd)
            ipinfo = res[1:3]
            print(ipinfo)
        elif self.mode == 'ssh':
            import paramiko
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.ssh_hostname,port=self.ssh_port,username=self.ssh_user,password=self.ssh_pwd)
            stdin,stdout,stderr = ssh.exec_command(cmd)
            result = stdout.read()
            # print(result)
            ssh.close()
            return result
        elif self.mode == 'salt':
            import subprocess
            cmd = "salt '%s' cmd.run '%s'" % (self.hostname,cmd)
            res = subprocess.getoutput(cmd)
            return res
        else:
            raise ('只支持agent/ssh/salt三种模式')