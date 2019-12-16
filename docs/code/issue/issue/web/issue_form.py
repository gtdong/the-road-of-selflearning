from django import forms
from .models import Issue
from utils.auth import NewModelform


class FileForm(NewModelform):

    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),label="文件")

    class Meta:
        model = Issue
        fields=["project","backup"]


class GitForm(NewModelform):

    class Meta:
        model = Issue
        fields=["project","backup"]

