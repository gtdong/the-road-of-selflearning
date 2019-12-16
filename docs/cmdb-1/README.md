自动化运维开发： devops
	cmdb day01
	

一、为什么要做cmdb？
	
	1. 项目上线的流程：
            
        
        调研需求分析 ---》 开会确定日期 ---》 开发程序 ---》 项目测试人员 ---》代码上线（运维来负责）
        
        传统上线方式：
            直接代码解压 ，启服务， 访问项目， 进行测试
            
            弊端：
                
                - 手工上线  运维来干预 
                - 加机器， 需要重复进行代码的部署
        
            优化策略：
                代码上线系统 
                
                必要条件：需要知道服务器的信息 （服务器的主机名， 硬盘大小。。。）
                
         
    2. 一个公司即将上市， 审查公司的资产 
        
        传统方式,统计公司服务器资产的方式：
            excel表格 
                最后信息会变得不准确
                导致年底进行审计的时候，资产变得无法进行准确的统计
                
                
    CMDB：
        
        配置管理数据库
        
        记录服务器的资产信息（包括 机架位置， 主机名，硬盘， 网卡， 产品线， 管理员等）的
        
        位置：
            是自动化运维的基石
            
            
二、cmdb实现的方案：
        核心的代码：
            1. linux相关的命令   megacli 
            2. Python的代码执行linux命令， 得到结果返回给服务端
            
        业内：
            4套实现方案
        
        
        三套方案全部实现
        
        
        目标：
            
            写一份代码， 通过改变配置实现三套方案
            
            客户端的采集
 三、代码实现：
 
        目录结构：
            
            bin  ： 核心的启动文件  start.py 
            conf : 配置文件夹  
            lib  ：库文件 
            log  : 不建议将日志文件夹放在项目中   /var/log  mkidr /logs/cmdb/
            src  : 核心的源代码目录
            test : 开发的过程中， 需要进行代码的调试 
            
            
        1. 高级配置文件的实现 ：
            
            django的配置：
                from django.conf import global_settings, settings
                settings.TIME_ZONE
                
                将自定制的配置和全局的配置集成在一个对象上， 之后想要使用任何属性的时候， 直接可以通过此对象获得
            
            技术要点：
                
                getattr : 反射获取 对应的值
                setattr : 反射设置
                
        
        2.  编程思想：
            
                高内聚低耦合
                    
                    写一个类或者一个函数的时候， 我们需要明确一下次函数或者此类主要负责干啥的
                    
                    class User():
                        #### 和用户相关的一些逻辑
                        
                        def getUserInfo():
                            #### 获取用户的信息
                            
                            ### 处理订单相关的业务逻辑
                            
                    
            
                可插拔式的配置：
                    settings.py:
                        PLUGINS_DICT = {
                            "basic" : 'src.plugins.basic.Basic',
                            "disk" : 'src.plugins.disk.Disk',
                            "memory" : 'src.plugins.memory.Memory',
                            "nic" : 'src.plugins.nic.Nic',
                            "cpu" : 'src.plugins.cpu.Cpu'
                        }
                        参考django的中间件
                    
                        def execute(self):

                            for k, v in self.plugins_dict.items():
                                '''
                                k: basic 
                                v: src.plugins.basic.Basic  字符串
                                '''
                                module_path, cls_name = v.rsplit('.', 1)
                                module = importlib.import_module(module_path)  #### 导入路径
                                cls = getattr(module, cls_name)   ##### 获取对应的类名
                                cls().process()    #### 执行该类对应的方法
            
                        插件的代码：
                        

                            class Memory():

                                def process(self):
                                    print('memory')
            
        
        
        3. 插件代码重复：
            
            解决的方法：
                1. base.py 写一个基类， 所有的插件继承这个基类， 只需要执行该基类中的方法
                
                2. 
        
            
        
            
        
        
        
        
        

        
