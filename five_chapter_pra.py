# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:39:42 2020

@author: 我思故我在
"""

#1、创建一个你最喜欢歌手的列表。
siger=["wlh","GD","zjl","ljj"]
print(siger)

#2、创建一个由元组构成的列表，每个元组包含居住过或旅游过的城市的经纬度。
location=[(35.2300,14.0002),(45.30007,37.20001),(50.0004,45.6667)]
print(location)

#3、构建一个包含你不同属性的字典：身高、最喜欢的颜色和最喜欢的作者等。
My_quality={"height":"178","lovecolor":"blue","loveauthor":"Yuhua"}
print(My_quality)

#4、编写一个程序，让用户询问你的身高、最喜欢的颜色或最喜欢的作者，并返回上一个挑战者创建的字典。
h=input("How tall are you,please:")
c=input("Which color do you like best:")
a=input("Which author do you like best:")

My_quality["height"]=h
My_quality["lovecolor"]=c
My_quality["loveauthor"]=a
print(My_quality)
#何夏华最强。
#5、创建一个字典，将最喜欢的歌手映射至最喜欢的歌曲。
siger_song={"zjl":"gbqq","wlh":"wmdg"}
print(siger_song)

#6、列表、元组和容器只是Python中内置容器的一部分。自行研究Python中的集合（也是一种容器）在什么情况下可以使用集合。
