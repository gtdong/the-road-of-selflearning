//循环
package main

import "fmt"

func main() {

	////for 循环
	//for 第一部分;第二部分;第三部分{
	//
	//}
	//基本写法
	//for i:=0;i<100;i++{
	//	fmt.Println(i)
	//}
	//fmt.Println(i)
	//其他用法1 省略第一部分
	//i:=0
	//for ;i<100;i++{
	//	fmt.Println(i)
	//}
	//fmt.Println(i)
	//其他用法二 省略第三部分
	//i:=0
	//for ;i<100;{
	//	i=i+1
	//	fmt.Println(i)
	//}
	//其他用法三 省略第二部分
	//for ;;{
	//	fmt.Println("xxx")
	//}
	//更多使用
	//for a<10  表示写在第二个位置
	//a:=0
	//for a<10{
	//	fmt.Println(a)
	//}
	//死循环
	//for {
	//	fmt.Println("xxx")
	//	break
	//}
	//break 和continue

	for i:=0;i<10 ;  i++{
		if i==5{
			//continue
			break
		}
		fmt.Println(i)

	}
}
