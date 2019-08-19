from django.db import models

# Create your models here.
class BookList(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)  # 总共八位 小数占两位
    publish_date = models.DateField()

    def __str__(self):
        return self.title


"""
一对多 外键字段 通常建在多的那一方
多对多 外键字段 无论建在哪一方都可以  但是推荐你建在查询频率较高的一方
一对一 外键字段 无论建在哪一方都可以  但是推荐你建在查询频率较高的一方
"""
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    publish_date = models.DateField(auto_now_add=True)
    # 出版社外键
    publish = models.ForeignKey(to='Publish')  # 默认关联的就是Publish表的主键字段
    """
    一对多外键字段 在书写的时候 orm会自动加_id后缀
    所以 你不要加_id了
    """
    # 作者外键
    authors = models.ManyToManyField(to='Author')  # 默认关联的就是Author表的主键字段
    """多对多字段是虚拟字段 不会在表中展示出来
        只是用来告诉django orm自动创建书籍和作者的第三张表
        还可以跨表的查询的提供方便
    """

class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    addr = models.CharField(max_length=32)

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=32)
    # 一对一
    """
     一对一外键字段 在书写的时候 orm会自动加_id后缀
    所以 你不要加_id了
    """
    author_detail = models.OneToOneField(to='AuthorDetail')

class AuthorDetail(models.Model):
    phone = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
