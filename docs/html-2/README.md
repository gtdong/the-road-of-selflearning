```

   html常用标签之form表单元素标签
      1.form表单的基本概念
         和后台进行交互的元素
      
      2.常见的input标签
         <form action='url地址' method='get/post'>
            文本框: <input type='text' name='username'>
            密码框: <input type='password' name='pwd'>
            复选框: <input type='checkbox' name='hobby'>  足球
                  <input type='checkbox' name='hobby'>  篮球
                  <input type='checkbox' name='hobby'>  羽毛球
            单选框: <input type='radio' name='gender'> 男
                  <input type='radio' name='gender'> 女
             性别: <input type="radio" name="gender" value="1" checked>男
                  <input type="radio" name="gender" value="0">女
                  <input type="file" >
                  <input type="hidden" name="token" value="dsadnsajdnskandksandskankdsandsjakndsa" /><br>

                  <select name="city" >
                     <option value="bj">北京</option>
                     <option value="tj" selected="selected">天津</option>
                     <option value="hb">河北</option>
                     <option value="sd">山东</option>
                     <option value="nm">内蒙</option>
                  </select><br>

                  <textarea cols="50" rows="30" name="content">

                  </textarea>
            普通按钮: <input type='button' value='普通按钮'>
            提交按钮: <input type='submit' value='提交'>
            重置按钮: <input type='reset' value='重置'>
         </form>
      
         http的两种常见方式:
            get / post 
            
            get方式:
               - form表单中, method如果不写, 默认是get方式, 还可以method='get'
               缺点:
                  - 传输的内容明文 , 不太安全
                  - 浏览器对url的长度有限制 (chrom 限制4096个字节 其他限制1024)
               
               http底层:
                  请求头:
                     GET / HTTP/1.1
                     Host: localhost:8000/?username=zekai&pwd=123qwe
                     Connection: keep-alive
                     Cache-Control: max-age=0
                     Upgrade-Insecure-Requests: 1
                     User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
                     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
                     Accept-Encoding: gzip, deflate, br
                     Accept-Language: zh-CN,zh;q=0.9
                     Cookie: Pycharm-ed91cad7=93847e52-e290-42ae-ac89-b08da95066ed
               
               
            post方式:
               - form表单中, method必须指定为 method=post
               优点:
                  
               
               http底层:
                  请求头:
                     POST / HTTP/1.1
                     Host: localhost:8000
                     Connection: keep-alive
                     Cache-Control: max-age=0
                     Upgrade-Insecure-Requests: 1
                     User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
                     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
                     Accept-Encoding: gzip, deflate, br
                     Accept-Language: zh-CN,zh;q=0.9
                     Cookie: Pycharm-ed91cad7=93847e52-e290-42ae-ac89-b08da95066ed

                  请求体:
                     username=zekai&pwd=123qwe
                  
         属性:
            value: 默认值
            placeholder : html5 的规则  提示语句
         
         默认选中的属性:
            select:
               selected
            checkbox / radio:
               checked

         
         ps:
            当一个中有“上传文件域”，必须指定MIME类型enctype=“multipart/form-data”>，否则无法上传文件上传文件域，只在method=“post”下才有效
               
            type=hidden :  提交一些不想让用户看到的东西到后台,  比如说: token, id 
            
            
      3.select下拉列表
      4.textarea多行文本框
   
   

今日内容:

   补充: &nbsp; 空格
   
   css:
      
      1. 布局方式:
         a. table方式布局
         b. div + table 结合着布局
         c. div + css 进行布局
      
      2. css的概念:
         布局以及样式
      
      3. css的三种引入方式:
         
         a. 直接在标签中写入 行内样式
            <div style="background-color: red; font-size: 25px">helloworld</div>
            
            缺点:
               1. css样式过长
               2. 样式和内容混合, 不便于后期的维护
         b. 内部样式
            css的样式写在head标签中间
            
            <style type="text/css">
               选择器 {
                  (属性)background-color: (属性值)red;
               }
               选择器: 作用域  会对此选择器发生作用
               
               div{
                  background-color: red;
                  font-size: 25px
               }
            </style>
            
            
         c. 外部样式
   
            将css写入到一个单独的文件中, 然后在html中直接引入
            
            html:
               <link rel="stylesheet" href="./a.css">
            css:
                div{
                  background-color: black;
                  font-size: 25px
               }
   
      4. 选择器:
         
         选择器: 作用域  会对此选择器发生作用
               
         div{
            background-color: red;
            font-size: 25px
         }
         
         a. 标签(html标签)选择器
            css:
               div(html标签){
                  font-size: 25px;
                  background-color: bisque;
               }
            html:
               <div>this is  div</div>
         
         b. ID选择器
            css:
               #i1(id选择器){
                  background-color: red;
               }
            html:
               <div id="i1">ndsandjsanjdsnajd</div>
            
            注意:
               ID应该是唯一的  才有意义
   
         c. 类别选择器:
            css:
               .c1{
                  font-size: 25px;
                  background-color: green;
               }
            html:
               <div>this is  div</div>
               <div class="c1">ndsandjsanjdsnajd</div>
               <div>djskadksamfk</div>
               <div class="c1">ry8ewr8ewq</div>
               <div class="c1">hfgldhglfd</div>
         
         d. * {margin:0;padding:0;}

            将网页上所有的元素运用上此样式
            
         e. 包含选择器:
            css:
               .i1 span {
                  background-color: coral;
               }
            html:
               <div class="i1">
                  <span>this is span</span>
               </div>
               <div class="c1">ndsandjsanjdsnajd</div>
               <span>bdjsabjdsbajdsja</span>
      
         f.分组选择器
                css:
               .c1,span{
                  color: red;
               }
            html:
               <div class="c1">ndsandjsanjdsnajd</div>
               <span>bdjsabjdsbajdsja</span>
         
         g.伪类选择器:
            css:
               a:hover{
                  color: red;
               }
               a:active{
                  color: green;
               }
               a:visited{
                  color: aquamarine;
               }
            html:
               <a href="http://www.baidu.com">跳转到百度</a>
   
         h. 优先级:
            行内样式 > ID选择器 > 类别选择器 > 标签选择器  > 通配符选择器
            css:
                #show1{color:gold;}
               .show {color:pink;}
               /*h1 {color:red;}*/
               * {color:green;}
            html:
                <h1 id="show1" class="show" style="color:gray;">优先级测试</h1>

      段落(文本)属性和边框以及背景属性

         1. 边框:
            border: 1px solid red;
            如果你不知道你所占的div的大小的时候, 可以使用border
         
         2. 文本属性:
            font-size: 设置字体的大小
            color: 设置字体的颜色
            text-align : left/right/center
            line-height: 行高  字体居中显示   取值应和height的值一样
            text-decoration: underline/line-through/overline
            
         3. background-color: 颜色
            颜色的取值:
               a. 颜色的英文名 (red/yellow等)
               b. 十六进制 (#dddddd)
               
               color:#292378; //6个十六进制数获得颜色
               color:#A64; //#AA6644的缩写
               color:red; //颜色关键字定义颜色
               color:rgb(100,159,170); //rgb定义颜色
         
            ps: chrome控制台可以获取你想要的颜色
         
         4. 背景图像:
            background-img:
               background-image: url("aaa.png");
               background-repeat: repeat-y;
               background-position-y: 图像位置  距离浏览器窗口顶部的距离
               
               background-position-x: 图像位置  距离浏览器左边的距离
               
               
         以下属性只对块级元素发生效果    
            
         5. 布局属性:
             
            外边距:
               一个div和另一个div之间的距离
               
               margin-top: 上边距
               margin-bottom: 下边距
               margin-left: 左边距
               margin-right: 右边距
               
               margin : 10px  : 上下左右  都是10px
               margin : 10px 20px; 上下是10px 左右是20px
               margin : 10px 20px 30px   
                     margin-top: 10px;
                     margin-right: 20px;
                     margin-bottom: 30px;
                     margin-left: 20px;
               margin : 10px 20px 30px 40px;
               
            
            内边距:
               padding-top:10px;   文字距离div顶部的距离
               padding-left:20px;  文字距离div左边的距离
               padding-right:20px;
               padding-bottom: 30px;
               
               
               
               padding: 10px; 上下左右  都是10px
               padding : 10px 20px; 上下是10px 左右是20px
               padding : 10px 20px 30px   
                     margin-top: 10px;
                     margin-right: 20px;
                     margin-bottom: 30px;
                     margin-left: 20px;
               padding : 10px 20px 30px 40px;
      
      
            *{
               margin:0;
               padding:0;
            }
            
            取消自带的留白
      
         6. 浮动属性:
            
            float: left / right;
            
            如果儿子飘起来, 老子管不住:
                <div style="clear: both"></div>
            
         7. display:
            display: block;  设置行内元素成一个块级元素
            display: inline; 设置块级元素成一个行内元素
            display: inline-block; 此元素分别具有块级元素和行内元素的特性
      
         
         8. overflow溢出处理属性

            overflow: auto; 自动设置滚动条
               
            overflow: none: 自动隐藏超出的部分
         
         9. 定位属性
            
            position : fixed/ releative/ absolute
               top: 0;
               left: 0;
               right: 0;
               bottom:0;
            
            releative: 基于自己原来的位置进行定位, 单独使用没有任何的意义
            
            absolute 是要和releative配合使用的
            
            （祖先元素的定位方式（relative）来进行定位

               找祖先元素是否有定位，如果没有定位，找到<body>，就相对body来定位
               如果找到祖先元素有定位，相对祖先元素来定位
      
      
         补充:
            border-radius: 50% : 图像变圆角
      
   
   
   作业:
      
   
   
   
   javascript:























   
   
   
```