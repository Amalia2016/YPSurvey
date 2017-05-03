# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:31:14 2017

@author: Amalia
"""

#import matplotlib.pyplot as plt
import simplejson as json
import urllib2
import requests

#import numpy as np
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
from bokeh.charts import defaults

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
    script10, div10 = components(p_10)
    script11, div11 = components(p_11)
    script12, div12 = components(p_12)
            
    return js_resources, css_resources, script1, div1, script2, div2, script3, div3, script4, div4, script5, div5, script6, div6, script7, div7, script8, div8, script9, div9, script10, div10, script11, div11, script12, div12


