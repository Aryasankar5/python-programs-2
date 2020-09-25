# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:34:47 2020

@author: ARYA SHANKAR
"""

def fibo(num):
   if num <= 1:
       return num
   else:
       return(fibo(num-1) + fibo(num-2))

nterms=int(input("Enter the number of terms: "))


if nterms <= 0:
   print("Enter a positive integer : ")
else:
   print("Fibonacci sequence is :")
   for i in range(nterms):
       print(fibo(i))