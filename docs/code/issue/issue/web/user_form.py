from django import forms
from .models import UserProfile
from utils.auth import NewModelform


class UserForm(NewModelform):
    class Meta:
        model = UserProfile
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data['email']
        print(email) #前端的值
        print(self.instance.email) #数据库的值
        user = UserProfile.objects.filter(email=email)
        if user.count() == 0:  # 查不到值
            return email
        elif user.count() == 1 and email == self.instance.email:  # 查到了1条记录，并且邮箱没有改变
            return email
        else:
            raise forms.ValidationError("邮箱已存在")
