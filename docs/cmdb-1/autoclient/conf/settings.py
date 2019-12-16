### 自定制配置
import  os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODE = 'agent' ## agent/ssh/salt

SSH_USER = 'root'
SSH_PORT = 22
SSH_PWD  = 'dsadsa'
SSH_HOSTNAME = 'c1.com'

DEBUG = True

PLUGINS_DICT = {
    "basic" : 'src.plugins.basic.Basic',
    "disk" : 'src.plugins.disk.Disk',
    "memory" : 'src.plugins.memory.Memory',
    "nic" : 'src.plugins.nic.Nic',
    "cpu" : 'src.plugins.cpu.Cpu',
    "board" : 'src.plugins.board.Board',
}

API_URL = 'http://127.0.0.1:8000/api/'

