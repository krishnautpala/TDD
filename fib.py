#!/usr/bin/python
import sys

# fib recurssion

def Fib_recursion(number):
    if (number == 1):
	return 0
    if (number == 2):   
	return 1
    return (Fib_recursion(number-1)+Fib_recursion(number-2));
