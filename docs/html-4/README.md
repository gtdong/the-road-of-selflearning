### 文档加载

```js
$(document).ready(function(){
// 在这里写你的JS代码...
})

$(function(){
// 你在这里写你的代码
})
```

### jQuery简介

类似于python里面的模块，帮我们封装了原声js操作DOM的语法

参考博客:<https://www.cnblogs.com/Dominic-Ji/p/10490669.html>

### jQuery能干的事

* 查找标签
* 修改标签属性及样式
* ajax异步请求
* 事件绑定

### jQuery与原生js操作标签简易程度对比

```js
var d1Ele = document.getElementsByTagName('div')[0];
d1Ele.style.color = 'red';

$('div').css('color','blue');
```

### jQuery使用步骤

* 必须先利用script标签src属性导入jquery文件或者使用cdn(内容分发网络)直接访问
* 在按照jquery固定的语法结构操作即可($(选择器).action())

Ps:需要了解的是jquery类似于python里面的模块，模块在导入使用的时候是模块名前缀的方式，其实jquery也是如此jquery()，只是为了书写方便，将jquery直接以$代替了，两者等价。

### jQuery基本选择器的使用

```js
$('div')
$('.c1')
$('#d1')
```

### jQuery对象与原生js对象的异同

```js
// jQuery对象是数组，按照索引取出里面的单个元素就是原生的js对象
// js转jQ
$(d1Ele)
// jQ转js
$('div')[0]
```

### jQuery属性查找

参考博客:https://www.cnblogs.com/Dominic-Ji/p/10490669.html

* 三种基本选择器
* 层级选择器
* 基本筛选器



* 样式操作

  ```js
  addClass();// 添加指定的CSS类名。
  removeClass();// 移除指定的CSS类名。
  hasClass();// 判断样式存不存在
  toggleClass();// 切换CSS类名，如果有就移除，如果没有就添加。
  ```

* 模态框示例(js+jq)

  

* 表单筛选器

  ```js
  # 针对表单内的标签
  $('input[type="text"]')
  # 简化写法
  $(':text')
  
  # 找到所有被选中的checkbox
  $(':checkbox')  # 注意select框中默认selected标签也会被找到
  $('input:checkbox')
  ```

* 筛选器方法

  ```js
  # 避免$('input:first')太麻烦
  $('input').first()
  
  $("#id").next()
  $("#id").nextAll()
  $("#id").nextUntil("#i2")
  
  $("#id").prev()
  $("#id").prevAll()
  $("#id").prevUntil("#i2")
  
  $("#id").parent()
  $("#id").parents()  // 查找当前元素的所有的父辈元素
  $("#id").parentsUntil() // 查找当前元素的所有的父辈元素，直到遇到匹配的那个元素为止。
  
  $("#id").children();// 儿子们
  $("#id").siblings();// 兄弟们
  ```

* jquery链式操作

  ```js
  # 一行代码实现第一个p变红，第二个p变绿
  <div>
  	<p>p1</p>
  	<p>p2</p>
  </div>
  
  $('div>p').first().addclass('c1').next().addclass('c2');
  ```

### jQ操作CSS

```js
// 一个参数获取属性
$('#p1').css('font-size')
// 两个参数设置属性
$('#p1').css('font-size','24px')


// 一次设置多个属性
$('#p1').css({"border":"1px solid black","color":"blue"})
```

### 位置操作

* 相对定位:相对原来的位置(不脱离文档流)
* 绝对定位:相对已经定位过的父标签(脱离文档流)
* 固定定位:相对于浏览器窗口固定在某个位置(脱离文档流)

```js
// 不加参数获取位置参数
$(".c3").offset()
// 加参数设置位置参数
$(".c3").offset({top:284,left:400})

// position只能获取值，不能设置值

// scrollTop获取当前滚动条偏移量
$(window).scrollTop();
$(window).scrollTop(0);  // 设置滚动条偏移量
```

### 尺寸

盒子模型

```js
height()
width()
innerHeight()
innerWidth()
outerHeight()
outerWidth()
```

### 文本操作

```js
# text()与html()

# val()  输入框内部的文本值
```





### 自定义登陆校验

jquery绑定事件实现简介

取消标签自带的事件效果

```html
<form action="">
  <div>
    <label for="input-name">用户名</label>
    <input type="text" id="input-name" name="name">
    <span class="error"></span>
  </div>
  <div>
    <label for="input-password">密码</label>
    <input type="password" id="input-password" name="password">
    <span class="error"></span>
  </div>
  <div>
    <input type="button" id="btn" value="提交">
  </div>
</form>
<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
<script>
  $("#btn").click(function () {
    var username = $("#input-name").val();
    var password = $("#input-password").val();

    if (username.length === 0) {
      $("#input-name").siblings(".error").text("用户名不能为空");
    }
    if (password.length === 0) {
      $("#input-password").siblings(".error").text("密码不能为空");
    }
  })
</script>
<!--js代码取消默认事件的方式-->
return false
```

### 属性操作

```js
// 获取文本属性
$('#d1').attr('s1')  // 获取属性值
$('#d1').attr('s1','haha')  // 设置属性值
$('#d1').attr({'num':50,'taidi':'gay'})  // 设置多个属性
$('#d1').removeAttr('taidi')  // 删除一个属性


// 获取check与radio标签的checked属性
$('#i1').prop('checked')
$('#i1').prop('checked',true)
```

### 文档处理

```js
// 标签内部尾部追加元素
$('#d1').append(pEle)
$pEle.appendTo($('#d1'))

// 标签内部头部添加元素
$('#d1').prepend(pEle)
$pEle.prependTo($('#d1'))

// 标签外部下面添加元素
$(A).after(B)// 把B放到A的后面
$(A).insertAfter(B)// 把A放到B的后面

// 标签外部上面添加元素
$(A).before(B)// 把B放到A的前面
$(A).insertBefore(B)// 把A放到B的前面

// 替换标签
replaceWith()  // 什么被什么替换
replaceAll()  // 拿什么替换什么



// this参数补充知识
// 克隆事例
<button id="b2">屠龙宝刀，点击就送</button>
// clone方法加参数true，克隆标签并且克隆标签带的事件
  $("#b2").on("click", function () {
    $(this).clone(true).insertAfter(this);  // true参数
  });
```





### jQuery事件绑定

```js
// hover事件
$('p').hover(  // 写两个函数一个表示鼠标移进去，另一个标示鼠标移出来
  function () {
    alert('来啦，老弟')
  },
  function () {
    alert('慢走哦～')
  }
)
// input实时监听
    $('#i1').on('input',function () {
        console.log($(this).val())
    });
// focus/blur 其他同理js事件

// 取消标签默认的事件(两种方式)
return false
$('input').click(function (e) {
        alert(123);
        // return false
        e.preventDefault();
    });



// 事件冒泡
div>p>span  // 三者均绑定点击事件

$("span").click(function (e) {
        alert("span");
        e.stopPropagation();  // 阻止事件冒泡
    });

// 事件委托
<button>按钮</button>
<script src="jQuery-3.3.1.js"></script>
<script>
    $('body').on('click','button',function () {
        alert(123)
    })
</script>
```

### jQuery自带的动画效果

```js
$('img').hide(5000)
$('img').show(5000)

$('img').slideUp(5000)
$('img').slideDown(5000)


$('img').fadeIn(5000)
$('img').fadeOut(5000)
$('img').fadeTo(5000,0.4)
```

### each()

```js
$.each(array,function(index){
  console.log(array[index])
})

$.each(array,function(){
  console.log(this);
})

// 支持简写
$divEles.each(function(){
  console.log(this)  // 标签对象
})
```

### data()

```js
$("div").data("k",100);//给所有div标签都保存一个名为k，值为100
$("div").data("k");//返回第一个div标签中保存的"k"的值
$("div").removeData("k");  //移除元素上存放k对应的数据
```





### Bootstarp框架

参考网址:<https://v3.bootcss.com/getting-started/>

#### 使用

* 下载生产环境下的文件
* cdn访问

#### 文件划分

* js:只需要留一个bootstrap.min.js即可
* css:只需要一个bootstrap.min.css即可
* Fonts:一个都不要删

**注意:**bootstrap中的js文件依赖于jQuery，所以使用bootstrap需要先导入jQuery

### 实际网站精选

### 布局容器

### 栅格系统

### 媒体查询

```css
<style>
				.c1 {
            background-color: red;
        }
        @media screen and (max-width: 600px){
            .c1 {
                background-color: green;
            }
        }
</style>				
<div class="col-md-6 red c1"></div>
```

### 响应式列重置



### 表格标签

### 表单

### 按钮

### FontAwesome图标库使用(只需要留css和fonts文件夹)

### SweetAlert使用

https://lipis.github.io/bootstrap-sweetalert/

下载完成后只需要用dist文件夹即可









































