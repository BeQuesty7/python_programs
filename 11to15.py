"""
11. Reverse a Number
Reverse an integer without converting it to a string.
Input: 12345
Output: 54321
"""


def reverse_num(num):
    reverse=0
    while num>0:
        n=num%10
        num=num//10
        reverse=n+(reverse*10)
    return reverse

print(reverse_num(12345))

"""
12. Palindrome Number
Check whether a number reads the same forward and backward.
Input: 121
Output: Palindrome
Input: 123
Output: Not Palindrome
"""
def reversenum(num):
        while num>0:
            n= num%10
            num=num//10
            reverse= n+(reverse*10)
        return reverse
    
def palindrome(num):
    if num==reversenum(num):
        print("Palindrome")
    else:
        print("not palindrome")
        
palindrome(121)
palindrome(123)    

"""
13. Count Even and Odd Digits
Count how many digits are even and how many are odd.
Input: 123456

Output:
Even = 3
Odd = 3
"""

def CountEO(num):
    even=[], odd=[]
    while num>0:
        n=num%10
        if n%2==0:
            even.append(n)
        else:
            odd.append(n)
        num=num//10
    print(f"Even = {len(even)}")
    print(f"Odd = {len(odd)}")
    
CountEO(123456)

"""
14. Factorial
Calculate n! using a loop.
Input: 5
Output: 120
"""

def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
        i+=1
    print(factorial)
factorial(5)


""" 
15. Power of a Number
Calculate a^b without using pow() or **.
Input: 2 5
Output: 32
"""

def power(n,m):
    result=1
    for i in range(m):
        result*=n
        i+=1
    print(result)
    
power(2,5)




