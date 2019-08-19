import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day20.settings")
    import django
    django.setup()
    from app01 import models
    # book_obj = models.BookList.objects.create(title='三国演义',price=123.23,publish_date='2019-01-01')
    # import datetime
    # ctime = datetime.date.today()
    # book_obj = models.BookList.objects.create(title='红楼梦',price=1666.23,publish_date=ctime)
    # print(book_obj)

    # models.BookList.objects.filter(title='三国演义').update(price=1123.23)
    """
    queryset的方法都是批量更新操作
    """
    # print(models.BookList.objects.all())
    # print(models.BookList.objects.filter(pk=2))  # 推荐使用filter
    # print(models.BookList.objects.get(pk=2))  # get获取到的就是数据对象本身 但是当条件不满足的时候 会直接报错  不推荐使用

    # models.BookList.objects.filter(pk=1).delete()


    # 更多查询方法
    #  exclude(**kwargs): 它包含了与所给筛选条件不匹配的对象
    # print(models.BookList.objects.exclude(pk=1))  # 取反

    # values(*field): 返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列
    # print(models.BookList.objects.values('title','price'))
    # values返回的是列表套字典

    # values_list
    # print(models.BookList.objects.values_list('title','price'))
    # 返回的是列表套元组

    # order_by(*field): 对查询结果排序
    # print(models.BookList.objects.order_by('price'))  # 默认是升序
    # print(models.BookList.objects.order_by('price').reverse())  # 降序

    # distinct(): 从返回结果中剔除重复纪录(如果你查询跨越多个表，可能在计算QuerySet时得到重复的结果。此时可以使用distinct()，注意只有在PostgreSQL中支持按字段去重。)
    """
    去重的前提是 数据必须是一模一样的 
    """
    # print(models.BookList.objects.filter(title='三国演义').values('title','price').distinct())

    # count(): 返回数据库中匹配查询(QuerySet)的对象数量。
    # print(models.BookList.objects.all().count())


    # exists(): 如果QuerySet包含数据，就返回True，否则返回False
    # print(models.BookList.objects.filter(pk=1).exists())


    # 神奇的双下划线查询
    # 查询价格大于2000的
    # print(models.BookList.objects.filter(price__gt=2000))
    # print(models.BookList.objects.filter(price__gte=2000))
    # 查询价格小于2000的
    # print(models.BookList.objects.filter(price__lt=2000))
    # print(models.BookList.objects.filter(price__lte=2000))

    # 价格在1000到2000之间的
    # print(models.BookList.objects.filter(price__range=[999,2000]))  # 两边都包含

    # 查询主键在指定的条件内
    # print(models.BookList.objects.filter(pk__in=[1,3]))


    """
    ORM多表操作
    """
    # 外键字段的增删改查
    # models.Book.objects.create(title='三国演义',price='123.23',publish_id=1)
    # publish_obj = models.Publish.objects.filter(pk=2).first()
    # models.Book.objects.create(title='西游记',price='122.23',publish=publish_obj)

    # models.Book.objects.filter(pk=1).update(publish_id=2)
    # publish_obj = models.Publish.objects.filter(pk=1).first()
    # models.Book.objects.filter(pk=1).update(publish=publish_obj)


    # book_obj = models.Book.objects.filter(pk=1).first()
    # # book_obj.authors.add(1)  # 在第三张表中 添加书籍和作者的关系
    # # book_obj.authors.add(1,2)  # 在第三张表中 添加书籍和作者的关系
    # author_obj1 = models.Author.objects.filter(pk=1).first()
    # author_obj2 = models.Author.objects.filter(pk=2).first()
    # book_obj.authors.add(author_obj1,author_obj2)
    """
    add即支持传数字 并且也支持传对象
    两者都可以是多个
    """

    # 改
    # book_obj = models.Book.objects.filter(pk=1).first()
    # book_obj.authors.set([2,])  # 修改
    """
       set即支持传数字 并且也支持传对象
       两者都可以是多个
       但是需要注意的是 传入的格式必须是可迭代对象
    """

    # 删
    # book_obj = models.Book.objects.filter(pk=1).first()
    # book_obj.authors.remove(2)
    """
       remove即支持传数字 并且也支持传对象
       两者都可以是多个
    """

    # 清空
    # book_obj = models.Book.objects.filter(pk=1).first()
    # book_obj.authors.clear()  # 清空当前数据所有的关联信息
    """
    clear括号内不需要传任何参数
    """

    """
    ORM跨表查询
    """
    # 基于对象的跨表查询
    """
    # 正向与反向的概念解释
        正向查询按字段
        反向查询按表名小写...
        
        # 一对一
        # 正向：author---关联字段在author表里--->authordetail		按字段
        # 反向：authordetail---关联字段在author表里--->author		按表名小写
            # 查询jason作者的手机号   正向查询
            # 查询地址是 :山东 的作者名字   反向查询
          
        # 一对多
        # 正向：book---关联字段在book表里--->publish		按字段
        # 反向：publish---关联字段在book表里--->book		按表名小写_set.all() 因为一个出版社对应着多个图书
        
        # 多对多
        # 正向：book---关联字段在book表里--->author		按字段
        # 反向：author---关联字段在book表里--->book		按表名小写_set.all() 因为一个作者对应着多个图书
    
    """

    """基于对象的跨表查询   子查询"""
    # 查询书籍id为1的出版社名称
    # book_obj = models.Book.objects.filter(pk=1).first()
    # print(book_obj.publish.name)
    # 查询出版社是南方出版社出版过的书的名字
    # publish_obj = models.Publish.objects.filter(name='南方出版社').first()
    # # print(publish_obj.book_set)  # app01.Book.None
    # print(publish_obj.book_set.all())

    # 查询作者是jason的手机号
    # author_obj = models.Author.objects.filter(name='jason').first()
    # print(author_obj.author_detail.phone)
    # 查询手机号是110的作者姓名
    # author_detail_obj = models.AuthorDetail.objects.filter(phone=110).first()
    # print(author_detail_obj.author.name)

    # 查询书籍id为1 的作者姓名
    # book_obj = models.Book.objects.filter(pk=1).first()
    # # print(book_obj.authors)  # app01.Author.None
    # print(book_obj.authors.all())  # app01.Author.None
    # 查询作者id为1的写过的书籍
    # author_obj = models.Author.objects.filter(pk=1).first()
    # print(author_obj.book_set)  # app01.Book.None
    # print(author_obj.book_set.all())

"""
反向
一对多和多对多反向的时候 都需要加_set.all()
一对一反向的时候  只需要写表名小写即可

正向
当正向查询的结果是多个的情况下 需要加all
否则直接点字段即可


ps:写orm语句的时候 不要一步到位
写一点运行一点看看
"""












