#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:30:53 2019

@author: dingyuhao
"""

def significant_inversions(l):
    global result
    global total
    result = []
    length = len(l)
    mid = length // 2
    total = 0
    return  merge(l[:mid],l[mid:])

def merge(list1, list2):
    global result
    global total
    if len(list1) != 1:
       length = len(list1)
       mid = length // 2
       list1 = merge(list1[:mid],list1[mid:]) 
    if len(list2) != 1:
       length = len(list2)
       mid = length // 2
       list2 = merge(list2[:mid],list2[mid:])
    #print(list1, list2)
    new_list = []
    con = 0
    index2 = 0
    
    for i in list1:

            if i > (2 * list2[index2]):
                
                pass
                
            else:
                for j in range(index2, len(list2)):
                    if i > (2 * list2[j]):
                        index2 = j
                        break
                    if j == len(list2) - 1:
                        index2 = -1
            if con != -1:
                while list2[con] >= i:
                    new_list.append(list2[con])
                    if con == len(list2) - 1:
                        con = -1
                        break
                    con += 1
            if index2 != -1:
                total += len(list2) - index2
                #for ii in range(index2, len(list2)):
                    #result.append([i, list2[ii]])
            new_list.append(i)

    if con != -1 and con <= len(list2) - 1:
        #print("It was here")
        #print(con, list1, list2)
        for i in range(con, len(list2)):
            new_list.append(list2[i])
    #print("new_list", new_list)
    return new_list
            
                
significant_inversions([87,342,12,42,53,6])
#print(result)
print("Total is", total)
           
            
        
    
       
    