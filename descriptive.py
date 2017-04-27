# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:31:14 2017

@author: Felix
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
#from bokeh.util.browser import view
#from jinja2 import Template

def descriptive():

    df = pd.read_csv("responses.csv")
    demographics0 = df.iloc[:,140:150]

    p_gen = demographics0.gender.value_counts().plot(kind='bar')

    #age_hist = demographics['age'].hist()
    #age_fig = age_hist.get_figure()
    #p_edu = demographics0.Education.value_counts().plot(kind='bar')

    resources = INLINE

    js_resources = resources.render_js()
    css_resources = resources.render_css()
    
    script, div = components(p_gen)
    
    return js_resources, css_resources, script, div


