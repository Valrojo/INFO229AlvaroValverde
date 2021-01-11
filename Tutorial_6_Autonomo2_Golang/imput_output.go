package main

import(
	"fmt"
	"bufio"
	"os"
	)

func main(){
	//Forma 1
	var edad int 
	fmt.Println("Coloca tu edad: ")
	fmt.Scanf("%d\n",&edad)
	fmt.Printf("Mi edad es %d\n",edad)

	//Forma 2
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Ingresa tu nombre: ")
	text,err := reader.ReadString('\n')

	if(err != nil){
		fmt.Println(err)
	}else{
		fmt.Println("Hola "+text)
	}
}
