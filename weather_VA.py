#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\Python\chromedriver.exe')
driver.get('https://www.yahoo.com/news/weather/')

