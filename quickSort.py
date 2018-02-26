# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:32:40 2018

@author: ben-malik
"""

def quicksort(arr):
    
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x <  pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot ]
    
    return quicksort(left) + middle + quicksort(right)
    
print (quicksort([2,34,343,2,23,-2]))

 