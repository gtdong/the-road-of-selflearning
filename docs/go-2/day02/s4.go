
//方法
package main

type Person3 struct {
	name string
	sex int
}
//定义方法
//fun关键字 (接收器) 方法名(参数)(返回值){}
//func (p Person3)Print()  {
//	fmt.Println(p.name)
//}
//func (p *Person3)changeName(name string)  {
//	p.name=name
//	fmt.Println(p)
//
//}
//func Print(p Person3)  {
//	fmt.Print(p.name)
//}
//func main() {
//	//p:=Person3{"lqz",1}
//	//p.Print()
//	//Print(p)
//	//指针接收器与值接收器
//	//p:=Person3{"lqz",1}
//	//fmt.Println(p)
//	//p.changeName("egon")
//	//fmt.Println(p)
//	//匿名字段的方法  会自动提升
//	//在方法中使用值接收器 与 在函数中使用值参数
//	var p *Person3
//	p=&Person3{"lqz",1}
//	//test4(p)
//	//(&p).test4()
//	test4(&p)
//	p.test4()
//	//(&p).test4()
//}

//func (p Person3)test4()  {
//	fmt.Println(p.name)
//}
//func test4(p Person3)  {
//	fmt.Println(p.name)
//}

//func (p *Person3)test4()  {
//		fmt.Println(p.name)
//}
//func test4(p *Person3)  {
//		fmt.Println(p.name)
//}


//在非结构体上的方法

//func (i string)add(y int) int {
//	return i+y
//}
//给int类型命别名叫myInt
//type myInt int
//
//func (i myInt)add(y myInt) myInt {
//	return i+y
//}
//func main() {
//	var a myInt=100
//	fmt.Println(a)
//	b:=a.add(4)
//	fmt.Print(b)
//}