package main

import (
	"fmt"
	"sync"
	"time"
)

//func main() {
//	//容量和长度
//	a:=make(chan int,3)
//	a<-1
//	a<-2
//	a<-3
//	//a<-4
//	fmt.Println(<-a)
//	fmt.Println(<-a)
//	//fmt.Println(<-a)
//}

//s示例
//func write(ch chan int) {
//	for i := 0; i < 5; i++ {
//		ch <- i
//		fmt.Println("successfully wrote", i, "to ch")
//	}
//	close(ch)
//}
//func main() {
//	ch := make(chan int, 2)
//	go write(ch)
//	time.Sleep(2 * time.Second)
//	for v := range ch {
//		fmt.Println("read value", v,"from ch")
//		time.Sleep(2 * time.Second)
//
//	}
//}


//func main() {
//	ch := make(chan string, 3)
//	ch <- "naveen"
//	ch <- "paul"
//	fmt.Println("capacity is", cap(ch))
//	fmt.Println("length is", len(ch))
//	fmt.Println("read value", <-ch)
//	fmt.Println("capacity is", cap(ch))
//	fmt.Println("new length is", len(ch))
//}
///WaitGroup等待所有协程结束
func process(i int, wg *sync.WaitGroup) {
	fmt.Println("started Goroutine ", i)
	time.Sleep(2 * time.Second)
	fmt.Printf("Goroutine %d ended\n", i)
	wg.Done()
}

func main() {
	no := 3
	//定义了WaitGroup变量
	var wg sync.WaitGroup
	for i := 0; i < no; i++ {
		wg.Add(1)
		go process(i, &wg)
	}
	wg.Wait()
	fmt.Println("All go routines finished executing")
}