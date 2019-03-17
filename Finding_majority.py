#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:51:08 2019

@author: dingyuhao
"""

def majority(l):
    length = len(l)
    mid = length // 2
    total_list, m , num = merge(l[:mid],l[mid:])
    if num > len(total_list) / 2:
        print("Majority element:",m,"Occurances:",num)
        return m ,num
        
    else:
        print("No majority")
        return "No majority"
    

def merge(list1, list2):
    if len(list1) != 1:
       length = len(list1)
       mid = length // 2
       list1, m1, num1 = merge(list1[:mid],list1[mid:]) 
    else:
        m1 = list1[0]
        num1 = 1
    if len(list2) != 1:
       length = len(list2)
       mid = length // 2
       list2, m2, num2 = merge(list2[:mid],list2[mid:])
    else:
        m2 = list2[0]
        num2 = 1
    #print(list1, m1, num1, list2, m2, num2)
    if m1 == m2:
        return list1+list2, m1, num1+num2
    else:
        if num1 > num2:
            for i in list2:
                if i == m1:
                    num1 += 1
            return list1+list2, m1, num1
        elif num2 > num1:
            for i in list1:
                if i == m2:
                    num2 += 1
            return list1+list2, m2, num2
        else:
            for i in list2:
                if i == m1:
                    num1 += 1
            for i in list1:
                if i == m2:
                    num2 += 1
            if num1 > num2:
                m = m1
            else:
                m = m2
            return list1+list2, m, max(num1, num2)
            
            


majority(["b","c","a","c","c","c","c","a","c","a","c","a","a"])
majority([1,2,3,1,1,1,2,2,2,3,3,3,4,5,6,2,2,1,1,1,1,1,1,1,1,1,1])
majority([1,1,2,2,3,3])


                
    