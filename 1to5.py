'''
1. Even or Odd
Given an integer n, determine whether it is even or odd.
Example
Input: 7
Output: Odd

'''

def even_or_odd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
        
        
even_or_odd(7)

'''
2. Positive, Negative, or Zero
Given an integer, determine whether it is positive, negative, or zero.
Input: -5
Output: Negative
'''

def p_n_z(n):
    if n>0:
        print("positive")
    elif n<0:
        print("negative")
    else:
        print("zero")
    
p_n_z(-5)

"""
3. Largest of Two Numbers
Given two integers, print the larger number.
Input: 15 9
Output: 15
"""
def larger(n,m):
    if n>m:
        print(n)
    elif m>n:
        print(m)
    else:
        print("equal")
        
larger(15,9)

"""
4. Largest of Three Numbers
Given three integers, find the largest without using max().
Input: 10 25 17
Output: 25

"""

def larger(n,m,o):
    if n>m and n>o:
        print(n)
    elif m>n and m>o:
        print(m)
    elif o>m and o>n:
        print(o)
    elif o==m and o==n:
        print(o)
    else:
        print(0)
        
larger(10,25,17)

"""
5. Divisible by 5 and 11
Check whether a number is divisible by both 5 and 11.
Input: 55
Output: Yes

"""

def divisibility(n):
    if n%5==0 and n%11==0:
        print("Yes")
    else:
        print("No")
        
divisibility(55)
