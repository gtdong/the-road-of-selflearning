//defer panic recover
package main

import "fmt"

func main() {
	//defer fmt.Println("xxx")
	//defer fmt.Println("aaa")
	//fmt.Println("yyy")
	//fmt.Println("zzz")

	a()
	b()
	c()
}

func a()  {
	fmt.Println("aaa")
}
func b()  {
	//在defer中捕获异常，恢复程序
	defer func() {
		//捕获异常，恢复程序
		//a:=recover()   //恢复程序
		//recover()   //恢复程序
		//fmt.Println(a)
		if ok:=recover();ok!=nil{
			fmt.Println("我有错误")
		}
	}()
	//defer fmt.Println("我永远会执行")
	fmt.Println("bbb")
	//主动抛出异常
	panic("我出异常了")
	fmt.Println("我永远不会执行")
}
func c()  {
	defer func() {
		if ok:=recover();ok!=nil{
			fmt.Println("我有错误")
		}
	}()
	fmt.Println("ccc")
}
