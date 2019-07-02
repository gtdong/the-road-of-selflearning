# 前端 （html，css， js）

重要性：  
	a. 前段和前面的Python没有任何关系  
	b. 前端语言的学习比python要简单很多  
	c. 前端不好好学， 后面项目没法做  
	d. 上面三个非常重要

## html


介绍：  
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
```html
分类：  
	单闭合标签：  
		eg: <meta charset="UTF-8">   
	双闭和标签：  
		eg: <title>Title</title>  

字体以及排版标签：
	<p></p>   ： 段落标签
	<br/> ： 换行标签
	<hr/> ： 华丽丽的分割线
	h1 , h2, h3,...h6 : 变大 变粗

无序列表：
	<ul type='circle'>
		<li>123</li>
		<li>内容</li>
		<li>456</li>
		<li>789</li>
	</ul>
	type属性：disc(实心圆点)(默认)、circle(空心圆圈)、square(实心方块)



有序列表：
	<ol type="i">
		<li>123</li>
		<li>内容</li>
		<li>456</li>
		<li>789</li>
	</ol>
	type编号类型，默认为整数。可选（1、A、a、Ⅰ、i）




超链接：
	<!--超链接-->
	<a href="http://www.baidu.com" target="_blank">调到百度</a>
	<a href="./aaa.html">跳到aaa</a>
							
	href: 要跳转的资源地址
	target: _blank : 新开一个页面跳转

div和span元素：
	a. 作用是需要和CSS配合使用的
	b. 块级标签 和 行内标签：
		块级标签： 是要独占一行
			div， p， h1---h6, ul ol
		行内标签：	占自己内容的宽度
			span, a, img

img:
	
	<img src="./my.jpeg" width="200px" height="100px"/>


						
表格：
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



form表单：			
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
## css：
- 样式  
- 相当于穿一件华丽的衣服  

## javascript （js） 
- 相当于让人动起来
