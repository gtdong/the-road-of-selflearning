
//select
package main

import (
	"fmt"
	"time"
)

//func process1(ch chan string) {
//	time.Sleep(10500 * time.Millisecond)
//	ch <- "process successful"
//}
//
//func main() {
//	ch := make(chan string)
//	go process1(ch)
//	for {
//		time.Sleep(1000 * time.Millisecond)
//		select {
//		case v := <-ch:
//			fmt.Println("received value: ", v)
//			return
//		default:
//			fmt.Println("no value received")
//		}
//	}
//
//}

//随机选取
func server1(ch chan string) {
	//去服务端拿数据，耗时操作
	ch <- "from server1"
}
func server2(ch chan string) {
	//去服务端拿数据，耗时操作
	ch <- "from server2"

}
func main() {
	output1 := make(chan string)
	output2 := make(chan string)
	go server1(output1)
	go server2(output2)
	time.Sleep(1 * time.Second)
	select {
	case s1 := <-output1:
		fmt.Println(s1)
	case s2 := <-output2:
		fmt.Println(s2)
	}
}
