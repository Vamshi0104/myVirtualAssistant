#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date
from datetime import datetime
import calendar
def dt():
    yy = int(input("Enter year to Display: "))  
    mm = int(input("Enter Month to Display or Else enter '0' to display Complete Year: "))
    if mm == 0:
        print(calendar.calendar(yy))
    else:
        print(calendar.month(yy,mm)) 
dt()

