from django import forms
from .models import Cron
from utils.auth import NewModelform


class CronForm(NewModelform):

    # minute=forms.ChoiceField([(i,i) for i in range(60)],label="分钟")
    # hour=forms.ChoiceField([(i,i) for i in range(24)],label="小时")
    # day=forms.ChoiceField([(i,i) for i in range(1,32)],label="日")
    # month=forms.ChoiceField([(i,i) for i in range(1,13)],label="月")
    # weekday=forms.ChoiceField([(i,i) for i in range(1,8)],label="周")
    class Meta:
        model = Cron
        # fields=["minute","hour","day","month","weekday","name","hosts_list"]
        exclude=["create_user","time"]

