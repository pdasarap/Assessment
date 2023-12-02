#!/usr/bin/env python
# coding: utf-8

# - Author: Pallavi Dasarapu
# - Problem: Left Rotate Array
# - Assessment from: Vail Systems
# - Date: 12/02/2023

# # Approach:
# 1. Created a helper function - reverseArray - to reverse the given array from given left to right.
# 2. leftRotateArray function which takes in array of integers and k - updates array each time it calls the reverseArray function
# 3. Conditions:
#     - if k<0: returns error message: "Negative k is not accepted"
#     - else: k=k%n - to handle any positive value of k (i.e. k<=n or k>n)
# 4. arr input takes in any sorted or unsorted array and returns the left-rotated array

# In[1]:


def reverseArray(arr, left, right):
    while left<right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    return arr


# In[2]:


def leftRotateArray(arr, k):
    if k<0:
        return "Negative k is not accepted"
    
    n = len(arr)
    k %= n
    
    arr = reverseArray(arr,0,k-1)
    arr = reverseArray(arr,k,n-1)
    arr = reverseArray(arr,0,n-1)
    
    return arr


# In[3]:


arr = [1,2,3,4,5,6,7]
k = 2
print(leftRotateArray(arr,k))


# In[4]:


arr = list(range(1,101))
k = 1007
print(leftRotateArray(arr,k))


# In[5]:


print(leftRotateArray([-1,-9,78,489,0,1,4,9],-5))


# # Complexities
# 1. Time Complexity: O(n) 
#     - three calls to helper function which is three while loops are run but each iterates through less than n elements each time - covering n elements twice 
#     - which would be O(2n)->O(n)
# 2. Space Complexity: O(1)
#     - we are not using any extra space to hold the array of n elements. changes are made inplace.
#     - we used constant extra space.

# In[ ]:




