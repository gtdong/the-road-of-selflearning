今日内容：
	数据库 MySQL
	

一. 数据库的介绍？
	之前， 我们存取数据的时候， 使用的是Excel表格来进行管理， 
	但是， 随着数据量的增多，使用Excel表格就不行了， 而且我么还有一些高级的查询，
	需要工具软件来帮助我们取完成
	这个软件就是数据库软件
	
	
	-----》 数据库就是一个帮助我们进行数据管理的软件（工具）

二. 数据库的分类
	a. 关系型数据库
			1. 有约束
			2. 基于硬盘存储的
			
			具体实现的软件：
				MySQL（免费），SQLServer（微软 c# .net）, Oracle(甲骨文， java)， SQLlite, DB2 
				mariadb, pgsql
				
	b. 非关系型数据库
			1. 没有约束   {“key”--->value, "key"---> "bdshabd"}
			2. 基于内存存储的
			
			具体实现的软件：
				Memcache(03), redis(10年 微博), mongodb
	
三. MySQL数据库
	
	a. 架构
		
		MySQL服务端：
			socketserver服务端
			接收来自客户端的指令， 执行， 然后将结果返回
		
		MySQL客户端：
			socket client客户端
			发送指令到服务端

	b. 安装：
		
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
		
	
	c. mysql的操作:
		
		show databases;
		
		操作文件夹（数据库）：
			操作文件（数据表）：
				数据行（具体的一行数据）
				数据行
				数据行
				
		大量的SQL指令（语句）
		
			数据库：
				
				增
					语句：
						create database 数据库名;
					例子：
						create database db1;
				删
					drop database （数据库名）db2;
				改
					删掉数据库， 然后新建
				查：
					列出当前数据库下面的所有数据库：show databases;
					
				使用数据库：
					use 数据库名(db2);
				
			数据表：
				
				增
					指令：
						create table 表名(
							列名， 列属性,
							列名， 列属性,
							列名， 列属性,
							列名， 列属性,
						);
					
					语句：

						版本0：
							create table t1(
								id  int,
								name char(32)
							);
							语句：
								insert into 表名 (列名1，列名2，...., 列n )values(值1，值2,...值n);
							例子：
								insert into t1 (id, name)values(1, 'zekai');
								insert into t1 (id, name)values(1, '你好');
						版本1：
							create table t2(
								id  int,
								name char(32)
							)charset=utf8;
							
							insert into t2 (id, name)values(1, 'zekai');
							insert into t2 (id, name)values(1, '你好');
							
							
						版本2：
							create table t3(
								id  int auto_increment primary key,
								name char(32)
							)charset=utf8;
							
							insert into t3 (name, age)values('zekai', 12);
							insert into t3 (name)values('eagon');
							insert into t3 (name)values('xxxx');
						
						版本3：
							create table t3(
								id  int auto_increment primary key,
								name char(32) not null default ''
							)engine=Innodb charset=utf8;
							
							auto_increment: 自增 要和primary key 一起使用
							null : 默认是是null值
							not null ： 不能为null
							default : 指定默认值
							
							最后一列语句不能加逗号
							
						ps:
							存储引擎：
								MyIsam （5.5以下）  和 Innodb（5.5以上）
								
						最终建表的语句格式：(********************)
						
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
						
						
						列类型：
							数字类型：
								
								tinyint
								smallint
								mediumint
								int
								bigint
								
								区别：
									范围不一样
								
								有符号
									
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
								
								
						查看建表语句：
							show create table 表名(t3);  ====> 建表过程显示
						
						查看表中列的详细信息：
							desc 表名(t3);
							
						查看数据：
							select * from 表名(t1);
		
				删
					drop table 表名; （表里的数据都会没有）
				改
					修改表中的列：
						修改一列：
							alter table 表名(t3) change  老列名(name)   新列名(usernme char(32));
						添加一列：
							alter table 表名(t3) add  新列名(age int); 
						删除一列;
							alter table 表名(t3) drop 老列名(age);
					
				查
					show tables;

					
				
				
					
			数据行：
				
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
				
					
			
			外键：（**********************************）
				一对多
				
				缺点：
					1. 重复太厉害
					
					2. 如果部门名称过长的话， 重复去写的话， 占用空间太厉害
					
				方法：
					通过新建一张表来解决
					
				
				
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
					constraint fk_userinfo_depart foreign key(depart_id) references department(id)，
					constraint fk_userinfo_depart foreign key(depart_id) references department(id)，
					constraint fk_userinfo_depart foreign key(depart_id) references department(id)，
				)engine=Innodb charset=utf8;
							
				insert into userinfo (name, age, depart_id) values ('zzzz', 12, 3);	
				insert into userinfo (name, age, depart_id) values ('kkkk', 23, 1);	
				insert into userinfo (name, age, depart_id) values ('hhhh', 45, 2);	
				insert into userinfo (name, age, depart_id) values ('bbbb', 56, 3);	
				
				insert into userinfo (name, age, depart_id) values ('zzzz', 12, 32);		
				
				
				ps:
					1. 主键名称不能重复
					2. 可一建多个外键，方法一样， 但是建立的外键一定是另一张表中的主键	