# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:55:34 2020

@author: 我思故我在
"""

#1、在计算机上找一个文件，并使用Python打印其内容。
import csv
with open("my_test.txt","w") as f:
#    f.write("Hello!I am Python!")
    st=csv.writer(f,delimiter=",")
    st.writerow(["good","morning!"])
    
with open("my_test.txt","r") as f:
#    print(f.read())
    r=csv.reader(f,delimiter=",")
    for i in r:
        print(",".join(i))

#2、编写一个程序来向用户提问，并将回答保存至文件。
i=input("Are you like orange?")
with open("my_test.txt","w") as f:
   f.write(i)

#3、将以下列表中的元素写入一个CSV文件：[["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man or Fire","Flight"]]。每个列表应该在文件中各占一行，其中元素使用逗号分隔。
import csv
with open("TestCSV.csv","w") as f:
    st=csv.writer(f,delimiter=",")
    st.writerow(["Top Gun","Risky Business","Minority Report"])
    st.writerow(["Titanic","The Revenant","Inception"])
    st.writerow(["Training Day","Man or Fire","Flight"])