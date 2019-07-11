
## css
- 样式  
- 相当于穿一件华丽的衣服  

### 1.布局方式:
    a. table方式布局
    b. div + table 结合着布局
    c. div + css 进行布局
      
### 2. css的概念:
    布局以及样式
      
### 3. css的三种引入方式:
```html
    a. 行内样式
       直接在标签中写入
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
   ```
   ### 4.选择器:
   ```html
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
```
### 段落(文本)属性和边框以及背景属性
```html
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
            &nbsp 空格

```






















   
   
   
```

