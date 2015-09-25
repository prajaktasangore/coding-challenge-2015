# Author: Prajakta Sangore
# Date: 23rd September 2015
# Problem: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#      	   Find the sum of all the multiples of 3 or 5 below 1000.



listOfMultiples = []

def findMultiples(a,b):

	for i in range(a,b):
		if(i%3 == 0 or i%5 == 0):
			listOfMultiples.append(i)
	return	sum(listOfMultiples)

print 'The sum of all the multiples of 3 and 5 below 1000 is ', findMultiples (1,1000)



	 		


	
	

