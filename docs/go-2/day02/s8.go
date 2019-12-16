
//接口嵌套

package main

import "fmt"

type SalaryCalculator interface {
	DisplaySalary()
}

type LeaveCalculator interface {
	CalculateLeavesLeft() int
}

type EmployeeOperations interface {
	SalaryCalculator
	LeaveCalculator
}

type Employee struct {
	firstName string
	lastName string
	basicPay int
	pf int
	totalLeaves int
	leavesTaken int
}

func main() {
	var a EmployeeOperations
	fmt.Println(a)
}