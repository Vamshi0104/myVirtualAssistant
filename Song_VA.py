#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from playsound import playsound
def f():
    while True:
            print("Here is Your Playlist Content :)")
            line = open("songs.txt").read()
            print(line)
            n=input("Which song or Background Music would we choose?\n")
            print("Note:Since there is no pause and stop button on selecting song would be played till last.")
            try:
                print("Playing your song or Background Music  Please Wait...")
                playsound(n+'.mp3')
                print("It was Awesome right!!")
            except:
                print('''Can't Find Your Song in Playlist!!:( 
        
                     Here is Your Playlist Content :)''')
                line = open("songs.txt").read()
                print(line)
                break
f()


# In[ ]:




