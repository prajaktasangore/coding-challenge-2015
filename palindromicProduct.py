#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author:  Prajakta Sangore
# Date:    28th September 2015
# Problem: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math
import time
import decimal

#Setting the start time to calucate the execution time later
start_time = time.time()

# Taking input from user
a = int(raw_input("Please enter the number of digits: "))

x = pow(10,a) - 1  
y = pow(10,(a-1))  

max_product = x*x
min_product = y*y

# Lists used in the 
list_1 = []   # storing a number
list_2 = []   

# Function to check if the given number is a palindrome 
def checkPalindrome(num):
    list_1 =[int(i) for i in str(num)]
    list_2 = list(reversed(list_1))
    if list_1 == list_2:
        return num
    else:
        return -1

# function to find the largest product which is a palindrome and a product of two 3 digit numbers
def findLargestPalindromeProduct():
  for i in xrange (max_product,min_product,-1):
      if (checkPalindrome(i) > -1):
          for number in xrange (x,y,-1):
              if(i%number == 0):
                z = i/number
                if(z in xrange(y,x)): 
                  print "The largest palindrome product = %d of %d and %d " %(i,z,number)
                  return 1



findLargestPalindromeProduct()

# Printing the total execution time taken 
print "total time taken for this program to execute = %s seconds" %round(time.time() - start_time,2)
