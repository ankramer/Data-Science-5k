#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 10:22:32 2018

@author: jakob.barke
"""
    
#Find largest Palindrome

list = []
for i in range(100,1000):
    for j in range(100,1000):
        num = i*j
        if str(num) == str(num)[::-1]:
            list.append(num)
print(max(list))


            
#Description
#Created an empty list
#Nested for loop to iterate through all three digit numbers (100-999)
#Mulitply each possibly combo of 3 digit numbers
#check if the result is a palindrome
#If it is a palindrome, add it to the list
#Find the max value in the list after all possible palindromes have been saved