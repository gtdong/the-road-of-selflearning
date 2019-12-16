from django import forms
from .models import InitLog
from utils.auth import NewModelform


class InitLogForm(NewModelform):
    class Meta:
        model = InitLog
        fields=["init","hosts_list"]
