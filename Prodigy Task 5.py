#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Analyze traffic accident data to identify patterns related to road conditions, weather, and time of day. Visualize accident hotspots and contributing factors.


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("RTA Dataset.csv")


# In[4]:


df.head()


# In[5]:


# Visualize accident hotspots
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Number_of_vehicles_involved', y='Number_of_casualties', hue='Accident_severity', data=df)
plt.title('Accident Hotspots and Severity')
plt.show()


# In[6]:


# Visualize contributing factors
plt.figure(figsize=(16, 6))
sns.countplot(x='Weather_conditions', hue='Accident_severity', data=df)
plt.title('Contributing Factors: Weather Conditions')
plt.show()


# In[7]:


# Visualize Age distribution of drivers
plt.figure(figsize=(12, 6))
sns.histplot(x='Age_band_of_driver', data=df, bins=20, kde=True)
plt.title('Age Distribution of Drivers')
plt.show()


# In[8]:


# Visualize Time of day vs. Accident count
plt.figure(figsize=(12, 6))
sns.countplot(x='Time', data=df, order=df['Time'].value_counts().index)
plt.title('Accident Count by Time of Day')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[9]:


# Visualize Day of week vs. Accident count
plt.figure(figsize=(10, 6))
sns.countplot(x='Day_of_week', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Accident Count by Day of Week')
plt.show()


# In[10]:


# Visualize Type of Collision vs. Accident severity
plt.figure(figsize=(12, 6))
sns.countplot(x='Type_of_collision', hue='Accident_severity', data=df)
plt.title('Type of Collision vs. Accident Severity')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[11]:


# Visualize Light conditions vs. Accident severity
plt.figure(figsize=(12, 6))
sns.countplot(x='Light_conditions', hue='Accident_severity', data=df)
plt.title('Light Conditions vs. Accident Severity')
plt.show()


# In[ ]:




