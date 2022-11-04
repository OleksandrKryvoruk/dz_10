#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
2. Напишіть програму, яка б приймала список з числами та перевіряла
чи всі числа в ньому унікальні. Реалізуйте у функції декілька обробок
виключень.
"""
import sys

def ask_number(val):
    
    my_number = []
    
    try:
        my_number.extend(val)
        my_uninum = set(my_number)
        if sum(my_number) == sum(my_uninum):
            print("All numbers are unique")
        else:
            print("Numbers are not unique", file=sys.stderr)
        print("Entered numbers:", my_number)
        print("Unique numbers:", my_uninum)    
    except TypeError as err1:
        print(f"It's not an integer {err1}", file=sys.stderr)
    except Exception as err2:
        print(f"Something wrong {err2}", file=sys.stderr)

    
#ask_number([445, 67])
#ask_number([445, 67, 5, 5, 3, 6, 6])
ask_number(["fg", 67])

