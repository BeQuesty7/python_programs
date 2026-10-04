'''
21. Reverse a String
Reverse a string.
Don't use [::-1].
Input: "python"
Output: "nohtyp"

'''

def reverse(string):
    reversed=""
    for char in string:
        reversed= char + reversed
    print(reversed)
    
reverse("python")

'''
22. Palindrome String
Check whether a string is a palindrome.
Input: "madam"
Output: Palindrome
'''
def palindromeChecker(string):
    left=0
    right=len(string)-1
    while left < right:
        if string[left] == string[right]:
            left+=1
            right-=1
        else:
            return "Not Palindrome"
    return "Palindrome"

print(palindromeChecker("madam"))

'''
23. Count Vowels and Consonants
Count vowels and consonants in a string.
Input: "hello"

Output:
Vowels = 2
Consonants = 3
Ignore spaces and special characters.
'''


def Countstr(string):
    cleaned= "".join(filter(str.isalpha,string))
    for char in cleaned:
        vowels=0
        consonants=0
        Vowels=["a","e","i","o","u"]
        if char in Vowels:
            vowels+=1
            continue
        else:
            consonants+=1
            continue
            
    print(f"Vowels={vowels}\nConsonants={consonants}") 
    
Countstr("hello")      


""" 
24. Count Character Frequency
Given a string, count how many times each character occurs.
Input: "banana"

Output:
b = 1
a= 3
n = 2
Try solving this using a dictionary.
"""

def charFreq(string):
    frequency={}
    for char in string:
        if char not in frequency:
            frequency[char]=1
        else:
            frequency[char]+=1
    for key in frequency.keys():
        print(f"{key}={frequency[key]}")
        
charFreq("banana")
    
'''
25. First Non-Repeating Character
Find the first character that appears only once.
Input: "aabbcddee"
Output: c
If none exists:
Output: -1
'''

def FirstNRC(string):
    frequency={}
    for char in string:
        if char not in frequency.keys():
            frequency[char]=1
        else:
            frequency[char]+=1
    for key in frequency.keys():
        if frequency[key]==1:
            print(key)
            break

    values = list(frequency.values())
    if 1 not in values:
        print(-1)
    
FirstNRC("aabbccddee")
