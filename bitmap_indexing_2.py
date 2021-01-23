# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 23:22:58 2020

@author: falguni
"""
import math
str1  = input("enter the string to encode")
#str1 = "0110000000100000100"

encode = ""

list1 = str1.split("1")

def check(list1):
    if(str1[-1]=="0"):
        list1.pop()
    x= len(list1)-1
    if(list1[x]==""):
        list1.pop()
    
    
    
check(list1)    
print(list1)

def decimalToBinary(n):
    str1 = bin(n).replace("0b", "")  
    return str1

for item in list1:
    i  = len(item)
    print(i)
    try:   
        j  =  math.ceil(math.log(i,2))
    except:
        j=1
    if(i==0 or i==1 ):
        j=1
    if(i==2):
        j=2
    for k in range(j-1):
        encode = encode+"1"
    
    encode = encode +"0"
    encode = encode + decimalToBinary(i)
    print("encode str at each step-->",encode)


print("final encoding", encode)
print()

#decode  = input("Enter the string to decode")

decode  = encode

#decode = "11101101001011"
print("decode this" , decode)



'''i1 = decode.find("0")
print(decode[i1+1:i1+i1+2])
decode = decode[i1+i1+2:]
print("kk",decode)'''




def binaryToDecimal(n): 
    return int(n,2)


dec=[]
for i in range(len(decode)):
    if(len(decode)!=0):
        list2=""
        print("index of zero",decode.find("0"))
        ind = decode.find("0")
        #print("list to conside",decode[ind+1:ind+2])
        for i in range(ind+1):
            #print(decode[ind+1:])
            inter = decode[ind+1:]
            try:
                list2= list2+(inter[i])
            except:
                break
           
        
        #print("lis",list2)
        dec.append(binaryToDecimal(list2))
        print("decimal",binaryToDecimal(list2))
        print()
        decode = decode[ind+ind+2:]
        #print(decode)
    else:
        break
print(dec)
val = ""
for i in dec:
    for j in range(i):
        val = val+"0"
    val =val+"1"

print(val)


'''while(1):
  print("Enter Your Choice:")
  print("1 --> Encode the String")
  print("2 --> Decode above encoded string")
  print("3 --> Decode the string")
  print("0--> Exit")
  ch = int(input())
  if (ch == int(0)):
    break
  elif(ch == 1):
      encode()
  elif(ch ==2):
      decode()
  elif(ch == 3):
      decode_particular()

        
'''