#!/usr/bin/env python
# coding: utf-8

# In[16]:


"""
3. Напишіть користувацький клас виключення з функціоналом на свій
вибір. Викличте його за допомогою інструкції гаїзе.
"""
class NameCheck(Exception):
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        if self.name == "":
            return 'name is empty!'
        else:
            return self.name

raise NameCheck("")

