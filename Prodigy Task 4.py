#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Analyze and visualize sentiment patterns in social media data to understand public opinion and attitudes towards specific topics or brands.


# In[16]:


#Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


# Data PreProcessing


# In[18]:


data = pd.read_csv("twitter_training.csv",header = None)
data.head()


# In[19]:


columns= ['Tweet ID','Subject','Sentiment', 'Text']  
data.columns = columns
data.head()


# In[ ]:


# Visualising Distribution Of Sentiments


# In[22]:


sentiments = data['Sentiment'].value_counts()
sentiments


# In[23]:


plt.figure(figsize=(10, 8))
sns.barplot(x=sentiments.index, y=sentiments.values)
plt.title('Sentiment Distribution',fontsize = 22)
plt.xlabel('Sentiment',fontsize = 17)
plt.ylabel('Count',fontsize = 17)
plt.show()

