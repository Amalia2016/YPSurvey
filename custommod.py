# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:31:14 2017

@author: Amalia
"""

#import matplotlib.pyplot as plt
#import simplejson as json
#import urllib2
#import requests
import numpy as np
import scipy as sc
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

#import quandl

#import io

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.resources import CDN, Resources, INLINE
from bokeh.embed import components, autoload_static, file_html, standalone_html_page_for_models

from bokeh.charts import Bar, Histogram, output_file, show, defaults
from bokeh.charts.attributes import cat, color
from bokeh.charts.operations import blend
from bokeh.charts.utils import df_from_json
from bokeh.charts import defaults

from bokeh.io import output_notebook, save


#from bokeh.util.browser import view
#from jinja2 import Template

def descriptive(df):
  
    health0 = df.iloc[:,73:76]
    spending0 = df.iloc[:,133:140]
    demographics0 = df.iloc[:,140:150]
    
    df2 = pd.concat([demographics0, spending0, health0], axis=1).reset_index(drop=True)
    df2.dropna(inplace=True)
    age = df2[['Age']].copy()
    age.dropna(inplace=True)

    #pd.options.display.float_format = '{:,.0f}'.format

    dic_smoking = {'never smoked': '1 - never smoked', 'tried smoking':'2 - tried smoking', 'former smoker': '3 - former smoker', 'current smoker': '4 - current smoker'}
    dic_alcohol = {'never':'1 - never', 'social drinker': '2 - social drinker', 'drink a lot': '3 - drink a lot'}
    df2['Alcohol'].replace(dic_alcohol, inplace = True)
    df2['Smoking'].replace(dic_smoking, inplace = True)
   
    defaults.width = 350
    defaults.height = 350
    defaults.tools = False

    p_gen = Bar(df2, label = 'Gender', color=color(columns='Gender', palette=['Red', 'Green', 'Yellow'],
                      sort=False), title="Frequencies by Gender", legend = 'top_right')
    p_age = Histogram(age, values = 'Age', bins = 10, title="Frequencies by Age", color = 'Blue')
    p_edu = Bar(df2, label = 'Education', title="Frequencies by Education Level", legend=False, color='Orange')
   
 
   
    p_4 = Bar(df2, label='Finances', agg='mean', group='Gender',
        title="Savers, by GENDER", legend = False)
    p_5 = Bar(df2, label='Branded clothing', agg='mean', group='Gender',
        title="Spenders on Branded Clothing, by GENDER", legend = False)
    p_6 = Bar(df2, label='Entertainment spending', agg='mean', group='Gender',
        title="Spenders on Entertainment, by GENDER", legend = False)
    p_7 = Bar(df2, label='Spending on looks', agg='mean', group='Gender',
        title="Spenders on Looks, by GENDER", legend = False)
    p_8 = Bar(df2, label='Spending on gadgets', agg='mean', group='Gender',
        title="Spenders on Gadgets, by GENDER", legend = False)
    p_9 = Bar(df2, label='Spending on healthy eating', agg='mean', group='Gender',
        title="Spenders on Healthy Eating, by GENDER", legend = False)
    p_10 = Bar(df2, label='Smoking', agg='mean', group='Gender',
        title="Smoking, by GENDER", legend = False)
    p_11 = Bar(df2, label='Alcohol', agg='mean', group='Gender',
        title="Drinking, by GENDER", legend = False)
    p_12 = Bar(df2, label='Healthy eating', agg='mean', group='Gender',
        title="Healthy Lifestyle, by GENDER", legend = False) 

    resources = INLINE

    js_resources = resources.render_js()
    css_resources = resources.render_css()
    
    script1, div1 = components(p_gen)
    script2, div2 = components(p_age)
    script3, div3 = components(p_edu)

    script4, div4 = components(p_4)
    script5, div5 = components(p_5)
    script6, div6 = components(p_6)
    script7, div7 = components(p_7)
    script8, div8 = components(p_8)
    script9, div9 = components(p_9)
    script10, div10 = components(p_10)
    script11, div11 = components(p_11)
    script12, div12 = components(p_12)
            
    return js_resources, css_resources, script1, div1, script2, div2, script3, div3, script4, div4, script5, div5, script6, div6, script7, div7, script8, div8, script9, div9, script10, div10, script11, div11, script12, div12


def preprocess_nan(df, r):
    cat_list = ['Gender','Left - right handed','Education','Only child','Village - town','House - block of flats',
                'Smoking', 'Alcohol', 'Punctuality', 'Lying', 'Internet usage']
    float_list = ['Height', 'Weight', 'Age']
    all_list = df.columns.tolist()
    numeric_cols = [x for x in all_list if x not in cat_list+float_list]
    if r == 1:                  # for visualization of distributions not necessary to show missing values
        df.dropna(inplace=True)  
    elif r == 2:                # for correlations
        df.dropna(subset= cat_list, inplace=True)
        df.fillna(0, inplace=True)
    elif r == 3:                # for modeling
        df.fillna(df.mean(), inplace=True)
    df[numeric_cols] = df[numeric_cols].astype(int)   # all ordinal features should be integer
    return df

def preprocess_cat_plot(df):
    dic_smoking = {'never smoked': '1 - never smoked', 'tried smoking':'2 - tried smoking', 'former smoker': '3 - former smoker', 'current smoker': '4 - current smoker'}
    dic_alcohol = {'never':'1 - never', 'social drinker': '2 - social drinker', 'drink a lot': '3 - drink a lot'}
    df['Alcohol'].replace(dic_alcohol, inplace = True)
    df['Smoking'].replace(dic_smoking, inplace = True)
    
    dic_punctuality = {'i am often early': '3 - i am often early', 'i am always on time': '2 - i am always on time', 'i am often running late': '1 - i am often running late'}
    dic_lying = {'never': '1 - never', 'only to avoid hurting someone': '2 - only to avoid hurting someone', 'sometimes': '3 - sometimes', 'everytime it suits me': '4 - everytime it suits me'}
    dic_internet_usage = {'no time at all': '1 - no time at all', 'less than an hour a day': '2 - less than an hour a day', 'few hours a day': '3 - few hours a day', 'most of the day': '4 - most of the day' }
    dic_education = {'currently a primary school pupil': '1 - currently a primary school pupil', 'primary school':'2 - primary school', 'secondary school': '3 - secondary school', 'college/bachelor degree': '4 - college/bachelor degree', 'masters degree': '5 - masters degree', 'doctorate degree': '6 - doctorate degree'}
    
    df['Punctuality'].replace(dic_punctuality, inplace = True)
    df['Lying'].replace(dic_lying, inplace = True)
    df['Internet usage'].replace(dic_internet_usage, inplace = True)
    df['Education'].replace(dic_education, inplace = True)
    return df

def preprocess_cat_mod(df):
    dic_smoking = {'never smoked': 1, 'tried smoking':2, 'former smoker': 3, 'current smoker': 4}
    dic_alcohol = {'never':1, 'social drinker': 2, 'drink a lot': 3}
    df['alcohol'].replace(dic_alcohol, inplace = True)
    df['smoking'].replace(dic_smoking, inplace = True)

    dic_punctuality = {'i am often early':3, 'i am always on time': 2, 'i am often running late': 1}
    dic_lying = {'never': 1, 'only to avoid hurting someone': 2, 'sometimes': 3, 'everytime it suits me': 4}
    dic_internet_usage = {'no time at all': 1, 'less than an hour a day':2, 'few hours a day': 3, 'most of the day': 4 }
    df['punctuality'].replace(dic_punctuality, inplace = True)
    df['lying'].replace(dic_lying, inplace = True)
    df['internet_usage'].replace(dic_internet_usage, inplace = True)

    dic_gender = {'female': 0, 'male': 1}
    dic_left_right_handed = {'left handed':0, 'right handed':1}
    dic_education = {'currently a primary school pupil': 1, 'primary school':2, 'secondary school': 3, 'college/bachelor degree': 4, 'masters degree': 5, 'doctorate degree': 6}
    dic_only_child = {'no': 0, 'yes': 1}
    dic_village_town = {'village': 0, 'city': 1}
    dic_house_block_of_flats = {'block of flats': 0, 'house/bungalow':1}
    df['gender'].replace(dic_gender, inplace = True)
    df['left__right_handed'].replace(dic_left_right_handed, inplace = True)
    df['education'].replace(dic_education, inplace = True)
    df['village__town'].replace(dic_village_town, inplace = True)
    df['house__block_of_flats'].replace(dic_house_block_of_flats, inplace = True)
    df['only_child'].replace(dic_only_child, inplace = True)
    return df

def preprocess_outliers(df):
    return df

def create_categories(df):
    # column names for categories
    music = df.iloc[:,0:19].columns.tolist()
    movies = df.iloc[:,19:31].columns.tolist()
    #interests_hobbies = df1.iloc[:,31:63].columns.tolist()
    phobias = df.iloc[:,63:73].columns.tolist()
    health = df.iloc[:,73:76].columns.tolist()
    traits = df.iloc[:,76:133].columns.tolist()
    spending = df.iloc[:,133:140].columns.tolist()
    demographics = df.iloc[:,140:150].columns.tolist()
    interests = df.iloc[:,31:46].columns.tolist()
    hobbies = df.iloc[:,46:63].columns.tolist()
    
    d_categ = {'music': music, 'movies': movies, 'interests': interests, 'hobbies': hobbies, 'phobias': phobias, 'health': health, 'traits': traits, 'spending': spending, 'demographics': demographics}
    return d_categ
    
def plotting(df, category):
    # clean missing values
    df1 = df.copy()
    df1 = preprocess_nan(df, 1)
    df1 = preprocess_cat_plot(df1)
    d_categ = create_categories(df1)
    if category not in d_categ:
        return False, False, False, False
    
    col_label = d_categ[category]
    
    verify = True if all([True if col in df1.columns.tolist() else False for col in col_label]) else False
    if not verify:
        return False, False, False, False
    
    df2 = df1[col_label].copy()
  
    defaults.width = 350
    defaults.height = 350
    defaults.tools = False
    
    col_type = [True if df2[col].dtype == 'float' else False for col in col_label]
    #fig_title = ['Frequencies by '+col for col in col_label]
    #paletteBar = ['Red', 'Green', 'Yellow']
    colorBar   = 'Orange'
    colorHist  = 'Blue'
    #group_by = ['Gender']
    
    fig = [figure() for i in range(len(col_label))]
    for i in range(len(col_label)):
        if col_type[i]:
            fig[i] = Histogram(df2, values = col_label[i], bins = 10, color = colorHist)  # title=fig_title[i],
        else:
            fig[i] = Bar(df2, label = col_label[i], legend=False, color=colorBar)   # title=fig_title[i], 
            
    # make a grid
    grid = gridplot(fig, ncols=3, plot_width=250, plot_height=250)    
    #show(grid)
    
    resources = INLINE

    js_resources = resources.render_js()
    css_resources = resources.render_css()
    
    script, div = components(grid)
    
    return js_resources, css_resources, script, div



