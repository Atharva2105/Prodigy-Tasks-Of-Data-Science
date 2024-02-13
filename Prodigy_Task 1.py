#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.


# In[4]:


import numpy as numpy 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[9]:


# Read the entire dataset from a CSV file
df = pd.read_csv("Total Population.csv", index_col=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'])


# In[10]:


# Choose multiple countries for comparison
selected_countries = ["United States", "China", "India"]
population_data = df.loc[selected_countries, :]


# In[11]:


# Extract years and corresponding population data for each country
years = population_data.columns[4:]
population_values = population_data.iloc[:, 4:]


# In[12]:


# Plotting the bar chart
plt.figure(figsize=(15, 6))
plt.subplot(1, 1, 1)
population_values.T.plot(kind='bar', ax=plt.gca())
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Bar Chart Comparison')
plt.legend(title='Country')


# In[13]:


# Plotting the histogram
plt.subplot(1, 2, 2)
population_values.T.plot(kind='hist', bins=10, alpha=0.7, stacked=True, ax=plt.gca())
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.title('Population Histogram Comparison')
plt.legend(title='Country')


# In[ ]:




