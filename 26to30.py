'''
26. Find Largest Element
Find the largest element in a list without using max().
Input: [4, 8, 1, 9, 3]
Output: 9

'''
def largest(list):
    largest=0
    for i in range(len(list)-1):
        if largest<list[i]:
            largest =list[i]
            i+=1
        elif list[i]> list[i+1]:
            largest =list[i]
            i+=1   
        elif largest> list[i]:
            i+=1
        else:
            largest=list[i+1]
            i+=1
    return largest
print(largest([4,8,1,9,3]))

'''
27. Find Second Largest Element
Find the second-largest distinct element.
Input: [10, 5, 8, 10, 3]
Output: 8
Don't simply sort the array.
'''
def seclargest(list):
    largest=float("-inf")
    second= float("-inf")
    for x in list:
        if x>largest:
            second= largest
            largest=x
        elif x>second and x!=largest:
            second=x
    print(second)
seclargest([10,5,8,10,3])   

'''
28. Remove Duplicates
Remove duplicate elements while maintaining their original order.
Input: [4, 2, 4, 1, 2, 5]
Output: [4, 2, 1, 5]
'''

def rem_duplicate(list):
    cleaned=[]
    for i in range(0,len(list)):
        if list[i] not in cleaned:
            cleaned.append(list[i])
        else:
            i+=1
    print(cleaned)
rem_duplicate([4,2,4,1,2,5])
            
'''
29. Find Missing Number
You are given n distinct numbers from 
0 to n. Find the missing number.
Input: [3, 0, 1]
Output: 2
Another example:
Input: [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8
Try solving it in O(n) time and O(1)
extra space.
'''
def missingnum(list):
    misnum=-1
    for i in range(0,max(list)):
        if i  not in list:
            misnum=i
    print(misnum)

missingnum([0,5,4,2,8,7,1,6])

'''
30. Move All Zeros to the End
Move all zeros to the end while maintaining the relative order of non-zero elements.
Input:
[0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]
Try to solve it in O(n) time.
'''
def movingzeros(list):
    new_list=[]
    for i in list:
        if i!=0:
            new_list.append(i)
    for i in list:
        if i==0:
            new_list.append(i)
            
    print(new_list)

movingzeros([0,2,0,9,5])

