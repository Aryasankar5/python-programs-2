# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:08:04 2020

@author: ARYA SHANKAR
"""
list=[]
n=int(input("Enter the number of elements : "))
for i in range(1,n+1):
    a=int(input("Enter the %d element :" %i))
    list.append(a)
print("The list of positive numbers are : ")
for num in range(n):
    if(list[num]>=0):
        print(list[num])