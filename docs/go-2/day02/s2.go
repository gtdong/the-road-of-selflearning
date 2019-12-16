//指针
package main

import "fmt"

func main() {
	//*  反解  解引用
	// & 取地址符号
	//b:=156
	//& 取地址符号,取出b的地址,赋给a
	//var a *int=&b
	////var a=&b
	////a:=&b
	//fmt.Println(a)
	//fmt.Println(*a)
	//多次取地址
	//b:=156
	//a:=&b
	//c:=&a
	//d:=&c
	////fmt.Println(d)
	//fmt.Println(*(*(*d)))
	//指针的零值  是nil
	//var a *int
	//fmt.Println(a)

	//用指针来修改 b 的值(不可变类型的值)

	//var a=10
	//fmt.Println(a)
	////test(a)
	//test2(&a)
	//fmt.Println(a)
	//不要向函数传递数组的指针，而应该使用切片
	//a:=[5]int{1,2,3,4,5,}
	//fmt.Println(a)
	////test(&a)
	//test2(a[:])
	//fmt.Println(a)

}
func test(a *[5]int)  {
	(*a)[0]=100
	fmt.Println(a)
}
func test2(a []int)  {
	a[0]=999
	fmt.Println(a)
}
//func test(a int)  {
//	a=100
//	fmt.Println(a)
//}
//func test2(a *int)  {
//	fmt.Println(*a)
//	*a=999
//	fmt.Println(*a)
//}
