//数组
package main

import "fmt"

func main() {
	//基本定义/定义并初始化
	//var a [3]int=[3]int{1,2,3}
	//var a =[3]int{1,2,3}
	//a:=[3]int{1,2,3}
	//fmt.Println(a)
	//指定位置初始化
	//a:=[10]string{9:"lqz",8:"xxx"}
	//fmt.Println(a)
	//数组使用
	//var a [3]int=[3]int{1,2,3}
	////a[0]=100
	//////a[1]="lqz"
	////fmt.Println(a)
	////b:=a[2]
	////var b int=a[2]
	//fmt.Println(a[2])
	// ... 的使用(少用)
	//a :=[...]int{9:1}
	//fmt.Println(a)
	//fmt.Println(len(a))
	//数组大小是类型一部分
	//var a [3]int
	//a:=[3]int{1,2,3}
	//b:=[4]int{1,2,3}
	//
	//b=a
	//fmt.Println(b)
	//数组是值类型
	//a:=[3]int{1,2,3}
	//fmt.Println(a)
	//test(a)
	//fmt.Println(a)
	//数组迭代
	//a:=[3]int{1,2,3}
	//for i:=0;i<len(a);i++{
	//	fmt.Println(a[i])
	//}
	//第二种方式(常见)
	//range :python中range函数
	// 关键字
	//range 可迭代   如果用一个值接收：就是索引  如果用两个值接收：就是索引和值
	//for i,v:=range a{
	//	//fmt.Println(i)
	//	fmt.Println(a[i])
	//	fmt.Println(v)
	//}

	//多维数组
	//定义一个二位数组
	//var a [5][3]int=[5][3]int{{1,2,3},{4,4,4}}
	var a [5][3]int=[5][3]int{2:{4,4,4}}
	fmt.Println(a)
	//循环
	//for i := 0; i < len(a); i++ {
	//	for j := 0; j < len(a[i]); j++ {
	//		fmt.Println(a[i][j])
	//	}
	//}
	//for _,v:=range a{
	//	for _,v1:=range v{
	//		fmt.Println(v1)
	//	}
	//}

}

//func test(a [3]int)  {
//	a[1]=1000
//	fmt.Println(a)
//}
