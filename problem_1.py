#!/usr/bin/python

# https://projecteuler.net/problem=1

sum=0 # Initialize our sum variable to 0

for i in range(1,1000): # Count through numbers 1 to 999
    if i%3==0 or i%5==0:        ## Determine if they are divisible by 3 or 5
        sum+=i # If so, add 1 to our sum, else do nothing

print(sum) # Print our answer
