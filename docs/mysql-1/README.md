# 今日内容：
&#160; &#160; &#160; &#160;数据库 MySQL
	

## 一. 数据库的介绍
&#160; &#160; &#160; &#160;数据库，简而言之可视为电子化的文件柜——存储电子文件的处所，用户可以对文件中的数据运行新增、截取、更新、删除等操作。
所谓“数据库”系以一定方式储存在一起、能予多个用户共享、具有尽可能小的冗余度、与应用程序彼此独立的数据集合。一个数据库由
多个表空间（Tablespace）构成。  
&#160; &#160; &#160; &#160;[维基百科定义](https://zh.wikipedia.org/wiki/%E6%95%B0%E6%8D%AE%E5%BA%93)
## 二. 数据库的分类
&#160; &#160; &#160; &#160;目前我们常用的数据库分为关系型数据库和非关系型数据库  
### a. 关系型数据库  
&#160; &#160; &#160; &#160;指采用了关系模型来组织数据的数据库。关系模型指的就是二维表格模型，而一个关系型数据库就是由二维表及其之
间的联系所组成的一个数据组织。 
关系模型中常用的概念：  
&#160; &#160; &#160; &#160;**关系:** 一张二维表，每个关系都具有一个关系名，也就是表名  
&#160; &#160; &#160; &#160;**元组:** 二维表中的一行，在数据库中被称为记录  
&#160; &#160; &#160; &#160;**属性：** 二维表中的一列，在数据库中被称为字段  
&#160; &#160; &#160; &#160;**域：** 属性的取值范围，也就是数据库中某一列的取值限制  
&#160; &#160; &#160; &#160;**关键字：** 一组可以唯一标识元组的属性，数据库中常称为主键，由一个或多个列组成  
&#160; &#160; &#160; &#160;**关系模式：** 指对关系的描述。其格式为：关系名(属性1，属性2， ... ... ，属性N)，在数据库中成为表结构  
&#160; &#160; &#160; &#160;当今十大主流的关系型数据库：Oracle，Microsoft SQL Server，MySQL，PostgreSQL，DB2，icrosoft Access， SQLite，Teradata，MariaDB(MySQL的一个分支)，SAP
### b. 非关系型数据库  
&#160; &#160; &#160; &#160;非关系型数据库都是针对某些特定的应用需求出现的，因此，对于该类应用，具有极高的性能。依据结构化方法以及应用场合的
不同，主要分为以下几类：  

**面向高性能并发读写的key-value数据库:**  
&#160; &#160; &#160; &#160;key-value数据库的主要特点是具有极高的并发读写性能  
Key-value数据库是一种以键值对存储数据的一种数据库，类似Java中的map。可以将整个数据库理解为一个大的map，
每个键都会对应一个唯一的值。  
&#160; &#160; &#160; &#160;主流代表为： Redis， Amazon DynamoDB， Memcached，Microsoft Azure Cosmos DB和Hazelcast  

**面向海量数据访问的面向文档数据库：**  
&#160; &#160; &#160; &#160;这类数据库的主要特点是在海量的数据中可以快速的查询数据文档存储通常使用内部表示法，可以直接在应用程序中处理，
主要是JSON。JSON文档也可以作为纯文本存储在键值存储或关系数据库系统中。
主流代表为MongoDB，Amazon DynamoDB，Couchbase，Microsoft Azure Cosmos DB和CouchDB  

**面向搜索数据内容的搜索引擎：**  
&#160; &#160; &#160; &#160;搜索引擎是专门用于搜索数据内容的NoSQL数据库管理系统。主要是用于对海量数据进行近实时的处理和分析处理，可用
于机器学习和数据挖掘主流代表为Elasticsearch，Splunk，Solr，MarkLogic和Sphinx  

**面向可扩展性的分布式数据库:**  
&#160; &#160; &#160; &#160;这类数据库的主要特点是具有很强的可拓展性普通的关系型数据库都是以行为单位来存储数据的，擅长以行为单位的读入
处理，比如特定条件数据的获取。因此，关系型数据库也被成为面向行的数据库。相反，面向列的数据库是以列为单位来存储数
据的，擅长以列为单位读入数据。这类数据库想解决的问题就是传统数据库存在可扩展性上的缺陷，这类数据库可以适应数据量
的增加以及数据结构的变化，将数据存储在记录中，能够容纳大量动态列。由于列名和记录键不是固定的，并且由于记录可能有
数十亿列，因此可扩展性存储可以看作是二维键值存储。  
&#160; &#160; &#160; &#160;主流代表为：Cassandra，HBase，Microsoft Azure Cosmos DB，Datastax Enterprise和Accumulo
### c.关系型与非关系型数据库的比较:
**1.成本：** Nosql数据库简单易部署，基本都是开源软件，不需要像使用Oracle那样花费大量成本购买使用，相比关系型数据库
价格便宜。  
**2.查询速度：** Nosql数据库将数据存储于缓存之中，而且不需要经过SQL层的解析，关系型数据库将数据存储在硬盘中，自然查
询速度远不及Nosql数据库。  
**3.存储数据的格式：** Nosql的存储格式是key,value形式、文档形式、图片形式等等，所以可以存储基础类型以及对象或者是
集合等各种格式，而数据库则只支持基础类型。  
**4.扩展性：** 关系型数据库有类似join这样的多表查询机制的限制导致扩展很艰难。Nosql基于键值对，数据之间没有耦合性，
所以非常容易水平扩展。  
**5.持久存储：** Nosql不使用于持久存储，海量数据的持久存储，还是需要关系型数据库  
**6.数据一致性：** 非关系型数据库一般强调的是数据最终一致性，不像关系型数据库一样强调数据的强一致性，从非关系型数据库
中读到的有可能还是处于一个中间态的数据，Nosql不提供对事务的处理  
参考：https://www.jianshu.com/p/fd7b422d5f93
	
## 三. MySQL数据库
	
### a. 架构
* MySQL服务端：socketserver服务端，接收来自客户端的指令， 执行， 然后将结果返回
    
* MySQL客户端：socket client客户端，发送指令到服务端
### b. 安装：
```shell
http://dev.mysql.com/downloads/mysql/

1.zip：
压缩包 （MySQL的客户端和服务端已经开发好， 然后打包给你）

2.exe文件或者msi文件：
点点点 （下一步）

3.目录结构：
bin : 
    MySQLd : 启动MySQL服务端的
    MySQL  : 连接服务端
data: 
    存放数据文件

4.具体的安装：
mac：
    brew install mysql	

windows:
    a.解压

    b.进入到bin

    c.mysqld  (默认一个用户名root)

    d.mysql -uroot -p 直接回车 再回车

    e：mysql>输入指令

环境变量：
    右键计算机】--》【属性】--》【高级系统设置】--》【高级】--》【环境变量】--》
    【在第二个内容框中找到 变量名为Path 的一行，双击】 --> 添加
    
```
### c. mysql的操作:
```shell 
操作文件夹（数据库）：
操作文件（数据表）：
    数据行（具体的一行数据）
    数据行
    数据行

大量的SQL指令（语句）
```
#### 数据库
```shell
增:
	语句：
	    create database 数据库名;
	例子：
	    create database db1;
删:
	drop database （数据库名）db2;
改:
	删掉数据库， 然后新建
查:
	列出当前数据库下面的所有数据库：show databases;

使用数据库：
	use 数据库名(db2);
```
#### 数据表
```shell

    查看建表语句：
	show create table 表名(t3);  ====> 建表过程显示

    查看表中列的详细信息：
	desc 表名(t3);

    查看数据：
	select * from 表名(t1);

增:

	语句：
		create table 表名 (
		    列1 列属性 [是否为null 默认值],
		    列2 列属性 [是否为null 默认值],
		    .....
		    列n 列属性 [是否为null 默认值]
		)engine = 存储引擎  charset = 字符集
		
	例子：	
		create table t4(
		    id  int auto_increment primary key,
		    id  unsigned int auto_increment primary key,
		    name char(32) not null default '',
		    create_time datetime not null default '1970-01-01 00:00:00'
		)engine=Innodb charset=utf8;

		auto_increment: 自增 要和primary key 一起使用
		null : 默认是是null值
		not null ： 不能为null
		default : 指定默认值
		最后一列语句不能加逗号

	ps:
	存储引擎：
		MyIsam （5.5以下）  和 Innodb（5.5以上）

    列类型：
		数字类型：
			tinyint
			smallint
			mediumint
			int
			bigint

			区别：
				1.范围不一样
				2.有符号
				
				  无符号
				  unsigned

	    	场景：
				看公司的业务需求


		字符串类型：

			char(32) : 最长的长度是32，  定长  hello（5）注意剩下的27个就浪费了  效率高
			varchar(32) : 最长不能超过32  变长 hello (5) 算一下存的值的长度，但是剩下的27个字符不会浪费

			场景：	
				存的值都是一个固定长度， char(32)
				不能确定存的值是多长， 此时用一个varchar()存储

			user：
				id    username(varchar(128))    pwd（ char(32)）

			text : 文本 可以存一篇文章


		时间日期类型：

	   		datetime ：时间日期类型  （2019-06-13 15:30:56）

删:
	drop database （数据库名）db2;
改:
	删掉数据库， 然后新建
查:
	列出当前数据库下面的所有数据库：show databases;

使用数据库：
	use 数据库名(db2);
```
#### 数据行：

```shell
增
	指令：	
		insert into 表名(列1，列2，...., 列n) values (‘值1’, '值2'， ..., '值n');
	实例：

		#添加一行数据：
		insert into t3 (name, age)values('zekai', 12);

		#添加多行数据：
		insert into t3 (username, age)values('zekai', 12), ('eagon', 78), ('lxxx', 83);
		#将别的表中的数据添加到表中：
		insert into t4 (name, age) select usernme,  age from t3;	
删
	指令：	
		delete from 表名(t2);  ### 再次插入数据的时候， id是从上一次主键id开始的
		truncate t4;  ### 删除数据， 然后再次插入数据的时候， id从1开始
		delete from t2 where id=10;

改
	指令：	
		update 表名 set name='xxxx';
	语句：	
		update t4 set name='kkkk',age=12,gender='女' where id=2;
		update t4 set name='kkkk' where id>2;
		update t4 set name='kkkk' where id<2;
		update t4 set name='kkkk' where id<=2;
		update t4 set name='kkkk' where id>=2;
		update t4 set name='kkkk' where id!=2;

查
	指令：	
		select * from t3; ### 将所有的列的值全部显示
		select 列名1, 列名2.... from t3;

	where条件：

		select * from t3 where id=12;
		select * from t3 where id>12;
		select * from t3 where id>=12;
		select * from t3 where id<12;
		select * from t3 where id<=12;
		select * from t3 where id!=12;

		select * from t4 where id > 13 and id < 30; 

		select * from t4 where id > 13 or name='mmmm'; 

		between ... and : 在某一个范围之内（闭区间）

		select * from t4 where id between 13 and 30;
		in：
		select * from t4 where id in (16,20,30);
		not in:
		select * from t4 where id not in (16,20,30);

	通配符匹配：

		select * from t4 where name like 'j%';  %： 匹配字符串后面所有的字符
		select * from t4 where name like 'j_';  _:  只匹配一个字符 

	限制取几条：

		select * from t4 limit 索引偏移量，取多少条

		select * from t4 limit 0, 10;

		page      索引偏移量      取多少条(offset)   
		  1          0               10
		  2          10              10
		  3          20              10
		  ......

		  n          (n-1)*offset   offset

		分页的SQL语句：(****************)

		page = input('please input page num:')
		offset = 20

		select * from t4 limit (page-1)*offset, offset;


	排序：
		从大到小 ： 降序

		从小到大 ： 升序

		order by 列名 desc/asc

		select * from t4 order by age desc, id asc; ### 首先按照age进行降序， 如果age相同的话，再按照id进行升序排列

	分组：

		group by 列名

		聚合函数：
		count(): 计数
		sum()  : 求和
		max()  : 最大值
		min()  : 最小值
		avg()  : 平均值

		例子：	
		select age, count(age) from t4 group by age;
		select age, sum(age) from t4 group by age;

		having：

		select age, count(id) as cnt from t4 group by age having cnt>=2;

		对分组完之后的结果进行二次删选

		和where条件的区别;
		where 对表中原生的列进行删选
		having 对分组之后的结果进行二次删选
	
	联表查询：
		select score.student_id ,student.sname from score left join student
		on score.student_id = student.sid and number > 60;

```
#### 主键和外键

主键、外键和索引的区别？

||主键|外键|
|-|-|-|
|定义|唯一标识一条记录，不能有重复的，不允许为空|表的外键是另一表的主键, 外键可以有重复的, 可以是空值|
|作用|用来保证数据完整性|用来和其他表建立联系用的|
|个数|主键只能有一个|一个表可以有多个外键|

```shell
create table department(
id int auto_increment primary key, 
name varchar(32) not null default ''
)engine=Innodb charset=utf8;

insert into department (name) values ('公关部'), ('前台部'), ('保安部'), ('xxxx');

create table userinfo(
id int auto_increment primary key, 
name varchar(32) not null default '',
age int not null default 1,
depart_id int, 
constraint fk_userinfo_depart foreign key(depart_id) references department(id)，
)engine=Innodb charset=utf8;	

```
