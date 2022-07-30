#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import random
from gmssl import sm3, func


# In[2]:


def improved_birthday_attack(l):
    m=2**l
    x=random.randint(0,m).to_bytes(4, byteorder='little', signed=True)
    x1=x;x2=x;i=0
    while(1):
        x1=bytes(sm3.sm3_hash(func.bytes_to_list(x1)),encoding ="utf8")
        x2=bytes(sm3.sm3_hash(func.bytes_to_list(x2)),encoding ="utf8")
        x2=bytes(sm3.sm3_hash(func.bytes_to_list(x2)),encoding ="utf8")
        i+=1
        if x1 == x2: break
    x2=x1;x1=x
    for i in range (1,i):
        if sm3.sm3_hash(func.bytes_to_list(x1))==sm3.sm3_hash(func.bytes_to_list(x2)):
            return (x1,x2)
            break
        else:
            x1=bytes(sm3.sm3_hash(func.bytes_to_list(x1)),encoding ="utf8")
            x2=bytes(sm3.sm3_hash(func.bytes_to_list(x2)),encoding ="utf8")
    


# In[ ]:


a=improved_birthday_attack(10)


