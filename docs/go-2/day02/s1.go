
//maps
package main

import "fmt"

func main() {
	//定义map
	//var a map[int]string
	//if a ==nil{
	//	fmt.Println("xxxxx")
	//}
	//fmt.Println(a)
	//定义并初始化
	//var a map[int]string=make(map[int]string)
	//if a ==nil{
	//	fmt.Println("sssd")
	//}
	//fmt.Println(a)
	//maps的使用
	//var a map[int]string
	//var a map[int]string=make(map[int]string)
	//var a =make(map[int]string)
	//a:=make(map[int]string)
	//a[1]="xxx"
	//a[2]="yyy"
	//fmt.Println(a)
	//声明并赋初值
	//var a map[int]string=map[int]string{1:"xxx",2:"yyy",}
	//fmt.Println(a)
	//取值
	//var a map[int]string=map[int]string{1:"xxx",2:"yyy",}
	//var a map[string]int=map[string]int{"q":10,}
	////fmt.Println(a[1])
	//fmt.Println(a["xx"])
	//fmt.Println(a["q"])
	//ok 是变量名
	//var ok bool
	//var b int
	//b,ok:=a["q"]
	//if ok{
	//	fmt.Println("值存在")
	//}else {
	//	fmt.Println("值不存在")
	//}
	//fmt.Println(b,ok)

	//删除元素
	//var a map[string]int=map[string]int{"q":10,"xx":199,}
	//delete(a,"q")
	//fmt.Println(a)
	//获取长度
	//var a map[string]int=map[string]int{"q":10,"xx":199,}
	//fmt.Println(len(a))
	//Map 是引用类型
	//var a map[string]int=map[string]int{"q":10,"xx":199,}
	//fmt.Println(a)
	//test(a)
	//fmt.Println(a)
	//相等性的判断
	//var a map[string]int=map[string]int{"q":10,"xx":199,}
	//var b map[string]int=map[string]int{"q":10,"xx":199,}
	////if a==b{  //报错
	////}
	//if b==nil{
	//}
	//字典存储是无序的
	a:=map[int]string{1:"q",2:"w",3:"r",4:"y"}
	for k,v:=range a{
		fmt.Println(k)
		fmt.Println(v)
	}
}

//func test(a map[string]int)  {
//	a["y"]=100
//	fmt.Println(a)
//}