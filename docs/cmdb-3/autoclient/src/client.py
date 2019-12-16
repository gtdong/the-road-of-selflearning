#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import requests
from lib.config.conf import settings
from src.plugins import PluginsManager
from concurrent.futures import ThreadPoolExecutor
import os

class Base():
    def postInfo(self,res):
        print('--------------------------')
        requests.post(settings.API_URL,json=res)


class Agent(Base):

    def collect(self):

        res = PluginsManager().execute()
        hostname = res['basic']['data']['hostname']
        info = open(os.path.join(settings.BASEDIR,'conf/cert'),'r',encoding='utf8').read()

        if not info.strip():
            with open(os.path.join(settings.BASEDIR,'conf/cert'),'w',encoding='utf8') as fp:
                fp.write(hostname)
        else:
            res['basic']['data']['hostname'] = info


        for k, v in res.items():
            print(k, v)

        self.postInfo(res)

class SSHSalt(Base):
    def get_hostnames(self):
        hostnames = requests.get(settings.API_URL)

        return hostnames

    def run(self,hostname):
        res = PluginsManager(hostname).execute()
        self.postInfo(res)



    def collect(self):
        hostnames = self.get_hostnames()


        ### 一台一台去执行 串行
        p = ThreadPoolExecutor(10)


        for hostname in hostnames:
            # res = PluginsManager(hostname).execute()
            # self.postInfo(res)
            p.submit(self.run,(hostname,))
