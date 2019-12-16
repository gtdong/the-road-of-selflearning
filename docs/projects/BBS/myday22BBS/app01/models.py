from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    phone = models.BigIntegerField(null=True,blank=True)  # 告诉django admin该字段可以为空
    # auto_now_add 创建时自动添加当前时间
    create_time = models.DateField(auto_now_add=True)
    # upload_to需要传一个路径
    # default 默认头像的路径
    avatar = models.FileField(upload_to='avatar/', default='avatar/default.png')
    # 跟Blog表一对一
    blog = models.OneToOneField(to='Blog',null=True)

    class Meta:
        verbose_name_plural = '用户表'
        # verbose_name = '用户表'


    def __str__(self):
        return self.username

class Blog(models.Model):
    site_name = models.CharField(max_length=32)
    site_title = models.CharField(max_length=64)
    # 存css文件的路径
    theme = models.CharField(max_length=32)

    def __str__(self):
        return self.site_name  # 返回的是字符串类型


class Category(models.Model):
    name = models.CharField(max_length=32)
    blog = models.ForeignKey(to='Blog')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)
    blog = models.ForeignKey(to='Blog')
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    # 存大文本
    content = models.TextField()
    create_time = models.DateField(default='2019-01-01')
    # 跟站点表一对多
    blog = models.ForeignKey(to='Blog',null=True)
    # 跟分类一对多
    category = models.ForeignKey(to='Category',null=True)
    # 跟标签多对多,手动创建第三张表
    tag = models.ManyToManyField(to='Tag', through='Article2Tag', through_fields=('article', 'tag'))


    up_num = models.IntegerField(default=0)
    down_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class Article2Tag(models.Model):
    article = models.ForeignKey(to='Article')
    tag = models.ForeignKey(to='Tag')




class UpAndDown(models.Model):
    user = models.ForeignKey(to='UserInfo')
    article = models.ForeignKey(to='Article')
    is_up = models.BooleanField()


class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo')
    article = models.ForeignKey(to='Article')
    content = models.CharField(max_length=255)
    # 评论时间
    create_time=models.DateTimeField(auto_now_add=True)
    # parent =models.ForeignKey(to='Comment',to_field='nid')
    # 自关联,存父评论id
    parent = models.ForeignKey(to='self',null=True)
    # parent =models.IntegerField()
