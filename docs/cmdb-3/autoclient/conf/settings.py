#!/usr/bin/env python3
# -*- coding: utf-8 -*-
### 自定义配置

import os
BASEDIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASEDIR =
MODE = 'agent'  #agent/ssh/salt
SSH_USER = 'root'
SSH_PORT = 22
SSH_PWD = '123456'
SSH_HOSTNAME = '192.168.200.139'
DEBUG = True

PLUGINS_DICT = {
    "basic": 'src.plugins.basic.Basic',
    "disk": 'src.plugins.disk.Disk',
    "memory": 'src.plugins.memory.Memory',
    "nic": 'src.plugins.nic.Nic',
    "cpu": 'src.plugins.cpu.Cpu',
    "board": 'src.plugins.board.Board',
}
API_URL = 'http://127.0.0.1:8000/api/asset/'