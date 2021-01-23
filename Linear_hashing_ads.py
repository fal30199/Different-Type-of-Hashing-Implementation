# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:45:38 2020

@author: falguni
"""
from collections import OrderedDict 

M = 4
capacity_of_bucket = 2
laod_factor = 0.70
split_node = [0]

#bucket=[[] for i in range(capacity_of_bucket)]

bucket={}

bucket1 = bucket

def hash_fun_1(key):
    h  = key % M   
    return h

def hash_fun_2(key):
    h = key % (2*M)
    return h

    

def bucket_constrain(key):
    #print(len(bucket[key]))
    if(len(bucket[key]) < 2):
        return True
    else:
        return False
    

def keys_in_bucket(d): 
  
    # using dict.items() 
    count = 0
    for key, value in d.items(): 
        if isinstance(value, list): 
              count += len(value) 
    return(count) 


def insert_into_bucket(key , value):
    bucket.setdefault(key, [])
    if(bucket_constrain(key)):
        bucket[key].append(value)
        current_keys_in_bucket = (len(bucket))
        val = keys_in_bucket(bucket)
        #print("numerator",val)
        #print("demnominator",(current_keys_in_bucket),"*",(capacity_of_bucket))
        inter_lf = val/(M*capacity_of_bucket)
        print("intermediate load factor", inter_lf)
        return inter_lf
    else:
        print("bucket is overflowed and load factor exceed")
      
        return -1

def split_dueto_lf_noof(list1):
    print("lisq",list1)
    for value in list1:
            key = hash_fun_2(value)
            print("new hased key", key,value)
            inter_lf = insert_into_bucket(key, value)
            print("Updated bucket after split", bucket)
    split_node[0]=split_node[0]+1
        
    


def insertion():
    value = int(input("Enter the Value to be insert"))
    key = hash_fun_1(value)
    list1 = []
    list2=[]
    inter_lf = insert_into_bucket(key, value)
    if(inter_lf > 0.70):
        print("for load factor ++ Split will occur at", bucket[split_node[0]])
        for i in bucket[split_node[0]]:
            list1.append(i)
        bucket[split_node[0]].clear()
        split_dueto_lf_noof(list1)
        print("split node", split_node[0])
    elif(inter_lf == -1):
        print("1st time for overflow and load factor++ Split will occur at", bucket[split_node[0]])
        for i in bucket[split_node[0]]:
            list2.append(i)
        bucket[split_node[0]].clear()
        split_dueto_lf_noof(list2)
        print("split node", split_node[0])
        value1 = int(input("Enter the Value Again to insert"))
        key1 = hash_fun_1(value1)
        inter_lf = insert_into_bucket(key1, value1)
        if(inter_lf > 0.70):
            '''write code here'''
        elif(inter_lf == -1):
            list3=[]
            print("2nd time for overflow and load factor++ Split will occur at", bucket[split_node[0]])
            for i in bucket[split_node[0]]:
                list3.append(i)
            bucket[split_node[0]].clear()
            split_dueto_lf_noof(list3)
            print("split node", split_node[0])
            value2 = int(input("Enter the Value Again to insert which created overflow "))
            key2 = hash_fun_1(value2)
            inter_lf = insert_into_bucket(key2, value2)
            print("buccc",bucket)
            
        
        
    else:
        #print("bucket get over flowed at bucket", bucket[key] )
        '''for value in bucket[key]:
            key = hash_fun_2(value)
            print("2nd", key)
            inter_lf = insert_into_bucket(key, value)
            (bucket[key]).remove(value)'''
        
    
    
    

while(1):
  print("Enter Your Choice:")
  print("1 - > Insert")
  print("0 - > Exit")
  ch = int(input())
  if (ch == int(0)):
    break
  else:
    insertion()
    bucket = OrderedDict(sorted(bucket.items()))  
    print(bucket)
    
