# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:31:14 2017

@author: Amalia
"""

#import matplotlib.pyplot as plt
import simplejson as json
import urllib2
import requests

import numpy as np
import scipy as sc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import requests
#import quandl

#import io

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.resources import CDN, Resources, INLINE
from bokeh.embed import components, autoload_static

from bokeh.charts import Bar, Histogram, output_file, show, defaults
from bokeh.charts.attributes import cat, color
from bokeh.charts.operations import blend
from bokeh.charts.utils import df_from_json
#from bokeh.util.browser import view
#from jinja2 import Template

def descriptive(df, df_cols_transf):
    
    new_col_names = list(df_cols_transf.transf_col_name.values)
    
    music0 = df.iloc[:,0:19]
    movies0 = df.iloc[:,19:31]
    interests0 = df.iloc[:,31:46]
    hobbies0 = df.iloc[:,46:63]
    interests_hobbies0 = df.iloc[:,31:63]
    phobias0 = df.iloc[:,63:73]
    health0 = df.iloc[:,73:76]
    traits0 = df.iloc[:,76:133]
    spending0 = df.iloc[:,133:140]
    demographics0 = df.iloc[:,140:150]
    
    dic_smoking = {'never smoked': 1, 'tried smoking':2, 'former smoker': 3, 'current smoker': 4}
    dic_alcohol = {'never':1, 'social drinker': 2, 'drink a lot': 3}
    dic_punctuality = {'i am often early':3, 'i am always on time': 2, 'i am often running late': 1}
    dic_lying = {'never': 1, 'only to avoid hurting someone': 2, 'sometimes': 3, 'everytime it suits me': 4}
    dic_internet_usage = {'no time at all': 1, 'less than an hour a day':2, 'few hours a day': 3, 'most of the day': 4 }
    dic_gender = {'female': 0, 'male': 1}
    dic_left_right_handed = {'left handed':0, 'right handed':1}
    dic_education = {'currently a primary school pupil': 1, 'primary school':2, 'secondary school': 3, 'college/bachelor degree': 4, 'masters degree': 5, 'doctorate degree': 6}
    dic_only_child = {'no': 0, 'yes': 1}
    dic_village_town = {'village': 0, 'city': 1}
    dic_house_block_of_flats = {'block of flats': 0, 'house/bungalow':1}
    
    df1 = df.copy()
    df1.columns = new_col_names
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
    
    from bokeh.charts import defaults

    defaults.width = 350
    defaults.height = 350
    defaults.tools = False

    age = demographics0[['Age']].dropna()
    
    #p_gen = demographics0.gender.value_counts().plot(kind='bar')
    p_gen = Bar(demographics0, label = 'Gender', color=color(columns='Gender', palette=['Red', 'Green', 'Yellow'],
                      sort=False), title="Frequencies by Gender", legend = 'top_right')
    p_age = Histogram(age, values = 'Age', bins = 10, title="Frequencies by Age", color = 'Blue')
    p_edu = Bar(demographics0, label = 'Education', title="Frequencies by Education Level", legend=False, color='Orange')
    #save(p,'test3.html')
    
    df2 = pd.concat([demographics0, spending0], axis=1).reset_index(drop=True)
    df2 = df2.dropna()
    
#    p_4 = Bar(df2, label='Finances', values='Age', agg='mean', group='Gender',
#        title="Savers by Age, grouped by GENDER", legend = 'bottom_right')
#    p_5 = Bar(df2, label='Branded clothing', values='Age', agg='mean', group='Gender',
#        title="Spenders on Branded Clothing by Age, grouped by GENDER", legend = 'bottom_right')
#    p_6 = Bar(df2, label='Entertainment spending', values='Age', agg='mean', group='Gender',
#        title="Spenders on Entertainment by Age, grouped by GENDER", legend = 'bottom_right')
#    p_7 = Bar(df2, label='Spending on looks', values='Age', agg='mean', group='Gender',
#        title="Spenders on Looks by Age, grouped by GENDER", legend = 'bottom_right')
#    p_8 = Bar(df2, label='Spending on gadgets', values='Age', agg='mean', group='Gender',
#        title="Spenders on Gadgets by Age, grouped by GENDER", legend = 'bottom_right')
#    p_9 = Bar(df2, label='Spending on healthy eating', values='Age', agg='mean', group='Gender',
#        title="Spenders on Healthy Eating by Age, grouped by GENDER", legend = 'bottom_right')
    
    p_4 = Bar(df2, label='Finances', agg='mean', group='Gender',
        title="Savers, grouped by GENDER", legend = 'bottom_right')
    p_5 = Bar(df2, label='Branded clothing', agg='mean', group='Gender',
        title="Spenders on Branded Clothing, grouped by GENDER", legend = 'bottom_right')
    p_6 = Bar(df2, label='Entertainment spending', agg='mean', group='Gender',
        title="Spenders on Entertainment, grouped by GENDER", legend = 'bottom_right')
    p_7 = Bar(df2, label='Spending on looks', agg='mean', group='Gender',
        title="Spenders on Looks, grouped by GENDER", legend = 'bottom_right')
    p_8 = Bar(df2, label='Spending on gadgets', agg='mean', group='Gender',
        title="Spenders on Gadgets, grouped by GENDER", legend = 'bottom_right')
    p_9 = Bar(df2, label='Spending on healthy eating', agg='mean', group='Gender',
        title="Spenders on Healthy Eating, grouped by GENDER", legend = 'bottom_right')
 
    #hist2 = Histogram(df2, values='Age', label='Spending on looks', color='cyl', legend='top_right',
    #              title="MPG Histogram by Spending on Looks Count", plot_width=400)
    
    #output_file("histograms.html")

    #show(
    #        vplot(
    #                hplot(hist, hist2, hist3),
    #                hplot(hist4, hist5)
    #            )
    #        )

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
            
    return js_resources, css_resources, script1, div1, script2, div2, script3, div3, script4, div4, script5, div5, script6, div6, script7, div7, script8, div8, script9, div9


