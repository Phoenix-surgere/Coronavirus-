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


print(cases.info())
cases.set_index('SNo', inplace=True, drop=True)

by_time = cases[['Deaths', 'Recovered', 'Confirmed', 'ObservationDate']].groupby(
        by=['ObservationDate']).sum()
by_time.index = pd.to_datetime(by_time.index)
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=90)
plt.grid(True)
sns.lineplot(ax=ax1, data=by_time.resample('W').sum())
ax1.title.set_text('Coronavirus Effects over Time')
ax1.set_ylabel('No of Individuals')

#Correct way to get latest statistics!
latest = cases[cases.ObservationDate == cases.ObservationDate.max()]

#EVERYTHING BELOW IS WRONG DUE TO MY MISCONCEPTION - NUMBERS REPORTED ARE TOTALS, NOT CHANGES - WILL FIX BY FRIDAY
by_country = cases[['Confirmed', 'Deaths', 'Recovered','Country/Region']].groupby(
        by=['Country/Region']).sum().sort_values(by='Confirmed', ascending=False)


fig, ax1 = plt.subplots()
plt.xticks(rotation=90)
sns.barplot(x='Country/Region', y='Confirmed', data=by_country.reset_index().iloc[0:20])
ax1.title.set_text('Coronavirus Confirmed Patients by Country - TOP 20')
plt.grid(True)
ax1.set_ylim(0, 70000)


by_both = cases[['Confirmed', 'Deaths', 'Recovered',
                    'Country/Region', 'ObservationDate']].groupby(
        by=['Country/Region', 'ObservationDate']).sum().sort_values(by='Confirmed', ascending=False)

data=by_country.reset_index().iloc[0:10]
top_countries_by_confirmed = list(data['Country/Region'].iloc[0:10])

by_both.loc[top_countries_by_confirmed].reset_index().pivot(
  'ObservationDate','Country/Region', 'Confirmed').plot(title='Var1', grid=True)



