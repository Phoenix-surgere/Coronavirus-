# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 01:37:00 2020

@author: black
"""

import pandas as pd
import zipfile
import numpy as np 
import seaborn as sns
seed = 2018
np.random.seed(seed)

zf = zipfile.ZipFile('novel-corona-virus-2019-dataset.zip') 
cases = pd.read_csv(zf.open('covid_19_data.csv'))

