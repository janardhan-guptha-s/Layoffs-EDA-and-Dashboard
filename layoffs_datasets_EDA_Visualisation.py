#!/usr/bin/env python
# coding: utf-8

# ### In this notebook, I have explored the data, transformed the data to required format using Pandas, visualized the data using Plotly & found the below observations: 
# 1. Top 10 companies that laid off
# 1. Top 3 companies that laid off year-wise
# 1. Top 3 locations where most layoffs happened year-wise
# 1. Top 20 companies that laid off x% of employees
# 1. Top 10 countries where most layoffs happened
# 1. Top 10 locations where most layoffs happened in USA
# 1. Top locations where most layoffs happened in India
# 1. Relationship between funds received and layoffs
# 1. In which stage of the company had the most lay offs?
# 1. Which industry had the most layoffs?
# 1. Total layoffs year-wise
# 1. Year wise layoffs according to country

# # Importing libraries

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# # Let`s dive into the data 

# In[33]:


df = pd.read_csv('layoffs.csv')
df


# In[34]:


# Total companies
df.company.nunique()
len(df.company.unique())


# In[35]:


# But shape is 1634
df.shape


# ### Total company count and the Shape is 3806. Let's see duplicate companies

# In[36]:


df.company.value_counts().sort_values(ascending=False)


# In[37]:


df.company.value_counts() > 1


# In[38]:


df[df.company == "Uber"]


# ### Company can lay off on different dates. So, there are duplicate company values

# In[39]:


df.groupby('company').sum()


# In[40]:


df.groupby('company').sum().loc['Uber',:]


# ### Find NaNs

# In[41]:


df.head(2)
df.isnull().sum()


# ### Fill NaNs with 0s

# In[14]:


df.fillna(value=0,inplace=True)
df.isnull().sum()


# In[42]:


df.head()


# ## Top 10 companies that laid off 

# In[45]:


top10_idx = df['total_laid_off'].sort_values(ascending=False)[:10].index
top10_idx
df.iloc[top10_idx,:]
px.bar(df.iloc[top10_idx,:],x='company',y='total_laid_off', text='total_laid_off',title='Top 10 companies that laid off')


# ### This is wrong, Meta and Amazon are repeated. Need to clean the data such that there are no duplicate companies.

# In[46]:


df_no_dup = df.copy()


# In[48]:


# Top 10 companies that laid off 
df_no_dup.groupby('company').total_laid_off.sum().sort_values(ascending=False)[:10]
px.bar(df_no_dup.groupby('company').total_laid_off.sum().sort_values(ascending=False)[:10],text_auto=True,title='Top 10 companies that laid off',
      labels={"x":"Company","y":"Layoffs"})


# ### This is correct :)

# # Top 3 companies that laid off year-wise

# In[55]:


df.head()


# In[56]:


df = df[df['date'] != '2025-09-23'] # 2025 delete


# In[57]:


df.head()


# ### Need to filter only year from date column

# In[58]:


df["Year"] = df["date"].map(lambda x : x[:4])
df


# In[62]:


df.groupby(["Year"],sort=False)["total_laid_off"].max()


# In[63]:


df.groupby(['Year','company']).total_laid_off.agg([max])


# In[87]:


top_3_year_wise = df.groupby(['Year','company']).total_laid_off.agg([max])
top_3_year_wise


# In[88]:


top_3_year_wise["max"]
top_3_year_wise["max"].groupby(['Year'],group_keys=False)


# In[89]:


# Got it from https://stackoverflow.com/questions/27842613/pandas-groupby-then-sort-within-groups 
g = top_3_year_wise["max"].groupby(['Year'],group_keys=False)
top_3_year_wise2 = g.apply(lambda x : x.sort_values(ascending=False).head(3)) # Selecting each group, sorting & taking top 3
top_3_year_wise2


# In[90]:


g.nlargest(3) # Get top 3 in each group ( inbuilt method )


# In[91]:


top_3_year_wise2.index
top_3_year_wise2.values


# In[92]:


top_3_year_wise3 = pd.DataFrame()
top_3_year_wise3["total_laid_off"] = top_3_year_wise2.values
top_3_year_wise3


# In[93]:


y = []
c = []
for i,j in top_3_year_wise2.index:
    y.append(i)
    c.append(j)
top_3_year_wise3["Year"] = y
top_3_year_wise3["Company"] = c
top_3_year_wise3


# In[94]:


px.bar(top_3_year_wise3,x='Year',y='total_laid_off',color='Company', title='Top 3 companies that laid off year-wise',text_auto=True)


# ## Top 3 locations where most layoffs happened year-wise

# In[73]:


df.head()
top_3_loction_year_wise = df.groupby(["Year","location"]).total_laid_off.agg([max])
top_3_loction_year_wise


# In[76]:


g1 = top_3_loction_year_wise.groupby(["Year"],group_keys=False)
top_3_loction_year_wise2 = g1.apply(lambda x : x.sort_values(["max"], ascending=False).head(3)) 
top_3_loction_year_wise2


# In[78]:


top_3_loction_year_wise2.values.reshape(15,).tolist()


# In[80]:


top_3_loction_year_wise3 = pd.DataFrame()
top_3_loction_year_wise3["total_laid_off"] = top_3_loction_year_wise2.values.reshape(15,).tolist()
top_3_loction_year_wise3


# In[95]:


y = []
l = []
for i,j in top_3_loction_year_wise2.index:
    y.append(i)
    l.append(j)
top_3_loction_year_wise3["Year"] = y
top_3_loction_year_wise3["Location"] = l
top_3_loction_year_wise3


# In[96]:


px.bar(top_3_loction_year_wise3,x='Year',y='total_laid_off',color='Location', title='Top 3 locations year-wise where layoffs happened the most',text_auto=True)


# ## Top 20 companies that laid off x% of employees

# In[84]:


(df_no_dup.groupby('company').percentage_laid_off.sum().sort_values(ascending=False)[:20])*100
px.bar((df_no_dup.groupby('company').percentage_laid_off.sum().sort_values(ascending=False)[:20])*100,text_auto=True,title='Top 20 companies that laid off x% of employees')


# In[97]:


# Country wise lay offs percentage
country_group  = df.groupby(['country']).sum().sort_values(['total_laid_off'],ascending=False)
country_group.head(10)


# ## Top 10 countries where most layoffs happened

# In[98]:


px.bar(country_group.iloc[:10,0],text_auto=True,title='Top 10 countries where most layoffs happened')


# ## Top 10 locations where most layoffs happened in USA

# In[99]:


# Only USA location wise
location_usa_group  = df[df.country == "United States"].groupby(['location']).sum().sort_values(['total_laid_off'],ascending=False)
location_usa_group


# In[100]:


# Top 10 places in the US
px.bar(location_usa_group.iloc[:10,:1], text_auto=True,title='Top 10 locations where most layoffs happened in USA')


# ## Top 10 locations where most layoffs happened in India

# In[101]:


px.bar(df[df.country == "India"].groupby(['location']).sum().sort_values(['total_laid_off'],ascending=False).iloc[:10,:1], text_auto=True,title='Top locations where most layoffs happened in India')


# ## Relationship between funds and layoffs
# 

# In[102]:


df["funds_raised"].corr(df["total_laid_off"])
px.line(df,x='total_laid_off',y='funds_raised',hover_name='company')
px.line(df,x='funds_raised', y='total_laid_off',hover_name='company')


# In[103]:


px.scatter(df,x='funds_raised', y='total_laid_off',hover_name='company')
px.scatter(df,x='total_laid_off',y='funds_raised',hover_name='company')


# ### As we can see in the above plot, there is no dependency b/w funds & lay offs

# ## In which stage of the company had the most lay offs?

# In[104]:


df["stage"].unique()


# In[105]:


df.groupby(["stage"]).total_laid_off.sum()


# In[106]:


px.bar(df.groupby(["stage"]).total_laid_off.sum().sort_values(ascending=False),title='Layoffs & company stage',
       text_auto=True,orientation='h'
      )


# ## Which industry had the most layoffs?

# In[113]:


df['industry'] = df['industry'].replace('https://www.calcalistech.com/ctechnews/article/rysmrkfua', 'calcalistech')


# In[114]:


top_industry_wise = df.groupby(['industry']).total_laid_off.sum().sort_values(ascending=False)
top_industry_wise


# In[115]:


top_industry_wise.shape


# In[116]:


px.bar(x=top_industry_wise.index,y=top_industry_wise.values,text_auto=True,labels={'x': 'Industry', 'y':'Layoffs'},
      title='Industry vs Layoffs')


# ## Total layoffs year-wise

# In[117]:


total_laid_year_wise = df.groupby(["Year"]).total_laid_off.sum()
total_laid_year_wise


# In[118]:


px.bar(x=total_laid_year_wise.index,y=total_laid_year_wise.values,
      labels={"x":"Year","y":"Layoffs"},
       text_auto=True,
       title="Year-wise layoffs"
      )


# ## Year wise layoffs according to country

# In[119]:


total_laid_year_country_wise = df.groupby(["Year","country"]).total_laid_off.sum()
total_laid_year_country_wise


# In[120]:


len(df.country.unique()) # We have 55 countries


# In[121]:


total_laid_year_country_wise_year = []
total_laid_year_country_wise_country = []
for i,j in total_laid_year_country_wise.index:
    total_laid_year_country_wise_year.append(i)
    total_laid_year_country_wise_country.append(j)


# In[122]:


total_laid_year_country_wise2 = pd.DataFrame({
    "Year": total_laid_year_country_wise_year,
    "Country": total_laid_year_country_wise_country,
    "total_laid_off": total_laid_year_country_wise.values 
})


# In[123]:


total_laid_year_country_wise2


# In[124]:


total_laid_year_country_wise2.sort_values(["Year","total_laid_off"],ascending=False,inplace=True)


# In[125]:


px.bar(total_laid_year_country_wise2,x='Year',y='total_laid_off',color='Country',text='Country',
      title='Year wise layoffs according to country'
      )

