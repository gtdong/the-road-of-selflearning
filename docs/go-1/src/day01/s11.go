
//切片
package main

import "fmt"

func main() {
	//切片定义
	//切片底层基于数组
	//a:=[9]int{1,2,43}
	//fmt.Println(a)
	//b:=a[1:3]
	//fmt.Println(b)
	////b[0]=100
	//a[1]=999
	//fmt.Println(b)
	//fmt.Println(a)
	//a:=[5]int{1,2,43,0,0}
	//b:=a[1:3]
	//fmt.Println(b)
	//fmt.Println(len(b))
	////切片追加值
	//b=append(b,10)
	//b=append(b,11)
	//b=append(b,12)
	////b=append(b,13)
	//fmt.Println(b)
	//fmt.Println(len(b))
	//fmt.Println(a)
	//a[3]=888
	//fmt.Println(a)
	//fmt.Println(b)
	//查看切片的容量/长度
	//a:=[5]int{1,2,43,0,0}
	//b:=a[1:3]
	//fmt.Println(len(b))   //2
	////查看容量
	//fmt.Println(cap(b))   //4
	//b=append(b,10)
	//b=append(b,11)
	//b=append(b,12)
	//fmt.Println(len(b))  //5
	////查看容量（容量如果不够了，每次都会翻倍）
	//fmt.Println(cap(b)) //8
	//fmt.Println(b[7])

	//切片第二种定义方式 中括号内不写东西，就是切片类型
	//切片的空是nil
	//通过make函数来完成初始化
	//var a []int=make([]int,5,5)
	////fmt.Println(a)
	//if a==nil{
	//	fmt.Println("xxxx")
	//}
	//fmt.Println(len(a))
	//fmt.Println(cap(a))
	//a=append(a,90)
	//fmt.Println(len(a))
	//fmt.Println(cap(a))
	//切片是什么类型  是引用类型
	//var a []int=make([]int,5,5)
	//fmt.Println(a)
	//test(a)
	//fmt.Println(a)
	//内存优化，copy函数
	//a:=[10000]int{1,2,3,4,5,}
	//b:=a[0:3]
	//
	//fmt.Println(b)
	//var c []int=make([]int,2,2)
	//copy(c,b)
	//fmt.Println(c)

	//python中的深拷贝和浅拷贝

}
func test(a []int)  {
	a[0]=999
	fmt.Println(a)
}
