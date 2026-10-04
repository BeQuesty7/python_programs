""" 
16. Prime Number
Check whether a number is prime.
Input: 17
Output: Prime
Constraint: Try to solve it without 
checking every number up to n.
"""

def prime(n):
    if n <2:
        return "Not prime"
    else:
        i=2
    while i*i <=n:
        if n%i==0:
            return "Not prime"
        else:
            i+=1
    return "Prime"
print(prime(17))
        

""" 
17. Print Prime Numbers in a Range
Given L and R, print all prime numbers between them.
Input: 10 30
Output: 11 13 17 19 23 29

"""

def is_prime(n):
    if n<2:
        return False
    else:
        i =2
    while i*i<=n:
        if n%i==0:
            return False
        else:
            i+=1
    return True

def primeinbw(n,m):
    for i in range(n, m+1):
        if is_prime(i):
            print(i,end=" ")
           
primeinbw(11,29)



""" 
18. Fibonacci Series
Print the first n Fibonacci numbers.
Input: 7
Output: 0 1 1 2 3 5 8
"""
print("\n")
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
    a=min(n,m)
    b=max(n,m)
    while a!=0:
        remainder=b%a
        b=a
        a=remainder
    print("\n",b)
gcd(24,36)

'''
20. LCM of Two Numbers
Find the least common multiple of two numbers.
Input: 12 18
Output: 36
'''


def lcm(n,m):
    if n>m:
        start=n
    else:
        start=m
    
    while True:
        if start%n==0 and start%m==0:
            print("LCM =", start)
            break
        start+=1
        
lcm(12,18)




