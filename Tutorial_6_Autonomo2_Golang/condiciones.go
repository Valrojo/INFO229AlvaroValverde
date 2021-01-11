package main

import "fmt"

func main(){
	x := 10
	y := 5
	if x>y{
		fmt.Printf("%d es mayor que %d \n",x,y)
	}else if y>x{
		fmt.Printf("%d es mayor que %d \n",y,x)	
	}else{
		fmt.Println("Son iguales ")
	}
	
	
}
