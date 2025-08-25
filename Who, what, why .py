#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


import warnings
warnings.filterwarnings("ignore")


# pass

# In[7]:


df = pd.read_csv("netflix_titles.csv")
df.head()


# In[8]:


print("Shape of dataset:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDataset preview:\n", df.head())


# In[9]:


plt.figure(figsize=(6,5))
sns.countplot(data=df, x="type", palette="Set2")
plt.title("Distribution of Movies vs TV Shows", fontsize=14, weight="bold")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()


# In[10]:


titles_per_year = df["release_year"].value_counts().sort_index()


# In[11]:


plt.figure(figsize=(10,6))
sns.lineplot(x=titles_per_year.index, y=titles_per_year.values, marker="o")
plt.title("Number of Titles Released per Year", fontsize=14, weight="bold")
plt.xlabel("Release Year")
plt.ylabel("Count of Titles")
plt.show()


# In[12]:


type_trend = df.groupby(["release_year", "type"]).size().reset_index(name="count")
pivot = type_trend.pivot(index="release_year", columns="type", values="count").fillna(0)


# In[13]:


plt.figure(figsize=(10,6))
plt.stackplot(pivot.index, pivot["Movie"], pivot["TV Show"], labels=["Movies", "TV Shows"], alpha=0.8)
plt.legend(loc="upper left")
plt.title("Movies vs TV Shows Over Time", fontsize=14, weight="bold")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.show()


# In[14]:


country_series = df["country"].dropna().str.split(", ").explode()
top_countries = country_series.value_counts().head(10)


# In[15]:


plt.figure(figsize=(10,6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.title("Top 10 Content-Producing Countries", fontsize=14, weight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()


# In[16]:


pip install squarify


# In[18]:


import squarify


# In[19]:


plt.figure(figsize=(12,8))
squarify.plot(sizes=top_countries.values, label=top_countries.index, alpha=0.8, color=sns.color_palette("viridis", len(top_countries)))
plt.title("Treemap of Top Content-Producing Countries", fontsize=14, weight="bold")
plt.axis("off")
plt.show()


# In[20]:


genre_series = df["listed_in"].dropna().str.split(", ").explode()
top_genres = genre_series.value_counts().head(10)


# In[21]:


plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="mako")
plt.title("Top 10 Genres on Netflix", fontsize=14, weight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.show()

