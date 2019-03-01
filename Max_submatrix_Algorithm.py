#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:32:52 2019

@author: dingyuhao
"""
import random


#This is the main function, inputs are then list l, row number(行) c, and column number(列) k
# Note inside this function, we change the problem to a one-dimensional problem
def func(l,c,k):
    bigg = 0
    for i in range(c):
        for ii in range(c):

                new_list = []
                for column in range(k):
                    s = 0
                    for row in range(i, ii + 1):
                        s += l[row][column]
                    new_list.append(s)
                #print(i,ii,new_list)
                this_max = merge_count(new_list)
                
                if this_max > bigg:
                    bigg = this_max
    return bigg

# This is a fucntions calls the recursive function
def merge_count(l):
    if len(l) == 1:
        return l[0]
    else:
        middle = len(l) // 2
        return merge(l[0:middle], l[middle:len(l)])

# This is the recursive function that computes the middle part 
def merge(l1,l2):
    middle_1 = len(l1) // 2
    middle_2 = len(l2) // 2
    if len(l1) == 1 and len(l2) == 1:
        return max(l1[0], l2[0])
    elif len(l1) == 1 and len(l2) == 0:
        return l1[0]
    elif len(l1) == 0 and len(l2) == 1:
        return l2[0]

    
    biggest = 0
    num = 0
    for i in range(len(l2)):
        num += l2[i]
        if num > biggest:
            biggest = num
    biggest_1 = 0
    num = 0
    for i in range(len(l1)-1, -1, -1):
        #print(i)
        num += l1[i]
        if num > biggest_1:
            biggest_1 = num
    return max(biggest + biggest_1, merge(l1[0:middle_1], l1[middle_1:len(l1)]), merge(l2[0:middle_2], l2[middle_2:len(l2)]))

#This is a O(n^4) solution, only for testing purpose, I used this to test whether my previous algorithm si right
def test_func(l,c,k):
    
    bigg = 0
    for i in range(c):
        for ii in range(c):

                new_list = []
                for column in range(k):
                    s = 0
                    for row in range(i, ii + 1):
                        s += l[row][column]
                    new_list.append(s)
                #print(i,ii,new_list)
                result = []
                for iii in range(len(new_list)):
                    for iiii in range(len(new_list)):
                            result.append(sum(new_list[iii : iiii+1]))
                this_max = max(result)
                
                if this_max > bigg:
                    bigg = this_max
    return bigg  
# Test here, you can specify rows and columns, it auto generates the matrix
c = 10
k = 3
l = []
for i in range(c):
    sublist = []
    for ii in range(k):
        sublist.append(random.randint(-10,10))
    l.append(sublist)
#print(l)
print("Matrix is:")
for i in l:
    print(i)
a = func(l,c, k)  

b = test_func(l,c, k)
print("Algorithm result:", a)  
print("Test:",  b)
print(a == b)
#This code is to test my algorithm 1000 times
right = 0
times = 1000
for i in range(times):
    c = 4
    k = 4
    l = []
    
    for i in range(c):
        sublist = []
        for ii in range(k):
            sublist.append(random.randint(-10,10))
        l.append(sublist)
    

    a = func(l,c, k)  

    b = test_func(l,c, k)
    #print(a,b)
    if func(l,c,k) == test_func(l,c, k):
        right += 1
print("\n\nNow Running tests...")
print("After testing", times, "times, you get", right, "times right, which is", right*100/times, "% accuracy")
"""
#Debug purpose, this part is to test whether the one-dimensional part is right
for i in range(100):
    alist = []

    for i in range(10):
        alist.append(random.randint(-10,10))
    print(alist)

    middle = len(alist) // 2
    #print(alist[0:middle],alist[middle:len(alist)])
    merge_most = merge(alist[0:middle],alist[middle:len(alist)])
    biggest_leftmost = 0
    l = alist
    num = 0
    for i in range(len(l)):
            num += l[i]
            if num > biggest_leftmost:
                biggest_leftmost = num
    biggest_rightmost = 0
    num = 0
    for i in range(len(l)-1, -1, -1):
        num += l[i]
        if num > biggest_rightmost:
            biggest_rightmost = num
        
    
    result = []
    for iii in range(len(alist)):
    
        for iiii in range(len(alist)):
            result.append(sum(alist[iii : iiii+1]))
    
    
    print(biggest_rightmost, biggest_leftmost, merge_most)  
    print(max(biggest_rightmost, biggest_leftmost, merge_most) == max(result))
"""


