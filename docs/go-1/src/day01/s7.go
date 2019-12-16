//if 判断
package main

import "fmt"

func main() {
	a:=11;
	//大括号必须和条件在一行
	if a<10{
		fmt.Println("<10");
	}else if a>10{
		fmt.Println(">10");
	}else {
		fmt.Println("10")
	}

}
