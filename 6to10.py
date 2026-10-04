"""
6. Swap Two Numbers
Swap two numbers without using a third variable.
Input: a = 10, b = 20
Output: a = 20, b = 10

"""

def swapping(n,m):
    n,m = m,n
    print(f"n={n},m={m}")
    
swapping(n=12,m=13)



"""
 7. Sum of First N Natural Numbers
Given n, calculate:
1+2+3+⋯+n

Do not use the mathematical formula.
Input: 5
Output: 15
 
    
"""


def Sum(N):
    sum=0
    for n in range(N+1):
        sum+=n
    print(sum)

Sum(5)


"""
8. Multiplication Table
Print the multiplication table of n from 1 to 10.
Input: 5

Output:
5
10
15
20
...
50

"""

def MTable(N):
    for n in range(1,11):
        print(N * n)
    
MTable(5)


"""
9. Count Digits
Given an integer, count how many digits it contains.
Input: 58392
Output: 5
Handle 0 correctly.

"""     

def Count(num):
    listn=list(str(num))
    return len(listn)

print(Count(58392))

'''
10. Sum of Digits
Find the sum of all digits of a number.
Input: 58392
Output: 27

'''
def Sum(num):
    sum=0
    while num>0:
        n=num%10
        num=num-n
        num=num//10
        sum+=n
    print(sum)
Sum(58392)



