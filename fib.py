#!/usr/bin/python
import sys

# fib recurssion

def Fib_recursion(number):
    if (number == 0):
	return 1
    if (number == 1):   
	return 2
    return (Fib_recursion(number-1)*Fib_recursion(number-2));
