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
data=latest.groupby('Country/Region').sum().sort_values(by=['Confirmed'],
                   ascending=False).iloc[0:20]
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=90)
data_copy=data.stack().reset_index()
data_copy.columns = ['Country', 'Status', 'No of Confirmed Cases']
confirmed = data_copy[data_copy['Status'].str.contains("Confirmed")]
sns.barplot(y='No of Confirmed Cases', x='Country',data=confirmed)
ax1.title.set_text('Coronavirus Confirmed Patients by Country - TOP 20')
plt.grid(True)


data=latest.groupby('Country/Region').sum().sort_values(by=['Deaths'],
                   ascending=False).iloc[0:20]
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=90)
data_copy=data.stack().reset_index()
data_copy.columns = ['Country', 'Status', 'No of Dead']
confirmed = data_copy[data_copy['Status'].str.contains("Deaths")]
sns.barplot(y='No of Dead', x='Country',data=confirmed)
ax1.title.set_text('Coronavirus Dead Patients by Country - TOP 20')
plt.grid(True)



data=latest.groupby('Country/Region').sum().sort_values(by=['Recovered'],
                   ascending=False).iloc[0:20]
fig, ax1 = plt.subplots(figsize=(10,6))
plt.xticks(rotation=90)
data_copy=data.stack().reset_index()
data_copy.columns = ['Country', 'Status', 'No of Recovered']
confirmed = data_copy[data_copy['Status'].str.contains("Recovered")]
sns.barplot(y='No of Recovered', x='Country',data=confirmed)
ax1.title.set_text('Coronavirus Recovered Patients by Country - TOP 20')
ax1.set_ylim([0,10000])
plt.grid(True)
