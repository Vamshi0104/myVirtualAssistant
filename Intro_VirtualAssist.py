#!/usr/bin/env python
# coding: utf-8

# In[2]:


from gtts import gTTS 
from playsound import playsound
import os 
def a():
    msg = '''Hi Vamshi. I am your VirtualAssistant ,assist you by performing calculations and providing dailyquotes,date,time,calendar and respond according to input . I am not a Robot but just a machine with userdefined funtionalities taking inputs and respond them in userfriendly way .So, feelfree to type in below inputbox for immediate response.'''
    t= gTTS(text=msg, lang='en', slow=False)
    playsound("intro_va.mp3")
a()

