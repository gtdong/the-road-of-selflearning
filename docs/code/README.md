#  Git简介

linux系统的创始人李纳斯一星期的时间开发出了git

## Git下载

<https://git-scm.com/>

## Git基本命令

工作区:当前编辑的区域

缓存区:add之后的区域

本地仓库:commit之后的区域

远程仓库:GitHub,gitlab,码云...

```shell
"进入想要管理的文件夹之后git bash here"
git init  # 初始化本地仓库(.git隐藏文件 包含了所有的操作记录)
git status  # 当前管理状态(没管之前是红色,管谁谁变绿色)  被管理之后文件只要有改动就会被自动检测并显示成红色
git add 文件名/.  # .表示管所有(全变绿色)
git commit -m '解释信息(越详细越好)'  # 将所有变绿的文件拷贝一份放到仓库(变白色)
# 初次提交需要设置邮箱和用户名(更具提示信息设计即可)
git config --global user.name  # 设置用户
git config --global user.email  # 设置邮箱

git config --global --unset user.name  # 删除用户
git config --global --unset user.email  # 删除邮箱


git log  # 查看提交记录
git reset --hard  '序列号'  # 回退到之前版本状态
git reflog  # 查看所有版本(包括回退之前的新版本)

git checkout filename # 回到最近的一次提交状态
git reset HEAD filename. # 将指定文件从缓存区拉取到工作区
git diff  # 对比缓存区和工作区的区别
git diff --cached  # 缓存区和本地仓库的区别  

"当开发某个功能到1/2时并且没有提交，如果想要回到原来的状态修复原来的代码"
git stash  # 将你开发一半的代码先暂时存起来(此时会自动回到修改之前的状态 大白话就是把红色文件全部暂存)
# 修复之前的bug
# 提交修复代码(可能会出现冲突 需要手动修改冲突)
git stash pop  # 再次回到开发某个功能到1/2处
"git stash 其他命令"
git stash list  # 查看暂存区所有的记录
git stash clear  # 清空暂存区
git stash apply 编号  # 将指定的编号记录拿出来 
git stash drop 编号  # 删除指定编号的记录 

"一般实际工作中修复bug不经常用git stash，而是使用分支结构"
git branch dev  # 创建分支(会拷贝master全部代码)
git checkout dev  # 切换分支(在切换到其他分支之前 一定要将当前分支的内容先提交)
# 如果master出现bug 一定不在直接在master上面修改bug因为可能还会有其他bug 应该再创建分支专门修复bug
git branch bug  # 创建bug修复bug并提交
git checkout master  # 切换回master分支 
git merge bug  # 将bug分支合并到master分支上(可能会产生冲突还是需要自己手动解决)
git branch -d bug  # 删除bug分支
git branch  # 查看所有的分支
"公司出现bug不要回答的太细只需要回答:创建一个bug分支，再bug分支上进行修复，修复完成后合并到master上即可"


"git面试题:git rebase的作用"
跟git merge一样也是合并分支，不同之处在于会将多个版本的线路直接合并成一条(让提交记录更加的简洁)，而git merge不会
也会产生冲突:手动修改完冲突之后再执行git rebase --skip
```

## Git之远程仓库

远程保存代码平台>>>:github

公共的:GitHub,码云

自己搭建:gitlab

```python
# 1.注册账户 + 创建项目 + 拷贝地址

# 2.第一次 本地代码推送远程
"""
cd 项目目录
git remote add origin 远程地址
git push origin master
git push origin dev

继续写代码
git add .
git commit -m ''
git push origin dev
"""

# 3.第一次公司
"""
git clone 远程地址
或者
1.创建目录
2.cd 目录下
3.git init
4.git remote add origin 远程地址
5.git pull origin master

创建dev分支
git checkout dev
git pull origin dev

继续写代码
"""

# 4.回家
"""
拉代码
	git pull origin dev
继续写代码
	git add .
	git commit -m ''
	git push origin dev
"""
```

## 面试题

```python
# 公司如何实现 协同开发
会给每个人创建一个分支，最后再合并到dev分支
master
dev
  -员工1
  -员工2
  -员工3

# 公司是否做代码的review 肯定会做
master
dev
	- review(小组长做审核)
一般小功能就会合并，防止出现太多的冲突

# 如何做协同开发
1.给开源项目提供代码 默认是无法让你修改的 但是可以通过创建合作者(协同开发)继续修改
2.如果这一个团队很牛逼 会一起合作很多项目 那么还可以创建组织，组织内多人可以开发多个项目

# 拷贝别人的项目 + 修改申请
fork + new pull request
```

## 忽略不重要文件

项目中创建gitignore文件,文件内写不想管理的文件名

这一步操作所有的代码管理平台都有自动生成和需要忽略的文件，所以也没必要自己自己手动创建但是需要知道，这样以后起码自己知道如何修改

## 作业

```python
"""
协同开发
	组长 创建仓库:合作者模式邀请成员
	创建master/dev/review分支
	小组成员创建自己的分支
		-各自写各自的代码
		-提交到自己的本地dev分支
	切换到本地的review分支，拉取远程的review分支然后合并本地dev代码 解决冲突
	再将本地review分支代码推送到远程代码仓库
		可能会有冲突
	小组长在review分支上审核小组成员代码
"""
```



# openpyxl模块

需要手动先安装该模块，该模块主要就是用来操作excel表格

小知识点:office excel表格文件的后缀名在03版本之前，都叫xls,03之后的版本后缀名xlsx

操作excel表格的python模块很多，以前比较流行的有兄弟俩:xlwd和xlrt(分别控制读写),今天介绍的openpyxl是最近很火的操作excel表格的第三方模块。他们之间的区别在于openpyxl只能操作03之后的后缀名是xlsx的，而兄弟俩既可以操作03之前的后缀名是xls的，有可以操作03之后的xlsx的

```python
# openpyxl简单使用
from openpyxl import Workbook


wb = Workbook()  # 实例化一个工作薄对象
# wb1 = wb.create_sheet('test')  # 创建一个名为test的工作簿 默认是在sheet后面
wb1 = wb.create_sheet('test',0)  # 还可以指定索引参数调整test位置
wb1.title = 'test01'  # 修改名称
wb1['A3'] = 666  # 在A3对应的表格中写数据666
wb1.cell(row=3, column=4, value=999)  # 在第三行第四列的位置上写数据999

# 除了写数据之外，还可以写函数(比如excel支持的求和，求差等很多常见的函数)
wb1['A4'] = 123
wb1['A5'] = 321
wb1['A6'] = '=sum(A4:A5)'  # 求A4与A5的和 注意等号一定要加

wb.save('1.xlsx')


# 进阶使用
# 表格通常包含表头和表体两部分
from openpyxl import Workbook


wb = Workbook()  
wb1 = wb.create_sheet('test',0)
wb1.append(['name','age','gender','phone'])
# wb1.append([])添加空行的方式
wd1.append(['jason','18','male',110])
# wd1.append(['jason','18','male',])  添加空的单元格 直接写空即可
wb.save('1.xlsx')
```

#### 读数据

```python
# 读数据
from openpyxl import load_workbook
wb = load_workbook('1.xlsx',read_only=True,data_only=True)
print(wb.sheetnames)  # 获取1.xlsx中所有的工作薄名称  结果是列表数据类型
wb1 = wb['test']  # 拿到工作薄test对象

# 第一种取值方式
print(wb1['A3'].value)  # 不是结果 需要再点value
print(wb1['A6'].value)  # 获取用函数统计的数据，发生无法取到值
# 第一需要加一个参数
# 第二需要人为的先去修改一下用程序产生的excel表格(不可能用程序产生excel文件之后又直接再用程序去读入，这样没有任何实际意义 通常用程序创建好表格后给人看，人讲自己修改的表格再交由程序处理)
print(wb1.cell(row=3,column=4).value)  # 第二种取值方式

# 获取一行行的数据
for row in wb1.rows:  # 拿到每一行的数据
  for data in row:  # 拿到一行行数据里面每一个单元格的数据
    print(data.value)
    
# 获取一列列的数据(如果想获取 必须把readonly去掉)
for column in wb1.columns:  # 拿到每一列的数据
 	for r in column:  # 拿到一列列数据里面每一个单元格的数据
    print(r.value)

# 获取最大的行数和列数
print(wb1.max_row)
print(wb1.max_column)
```



# Ansible简介

### 前期准备

* 虚拟机安装，并克隆出另外三台机器

* 修改另外三台克隆出来的机器

  ```shell
  vi /etc/sysconfig/network-scripts/ifcfg-eth0  
  vi /etc/sysconfig/network-scripts/ifcfg-eth1 
  ```

* 重启网络生效

  ```shell
  systemctl restart network
  ```

* xshell链接

  ```python
  # xshell6可使用一个月，过期卸载重新安装即可，循环往复即可连续使用 真香
  ```

### 简单介绍

在远程主机上批量执行命令或者脚本的一个工具(python2.7开发实现)

之前可能会使用到的工具有puppet(rubby开发实现，缺点:https各种配置认证，机器时间不一样永远无法配置成功)

目前比较流行的saltsatck(python2.7开发实现)、ansible(python2.7开发实现)

镜像地址:<https://opsx.alibaba.com/mirror?lang=zh-CN>查找epel源

### 安装

```shell
#先下载wget
yum install -y wget
#将epel源下载到本地
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
#安装ansible
yum install -y ansible
```

### ansible命令格式

```python
# 查看ansible帮助
ansible -h
# 命令格式
Usage: ansible <host-pattern> [options]

-a MODULE_ARGS  # 模块参数
-C, --check  # 干跑，白跑
-f FORKS, --forks=FORKS  # 指定并发，默认5个
--list-hosts  # 列出主机
-m MODULE_NAME  # 模块名称
--syntax-check  # 检查语法
-k  # 密码
```

### 链接机器

```python
# 小知识点补充:ping走的是ICMP协议

rpm -ql ansible|more # 查看ansible生成的文件

/etc/ansible
/etc/ansible/ansible.cfg  # 配置文件
/etc/ansible/hosts  # 配置管控机
/etc/ansible/roles  # 空文件夹
# 在hosts文件中将主机地址一个个添加进去

ansible 主机地址 -m ping -k  # ansible底层通过ssh实现

# 生成密钥
ssh-keygen
# 将公钥拷贝至目标主机
ssh-copy-id root@主机地址
# 通过ssh即可链接目标主机
ssh 'root@主机地址'
exit退出

# 完成上面的操作后 再去探测机器是否在线就不要再加-k
ansible 主机地址 -m ping

"""测试机器是否在线的方式及分组管理"""
ansible 192.168.226.101 -m ping  # 单独机器的ping
ansible 192.168.226.101,192.168.226.102 -m ping  # 多个机器的ping
ansible all -m ping  # 全部机器
# 分组:比如有N多台机器，有些是负责数据库的，有些是uwsgi的，有些是redis的等
ansible web -m ping  # 单个的组
ansible web,db -m ping  # 多个组的并集
ansible 'web:&db' -m ping  # 多个组的交集  必须是单引号 双引号不行
ansible 'web:!db' -m ping  # 多个组的差集，在前面但是不在后面
```



# ansible模块介绍

```python
ansible-doc -l |wc -l  # 查看ansible总模块数
```

## ansible-doc 命令格式

```python
ansible-doc 

-j  # 以json的方式返回数据
-l, --list  # 列出所有的模块
-s, --snippet # 以片段式显示模块信息 
# 常用命令
ansible-doc -s 模块名  # 查看模块帮助信息
```

## 模块介绍

* ### command

  分组机器批量执行系统命令

  ```shell
  ansible-doc -s command
  
  ansible web -m command -a "pwd"
  ansible web -m command -a "ls"
  ansible web -m command -a "chdir=/tmp pwd" #切换目录并执行命令
  ansible web -m command -a "creates=/tmp pwd" #因为tmp目录存在，pwd不会执行
  ansible web -m command -a "creates=/tmp2 pwd" #因为tmp2不存在，pwd执行
  ansible web -m command -a "removes=/tmp2 pwd" #因为tmp2不存在pwd不执行
  ansible web -m command -a "removes=/tmp pwd" #因为tmp目录存在，pwd会执行
  
  # 创建用户
  ansible web -m command -a 'useradd jason'
  # 设置密码(本机设置)  并需二次确认
  passwd jason
  # 设置密码(本机设置)  无需二次确认
  echo "123" |passwd --stdin jason #设置用户的密码
  ```

* ### shell

  当命令中包含$home和常见符号(<,>,|,;.&)等的时候，需要使用shell才能生效

  ```shell
  ansible-doc -s shell
  
  ansible web -m shell -a "echo '123' |passwd --stdin jason"
  ansible web -m shell -a "chdir=/tmp pwd" shabang
  ansible 192.168.226.101 -m shell -a "bash a.sh" #执行shell脚本
  ansible 192.168.226.101 -m shell -a "/root/a.sh" # 执行shell脚本，文件要有执行的权限
  ansible 192.168.226.101 -m shell -a "/root/a.py" #执行Python文件
  ```

* ### script

  在远程机器上执行本地脚本

  ```shell
  ansible-doc -s script
  
  ansible db -m script -a "/root/a.sh"  # 执行本地的文件，管控机的文件
  ansible db -m script -a "creates=/root/a.sh /root/a.sh"  # 判断被控机上的文件是否存在，如果不存在，就执行，如果存在，就跳过
  ansible db -m script -a "creates=/tmp /root/a.sh"  # 判断被控机上的文件
  ```

* ### copy

  将本地的文件拷贝到远程机器

  ```shell
  ansible-doc -s copy
  
  backup  # 创建一个备份文件，以时间戳结尾
  content  # 直接往文件里面写内容
  dest  # 目标地址
  group  # 属组
  mode  # 文件的权限 W 2 R 4 X 1
  owner  # 属主
  src  # 源地址
  ansible web -m copy -a "src=/etc/fstab dest=/tmp/f"  # 复制本地文件到远程主机，并修改文件名，多次执行不会改变，因为checksum值是一样的
  ansible web -m copy -a "src=a.sh dest=/tmp/a.sh backup=yes"  # 复制本地文件，并备份
  ansible web -m copy -a "src=a.sh dest=/tmp/a.sh backup=yes group=alex mode=755"  # 复制本地文件到远程主机，并指定属组和权限
  ansible web -m copy -a "src=/etc/init.d dest=/tmp backup=yes group=alex mode=755"  # 复制本地的目录到远程主机，修改目录权限，则目录里面的文件也会跟着变更
  ansible web -m copy -a "src=/etc/init.d/ dest=/tmp backup=yes group=alex mode=755"  #复制本地目录下的所有文件，
  ansible web -m copy -a "content='大弦嘈嘈如急雨，小弦切切如私语，嘈嘈切切错 杂弹，大珠小珠落玉盘' dest=/tmp/b"  # 直接往文件里面写内容，覆盖写，慎用
  ```

* ### FILE

  文件属组、权限、硬软链等

  ```python
  group  # 属组
  mode  # 权限
  owner  # 属主
  path  # 路径
  src  # 软硬链接
  	state =link
  	state =hard
  state
  	directory  # 目录
  	file  
  	touch  # 空文件
  	absent  # 删除
  	link  # 软连接
  	hard  # 硬链接
    
  ansible web -m file -a "path=/jason5 state=directory owner=jason" #创建目录，并制定属主
  ansible web -m file -a "path=/tmp/jason.txt state=touch mode=777" #创建文件，并指定权限
  ansible web -m file -a "path=/tmp/cron src=/var/log/cron state=link" #创建软链接，链接的是自己的文件
  ansible web -m file -a "path=/tmp/cron state=absent" # 删除软连接
  ansible web -m file -a "path=/jason5 state=absent" #删除文件夹
  ```

  **知识卡片**

  ```python
  """
  软连接   快捷方式(windows)   ln -s   源文件修改软连接修改     源文件删除软连接失效   可以跨分区 
  硬链接   硬盘的位置 ln       源文件修改硬链接修改  					  源文件删除硬链接不变 	不可以跨分区
  复制     开辟新空间 cp       源文件修改cp的不变   					  源文件删除不变 				可以跨分区
  
  fdisk -l查看分区信息
  """
  ```

* ### fetch

  拉取远程主机文件

  ```python
  dest 目标地址
  src 源地址
  ansible web -m fetch -a "src=/var/log/cron dest=/tmp"  # 拉取远程主机的文件，并以主机ip地址或者主机名为目录，并且保留了原来的目录结构
  ```

* ### yum

  安装工具

  **1.自带的yum**

  ```python
  """
  1.yum跟rpm有什么关系，有什么区别
  rpm(redhat package manager) 需要手动解决依赖关系
  yum 可以解决依赖关系
  
  2.yum源怎么配置
  ls /etc/yum.repos.d/
  vi /etc/yum.repos.d/epel.repo
  文件内容如下:
  [epel]    #名称
  name=Extra Packages for Enterprise Linux 7 - $basearch  #全名或者描述信息
  baseurl=http://mirrors.aliyun.com/epel/7/$basearch  # 源url地址
  failovermethod=priority
  enabled=1  #是否启用，1启用，0不启用
  gpgcheck=0  #是否检验key文件(怕被串改 安全性较严，类似于优酷电影一致性较严)，0不校验 1校验
  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
  
  3.yum怎么安装包组
  yum list  # 查看所有的包组(安装没安装都有)   @代表已经安装
  yum grouplist  # 查包组信息
  # 安装包组
  yum groupinstall -y "Development Tools"  # 一个系统里面同一时刻只能用一个yum
  """
  ```

  **2.ansible中的yum模块**

  ```shell
  ansible-doc -s yum
  
  disablerepo  # 禁用某个源
  enablerepo  # 启用某个源
  name  # 包名
  state
  	install
  	remove
  	
  yum install -y python2-pip  # 在epel源中 	
  # 将主机中下载好的pip拷贝到其他被管控机上
  ansible all -m copy -a 'src=/etc/yum.repos.d/epel.repo dest=/etc/yum.repos.d/epel.repo'
  
  ansible web -m yum -a "name=python2-pip"  # 安装单个软件包
  
  # 查看是否安装 对应机器上执行下述命令
  rpm -q 包名
  # eg:rpm -q pip/python-pip/python2-pip/redis
  
  ansible web -m yum -a "name=python2-pip,redis"  # 安装多个软件包
  ansible web -m yum -a "name='@Development Tools'"  # 安装包组
  ansible web -m yum -a "name=nginx state=absent"  # 卸载
  ```

* ### pip

  python安装第三方模块的工具

  1.自带的

  ```python
  pip freeze > requirements.txt   # 将本地环境导出到某个文件中，文件中不写版本信息默认安装最新版本
  pip install -r requirements.txt  # 安装所有的包(******)
  
  pip list  # 查看所有的包
  pip uninstall flask  # 卸载
  
  # 下载包
  Python setup.py build 
  python setup.py install
  ```

  2.ansible中的pip模块

  ```python
  ansible-doc -s pip
  
  chdir  # 切换目录
  name  # 包名
  requirements  # 导出的文件
  virtualenv  # 虚拟环境
  
  # 安装django(时间较长～)
  ansible web -m pip -a "name=django==1.11"
  ```

* #### service

  程序软件服务相关

  ```python
  """
  centos版本对比
  启动
  systemctl start redis  # centos7
  service redis start  # centos6
  开机自启动
  systemctl enable redis  # centos7
  chkconfig redis on  # centos6
  """
  ansible-doc -s service
  
  # 关键参数
  enabled #开机启动
  name #服务名称
  state  
      started
      stopped
      restarted
      reloaded
  ansible web -m service -a "name=redis state=started" #启动
  ansible web -m service -a "name=redis state=stopped" #关闭
  ansible web -m service -a "name=redis enabled=yes" #设置开机自启动
  
  ps -ef|grep redis  # 查进程
  ss -tunlp  # 查端口 centos7里面没有netstate
  ```

  知识卡片

  ```python
  # 常见程序默认端口
  ssh 22
  http 80
  https 443
  mysql 3306
  redis 6379
  mongodb 27017
  oracle 1521
  tomcat 8080
  windows远程桌面 3389
  ftp 20 21
  django 8000
  flask 5000
  ```

* ### cron

  计划任务

  知识小卡片

  ```python
  crontab  # linux中计划/定时任务
  # 格式
  * * * * * job
  分 时 日 月 周 任务
  
  3/* * * * * job 每隔3分钟执行一次
  4 10-12 * * * job 10点-12点第4分钟执行，包括12点
  # 查看具体的范围
  cat /etc/crontab
  0-59 0-23 1-31 1-12 0-7(星期天可以是0也可以是7) 
  
  # 分钟最好不要用*
  * * * * * tar zcf /tmp/etc.tar.gz /etc  # 每分钟执行一次
  
  # 计划任务常用场景
  备份
  同步时间
  删除文件
  ```

  ansible同样提供了相应模块

  ```shell
  ansible-doc -s cron
  
  day  # 天
  disabled  # 禁用crontab，表现形式加#
  hour  # 小时
  job  # 任务
  minute  # 分钟
  month  # 月
  name  # 名字，描述信息
  user  # 用户
  weekday  # 周
  
  # 添加时名字必须不同，不加名称为None(crontab -l查看计划任务)
  ansible web -m cron -a "minute=12 name=touchfile job='touch /tmp/xiaoqiang.txt'"  # 创建
  ansible web -m cron -a "name=touchfile state=absent"  # 删除
  ansible web -m cron -a "minute=12 name=touchfile2 job='touch /tmp/jason.txt' disabled=yes"  # 注释
  ansible web -m cron -a "name=None state=absent"  # 删除名称为空的计划任务
  ```

* ### user

  自带的

  ```python
  tail /etc/passwd
  tail /etc/shadow
  id alex2
  
  # useradd主要功能
  useradd 
  
  -d  # 设置用户家目录
  useradd -d /opt/jason2 jason2
  -g  # 设置用户的属组
  useradd -g jason2 jason3 
  -G, --groups  # 附加组
  useradd -G jason2,root jason4
  -r, --system  # 系统账号
  useradd -r jason5  # 系统账号没有家目录
  -s, --shell  # 设置用户登录后的shell
  useradd -s /sbin/nologin jason8
  -u, --uid UID  # 设置用户的id
  
  useradd -u 2000 jason9
  设置了用户的id以后，再设置用户则从最大的id开始往后数 useradd jason10
  # 用户分类
  超级管理员 root 0
  普通用户
  	系统用户  启动一些服务或者进程，不能登录  
  					1-999  # centos7 
  					1-499  # centos6 从大到小
  	登录用户  可以登录的用户 
  					1000-65535  # centos7 
  					500-65535  # centos6  从小到大
  					
  userdel  # 删除用户
  userdel alex8  # 默认不删除家目录
  -r 删除用户的家目录
  userdel -r alex9  # 删除用户并删除用户的家目录
  ```

  ansible中的user模块

  ```python
  ansible-doc -s user
  
  group # 属组
  groups  # 附加组
  home  # 设置家目录
  name  # 用户名
  remove  # 删除用户并删除用户的家目录
  shell  # 用户登录后的shell
  system  # 系统用户
  uid  # 用户的id
  ansible web -m user -a "name=alex10 shell=/sbin/nologin home=/opt/alex10 uid=3000 groups=root" #创建用户，并指定用户的shell，家目录，uid，以及附加组
  ansible web -m user -a "name=alex11 shell=/sbin/nologin home=/opt/alex11"
  ansible web -m user -a "name=alex12 system=yes" #创建系统用户
  ansible web -m user -a "name=alex12 state=absent" #删除用户，单不删除家目录
  ansible web -m user -a "name=alex11 state=absent remove=yes" # 删除用户并删除用户的家目录
  ```

* ### group

  1.自带的

  ```python
  groupadd 
  -g 设置id
  -r 系统组
  超级管理员组 root 0
  普通组
  	系统组  1-999 
  					centos7 1-499 
  					centos6 从大到小 
  	登录用户组 1000-65535 
  					centos7 500-65535 
  					centos6 从小到大
  					
  # 查看
  tail /etc/group
  groupadd -g 3000 jason10  # 添加用户并设置id
  groupadd -r jason666  # 创建组
  ```

  2.ansible中的group模块

  ```python
  ansible-doc -s group
  
  gid  # 组id
  system  # 系统组
  name  # 名称
  ansible web -m group -a "name=jason10 system=yes gid=5000"  # 创建系统组
  ansible web -m group -a "name=jason11"  # 创建普通的组
  ansible web -m group -a "name=jason11 state=absent"  # 删除组
  ```

* ### setup

  收集远程主机的一些基本信息

  ```python
  # 查看详细信息
  ansible 主机名 -m setup|more
  
  ansible_all_ipv4_addresses  # 所有的ipv4地址
  ansible_all_ipv6_addresses  # 所有的ipv6地址
  ansible_architecture  # 系统的架构
  ansible_date_time  # 系统时间
  ansible_default_ipv4  # 默认的ipv4地址
  	address  # ip地址
  	alias  # 网卡名称
  	broadcast  # 广播地址
  	gateway  # 网关
  	netmask  # 子网掩码
  	network  # 网段
  ansible_default_ipv6  # 默认的ipv6地址
  ansible_device_links  # 系统的磁盘信息
  ansible_distribution  # 系统名称
  ansible_distribution_file_variety  # 系统的基于公司
  ansible_distribution_major_version  # 系统的主版本
  ansible_distribution_version  # 系统的全部版本
  ansible_dns  # 系统的dns 默认udp 端口53
  ansible_domain  # 系统的域 ldap
  ipv4  # ipv4地址
  ansible_env  # 系统的环境
  ansible_fqdn  # 系统的完整主机名
  ansible_hostname  # 系统的简写主机名
  ansible_kernel  # 系统的内核版本
  ansible_machine  # 系统的架构
  ansible_memtotal_mb  # 系统的内存
  ansible_memory_mb  # 系统的内存使用情况
  ansible_mounts  # 系统的挂载信息
  ansible_os_family  # 系统家族
  ansible_pkg_mgr  # 系统的包管理工具
  ansible_processor  # 系统的cpu
  ansible_processor_cores  # 每颗cpu的核数
  ansible_processor_count  # cpu的颗数
  ansible_processor_vcpus  # cpu的个数=cpu的颗数*每颗cpu的核数
  ansible_python  # 系统python信息
  ansible_python_version  # 系统python的版本
  ansible_system  # 系统名字
  ```

# playbook

ansible提供的脚本，遵循规范yaml(一般用于写配置文件)

可用于配制文件的语言:yaml、xml、json

- 冒号后面必须有空格
- 横线后面必须要空格
- 严格保持对齐
- 等号前面不能有空格？

yaml数据结构

- 字典 key：value
- 列表 (两种表示方式[], \-)

```python
- jason
- egon
- kevin
- tank 
# 上下等价 推荐使用上面的 清晰明了  
[jason,egon,kevin,tank]

# 练习网站:http://www.bejson.com/validators/yaml_editor/
```

### 基本命令

```python
ansible-playbook -h
ansible-playbook [options] playbook.yml [playbook2 ...]

-C, --check  # 白跑，执行但是不会有结果
--list-hosts  # 列出符合的主机
-f FORKS, --forks=FORKS  # 做并发
--syntax-check  # 检查语法
-k, --ask-pass  # 输入密码 
```

### 基本操作示例

```python
mkdir playbook
cd playbook
vi p1.yml

# 内部文本(首先必须是一个列表)  单个playbook
- hosts: web
  remote_user: root
  tasks:
  - name: createuser
    user: name=jason666 home=/opt/jason666 uid=4000
        
ansible-playbook --syntax-check p1.yml  # 检测语法
ansible-playbook -C p1.yml  # 干跑 
ansible-palybook p1.yml  # 真正执行文件
```

### 多个playbook(不建议写)

```python
cp p1.yml p2.yml
vi p2.yml

- hosts: web
  remote_user: root
  tasks:
  - name: createuser
    user: name=jason666 home=/opt/jason666 uid=4000 
  - name: copyfile
    copy: src=/etc/fstab dest=/tmp/fs
- hosts: db
  tasks:
  - name: copyfile
    copy: src=/etc/fstab dest=/tmp/fs

ansible-playbook --syntax-check p2.yml  # 检测语法
ansible-playbook p2.yml  # 执行
ansible-playbook p2.yml  # 再次执行  不会更改
"""
幂等性:不管执行多少次，得到的结果都是一样的(如:api接口)                  
"""
```

### 传参

#### 前戏

```shell
vi p3.yml

- hosts: web
  tasks:
  - name: createuser
    user: name=jason33
# 创建用户jason33 过段时间又需要创建其他用户tank33  频繁修改文件yml明显不合理

# 解决方案  传参！
# 方式1:命令中传值
- hosts: web
  tasks:
  - name: create{{user}}
    user: name={{user}}
ansible-playbook -e user=jason20 p3.yml

# 方式2:hosts文件中主机后面直接添加
[web]
192.168.226.[101:102] user=jason30

# 方式3:hosts文件中新增
[web:vars]
user=jason31

# 方式4:yml文件中配置
- hosts: web
  vars:
  - user: jason32
  tasks:
  - name: create{{user}}
    user: name={{user}}

# 方式5:了解
- hosts: web
  tasks:
  - name: yum
    yum: name=bc
  - name: sum
    shell: echo 11+22|bc
    register: user
  - name: echo
    shell: echo {{user.stdout}} > /tmp/echo.txt 
  - name: create{{user.stdout}}
    user: name=alex{{user.stdout}}
    
传参优先级:-e > playbook > hosts
```

* ### tags

  可以调用单独的任务

  ```python
  vi p7.yml
  
  - hosts: web
    tasks:
    - name: install
      yum: name=redis
    - name: copyfile
      copy: dest=/etc/redis.conf src=/etc/redis.conf
      tags: copy
    - name: start
      service: name=redis state=started
  
  yum install -y redis  # 安装redis
  ansible-playbook --syntax-check p7.yml  # 检测语法
  ansible-playbook -t copy p7.yml  # 执行
  ```

* ### handlers

  ```python
  - hosts: web
    tasks:
    - name: install
      yum: name=redis
    - name: copyfile
      copy: dest=/etc/redis.conf src=/etc/redis.conf
      tags: copy
      notify: restart  # 触发handlers里面的任务
    - name: start
      service: name=redis state=started
    handlers:
    - name: restart
      service: name=redis state=restarted
  ```

* ### template

  绝对路径

  ```python
  - hosts: web
    tasks:
    - name: install
      yum: name=redis
    - name: copyfile
      template: dest=/etc/redis.conf src=/etc/redis.conf
      tags: copy
      notify: restart
    - name: start
      service: name=redis state=started
    handlers:
    - name: restart
      service: name=redis state=restarted
  ```

  相对路径

  ```python
  - hosts: web
    tasks:
    - name: install
      yum: name=redis
    - name: copyfile
      template: dest=/etc/redis.conf src=redis.conf.j2
      tags: copy
      notify: restart
    - name: start
      service: name=redis state=started
    handlers:
    - name: restart
      service: name=redis state=restarted
  # 在当前目录下创建一个templates的目录，就可以使用相对路径
  ```

* ### when  类似于后端if判断

  ```python
  - hosts: web
    tasks:
    - name: copyfile
      copy: content="大弦嘈嘈如急雨" dest=/tmp/a.txt
      when: ansible_distribution_major_version=="7"
    - name: copyfile
      copy: content="小弦切切如私语" dest=/tmp/a.txt
      when: ansible_distribution_major_version=="6"
        
        
  - hosts: web
    tasks:
    - name: copyfile
      copy: content="大弦嘈嘈如急雨" dest=/tmp/a.txt
      when: user=="4"
    - name: copyfile
      copy: content="小弦切切如私语" dest=/tmp/a.txt
      when: user=="3"
  ```

* ### with_items

  ```shell
  - hosts: web
    tasks:
    - name: createuser
      user: name={{item}}
      with_items:
      - jason50
      - tank50
      - oscar50
  
  - hosts: web
    tasks:
    - name: createuser
      user: name={{item}}
      with_items:
      - jason51
      - tank51
      - oscar51
    - name: creategroup
      group: name={{item}}
      with_items:
      - jason60
      - tank60
      - oscar60
  ```

* ### 循环嵌套

  ```python
  - hosts: web
    tasks:
    - name: crateuser
      user: name={{item.name}}  group={{item.group}}
      with_items:
      - {"name":jason52,"group":jason60}
      - {"name":tank52,"group":tank60}
      - {"name":oscar52,"group":oscar60}
  ```

demo:安装nginx并启动，设置开机自启动，指定监听地址为ip地址

```shell
- hosts: web
  tasks:
  - name: install
    yum: name=nginx
  - name: copyfile
  	template: dest=/etc/nginx/nginx.conf src=/etc/nginx/nginx.conf
  - name: start
    service: name=nginx state=started enabled=yes
```



# roles

- 目录结构清晰
- 可以相互调用  - import_tasks: roles/nginx/tasks/install.yml
- 备份方便

案例:

```python
# 在任意位置新建roles文件夹  文件夹内建不同的功能
mkdir /data
cd /data/
mkdir roles
cd roles/
mkdir {nginx,uwsgi,redis,mysql}
cd nginx
# 之后不需要在文件内按照hosts、tasks、handlers等顺序依次书写  而是以文件夹的形式创建
data/roles/nginx/
├── files       # -- 静态文件
│   └── c.txt
├── handlers    # -- 触发的任务
│   └── main.yml   
				# - name: restart
        #   service: name=nginx state=restarted
├── tasks       # -- 任务（必须的）
│   ├── copyfile.yml  # 只需要书写对应的yml格式任务即可
			# - name: copyfile
  		# template: dest=/etc/nginx/nginx.conf src=/etc/nginx/nginx.conf	
│   ├── install.yml
			# - name: install
    	# yum: name=nginx
│   ├── main.yml  # (必须有main.yml文件  将其他yml文件导入即可也可以这里面直接写)
			# - import_tasks: install.yml
      # - import_tasks: copyfile.yml
      # - import_tasks: start.yml
      # - name: file
      #   copy: dest=/tmp/aaa.txt src=c.txt\
      # - name: createuser
      #   user: name={{ user }}
      #   notify: restart
│   └── start.yml
			# - name: start
      # service: name=nginx state=started enabled=yes
├── templates  # -- 动态文件，需要传递参数  拷贝nginx配置文件cp /etc/nginx/nginx.conf . 
│   └── nginx.conf  # yum install -y nginx下载并将配置文件弄一弄
└── vars      # -- 变量
    └── main.yml
  			# {"user":jason70}

data/nginx.ym
	# - hosts: web
  #   roles:
  #   - nginx
	
# nginx中worker_connections默认1024，理论最大在100万左右，再多nginx就无法正常启动了
# nginx中listen监听ipv4和ipv6，default_server含义:nginx默认多个server，访问使谁写了default_server就返回谁
# 上面的代码如果演示不成功 将nginx配置文件中的default_server删除即可
```

查找顺序

- 主文件看到roles，就会去roles目录下面找对应的目录
- 先去tasks目录里面找main.yml入口文件，如果遇到import_task则加载任务
- 如果遇到了template，则去templates目录里面找文件
- 如果遇到了copy，则去files目录里面找文件
- 如果遇到了变量，则去vars目录里面找main.yml文件
- 如果遇到了notify，则去handlers目录里面找main.yml文件

### ansible-galaxy

**别人写好的roles文件参考网站:**<https://galaxy.ansible.com/>

下载nginx相关roles文件:ansible-galaxy install geerlingguy.nginx

查看文件找寻固定格式

```shell
cd /root/.ansible/roles/geerlingguy.nginx
ll
vi tasks/main.yml  # 查看yml配置
```



# nginx+uwsgi介绍

```python
pip list  # 查看安装过的模块
rpm -q nginx  # 查看是否安装某款服务

pip install django == 1.11.11  # 安装django并指定版本
yum install -y nginx  # 安装nginx

"""单独在一台被控机上测试"""
mkdir /data
cd /data/

# 命令行创建django项目
django-admin startproject mysite
cd mysite/
python manage.py startapp app01

# 修改配置文件
ALLOWED_HOSTS = ["*"]
DEBUG = False
注册app01

# 启动访问
python manage.py runserver 0.0.0.0:8080  # 需要关闭防火墙 iptables -F

# django默认使用的wsgiref并发量太小 换成uwsgi
pip install uwsgi  # 可保持django运行 重新开设xshell窗口安装即可
# 报错 需要下载python-devel(开发必备的包) 秉持原则:缺什么装什么不用的别装  然后重新安装即可
yum install -y python-devel

  
# 启动uwsgi 需要切换到项目目录下
uwsgi --http :8090 --module mysite.wsgi
# 将uwsgi服务写入配置文件中
vi /etc/uwsgi.ini  
"""
[uwsgi]
http = 0.0.0.0:8000
# the local unix socket file than commnuincate to Nginx
# socket = /data/mysite/mysit.socket
# the base directory (full path)
chdir = /data/mysite
# Django's wsgi file
wsgi-file = mysite/wsgi.py
# maximum number of worker processes
processes = 4
#thread numbers startched in each worker process
threads = 2
# clear environment on exit
vacuum          = true  # uwsgi关闭之后 将临时生成的文件删除掉
daemonize = /data/mysite/uwsgi.log  # 后台启动 守护进程
py-autoreload=1  # py文件改动 自动重新加载
"""


# 配置文件启动
uwsgi --ini /etc/uwsgi.ini
# nginx做代理  修改配置文件(可以直接修改nginx自带的 也可自定义配置)
vi /etc/nginx/nginx.conf
"""
location / {
	include /etc/nginx/uwsgi_params;
	uwsgi_pass 127.0.0.1:8000;
}
"""
# 重启服务
systemctl restart nginx
# 访问10.0.0.101:80端口报错  针对nginx访问报错  有三种配置方式


# 第一种
# uwsgi的配置   vi /etc/uwsgi.ini
http = 0.0.0.0:8000
# nginx的配置   vi /etc/nginx/nginx.conf
location / {
	proxy_pass http://127.0.0.1:8000;
}
# 重启服务
systemctl restart nginx
# 仍然无法访问  查看系统日志  访问成功日志(access.log)和报错日志(error.log)
tail -f /var/log/nginx/error.log  # 报权限错误
setenforce 0  # selinux安全控件(非常牛逼的认证方式 但实际工作不用)
vi /etc/selinux/config
"""
修改配置
SELINUX=disabled
"""
pkill -9 uwsgi  # 杀掉uwsgi的进程

# 第二种
# uwsgi的配置  vi /etc/uwsgi.ini
socket = 0.0.0.0:8000
# nginx的配置  vi /etc/nginx/nginx.conf
include /etc/nginx/uwsgi_params;
uwsgi_pass 127.0.0.1:8000;
# 重启服务
systemctl restart nginx
  
# 第三种
# uwsgi的配置  vi /etc/uwsgi.ini
socket = /data/mysite/mysite.socket
# nginx的配置  vi /etc/nginx/nginx.conf
include /etc/nginx/uwsgi_params;
uwsgi_pass unix:/data/mysite/mysite.socket;
# 重启服务
systemctl restart nginx
```



# Celery

## 什么是Clelery

Celery是一个简单、灵活且可靠的，处理大量消息的分布式系统

专注于实时处理的异步任务队列

同时也支持任务调度

## 架构组成部分

- #### **消息中间件（message broker）**

  Celery本身不提供消息服务，但是可以方便的和第三方提供的消息中间件集成。包括，RabbitMQ, Redis等等

- #### **任务执行单元（worker）**

  Worker是Celery提供的任务执行的单元，worker并发的运行在分布式的系统节点中。

- #### **任务执行结果存储（task result store）**

  Task result store用来存储Worker执行的任务的结果，Celery支持以不同方式存储任务的结果，包括AMQP，Redis等

celery只提供worker，其他两个部分由第三方提供

## 安装

提示:celery由于是个小组织在维护暂时没有足够的经费，所以默认不支持windows，可以借助于第三方模块eventlet实现兼容

```python
pip install celery
pip install eventlet
```

## 基本使用

```python
# s1.py  
from celery import Celery
c = Celery('task',broker='redis://127.0.0.1:6379/2')
@c.task
def myfunc1():
    return 'myfunc1'
@c.task
def myfunc2():
    return 'myfunc2'
@c.task
def myfunc3():
    return 'myfunc3'

# s2.py  
from s1 import myfunc1,myfunc2,myfunc3
s = myfunc1.delay()
print(s)
```

命令行启动worker:celery worker -A s1 -l info

windows上需要加安装的脚手架，命令稍微变化一下:celery worker -A s1 -l info -P eventlet

右键执行s2.py文件得到任务uuid号，利用range新增多个消费者

新建命令行新增worker启动s2查看接受任务个数:celery worker -A s1 -l info(celery worker -A s1 -l info -P eventlet)

## 进阶

异步任务提交的结果需要回调机制进行处理，需要用到backend

```python
c = Celery('task',broker='redis://127.0.0.1:6379/2',backend='redis://127.0.0.1:6379/0')
```

命令行获取任务id号，

redis查看结果

```python
redis-cli  -h 192.169.226.133
select index
keys *
get key  # 结果斜杠 起转义效果
```

项目中查看结果

```python
# s2.py  
from s1 import myfun1,myfun2,myfun3,c
from celery.result import AsyncResult

s=myfun1.delay(10,20)
print(s.id)
r=AsyncResult(id=s.id,app=c)
# 获取状态
print(r.status)
print(r.successful())
# 获取值
print(r.get())
# 只获取报错信息
print(r.get(propagate=False))
# 获取具体出错的位置
print(r.traceback)
```

## Celery延时任务

```python
# s1.py
from celery import Celery
import time
c=Celery("task",broker="redis://127.0.0.1:6379/0",backend="redis://127.0.0.1:6379/1")

@c.task
def myfun1(a,b):
    return f"myfun1{a}{b}"
@c.task
def myfun2():
    return "myfun2"
@c.task
def myfun3():
    return "myfun3"
  
# s2.py
from s1 import myfun1,myfun2,myfun3,c
from celery.result import AsyncResult

#指定多长时间以后执行
# s=myfun1.apply_async((10,20),countdown=5)

#第二种方式，使用utc时间
from datetime import timedelta
from datetime import datetime
ctime = datetime.now()
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
time_delay = timedelta(seconds=10)
task_time = utc_ctime + time_delay
# 延时:生产者直接生产 消费者等相应时间再执行
s=myfun1.apply_async((10,20),eta=task_time)
print(s.id)
```

- celery worker -A celery_task -l info  -P  eventlet
- 执行s2.py文件

## Celery执行定时任务

```python
# s1.py
from celery import Celery
import time
c=Celery("task",broker="redis://127.0.0.1:6379/0",backend="redis://127.0.0.1:6379/1")

@c.task
def myfun1(a,b):
    return f"myfun1{a}{b}"
@c.task
def myfun2():
    return "myfun2"
@c.task
def myfun3():
    return "myfun3"
  
# s2.py
from s1 import c
from celery.beat import crontab
c.conf.beat_schedule = {
    "name": {  # 任务名称
        "task": "s1.myfun1",  # 需要执行的任务
        "schedule": 3,  # 间隔时间
        "args": (10, 20)  # 给任务传参
    },
    "crontab": {
        "task": "s1.myfun1",
        "schedule": crontab(minute=44),   # 时间也可以是crontab格式
        "args": (10, 20)
    }
  	# 'add-every-12-seconds': {
    #     'task': 'celery_task.tasks1.test_celery',
    #     每年4月11号，8点42分执行
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'args': (16, 16)
    # },
}
```

- 启动一个beat(celery beat -A s2 -l info)
- 启动work执行(celery worker -A s1 -l info -P  eventlet)

# django结合celery一起使用(了解)

* 新建django(mydjango)项目，在项目目录下新建一个名字必须叫celery的py文件

  ```python
  from __future__ import absolute_import, unicode_literals
  import os
  from celery import Celery
  
  # set the default Django settings module for the 'celery' program.
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydjango.settings') #与项目关联
  
  app = Celery('tests',backend='redis://127.0.0.1:6379/0',broker='redis://127.0.0.1:6379/1')
  # redis可以修改配置文件设置密码 
  """
  vi /etc/redis.conf
  解开注视requirepass 密码
  重启redis:systemctl restart redis
  命令行:auth 密码 完成身份验证
  书写配置:redis://:密码@127.0.0.1:6379/0
  """
  #创建celery对象
  # Using a string here means the worker doesn't have to serialize
  # the configuration object to child processes.
  # - namespace='CELERY' means all celery-related configuration keys
  #   should have a `CELERY_` prefix.
  app.config_from_object('django.conf:settings', namespace='CELERY')
  #在django中创建celery的命名空间
  # Load task modules from all registered Django app configs.
  app.autodiscover_tasks()
  #自动加载任务
  ```

* 编辑同级别目录下的init文件

  ```python
  from __future__ import absolute_import, unicode_literals
  from .celery import app as celery_app
  
  __all__ = ['celery_app']
  ```

* 在创建的应用下新建tasks.py文件夹

  ```python
  from celery import shared_task
  
  @shared_task
  def add(x, y):
      return x + y
  
  @shared_task
  def mul(x, y):
      return x * y
  
  @shared_task
  def xsum(numbers):
      return sum(numbers)
  ```

* views文件中新增视图函数

  ```python
  from .tasks import add
  from celery.result import AsyncResult
  from mydjango.celery import app
  
  def index(request):
      result = add.delay(2, 3)
      ret = AsyncResult(id=s.id,app=app)
      return HttpResponse('返回数据{}'.format(ret.get()))
  ```

* 安装组件(定时任务)

  ```python
  pip install django-celery-beat
  ```

* 组册到已经按照的app中

  ```python
  INSTALLED_APPS = (
      ...,
      'django_celery_beat',
  )
  ```

* 执行数据库迁移命令

  ```python
  python3 manage.py makemigrations #不执行这个会有问题
  python3 manage.py migrate
  ```

* admin访问后台

  添加表信息，注意每次新增任务必须重启celery

* 启动beat

  ```python
  celery -A mydjango beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
  ```

* 启动worker

  ```python
  celery worker -A mydjango -l info 
  ```

补充:默认是监听单个py文件，也可以监听目录

```python
app = Celery('tests',backend='redis://127.0.0.1:6379/0',broker='redis://127.0.0.1:6379/1',include=['py文件路径1','py文件路径2'])
# redis可以修改配置文件设置密码 
```



# 网络基础

以ipv4为例:4个字节，32位二进制数

网络位:用来表示在哪个网段

主机位:用来表示网段中的某一台主机

ip地址 = 网络位 + 主机位

共有地址:所有人都可以访问到

私有地址:同一个局域网内才能访问到

### 分类

* A类	

  超大型网络 

  ```python
  """
  前八位网络位，后24位主机位
  可用主机 2**24 - 2 (0.0.0.0 , 1.1.1.1)
  网络位 1～126 127作为回环地址
  
  私有地址:10.0.0.0
  """
  ```

* B类     

  大型网络

  ```python
  """
  前16位网路位，后16位主机位
  可用主机 2**16 - 2
  网络位 128~191
  
  私有地址:172.16~172.31
  """
  ```

* C类

  小型网络

  ```python
  """
  前24位为网络位 后8位主机位
  可用主机 2**8 - 2
  网络位 192~223
  
  私有地址：192.168.0～192.168.255
  """
  ```

* D类

  多播(多组广播、组播)

  ```python
  """网络位224~239"""
  ```

* E类

  以留后用

  ```python
  """网络位240~255"""
  ```



# 前端框架AdminLTE介绍



# 发布(部署)流程

- 灰度发布/金丝雀发布

  服务器不止有一台，可能有多台服务器在跑我们的程序(1.0版本)

  从多台服务器中随机抽取一台将上面的程序迭代成1.1版本,开发和测试人员都在这台机器上做测试,当测试没有任何问题的情况下才会讲剩下的全部机器从1.0版本全部变成1.1版本,如果测试有问题，那么只需要将这一台机器做回滚操作到原先的版本即可

  扩展知识:之所以叫金丝雀发布，是因为早起挖矿的时候，矿里面含有瓦斯，而人不易觉察出瓦斯，而金丝雀对瓦斯的敏感度很高，所以在下矿井之前先把金丝雀放下去，如果金丝雀没事那么人在下去，如果有事那么就不下去，以最小的损失来测试环境

  这种发布方式也是目前公司用的比较多的一种发布方式

- 蓝绿发布

  有十台服务器跑着1.0版本的程序，然后再准备10台统一升成1.1版本，在整个一个里面做测试，如果没有问题就直接讲原先的所有的1.0版本升级到1.1版本(好处在于可以讲生产环境上的用户数据请求全部模拟到测试环境中做回放测试)

  这种方式比较浪费资源一般在docker或者k8s中使用

- 滚动发布(很少使用)

  随机抽取机器发布，并且一旦开启就不能暂停，你也无法知道某个时间点到底哪台服务器处于发布状态

- 直接发布

  直接全部升级到最新版本



# 需求分析

- 发布代码
  - git发布
  - 文件发布
- 日志
- 主机管理(cmdb服务器资产管理系统:调用该系统api接口)
- 用户管理(开发，运维，测试人员的权限问题)
- 项目管理(公司一般都会有多个项目)
- 命令管理
- 计划任务
- 初始化
  - 系统初始化
  - 环境初始化

### 

# 模型表设计



# 准备工作

新建django项目

```python
ALLOWED_HOSTS = ['*']  # 允许所有host访问
# 静态文件配置
# 数据库可以选择MySQL或者sqlite
```

使用AdminLTE框架对主页进行模块拆分

```python
-templates
  --master
  	---base.html  # 模版
    ---body_aside.html  # 左侧栏
    ---body_nav.html  # 导航条
    ---css.html  # 主页css链接标签(link)
    ---js.html  # 主页js链接标签(script)
 --home.html  # 继承base.html
```

多功能网站:https://www.toolfk.com

简单回顾js文件夹下面的common文件夹下面的ui.common.js文件，回顾前端知识内容

前端用到的组件:<https://stephanwagner.me/jBox/options>



# 用户增删改查



# 需要安装的包

```python
yum install -y python36-pip python36-devel
pip3 install ansible
# 可能修改的配置文件
vi /etc/sysconfig/network-scripts/ifcfg-ens33
# 添加
IPADDR
NETMASK
```



# 启动项目

```python
python3 test_runner.py
# 阅读初始化代码test_runner.py >>> inventor.py >>> runner.py
# 执行命令直接修改test_runner代码即可 
{"action": {"module": "ping"}
```



# pycharm同步linux代码

pycharm提过了可以链接linux服务器并远程上传代码的功能，还可以设置成自动同步更新

tools	>>>	delevelopment	>>>	configuration	>>>	添加SFTP(填写主机地址)

配置完成后，项目名下右击再点development，可以上传代码也可以下载代码

还可以在tools里面设置自动上传代码Automatice Upload



# 主机的增删改查



# 初始化的增删改查



# 初始化机器的增删改查

```python
"""
1.在机器上有一个/update目录
2.目录里面有git个file两个目录
3.git目录放git代码
4.file目录放上传的文件
5.在新建项目的时候，要判断git目录里面是否有项目，如果有的话则判断是不是git目录，如果不是需要去git_path clone
6.python操作git
7.gitpython
"""

# gitpython模块操作
from git import Repo
from git import Git
# git init
r=Repo("C:\\Users\\Administrator\\Desktop\\derek")

# git add
r.index.add(["issue/utils/gitfile.py"])

# git commit -m
r.index.commit("python 操作git")

# git reset HEAD  将缓存区的内容拉取到工作区
# git checkout filename 将指定文件回滚到最近一次commit的地方
# git reset --hard 将文件回滚到指定的位置
r.index.reset(commit="e11f478c2e99e69969caf6e190751244d7b4608d",head=True)

# git branch
# 获取所有的分支
print([str(b) for b in r.branches])

# git tag
print(r.tags)

# 当前分支
print(r.active_branch)
r.index.checkout("dev1")

# git clone
Repo.clone_from()

# git tag -a
r.create_tag("v1.3")

# git branch dev4
r.create_head("dev4")

# git log
print([i.hexsha for i in r.iter_commits()])

git push origin master
r.remote().push("master")

# git pull origin master
r.remote().pull("master")
```

# 项目的增删改查



# 命令展示前端页面实现+命令下发后端展示

前端勾选插件:ztree

右侧目录栏展示:adminlte黑色面板

前端页面获取用户输入并传递至后端



# 计划任务增删改查

#### 前端页面展示(cron_create.html)

#### 后端业务逻辑(cron.py)



# 项目详情简介

project-detail.html



# 发布详情页面



# git



# 发布之nginx下线



# 发布之server发布



# 更新剩余机器



# 回滚








