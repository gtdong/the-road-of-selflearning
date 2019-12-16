from django import forms
from .models import Project,UserProfile
from utils.auth import NewModelform


class ProjectForm(NewModelform):

    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        self.fields["dev_user"].choices=[(du.pk,du.name) for du in UserProfile.objects.filter(role="0")]
        self.fields["test_user"].choices = [(tu.pk, tu.name) for tu in UserProfile.objects.filter(role="1")]
        self.fields["ops_user"].choices = [(ou.pk, ou.name) for ou in UserProfile.objects.filter(role="2")]


    class Meta:
        model = Project
        fields = "__all__"

