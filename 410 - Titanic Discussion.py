#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as mp

data = pd.read_csv("/Users/stevenbaez/Desktop/train.csv")


# In[2]:


data.head()


# In[3]:


subset = data[['Survived','Age', 'Sex']]


# In[5]:


import numpy as np
import matplotlib


# In[20]:


sb.catplot(x="Age", y="Sex",
                hue="Survived", col="Embarked",
                notch = False,
                palette = "Set2",
                data=data, kind="box",
                height=4, aspect=.7);


# In[17]:


sb.catplot(x="Age", y="Sex",
                hue="Survived", col="Pclass",
                notch = True,
                palette = "Set2",
                data=data, kind="box",
                height=4, aspect=.7);


# In[ ]:




