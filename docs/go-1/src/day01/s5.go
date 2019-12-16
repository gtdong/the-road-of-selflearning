
//函数
package main

func main() {
	//没有指名道姓传参，只能按位置传
	//var a int=test(1,2)
	//var a =test(1,2)
	//a :=test(1,2)
	//fmt.Println(a)
	//var a int
	//var b string
	//a,b=test(1,2,"计算")
	//var a,b=test(1,2,"计算")
	//a,b:=test(1,2,"计算")
	//a:=test(1,2,"计算")   //错误
	//a,_:=test(1,2,"计算")
	//fmt.Println(a)
	//test(1,2,3,4,5)
	//闭包函数   调用
	//aa:=3
	//a:=test(aa)
	//aa=19
	//a(5)

	//test(1,4)(a(),6)
	//aaa=test(1,4)
	//bbb=a()
	//aaa(bbb,6)
	//int类型默认空值是0
	//string类型默认空值是""
	//c,d:=test()
	//fmt.Println(c,d)
	//var a string
	//fmt.Println(a)
}
//func关键字 函数名（变量 变量类型，变量 变量类型）{
// }
//func test(a int,b int)  {
//func test(a ,b int)  {
//	fmt.Println(a+b)
//}
//带返回值
//func关键字 函数名（变量 变量类型，变量 变量类型）返回值类型{}
//func test(a ,b int) int {
//	return a+b
//}
//多返回值
//func test(a,b int,c string)(int,string){
//	return a+b,"计算成功"
//}

//可变长参数
//func test(a ...int)  {
//	//a 切片  类似于python中的列表
//	fmt.Println(a)
//	fmt.Println(a[0])
//}

//闭包
// 1 定义在函数内部
//2 对外部作用域有引用
// 补充：匿名函数 func ()(){}

//func test(a int)(int){
//	return 1
//}

//x什么时候传的，x值是几？

//def test（a,b）:
//	a(12)
//test(lambda x:x+1,19)


//func test()(func()(int,string)){
//	a:=10
//	//b:=func (){
//	//	fmt.Println(a)
//	//}
//	b :=func ()(int,string){
//		fmt.Println(a)
//		return 1,";lqz"
//	}
//	return b
//}

//func test(d int)(func(c int)()){
//	a:=func (c int)(){
//		fmt.Println(d+c)
//	}
//	return a
//}


//默认返回值

//func test()( a int , b int)  {
//
//	return a,b
//}


//函数格式
//func 名字(参数1 类型，参数2 类型)（返回类型，返回类型）{}






