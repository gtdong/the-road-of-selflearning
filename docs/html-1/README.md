# 前端 （html，css， js）

重要性：  
	a. 前段和前面的Python没有任何关系  
	b. 前端语言的学习比python要简单很多  
	c. 前端不好好学， 后面项目没法做  
	d. 上面三个非常重要

## html
### 介绍  
- 20个左右的标签  
- 相当于人体的骨架  
- 浏览器认识的一组规则   
- 浏览器执行的时候， 从上到下依次解释执行 （浏览器中html解释器）  
- 学习20个左右的规则  

编写html代码：  
	- 文件后缀建议以.html结尾  

运行：  
	1.pycharm打开网页  
	2.本地找到网页， 打开即可看到效果  
标签：

```html
<!--整体结构-->
<!DOCTYPE html>
<html lang="en">
<head>头部描述信息
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
真实的内容
</body>
</html>
```
```html
<!DOCTYPE html>： 解释器 html5

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd"> ： 解释器： html4
head中的标签：
meta描述网页元信息：
<meta charset="UTF-8">  ： 字符编码

seo： 
<meta name="keywords" content="开发者,博客园,开发者,程序猿,程序媛,极客,编程,代码,开源,IT网站,Developer,Programmer,Coder,Geek,技术社区" />
<meta name="description" content="博客园是一个面向开发者的知识分享社区。自创建以来，博客园一直致力并专注于为开发者打造一个纯净的技术交流社区，推动并帮助开发者通过互联网分享知识，从而让更多开发者从中受益。博客园的使命是帮助开发者用代码改变世界。" />

keywords和description用于提高网站在搜索引擎中的排名

<title>Title</title>
<link /> 
<script></script> 
						
```	
### 分类 
```html 
单闭合标签：  
	eg: <meta charset="UTF-8">   
双闭和标签：  
	eg: <title>Title</title>  

字体以及排版标签：
	<p></p>   ： 段落标签
	<br/> ： 换行标签
	<hr/> ： 华丽丽的分割线
	h1 , h2, h3,...h6 : 变大 变粗
```
### 无序列表：
```html
<ul type='circle'>
	<li>123</li>
	<li>内容</li>
	<li>456</li>
	<li>789</li>
</ul>
	
type属性：disc(实心圆点)(默认)、circle(空心圆圈)、square(实心方块)
```
### 有序列表：
```html
<ol type="i">
	<li>123</li>
	<li>内容</li>
	<li>456</li>
	<li>789</li>
</ol>
	
type编号类型，默认为整数。可选（1、A、a、Ⅰ、i）
```
### 超链接
```html
<a href="http://www.baidu.com" target="_blank">调到百度</a>
<a href="./aaa.html">跳到aaa</a>
							
href: 要跳转的资源地址
target: _blank : 新开一个页面跳转
```
### div和span元素
```html
    a. 作用是需要和CSS配合使用的
    b. 块级标签 和 行内标签：
	    块级标签： 是要独占一行
		    div， p， h1---h6, ul ol
	    行内标签： 占自己内容的宽度
		    span, a, img
```
### img
```html
<img src="./my.jpeg" width="200px" height="100px"/>
```
### 表格
```html
<table border="1px">
<!--        thead ： 表头-->
<thead>
<!--           tr： 一行数据-->
	<tr>
<!--                td: 单元格 写具体的内容-->
		<td>ID</td>
		<td>名称</td>
		<td>年龄</td>
	</tr>
</thead>
<tbody>
	<tr>
		<td>1</td>
		<td>zekai</td>
		<td>18</td>
	</tr>
	<tr>
		<td>2</td>
		<td>zekai2</td>
		<td>18</td>
	</tr>
	<tr>
		<td>3</td>
		<td>zekai3</td>
		<td>18</td>
	</tr>
</tbody>

</table>

tr: 一行数据
td： 具体的单元格数据内容
th: 讲表头的内容加粗

border： 表格加边框
width： 表格的宽度
height： 高度
align： center  left right
```

### form表单		
#### 常见的input标签
```html
<!--单行文本输入框-->
<input type="text"/>  

<!--密码输入框-->	
<input type="password"/>   

<!--复选框-->	
<input type="checkbox" checked='checked'/>    

<!--单选框-->	
<input type="radio"/>		

<!--提交按钮-->
<input type="submit" value='提交'/>	

<!--重置按钮-->	
<input type="reset" value='重置'/>	

<!--普通按钮-->
<input type="button" value=“普通按钮”/>	

<!--隐藏按钮-->
<input type="hidden" value=“隐藏按钮”/>	

<!--文本选择框-->	
<input type="file"/>
```


#### http的两种常见方式
```
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
```

#### 例子

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

```html
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
				   
```
## css：
- 样式  
- 相当于穿一件华丽的衣服  

## javascript （js） 
- 相当于让人动起来
