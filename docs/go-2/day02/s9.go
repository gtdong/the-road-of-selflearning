//go协程
package main

import (
	"fmt"
	"time"
)

func test6()  {
	fmt.Println("go go go ")

}
func main() {
	fmt.Println("开始")
	//go test6()
	//go test6()
	//go test6()
	for i:=0;i<5;i++{
		go test6()
	}
	time.Sleep(time.Second*1)

}