
### 1. 导入文件
from . import global_settings
from conf import settings

#### 集成自定制的配置和默认的配置
class Settings(object):
    def __init__(self):
        ### 集成全局配置
        for k in dir(global_settings):
            if k.isupper():
                v = getattr(global_settings, k)
                setattr(self, k, v)
        #### 集成自定制配置
        for k in dir(settings):
            if k.isupper():
                v = getattr(settings, k)
                setattr(self, k, v)
settings = Settings()





