""" 
16. Prime Number
Check whether a number is prime.
Input: 17
Output: Prime
Constraint: Try to solve it without 
checking every number up to n.
"""

def prime(n):
    pass

""" 
17. Print Prime Numbers in a Range
Given L and R, print all prime numbers between them.
Input: 10 30
Output: 11 13 17 19 23 29

"""

def primeinbw(n,m):
    pass



""" 
18. Fibonacci Series
Print the first n Fibonacci numbers.
Input: 7
Output: 0 1 1 2 3 5 8
"""

def fibo(n):
    series=[0,1]
    for i in range(2,n):
        series.append(series[i-1]+series[i-2])
    for i in series:
        print(i, end=" ")
        
fibo(7)

""" 
19. GCD of Two Numbers
Find the greatest common divisor of two numbers.
Input: 24 36
Output: 12
Try to implement the Euclidean algorithm.
"""

def gcd(n,m):
    pass


'''
20. LCM of Two Numbers
Find the least common multiple of two numbers.
Input: 12 18
Output: 36
'''


def lcm(n,m):
    pass




