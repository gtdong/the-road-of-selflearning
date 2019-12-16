import json
import requests
from lib.config.conf import settings
from src.plugins import PluginsManager

class Base():
    def postInfo(self, res):
        # requests.post(settings.API_URL, data=json.dumps(res))
        requests.post(settings.API_URL, json=res)


class Agent(Base):

    def collect(self):
        res = PluginsManager().execute()
        for k, v in res.items():
            print(k, v)

        self.postInfo(res)

class SSHSalt(Base):
    def get_hostnames(self):
        hostnames = requests.get(settings.API_URL)

        return hostnames

    def collect(self):
        hostnames = self.get_hostnames()
        for hostname in hostnames:
            res = PluginsManager(hostname).execute()
            self.postInfo(res)


