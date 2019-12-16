//信道
package main

import "fmt"

//func test7(a chan bool){
//	fmt.Println("go go go")
//	a<-true
//
//}
//func main() {
//	//定义一个信道
//	//var a chan bool=make(chan bool)
//	//var a =make(chan bool)
//	a :=make(chan bool)
//	go test7(a)
//	//<-a
//	//发送与接收默认是阻塞的
//
//	b:=<-a
//	fmt.Print(b)
//	//data := <- a // 读取信道 a
//	//a <- data // 写入信道 a
//	//a<-3
//	//var b int=<-a
//}

//更好的理解阻塞
//import (
//	"fmt"
//	"time"
//)
//
//func hello(done chan bool) {
//	fmt.Println("hello go routine is going to sleep")
//	time.Sleep(4 * time.Second)
//	fmt.Println("hello go routine awake and going to write to done")
//	done <- true
//}
//func main() {
//	done := make(chan bool)
//	fmt.Println("Main going to call hello go goroutine")
//	go hello(done)
//	<-done
//	fmt.Println("Main received data")
//}


//该程序会计算一个数中每一位的平方和与立方和，然后把平方和与立方和相加并打印出来
//import (
//	"fmt"
//)
//
//func calcSquares(number int, squareop chan int) {
//	sum := 0
//	//589%10==9
//	for number != 0 {
//		digit := number % 10
//		sum += digit * digit
//		number /= 10
//	}
//	squareop <- sum
//}
//
//func calcCubes(number int, cubeop chan int) {
//	sum := 0
//	for number != 0 {
//		digit := number % 10
//		sum += digit * digit * digit
//		number /= 10
//	}
//	cubeop <- sum
//}
//
//func main() {
//	number := 589
//	sqrch := make(chan int)
//	cubech := make(chan int)
//	go calcSquares(number, sqrch)
//	go calcCubes(number, cubech)
//	squares, cubes := <-sqrch, <-cubech
//
//	fmt.Println("Final output", squares + cubes)
//}
//死锁
//func main() {
////	ch := make(chan int)
////	ch <- 5
////}
//单向信道
//func sendData(sendch chan<- int) {
//	sendch <- 10
//}
//func main() {
//	sendch := make(chan int)
//	go sendData(sendch)
//	fmt.Println(<-sendch)
//}

//信道的关闭
//func test8(a chan int)  {
//	fmt.Println("go go go")
//	a<-1
//	//关闭信道
//	close(a)
//
//}
//func main() {
//	a:=make(chan int)
//	go test8(a)
//
//	v,ok:=<-a
//	v1,ok2:=<-a
//
//	fmt.Println(v)
//	fmt.Println(ok)
//	fmt.Println(v1)
//	fmt.Println(ok2)
//
//}
func producer(chnl chan int) {
	for i := 0; i < 10; i++ {
		chnl <- i
	}
	close(chnl)
}
func main() {
	ch := make(chan int)
	go producer(ch)
	for {
		v, ok := <-ch
		if ok == false {
			break
		}
		fmt.Println("Received ", v, ok)
	}
}
