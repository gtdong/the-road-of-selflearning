////
//////接口的类型断言
package main
////
////import "fmt"
////
//////定义一个接口
////
////type TDuck struct {
////	name string
////	age int
////}
////type PDuck struct {
////	name string
////	age int
////	sex int
////}
////type Duck interface {
////	run()
////	speak()
////}
////
////func (d TDuck)run()  {
////	fmt.Println("我是唐老鸭，走路————————")
////}
////func (d TDuck)speak()  {
////	fmt.Println("我是唐老鸭，说人话")
////}
////func (d TDuck)other()  {
////	fmt.Println("other")
////}
////func (d PDuck)run()  {
////	fmt.Println("我是普通鸭子，走路xcxxx")
////}
////func (d PDuck)speak()  {
////	fmt.Println("我是普通鸭子，说话嘎嘎嘎")
////}
////func (d PDuck)Tduckother()  {
////	fmt.Println("Tduckother")
////}
////func main() {
////	//d:=TDuck{}
////	//run(d)
////	p:=PDuck{}
////	run(p)
////	//run(d)
////	//类型选择（Type Switch）
////
////}
////func run(t Duck)  {
////	a:=t.(TDuck)
////	a.run()
////	a.speak()
////	a.other()
////}
////func run(t Duck)  {
////	switch a:=t.(type) {
////	case PDuck:
////		fmt.Println("PDuck类型")
////		a.Tduckother()
////	case TDuck:
////		fmt.Println("TDuck类型")
////		a.other()
////	default:
////		fmt.Println("不知道类型")
////	}
////}
//
//package main
//
//import "fmt"
////定义了一个接口，里面有Describe方法
//type Describer interface {
//	Describe()
//}
////定义了一个结构体，有两个属性
//type Person struct {
//	name string
//	age  int
//}
////给结构体绑定方法，实现了Describer接口
//func (p Person) Describe() {
//	fmt.Printf("%s is %d years old", p.name, p.age)
//}
//
//func findType(i interface{}) {
//	switch v := i.(type) {
//	case Describer:
//		v.Describe()
//	default:
//		fmt.Printf("unknown type\n")
//	}
//}
//
//func main() {
//	//findType("Naveen")
//	//p := Person{
//	//	name: "Naveen R",
//	//	age:  25,
//	//}
//	//findType(p)
//	findType(12)
//	b:=[2]int{2,3,}
//	findType(b)
//}
