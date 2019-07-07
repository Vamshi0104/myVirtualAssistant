#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gtts import gTTS 
from playsound import playsound
import os 
def bye():
    msg = "Bye Vamshi, Catch u later and Have a Good Day!!"
    t= gTTS(text=msg, lang='en', slow=False)
    playsound("bye.mp3")
bye()

