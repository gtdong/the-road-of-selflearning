from django import forms
from .models import Init
from utils.auth import NewModelform


class InitForm(NewModelform):
    class Meta:
        model = Init
        exclude=["create_user"]
