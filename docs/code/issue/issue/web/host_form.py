from django import forms
from .models import Host
from utils.auth import NewModelform


class HostForm(NewModelform):
    class Meta:
        model = Host
        fields = "__all__"

    def clean_hostip(self):
        hostip = self.cleaned_data['hostip']
        host = Host.objects.filter(hostip=hostip)
        if host.count() == 0:  # 查不到值
            return hostip
        elif host.count() == 1 and hostip == self.instance.hostip:  # 查到了1条记录，并且邮箱没有改变
            return hostip
        else:
            raise forms.ValidationError("ip地址已存在")
