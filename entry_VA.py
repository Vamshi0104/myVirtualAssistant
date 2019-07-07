#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gtts import gTTS 
from playsound import playsound
import datetime
import os
currentTime = datetime.datetime.now()
def hi():
    if currentTime.hour < 12:
        msg = "GoodMorning Vamshi , Welcome Back! It's been Long Time Interact by having a Morning Coffee"
    elif 12 <= currentTime.hour < 18:
        msg = "GoodAfternoon Vamshi , Welcome Back! It's been Long Time Interact by having a Cupof Tea"
    else:
         msg = "GoodEvening Vamshi , Welcome Back! It's been Long Time!"          
    t= gTTS(text=msg, lang='en', slow=False)
    playsound("hi.mp3")
hi()

