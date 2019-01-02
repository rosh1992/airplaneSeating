#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:03:56 2018

@author: rosha
"""

filename = "inputFile.txt"
file = open(filename, "r")
count=0

#inputList.remove(inputList[0])
inputList= []
windowIndex=[]

for line in file:
    if count==0:
        row_count = list(map(str, line.split()))
        count=1
    else:
        InputLine= list(map(str, line.split()))
        inputList.append(InputLine)

i=0
j=0
lines=[]
for i in range(len(inputList)):
    for j in range(len(inputList[i])):
        inputItem= inputList[i][j]
        inputItemLen= len(inputItem)-1
        if "W" in inputItem:
            lines.append(i)
            inputList[i][j]= inputItem[:inputItemLen]
            windowIndex.append(inputList[i][j])
            
#Sorting for Window seat
i=0
j=0
k=0
temp=0
for i in range(len(inputList)):
    for j in range(len(inputList[i])):
        for k in range(len(windowIndex)):
            if(inputList[i][j]==windowIndex[k]):
                temp= inputList[i][0]
                inputList[i][0]= inputList[i][j]
                inputList[i][j]= temp




#int(inputList[0][0])
#len(finalSeating)
#finalSeating[0]= [1,2,3]
m=0
i=0
k=0
flg=0
#len(inputList[0])
finalSeating = [[]]*int(row_count[1])
finalSeating1 = [[]]*int(row_count[1])
inputList1= inputList.copy()
#for i in range(len(inputList)):
counts=0
"""for k in range(len(inputList1)):
    if(i<int(row_count[1])):
        if(flg==1):
            m=k
            k=k-1
        if((m in lines) or (int(len(inputList1[k]))==int(row_count[1]))):
            finalSeating1[i]= inputList1[k]
            del inputList1[k]
            #counts=counts+1
            i=i+1
            flg=1
            
        else:
            m=m+1   
            flg=0
"""
k=0
for k in range(len(inputList1)):
    if((k in lines) and len(inputList[k])!=1):
        finalSeating1[i]= inputList[k]
        del inputList1[k-i]
        i=i+1
        #counts=counts+1

k=0
i=0
#Adding groups with Max length        
for k in range(len(inputList1)):
    if(flg==1):
        k=k-1
    if (int(len(inputList1[k])))==int(row_count[1]):
        #if(len(finalSeating1[i])==0):
        for i in range(len(finalSeating)):
            if(len(finalSeating1[i])==0):
                finalSeating1[i]=inputList1[k]
                del inputList1[k]
                flg=1
                break
        
k=0
m=0
for k in range(len(inputList1)):
    for m in range(len(finalSeating1)):
        if (len(finalSeating1[m])==0):
            if(len(inputList1[k])>=int(row_count[0])/2):
                finalSeating1[m]= inputList1[k]
                del inputList1[k]
                break
    
"""    if(i<int(row_count[1])):
        if(flg==1):
            k=k-1
        if(len(inputList[k])>=int(row_count[0])/2):
            finalSeating[i]= inputList[k]
            del inputList[k]
            flg=1
            i=i+1
"""
q=0
i=0
while(len(inputList1)!=0):
    for i in range(len(finalSeating1)):
        lenIL= len(inputList1[q])
        #if(len(finalSeating[i])==3 and lenIL==1):
        if((len(finalSeating1[i])+lenIL)==int(row_count[1])):
            finalSeating1[i].append(inputList1[q])
            del inputList1[q]
            break
            #q=q+1
        #elif(len(finalSeating[i])==2 and lenIL==2):
        #    finalSeating[i].append(inputList[q])
        #    q=q+1
        


finalSeating1

"""
len(inputList[1])
for line in file:
    
    print(line)
    if "W" in line:
        group= list(map(str, line.split()))
        group_len= len(group)
        if(int(row_count[1])< group_len):
            print("group length greater than number of seats")
        else:
            finalSeating.append([])
        
        print("found W")
        
finalSeating[0]=1

numrows = len()
numcols = len()


for i in range(int(row_count[0])):
    for j in range(int(row_count[1])):
        if finalSeating[i][j] is None:
            finalSeating[i][j]= 
    
    print(i)
""" 