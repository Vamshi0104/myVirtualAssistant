#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
def ranl(f):
    line = open(f).read().splitlines()
    return random.choice(line)
print(ranl('quotes.txt'))

