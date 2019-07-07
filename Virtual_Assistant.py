#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Virtual_Assistant""" 
from datetime import date
from gtts import gTTS 
from datetime import datetime
from playsound import playsound
import numpy as np
import os
import calendar
def va():
    print("Please Wait.... \n\nIntro About My Virtual_Assistant")
    i=int(input("Enter to '0' or '1'to Skip Intro or Listen Intro==>"))
    if i==1:
        get_ipython().run_line_magic('run', 'Intro_VirtualAssist.ipynb')
    print("To Search for New KeyWords Enter Yes or Y")
    greetings = ['Hola!!', 'Hello', 'Hi', 'Hey There!', 'Hey']
    randomgreeting = np.random.choice(greetings)
    question = ['How are you', 'How are you doing','How r u','How are u']
    responses = ['Thanks for asking I am good!!!', "Ya!I'm fine"]
    res = ['Bye!!!', 'Tata!!', 'Bye & Catch you Later', 'Goodbye', 'See U Again', 'Have a GoodDay']
    res1 = ['Bye', 'Tata', 'Catch you Later', 'goodbye', 'seeuagain']
    randomres = np.random.choice(res)
    randomresponse = np.random.choice(responses)
    while True:
        try:
            userinput = input(">>>Search Anything :").capitalize()
            if userinput in greetings:
                get_ipython().run_line_magic('run', 'entry_VA.ipynb')
                print(randomgreeting)
            elif userinput in question:
                print(randomresponse)
            elif userinput.find(' your age') != -1 or userinput.find(' ur age') != -1 or userinput.find(' born') != -1:
                print("I am created recently so I am Pretty Young :)")
            elif userinput.find(' your weight') != -1 or userinput.find(' ur weight') !=-1 or userinput.find(' you weigh') !=-1 or userinput.find(' u weigh') !=-1 : 
                print("I am pretty Light Weight thing build with Python :)")
            elif userinput.find('tall') !=-1 or userinput.find('Tall') !=-1:
                print("It Depends on Device that your using to interact :)")
            elif userinput.find('smart are')!=-1 or userinput.find('smart r')!=-1 :
                print("My Smartness Depends on Creator who Created me :)")
            elif userinput in res1:
                get_ipython().run_line_magic('run', 'exit_VA.ipynb')
                print(randomres)
                break
            elif '+' in userinput:
                print(eval(userinput))
            elif  '-'  in userinput:
                 print(eval(userinput))
            elif  '*'  in userinput:
                print(eval(userinput))
            elif  '/'  in userinput:
                print(eval(userinput))
            elif  '//'  in userinput:
                print(eval(userinput))
            elif userinput.find('date') != -1 or (userinput=='date' ) or (userinput=='Date'):
                print(date.today())
            elif userinput.find(' time ') != -1 or (userinput=='time' ) or (userinput=='Time'):
                print(datetime.time(datetime.now()))
            elif userinput.find('Thankyou') != -1 or (userinput=='Tq')  or (userinput=='Thanku'):
                print("It's my Pleasure!!:)")
            elif userinput.find('calendar')!= -1 or (userinput=='calendar' ) or (userinput=='Calendar'):
                get_ipython().run_line_magic('run', 'DateTime_VA.ipynb')
            elif userinput.find('Quote') != -1 or userinput.find('Quotes') !=-1:
                get_ipython().run_line_magic('run', 'Quotes_VA.ipynb')
            elif userinput.find('Song') !=-1 or userinput=='Song' or userinput=='song':
                get_ipython().run_line_magic('run', 'Song_VA.ipynb')
            elif userinput.find('Weather') !=-1 or userinput.find('Climate')!=-1 or userinput.find('weather')!=-1 or userinput.find('climate')!=-1:
                get_ipython().run_line_magic('run', 'weather_VA.ipynb')
            elif (len(userinput)==0):
                print("Error 404 Command unable to reach!!")
            else:
                print("Do you Want to Know More? Yes or No")
                if userinput.startswith('y') or userinput.startswith('Y'):
                    get_ipython().run_line_magic('run', 'wiki_VA.ipynb')
                else:
                    break
        except:
            print("Oops!! Something went Wrong Verify...")
        
va()


# In[13]:




