
# coding: utf-8

# # Getting the data

# In[3]:

import numpy as np
import scipy as sc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# The data was downloaded from Kaggle.

# In[5]:

df = pd.read_csv("responses.csv")


# In[6]:

df.shape


# In[7]:

df.head(2)


# # Missing Values

# In[8]:

# Function to create a table that checks for missing values
def missing_values_table(df): 
        mis_val = df.isnull().sum()
        mis_val_percent = 100 * df.isnull().sum()/len(df)
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0: 'Missing Values', 1 : '% of Total Values'})
        return mis_val_table_ren_columns 


# Most features have less than 1% missing values, expect for heigh and weight have close to 2%.

# # Features: 150 total

# We have 150 features and the column names were very long and with spaces and other characters in between words that were not practical for processing. However, the long column names are importante as they explain each question (feature/variable) in our data set. We also have short column names, which also are not also very useful as they included special characters. Therefore, some parsing was done on the short column names to create new column names. These transformed column names replaced the original column names in the dataframes. 
# 

# We have a file containing the columns long name, and short name (columns.csv). Some parsing with python and regex was done, and transformed the column names were exported to a csv file (columns-transf.csv). In Excel, some other additional information was added (column values for categorical features). The end result resembles more like a metadata file as it includes the data type (nominal, ordinal, interval or ratio), and values for the ordinal and categorical features. 

# In[9]:

df_cols = pd.read_csv("columns.csv")


# In[10]:

df_cols.shape


# In[11]:

# change column names to have only alphanumeric, no spaces but '_' between words, an all lower case
#==================================================================================================
import re
col_names = list(df.columns.values)
#new_col_names = [col.replace("-",'') for col in col_names]
#new_col_names = [col.replace("/",'') for col in col_names]
#new_col_names = [col.replace(",",'') for col in col_names]
new_col_names = [re.sub(r'[^a-zA-Z0-9_\s]', '', col) for col in col_names]
new_col_names = [col.replace(' ', '_') for col in new_col_names]
new_col_names = [col.lower() for col in new_col_names]


# In[12]:

# include the transformed column names in dataframe that contains all column decscriptions (original name, short, etc)
df_cols['transf_col_name'] = new_col_names
#df_cols.to_csv('columns_transf1.csv')   # not needed anymore


# In[13]:

df_cols_transf = pd.read_csv("columns_transf.csv")


# In[14]:

df_cols_transf.shape


# # Features Description

# <b>Music Preferences: 19 items. </b>
# 
# All ordinal features. Type of responses:
# <ul>Slow paced music 1-2-3-4-5 Fast paced music (integer).</ul>
# <ul>Strongly disagree 1-2-3-4-5 Strongly agree (integer).</ul>
# <ul>Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer).</ul>

# In[15]:

music0 = df.iloc[:,0:19]


# In[16]:

print missing_values_table(music0)


# <b> Movies Preference: 12 items. </b>
# 
# All ordinal features. Types of responses:
# <ul>Strongly disagree 1-2-3-4-5 Strongly agree (integer)</ul>
# <ul>Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)</ul>

# In[17]:

movies0 = df.iloc[:,19:31]


# In[18]:

print missing_values_table(movies0)


# <b>Interests and Hobbies: 32 items.</b>
# 
# Ordinal features. Type of responses:
# <ul>Not interested 1-2-3-4-5 Very interested (integer)</ul>

# In[19]:

interests0 = df.iloc[:,31:46]
hobbies0 = df.iloc[:,46:63]
interests_hobbies0 = df.iloc[:,31:63]


# In[55]:

print missing_values_table(interests_hobbies0)


# <b>Phobias: 10 items.</b>
# 
# All ordinal features. Type of responses:
# <ul>Not afraid at all 1-2-3-4-5 Very afraid of (integer)</ul>

# In[56]:

phobias0 = df.iloc[:,63:73]


# In[57]:

print missing_values_table(phobias0)


# <b>Health Habits: 3 items.</b>
# 
# Ordinal features. Type of responses:
# <ul>Strongly disagree 1-2-3-4-5 Strongly agree (integer)</ul>    
# 
# Categorical features: Values shown in dictionaries below.

# In[58]:

# Smoking habits: Never smoked - Tried smoking - Former smoker - Current smoker (categorical)
dic_smoking = {'never smoked': 1, 'tried smoking':2, 'former smoker': 3, 'current smoker': 4}
# Drinking: Never - Social drinker - Drink a lot (categorical)
dic_alcohol = {'never':1, 'social drinker': 2, 'drink a lot': 3}


# In[59]:

health0 = df.iloc[:,73:76]


# In[60]:

print missing_values_table(health0)


# <b>Personality Traits: 57 items.</b>
# 
# Ordinal features. Types of responses:
# <ul>Strongly disagree 1-2-3-4-5 Strongly agree (integer)</ul>
# 
# Categorical features:

# In[61]:

# Timekeeping.: I am often early. - I am always on time. - I am often running late. (categorical)
dic_punctuality = {'i am often early':3, 'i am always on time': 2, 'i am often running late': 1}
# Do you lie to others?: Never. - Only to avoid hurting someone. - Sometimes. - Everytime it suits me. (categorical)
dic_lying = {'never': 1, 'only to avoid hurting someone': 2, 'sometimes': 3, 'everytime it suits me': 4}
# How much time do you spend online?: No time at all - Less than an hour a day - Few hours a day - Most of the day (categorical)
dic_internet_usage = {'no time at all': 1, 'less than an hour a day':2, 'few hours a day': 3, 'most of the day': 4 }


# In[62]:

traits0 = df.iloc[:,76:133]


# In[63]:

print missing_values_table(traits0)


# <b>Spending Habits: 7 items.</b>
# 
# All Ordinal features. Types of responses:
# <ul>Strongly disagree 1-2-3-4-5 Strongly agree (integer)</ul>

# In[64]:

spending0 = df.iloc[:,133:140]


# In[65]:

print missing_values_table(spending0)


# <b>Demographic features: 10 items.</b>
# 
# Numerical features (interval, ratio):
# <ul>Age: (integer) range = 15 - 30</ul>
# <ul>Height: (integer)</ul>
# <ul>Weight: (integer)</ul>
# <ul>How many siblings do you have?: (integer) range = 0 - 10 </ul>
# 
# Categorical features: Shown in the dictionaries below.

# In[66]:

# Gender: Female - Male (categorical)
dic_gender = {'female': 0, 'male': 1}
# I am: Left handed - Right handed (categorical)
dic_left_right_handed = {'left handed':0, 'right handed':1}
# Highest education achieved: Currently a Primary school pupil - Primary school - Secondary school - 
# College/Bachelor degree - Masters degree - Doctorate degree (categorical)
dic_education = {'currently a primary school pupil': 1, 'primary school':2, 'secondary school': 3, 'college/bachelor degree': 4, 'masters degree': 5, 'doctorate degree': 6}
# I am the only child: No - Yes (categorical)
dic_only_child = {'no': 0, 'yes': 1}
# I spent most of my childhood in a: City - village (categorical)
dic_village_town = {'village': 0, 'city': 1}
# I lived most of my childhood in a: house/bungalow - block of flats (categorical)
dic_house_block_of_flats = {'block of flats': 0, 'house/bungalow':1}


# In[67]:

demographics0 = df.iloc[:,140:150]


# In[68]:

print missing_values_table(demographics0)


# # Work dataframes with replaced column names

# I keep an original dataframe to verify or check some processing on the work dataframes. I have two work dataframes. One of them will be used for encoding categorical features as some techniques won't allow raw categorical values.

# In[69]:

df.columns = new_col_names
df1 = df.copy()
df1.columns = new_col_names
df2 = df.copy()
df2.columns = new_col_names


# # Work dataframes df1 and df2 : replacing categorical features values

# df1 will have the categorical features values replaced by integer values.

# In[70]:

# change values of categorical features to integer values

df1['alcohol'].replace(dic_alcohol, inplace = True)
df1['smoking'].replace(dic_smoking, inplace = True)

df1['punctuality'].replace(dic_punctuality, inplace = True)
df1['lying'].replace(dic_lying, inplace = True)
df1['internet_usage'].replace(dic_internet_usage, inplace = True)

df1['gender'].replace(dic_gender, inplace = True)
df1['left__right_handed'].replace(dic_left_right_handed, inplace = True)
df1['education'].replace(dic_education, inplace = True)
df1['village__town'].replace(dic_village_town, inplace = True)
df1['house__block_of_flats'].replace(dic_house_block_of_flats, inplace = True)
df1['only_child'].replace(dic_only_child, inplace = True)


# In[71]:

music = df1.iloc[:,0:19]
movies = df1.iloc[:,19:31]
interests = df1.iloc[:,31:46]
hobbies = df1.iloc[:,46:63]
interests_hobbies = df1.iloc[:,31:63]
phobias = df1.iloc[:,63:73]
health = df1.iloc[:,73:76]
traits = df1.iloc[:,76:133]
spending = df1.iloc[:,133:140]
demographics = df1.iloc[:,140:150]


# df2 will have the categorical features encoded as dummy variables with pandas get_dummies.

# In[72]:

music2 = df2.iloc[:,0:19]
movies2 = df2.iloc[:,19:31]
interests2 = df2.iloc[:,31:46]
hobbies2 = df2.iloc[:,46:63]
interests_hobbies2 = df2.iloc[:,31:63]
phobias2 = df2.iloc[:,63:73]
health2 = df2.iloc[:,73:76]
traits2 = df2.iloc[:,76:133]
spending2 = df2.iloc[:,133:140]
demographics2 = df2.iloc[:,140:150]


# In[73]:

df2 = pd.get_dummies(health2, prefix=['alc', 'smo'], columns=['alcohol', 'smoking'], dummy_na=True)
df2 = pd.get_dummies(traits2, prefix=['pun', 'lie', 'int'], columns=['punctuality', 'lying', 'internet_usage'], dummy_na=True)
df2 = pd.get_dummies(demographics2, prefix=['gen', 'hnd', 'edu', 'voc', 'hbf', 'one'], columns=['gender', 'left__right_handed', 'education', 'village__town', 'house__block_of_flats', 'only_child'], dummy_na=True)


# # Descriptive statistics and correlations within groups of features

# <h2><b>Demographics</b></h2>

# In[40]:

demographics0.gender.value_counts().plot(kind='bar')


# In[76]:

age_hist = demographics['age'].hist()
age_fig = age_hist.get_figure()


# In[290]:

sns.boxplot(x='age', data=demographics)


# In[78]:

demographics0.Education.value_counts().plot(kind='bar')


# In[66]:


edu_hist = demographics['education'].hist()
edu_fig = edu_hist.get_figure()


# In[37]:

#demo1 = df[['age', 'gender', 'number_of_siblings','village__town', 'education', 'house__block_of_flats', 'only_child']]
demo1 = df[['age', 'gender', 'education']]
demo1 = demo1.replace({'education': dic_education})
#df_melt=pd.melt(df,id_vars=['education'], var_name='village__town', value_name='number_of_siblings')
#sns.stripplot(x="education", y="number_of_siblings", data=df_melt, hue='village__town')
fig = plt.figure(figsize=(20,10))
pd.options.display.mpl_style = 'default'
demo1.boxplot(by='education')


# In[39]:

demographics0.village__town.value_counts().plot(kind='bar')


# In[41]:

demographics0.house__block_of_flats.value_counts().plot(kind='bar')


# In[72]:

#demo1 = df[['age', 'gender', 'number_of_siblings','village__town', 'education', 'house__block_of_flats', 'only_child']]
demo1 = df1[['house__block_of_flats', 'education']]
#df_melt=pd.melt(df,id_vars=['education'], var_name='village__town', value_name='number_of_siblings')
#sns.stripplot(x="education", y="number_of_siblings", data=df_melt, hue='village__town')
fig = plt.figure(figsize=(20,10))
pd.options.display.mpl_style = 'default'
demo1.boxplot(by='house__block_of_flats')


# In[42]:

demographics0.left__right_handed.value_counts().plot(kind='bar')


# In[43]:

demographics0.only_child.value_counts().plot(kind='bar')


# In[63]:

siblings_hist = demographics['number_of_siblings'].hist()
siblings_fig = siblings_hist.get_figure()


# In[75]:

sns.heatmap(demographics.corr(),annot=True)


# <h2><b>Music Preference</b></h2>

# In[84]:

plt.figure(figsize=(25,6))
sns.barplot(x = music0.describe().columns, y=music0.describe().loc['mean'])


# In[79]:

fig = plt.figure(figsize=(10,10))
sns.heatmap(music.corr(),annot=True)


# <h2><b>Movies Preference</b></h2>

# In[85]:

plt.figure(figsize=(25,6))
sns.barplot(x = movies0.describe().columns, y=movies0.describe().loc['mean'])


# In[80]:

fig = plt.figure(figsize=(10,10))
sns.heatmap(movies.corr(),annot=True)


# In[82]:

fig = plt.figure(figsize=(10,10))
sns.heatmap(interests_hobbies.corr(),annot=True)


# In[2]:

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(15,15)) 
sns.heatmap(traits.corr(),annot=True)


# In[81]:

fig, ax = plt.subplots(figsize=(10,10)) 
sns.heatmap(phobias.corr(),annot=True)


# In[33]:

fig, ax = plt.subplots(figsize=(10,10)) 
sns.heatmap(spending.corr(),annot=True)


# In[ ]:




# In[44]:

plt.figure(figsize=(25,6))
sns.barplot(x = interests_hobbies0.describe().columns, y=interests_hobbies.describe().loc['mean'])


# In[330]:

health_demo = pd.concat([health,demographics], axis=1)


# In[22]:

from bokeh.charts import Histogram
from bokeh.plotting import show
from bokeh.io import output_notebook


# In[23]:

output_notebook()


# In[ ]:




# In[ ]:

from scipy.stats import linregress

linregress(x,y) #x and y are arrays or lists.


# In[307]:

traits_demo = pd.concat([traits, demographics], axis=1)


# In[328]:

test = traits_demo.loc[(traits_demo['gender'] == 0.0) & (traits_demo['age'] < 20)]


# In[324]:

test = df.loc[(df['age'] > 24) & (df['gender'].isin(['male']))]


# In[325]:

junk = test.hist('unpopularity')


# In[294]:

junk = traits.hist('loneliness')


# In[295]:

junk = traits.hist('assertiveness')


# In[296]:

junk = traits.hist('internet_usage')


# In[297]:

junk = traits.hist('personality')


# In[298]:

junk = traits.hist('life_struggles')


# In[338]:

fig = plt.figure(figsize=(20,20))
scol = spending.columns.values
print scol
#spending[col].hist()


# In[ ]:



