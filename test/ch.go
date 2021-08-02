package main

import (
	"fmt"
)

func main() {
	ch:=make(chan string,5)

	for i:=0;i<5;i++ {
		ch<-fmt.Sprintf("%d",i*i)
	}
	close(ch)

	for i := range ch{
		println(i)
	}
}

