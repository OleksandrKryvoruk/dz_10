#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
1. функцЈю, яка б приймала номер мЈсяця, а вертала його
назву. у функцјт декЈлькг обробок виключень.
"""
import sys

def ask_mounth():
    
    my_mounth = {1:'january', 2:'febrary', 3:'march', 4:'april', 5:'may', 6:'june',
            7:'july', 8:'august', 9:'september', 10:'october', 11:'november', 12:'december'}
    
    try:
        val = int(input("Enter the number of mounth: "))
        print(my_mounth[val])
    except KeyError as err1:
        print(f"It's out of range from 1 to 12 - {err1}", file=sys.stderr)
    except ValueError as err2:
        print(f"It's not an integer - {err2}", file=sys.stderr)
    finally:
        print("finally called")
    
ask_mounth()

