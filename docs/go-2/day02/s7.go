//接口进阶
package main

import "fmt"

type Describer interface {
	Describe()
}
type Person struct {
	name string
	age  int
}

func (p Person) Describe() { // 使用值接受者实现
	fmt.Printf("%s is %d years old\n", p.name, p.age)
}

type Address struct {
	state   string
	country string
}

func (a *Address) Describe() { // 使用指针接受者实现
	fmt.Printf("State %s Country %s", a.state, a.country)
}

func main() {
	//d1变量是一个接口类型（Describer）
	//var d1 Describer
	//p1 := Person{"Sam", 25}
	//d1 = p1
	//d1.Describe()
	//p2 := Person{"James", 32}
	//d1 = &p2
	//d1.Describe()

	var d2 Describer
	a := Address{"Washington", "USA"}

	/* 如果下面一行取消注释会导致编译错误：
	  cannot use a (type Address) as type Describer
	  in assignment: Address does not implement
	  Describer (Describe method has pointer
	  receiver)
	*/
	//d2 = a

	d2 = &a // 这是合法的
	// 因为在第 22 行，Address 类型的指针实现了 Describer 接口
	d2.Describe()

}
//结构体可以继承多个接口，当转成相应的接口时，只能使用该接口内的方法
//接口嵌套

