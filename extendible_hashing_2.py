# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 12:02:26 2020

@author: falguni
"""

import math
#Present

number1= 1
size = 4

def Hashing(keyvalue):
    
    return keyvalue % int(math.pow(2,number1))

def Hashing1(keyvalue): 
    
    return keyvalue % int(math.pow(2,number1))
    #return 2*Hashing(keyvalue)


#Start here
#New

#number1 = 1
s = 0
#curr_bkt =[]
buckets = [[] for _ in range(int(math.pow(2,number)))] 
print(buckets)
def insert_val(buckets, keyvalue): 
    global s
    global number1
    i=0
    hash_key = Hashing(keyvalue)
    s = hash_key
    print("hash", hash_key)
    buckets[hash_key].append(keyvalue)
    #print("buckets before", buckets)
    if (len(buckets[hash_key]) > size):
      curr_bkt = buckets[s]
      hash_key = Hashing1(keyvalue)
      if (len(buckets[hash_key]) <= 4):
        print("Size < 4")
        #print("S value:",s)
        #print("bucket[s]", buckets[s])
        #print("Keyvalue", keyvalue)
        buckets[s].remove(keyvalue)
        buckets[hash_key].append(keyvalue)
      else: 
        #number1 = number1 + 1
        #hash_key = Hashing(keyvalue)
        for i in range(int(math.pow(2,number1))):
          buckets.append([])
        number1 = number1 + 1 #2
        #curr_bkt = buckets[s]
        #print("curr_bkt",curr_bkt)
        #print("bucket[s]",buckets[s])
        buckets.pop(s)
        #buckets.append([])
        buckets.insert(s,[])
        for k in range(len(curr_bkt)):
          hash_key = Hashing1(curr_bkt[k])
          #print("new hash key", hash_key,"for", k)
          buckets[hash_key].append(curr_bkt[k])  
    print("Buckets:", buckets)
    '''else:
      buckets[hash_key].append(keyvalue)
      print("buckets before", buckets)

'''
  
    #ppt example
'''insert_val(buckets,11)
insert_val(buckets,4)
insert_val(buckets,21)
insert_val(buckets,25)
insert_val(buckets,15)
insert_val(buckets,14)
insert_val(buckets,1)
#insert_val(buckets,9)
#insert_val(buckets,20)'''

  

while(1):
  print("Enter Your Choice:")
  print("1 - > Insert")
  print("0 - > Exit")
  ch = int(input())
  if (ch == int(0)):
    break
  else:
   val  = int(input("enter the value"))
   insert_val(buckets,val)
  