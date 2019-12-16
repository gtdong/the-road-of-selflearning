////接口
package main
//
//import "fmt"
//
////定义一个接口
//
//type TDuck struct {
//	name string
//	age int
//}
//type PDuck struct {
//	name string
//	age int
//	sex int
//}
//type Duck interface {
//	run()
//	speak()
//}
//
//func (d TDuck)run()  {
//	fmt.Println("我是唐老鸭，走路————————")
//}
//func (d TDuck)speak()  {
//	fmt.Println("我是唐老鸭，说人话")
//}
//func (d TDuck)other()  {
//	fmt.Println("other")
//}
//func (d PDuck)run()  {
//	fmt.Println("我是普通鸭子，走路xcxxx")
//}
//func (d PDuck)speak()  {
//	fmt.Println("我是普通鸭子，说话嘎嘎嘎")
//}
//func main() {
//	d:=TDuck{}
//	//d.run()
//	//d.speak()
//	//p:=PDuck{}
//	//p.speak()
//	//p.run()
//	//run(p)
//	//run(d)
//	//fmt.Print()
//	//匿名空接口，可以接受任意类型的参数
//	//interface {
//	//}
//	//test5(12)
//	run(d)
//
//}
//
////type Empty interface {
////
////}
////func test5(a Empty)  {
////func test5(a interface{})  {
////	fmt.Print(a)
////}
//func run(t Duck)  {
//	t.run()
//	t.speak()
//}
