import symbol
import sys
import os
from tkinter import W
import turtle



def ask(num1,num2):
    while(True):
        f=(input())
        if(len(f)==0 or ord(f)<ord(str(num1)) or ord(f)>ord(str(num2))):
            print("\nwrong input\n")
        else:
            return int(f)


def ask_block():
    while(True):
        f=input()
        try:
            f=int(f)
        except:
            print("\nwrong input\n")
        else:
            if(f<1):
                print("\nwrong input\n")
            else:
                return f





def BWT(data):        #BWT use part 
    lst=[]  
    data=data+'\0'
    for i in range(len(data)):
        lst.append(data[i:]+data[:i])
    lst.sort()
    data2="".join([lst[i][-1] for i in range(len(data))])
          
    return data2

        
    


def useBWT(N):        #BWT 
    print("\nchoose open:\n1 - in_BWT.txt\n2 - enwik8\n3 - other\n")
    f2=ask(1,3)
    if(f2==1):
        name="in_BWT.txt"
    elif(f2==2):
        name="enwik8"
    elif(f2==3):
        print("enter name\n")
        name=input() 
        

    file=open(name, "r", encoding="utf-8")
    file2 = open("out_BWT.txt", "w", encoding="utf-8")
        
    L=os.path.getsize(name)

    for i in range(0,L,N):
        data=file.read(N)
        if (data!=""):
          data2 = BWT(data)
          file2.write(data2)                   

    file.close()
    file2.close()










def use_BWT_permutation(data):

    L=[(data[i], i) for i in range(len(data))]
    L.sort(key=lambda x:x[0])
    P=list(zip(*L))[1]
    inv_P=[0 for i in range(len(P))]
    for i in range(len(P)):
        inv_P[P[i]]=i
        
    S=""
    ind=0
    for j in range(len(data)):
        S=data[ind]+S
        ind=inv_P[ind]
    return(S[1:])
   





def unBWT_permutation(N):               #decode BWT with permutations

    name="back_Move-to-front.txt"
    name2="back_BWT.txt"
    file=open(name, "r", encoding="utf-8")
    file2 = open(name2, "w", encoding="utf-8")  
    
    L=os.path.getsize(name)
    
    for i in range(0,L,N):  
        data=file.read(N+1)
        if (data!=""):
            data2=use_BWT_permutation(data)
            file2.write(data2)
    file.close()
    file2.close()













            

def Move_to_front():            #Move-to-front 

    name="out_BWT.txt"
    file = open(name, "rb")
    file2 = open("out_Move-to-front.txt", "wb")




    data=file.read()
    dictionary = list(range(256))
    data2=bytearray(b'')
    num=0
    
    for i in data:
        num=dictionary.index(i)
        data2.append(num)
        dictionary.pop(num)
        dictionary.insert(0,i)


    file2.write(data2)
    file.close()
    file2.close()






def decodeMtF():            #decode Move-to-Front
    print("\nchoose open:\n1 - temp.txt\n2 - other\n")
    f2=ask(1,2)
    if(f2==1):
        name="temp.txt"
    else:
        print("\nenter name\n")
        name=input()
    file = open(name, "rb")
    file2 = open("back_Move-to-front.txt", "wb")
    
                   
    data = file.read()
    dictionary = list(range(256))
    data2=bytearray(b'')
    
    for i in data:
        data2.append(dictionary[i])
        d=dictionary.pop(i)
        dictionary.insert(0,d)

    file2.write(data2)
    file.close()
    file2.close()








from PIL import Image           #start
from io import BytesIO
import numpy as np
from decimal import Decimal
import math



f=0
f2=0
p=False
sign=0
while(True):        #main cycle    
    print("\nchoose action:\n1 - make BWT+MTF\n2 - decode BWT+MTF\n3 - exit program\n")   #main options
    f = ask(1,3)
    print("")


    if (f==1):          #use
        
        print("\ninput block size\n")   
        N = ask_block()                     
        useBWT(N)           #BWT
        Move_to_front()
        print("\nnext copy out_Move-to-front.txt to ari")
                

                
    elif(f==2):         #decode
        
        print("\ninput block size\n")   
        N = ask_block()
        decodeMtF()
        unBWT_permutation(N)
        



    elif(f==3):     #exit program       
        break
    
