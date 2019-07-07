#!/usr/bin/env python
# coding: utf-8

# In[3]:


import wikipedia 
from selenium import webdriver
str1=input(">>>Search for Any Word:")
l=['what','is','who','why','a','an','the','how','when','are','','was','there','their','then','this','that','?','.']
m=str1.split()
rw=[x for x in m if x.lower()  not in l and x.isalpha()]
k=' '.join(rw)
wikipedia.set_lang("en")
print (wikipedia.summary(k))
temp=input("Want to Explore more about Search String?Yes or No").startswith('y')
if temp==True:
    driver=webdriver.Chrome(executable_path='C:\Python\chromedriver.exe')
    driver.get('https://en.wikipedia.org/wiki/'+k)
else:
    print("Explore More,Knownledge is Wisdom!!")    

