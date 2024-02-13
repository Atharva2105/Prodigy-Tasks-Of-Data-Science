#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Perform data cleaning and explloratory data analysis on a datset of your choice such asthe Titanic dataset from Kaggle. Explore the relationship between varibales and identify patterns and trends in the data


# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


df = pd.read_csv("Titanic_data.csv")


# In[3]:


# Explore relationships between variables
sns.set(style="whitegrid")
plt.figure(figsize=(15, 8))


# In[4]:


# Relationship between Age and Fare
plt.subplot(2, 2, 1)
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df, palette='viridis')
plt.title('Relationship between Age and Fare')


# In[5]:


# Distribution of Pclass
plt.subplot(2, 2, 2)
sns.countplot(x='Pclass', hue='Survived', data=df, palette='muted')
plt.title('Distribution of Pclass')


# In[6]:


# Distribution of Sex
plt.subplot(2, 2, 3)
sns.countplot(x='Sex', hue='Survived', data=df, palette='pastel')
plt.title('Distribution of Sex')


# In[7]:


# Distribution of Embarked
plt.subplot(2, 2, 4)
sns.countplot(x='Embarked', hue='Survived', data=df, palette='deep')
plt.title('Distribution of Embarked')


# In[ ]:




