
//结构体

package main

import "fmt"

func main() {
	//定义一个结构体
	//type关键字 结构体的名字 struct{
	//     key值  类型
	//     key值  类型
	// }
	//type hobby struct{
	//	sleep bool
	//	play bool
	//}
	//type Person struct {
	//	Name string
	//	age int
	//	sex int8
	//	Hobby hobby
	//
	//}
	//匿名变量
	type Person struct {
		 name string
		 sex int
	}
	type Person2 struct {
		name string
		sex int
	}
	type Animal struct {
		 Person
		 Person2
		 //name string
		 //height int

	}
	//使用结构体
	//var a Person
	//a.age=19
	//a.Name="lqz"
	//a.sex=1
	//var a=Person{"lqz",19,1}
	//a:=Person{"lqz",19,1}
	//a:=Person{age:19,Name:"lqz",sex:1}
	//fmt.Println(a.Name)
	//
	//fmt.Println(a)
	//匿名结构体
	//p:=struct {
	//	name string
	//	age,sex int
	//}{}
	//p.name="lqz"
	//fmt.Println(p)
	//p:=Person{Name:"lqz",Hobby:hobby{sleep:true,}}
	//fmt.Println(p)
	//p.Hobby.play=true
	//fmt.Println(p)

	//匿名变量
	//p:=Person{"lqz",19}
	//p:=Person{string:"lqz",int:19}
	//fmt.Println(p.string)

	//变量提升
	//a:=Animal{}
	////a.name="xxxx"
	////a.Person.name="lqz"
	//a.Person2.name="lqz"
	////a.name="lqz"
	////a.Person.name="xxx"
	//fmt.Println(a)
	//结构体比较(能不能?分情况)
	//name1 := name{"Steve", "Jobs"}
	//name2 := name{"Steve", "Jobs"}
	//if name1 == name2 {
	//	fmt.Println("name1 and name2 are equal")
	//} else {
	//	fmt.Println("name1 and name2 are not equal")
	//}
	//结构体指针
	name1:=name{"liu","qingzheng"}
	fmt.Println(name1)
	test3(&name1)
	fmt.Println(name1)

}
func test3(name1 *name)  {
	//(*name1).firstName="xxxxx"
	//两种都可以,下面这种用的多
	name1.firstName="xxxxx"
	fmt.Println(name1)
}
type name struct {
	firstName string
	lastName string
}


//class Person:
//	def test(self,name)
//		self.name=name
//
//p=Peron()
//p.test('lqz')
//p.name
////类来调用就是个普通函数
//Peron.test(p2,'lqz')