#### 外键的变种：
```shell
		1.唯一索引：
			create table yyy(
				id int,
				num int,
				unique u_name (num) ,
				unique u_id_name (id, num)  ### 联合唯一索引   1,1   1,2
			)engine=Innodb charset=utf8;
			
		
		
		2.一对多：
			department：
				id   name
				 1    开发部
				 2    保安部
				 3    运维部
			
			userinfo
			
				id   name   age  depart_id
				1     zekai 23     1
				2     zekai 23     2
				3     zekai 23     1
				
		3.一对一：

			userinfo
			
				id   name     age 
				1     eagon   23     
				2     zekai   23     
				3     lxxx    23   
				4     linhaifeng   78
			
			blog表：				   外键 + 唯一约束
				id     url             uid
				1      /linhaifeng/     4
				2      /lxxx/           3
				
		
		4.多对多
			
			userinfo			
				id	name	age	
				1	root1	23	
				2	root2	24	
				3	root3	25	
				4	root4	26	
				5	root5	27	
			
			host	
				id	name
				1	c1.com
				2	c2.com
				3	c3.com
				
			user2host			
				id	uid	hid	
				1	1	1	
				2	1	2	
				3	1	3	
				4	2	1	
				5	2	3	
			
			1. 一个用户下面有多少台主机？
				
				目前：
					给userinfo表加一个字段  host_id
			
			
			2. 一台主机下面有多少个用户？
				
			
		5.SQL嵌套  子查询
			
			不建议大家在线上使用SQL子查询进行操作
			
			建议： 将SQL语句分叉成多条简单的SQL语句， 分别查询， 速度是快于嵌套查询
			
			公司：
				每周五  代码的review
				
				内容：
					1. 函数类 变量的命名风格
						
						大驼峰法 （def GetUserInfo）
						小驼峰法  （def getUserInfo）
						下划线    (def get_user_info)
						
						def getUserInfo
						
						user_info
					
					2. 函数的函数体不能超过30行  （高内聚低耦合）

					3. 变量名和等号之间 要加空格
					
					4. SQL语句是否有嵌套
```				
### d.pymysql
```shell
		安装： pip3 install pymysql
		
		create table userinfo (
			id int auto_increment primary key,
			name varchar(32) not null default '',
			email varchar(32) not null default ''
		)engine=Innodb charset=utf8;
		
		
  pymysql操作数据库：
		
			1. conn = pymysql.conn 链接数据库
			2. cursor = con.cursor()
			3. cursor.execute(sql语句)
			查询
				4. cursor.fetchone() # 取一行数据
				5. cursor.fetchmany(5) ## 取指定的数据
				6. cursor.fetchall() #  取到所有的结果集
			
			增加
				
				增加一条数据：
					cursor.execute(insert 语句， 传入的参数)
					
				增加多条数据：
					cursor.executemany(insert 语句， 传入的多个参数)
				
				conn.commit()				
				
			删除
				删除一条数据：
					cursor.execute(delete语句， 传入的参数)
					
				删除多条数据：
					cursor.executemany(delete语句， 传入的多个参数)
				conn.commit()
			
			修改
				删除一条数据：
					cursor.execute(update语句， 传入的参数)
					
				删除多条数据：
					cursor.executemany(update语句，传入的多个参数)
					
				conn.commit()
			
			
			
		安全问题：
			
			sql注入：
				攻击代码：
					1. zekai' #
						select * from user where name = 'zekai' #' and pwd = ''
						
					2. bdshabdhsa' or 1=1 #
						select * from user where name = 'bdshabdhsa' or 1=1 #' and pwd = ''
				
				产生的原因：
					
					太相信用户传入的值 （默认用户都是君子）
				
				如何防护：
					过滤用户输入的值
					
				python中的做法：
					sql = "select * from user where name = %s and pwd = %s"

					cursor.execute(sql, (username, pwd))
				
			
			csrf攻击
			
			xss攻击
		

	
	索引
		作用： 
			加速查找
		
		类似： 
			新华字典的索引目录   如果没有这个索引目录， 我们查询的时候需要从前到后进行遍历查询
			特殊的二进制文件， 就可以通过此文件定位到想要的值
			
		原理：
			B+ 树
		
		索引的类型：
		
			主键索引： 加速查找 + 不能为空 + 不能重复  primary key 
				create table xxx(
					id int ,
					
					name varchar(32) not null default '',
					unique uq_name (name)
				)
				
				alter tbale xxx change id  id int primary key;
				
			唯一索引： 加速查找 + 不能重复   unique(name)
				联合唯一索引： 加速查找 + 两列不能重复
				create table xxx(
					id int auto_increment primary key,
					
					name varchar(32) not null default '',
					unique uq_name (name)
				)
					
					create unique  ix_name on xxx (name)
				
				
				
			普通索引： 加速查找  index ix_name(name)
				组合索引： 加速查找 index ix_name_email (name, email)
			
				创建的两种方式：
				
					create table xxx(
						id int auto_increment primary key,
						
						name varchar(32) not null default '',
						
						index ix_name (name)
					)
					
					create index ix_name on xxx (name)
			
			查看索引：
				show indexes from xxxx;
				
			删除索引：
				对普通索引， 唯一索引：	
					drop index 索引名 on 表名；
				对主键索引：
					alter table 表名 drop primary key;
				
			是否需要对每一列都要加索引？
			
				不是的
				原因：
					索引固然加速了查找， 但是对增加， 删除， 修改， 效率是不高的
					
				加索引的原则：
					
					根据业务决定（向经常使用的字段上加索引）
			
			索引使用的条件：
				加了索引并不能一定用到
				根据具体的SQL语句判断是否用的索引
				
				索引不适用的情况：
					
					- 不要适用 like
					- 不要在语句中适用函数
			
			
			判断工具：
				explain：
					
					explain  sql语句
					
						type: all 
						
						extra: Using filesort
								这意味着mysql会对结果使用一个外部索引排序，而不是按索引次序从表里读取行。mysql有两种文件排序算法，这两种排序方式都可以在内存或者磁盘上完成，explain不会告诉你mysql将使用哪一种文件排序，也不会告诉你排序会在内存里还是磁盘上完成。
			
				慢日志:
					
					slow_query_log = OFF                            是否开启慢日志记录
					long_query_time = 2                              时间限制，超过此时间，则记录
					slow_query_log_file = /usr/slow.log        日志文件
				
				普通日志：
					general log
					

			
			事务：
				create table users (
					id int auto_increment primary key,
					name varchar(32) not null default '',
					money int not null default 0
				)engine=Innodb charset=utf8;
				
				
				insert into users (name, money) values ('zekai', 1000),('lxxx', 500);
				
				
				一组操作：
					update users set money=900 where id=1; （执行成功）
					
					update users set money=600 where id=2; （执行失败）
				
				概念：
					一组操作， 要么全都成功， 要么全都失败 
				
				用法：
					
					开启事务(start transaction)
					执行sql操作(普通sql操作)
					提交/回滚(commit/rollback)
				
				
				特性：（*****************************************）
					
					原子性(Atomicity)，原子意为最小的粒子，即不能再分的事务，要么全部执行，要么全部取消（就像上面的银行例子）
					一致性(Consistency)：指事务发生前和发生后，数据的总额依然匹配
					隔离性(Isolation)：简单点说，某个事务的操作对其他事务不可见的
					持久性(Durability)：当事务完成后，其影响应该保留下来，不能撤消，只能通过“补偿性事务”来抵消之前的错误
				
				
				事务支持引擎：

					Innodb 和 MyISam 区别：
						1. Innodb支持事务， myISam不支持
						2. 版本5.5 默认Innodb  版本5.5一下 默认MyISam
						3. Innodb支持行锁 （并发量大使用） MyISam表锁
					    
						
				备份：
					mysqldump
					
					
				
					
			
					
			
			
			
			
					
					
					
					
					
					
					
					
					
				
				
				
				
				
					
			
			
			
			
			
			
		
		
		
		
		
		
		
		
		
			
			
			
			
			
		
		
		
		
	
	
	
	
	
	
	
	
	
	
	事务
	
	
	
	
	前端
	
```shell



