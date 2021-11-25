#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[74]:


df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]}) 
df.groupby('grps').apply(lambda x: x.vals.nlargest(3).sum())

