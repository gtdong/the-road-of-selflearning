
## js
### 1. js书写的格式:
```html
css:

    style

js:

   <script>
            ....js的代码
   </script>
 ```
### 2. 放置的位置
```html 
css:
    head标签中

js:
    1. head标签中
    2. 可以放置在body之后  (推荐)
```
            
### 3. 引入第三方的js文件
```html
<script src="js的资源路径"></script>
```
    
### 4. 使用分号
```html
console.log('helloworld');
注意:
    建议大家在写js代码的时候, 加上分号
```
### 5. 以后写js代码的选择
```html
a. 编辑器 (pycharm) (永久生效)
b. console 开发者平台编写 (临时测试的js代码)
```
        

### 6. js的基础


#### a.变量声明
```html
python:
    name = 'zekai'
js:
    var name = 'zekai'

变量名命名的时候:
    可以使用 _，数字，字母，$ 组成，且不能以数字开头
```

#### b.JS变量类型
```html
python:
    字符串  str
    整型     int
    浮点型   float
    布尔    bool  True False
    列表    list
    字典    dict
    元组    tuple
    集合    set

js:
    字符串  str

        var name = 'zekai'  ## 字符串类型

            obj.length　　　　　　　　　　　　　　　长度  
            obj.trim()　　　　　　　　　　　　　　　移除空白
            obj.trimLeft()
            obj.trimRight()
            obj.charAt(n)　　　　　　　　　　　　　返回字符串中的第n个字符
            obj.concat(value, …)　　　　　　　　 拼接
            obj.indexOf(substring,start)　　　　子序列位置
            obj.substring(from, to)　　　　　　　根据索引获取子序列
            obj.slice(start, end)　　　　　　　　切片
            obj.toLowerCase()　　　　　　　　　　大写
            obj.toUpperCase()　　　　　　　　　　小写
            obj.split(delimiter, limit)　　　　　分割

    整型     int
        var age = 12  ### 整型

    浮点型   float
        var salary = 34.23

    布尔    bool
        var b = true /false

    数组    array
        var arr = ['zekai', 12, 'jjjj'];

            obj.length 数组的大小
            obj.push(ele) 尾部追加元素
            obj.pop() 尾部获取一个元素
            obj.unshift(ele) 头部插入元素
            obj.shift() 头部移除元素
            obj.slice( ) 切片
            obj.reverse( ) 反转
            obj.join(sep) 将数组元素连接起来以构建一个字符串
            obj.concat(val,..) 连接数组
            obj.sort( ) 对数组元素进行排序

    字典(json)    dict
        var d = {"name":'zekai', 'age':18}
```
#### c.运算符介绍
```html
算数运算符
    + - * %

    a++ ===> a += 1


    a-- ===> a -= 1

比较运算符:

    >   >=   <    <=    !=    ==    

    ===   : 全等  
        var a = 10;

        var b = "10";

        a == b
        true
        a === b
        false

    !==
赋值运算符

    =  +=   -=  *=   /=

    a+=1 ====> a = a + 1
```

#### d.流程控制
```html
顺序

分支
    if else if else



    python:

        分支:
            if 表达式判断:
                ...
            elif 表达式判断:
                ....
            elif 表达式判断:
                ....
            else:
                ....

    js:
        分支:

            var age = 18;

            if (age > 20){
                console.log('太大了');
            } else if (age >40 && age<50){
                console.log('xxxx')
            } else{
                console.log('xxxxxxxxx')
            }

循环

    python:

        for i in item :
            print(i)

        while


    js:

        数组:
            var arr = ['凤姐', '龙哥', '张三']

            第一种循环:
                for (var i in arr){
                    console.log(arr[i]);
                }

            第二种循环:

                for (var i=0; i<arr.length; i++){
                    console.log(arr[i]);
                }

        字典:
            var d = {"name":'zekai', 'age':18};

            第一种循环:
                for (var i in d){
                    console.log(d[i]);
                }

            第二种循环:

                不可以
   ```

#### e.函数
```html
python:
    def test():
        print('helloworld')

js:

    第一种方式:
        function test(){
            console.log('xxxxxxx');
            return 'xxxx'
        }

        也是有返回值
        test();

    第二种方式:

        var test1 = function (){
            console.log('hellotest1');
        }

        test1();
        ps: 阮一峰  http://www.ruanyifeng.com/home.html


ps: 语言和语言之间都是一样的
```


### 7. 类
```html
python:
    class Test():
        pass

    t = Test()

js:

    class Test(){


    }

    var t = new Test();


常见的其他函数:


    在数据传输流程中，json是以文本，即字符串的形式传递的，而JS操作的是JSON对象，所以，JSON对象和JSON字符串之间的相互转换是关键，例如：


    JSON字符串转换成JSON对象：

        var obj = JSON.parse(str); // 序列化

    JSON对象转换成JSON字符串：

        var str = JSON.stringify(obj); // 反序列化

```
## DOM
DOM: document Object model (文档对象模型)

### 1. 获取标签对象的三种方式
```html
        document.getElementById('#id'):
            获取的是单独的对象

        document.getElementsByClass('.class')
            获取的是列表  列表中套对象

        document.getElementsByTagName('div')
            获取的是列表  列表中套对象
```
### 2.  操作标签对象的内容以及属性

#### a.<div id='c1'>dsbhabdsha</div>
```html

    js:
        var obj = document.getElementById('c1')
        obj.innerText

        i1.innerText :  获取内容
        "这个是内容"
        i1.innerText = "设置的内容"  设置内容值

        i1.innerHTML= "<a href='#'>设置的内容</a>";  设置html标签

        获取input系列标签中的value值:
            obj2.value : 既可以设置  也可以获取
```
#### b.  获取属性
```html

        attributes

    获取单个属性值:
        getAttribute('id')

    设置属性值:
        obj3.setAttribute('k2', 'v2');

    删除属性值:
        obj3.removeAttribute('k1')

    type=button:
        disable : 设置是否禁用
```
#### c. // 在特定的时间内, 执行函数
```html
    // setInterval()  ### crontab
    // setInterval("test()", 1000);

    // setTimout()  ## 只执行一次结束  ## at
    //setTimeout("test()", 1000);
```
### 3. 设置css样式:
```html
大颗粒度的设置:
    style:

        .c2{
            xxxx
        }

    js:
        d1.classList.add('c2')  : 添加样式

        d1.classList
        d1.classList.remove('c2'): 删除样式

细颗粒度的设置:

    对象.style.css的属性 = 值:

        两种情况:
            1.
                css: 
                    color: red;
                DOM:
                    obj.style.color = 'red'
            2. 
                css:
                    font-size: 20px;
                    background-position-y

                DOM:
                    obj.style.fontSize = "20px"

```


### 4. 事件:
```html
        onclick: 点击事件
        onmouseover: 鼠标放上去, 触发函数
        onmouseout: 鼠标移开, 触发函数

        obfouces: 获取焦点
        onblur :  失去焦点

    事件的绑定方式:
        DOM1:
            <input type="text" onclik="f1();" >

        DOm2:
            html:
                <input type="text"  id='i1'>

            js:
                var obj = document.getElementById('i1')
                obj.onclick = function (){

                }
```

### 5.  window常见方法:

```html
alert('1234')

confirm('是否确定删除?');

open(): 打开一个网页

location.href = "资源"  ### 跳转到某一个网页

location.reload(): 刷新当前页面
```
                    
