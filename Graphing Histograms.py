# Import libraries
import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

# Creating dataset
file = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/RawPWD2019datawithRainFall.xlsx')
df = pd.DataFrame(file)

"""
########################
DATA = (df.loc[(df['Bacteria'] == ('Enterococci'))])
DataList = DATA['Rain per Each Day'].tolist()

fig = plt.figure(figsize=(10, 7))
n, bins, patches = plt.hist(DataList,bins='rice')

xticks = [(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])]
xticks_labels = [ "{:.2f}\nto\n{:.2f}".format(value, bins[idx+1]) for idx, value in enumerate(bins[:-1])]
plt.xticks(xticks, labels = xticks_labels)

# plot values on top of bars
for idx, value in enumerate(n):
    if value > 0:
        plt.text(xticks[idx], value+1, int(value), ha='center')

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount')
plt.ylabel('Frequency of Data Collected')
plt.title('Frequency of One Day Rainfall for all locations when Gathering Data')
plt.savefig('Frequency of One Day Rainfall for all locations when Gathering Data.png')

########################

# Bartrams Garden
# Frankford Boat Launch
# Independence Seaport Museum
# John Heinz National Wildlife Refuge

########################
DATA = (df.loc[(df['Bacteria'] == ('Enterococci'))
            & (df['loc.descrip'] == ('Bartrams Garden'))])
DataList = DATA['Rain per Each Day'].tolist()

plt.figure(figsize=(10, 7))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount')
plt.ylabel('Frequency of Data Collected')
plt.title('Bartrams Garden Frequency of One Day Rainfall when Gathering Data')
# Creating plot
bp1 = plt.hist(DataList, bins=len(DataList1), width = .2, color='#0504aa',rwidth=1)
plt.savefig('Bartrams Garden Frequency of One Day Rainfall when Gathering Data.png')

########################
DATA = (df.loc[(df['Bacteria'] == ('Enterococci'))
            & (df['loc.descrip'] == ('Frankford Boat Launch'))])
DataList = DATA['Rain per Each Day'].tolist()

plt.figure(figsize=(10, 7))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount')
plt.ylabel('Frequency of Data Collected')
plt.title('Frankford Boat Launch Frequency of One Day Rainfall when Gathering Data')
bp2 = plt.hist(DataList, bins=len(DataList), width = .2, color='#0504aa',rwidth=1)
plt.savefig('Frankford Boat Launch Frequency of One Day Rainfall when Gathering Data.png')
"""
########################
DATA = (df.loc[(df['Bacteria'] == ('Enterococci'))
            & (df['loc.descrip'] == ('Independence Seaport Museum'))])
DataList = DATA['Rain per Each Day'].tolist()
i = 0
binlist = []
while i < max(DataList):
    binlist.append(round(i,2))
    i += .05

print("bin list", binlist)
fig = plt.figure(figsize=(20, 7))
n, bins, patches = plt.hist(DataList, bins=binlist, align='left', color='lightpink',rwidth=.5)
plt.xticks(binlist,fontsize = 8)

xticks = [(bins[idx] + value)/2 for idx, value in enumerate(bins[:-1])]
# plot values on top of bars
for idx, value in enumerate(n):
    if value > 0:
        plt.text(xticks[idx], value+.1, int(value), ha='center')

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount')
plt.ylabel('Frequency of Data Collected')
plt.title('Independence Seaport Museum of One Day Rainfall when Gathering Data')
#plt.savefig('Independence Seaport Museum of One Day Rainfall when Gathering Data.png')

"""
########################
DATA = (df.loc[(df['Bacteria'] == ('Enterococci'))
            & (df['loc.descrip'] == ('John Heinz National Wildlife Refuge'))])
DataList = DATA['Rain per Each Day'].tolist()

plt.figure(figsize=(10, 7))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount')
plt.ylabel('Frequency of Data Collected')
plt.title('John Heinz National Wildlife Refuge Frequency of One Day Rainfall when Gathering Data')
bp4 = plt.hist(DataList, bins=len(DataList), width = .2, color='#0504aa',rwidth=1)
plt.savefig('John Heinz National Wildlife Refuge Frequency of One Day Rainfall when Gathering Data.png')


########################


DATA = (df.loc[(df['Bacteria'] == ('Enterococci'))])
DataList = DATA['Count of days after .1 Rainfall Event'].tolist()
binlist = list(range(max(DataList)+2))
fig = plt.figure(figsize=(10, 7))
n, bins, patches = plt.hist(DataList, bins=binlist, align='left', width =.5, color='lightpink',rwidth=.5)
plt.xticks(binlist)

xticks = [(bins[idx] + value)/2 for idx, value in enumerate(bins[:-1])]
# plot values on top of bars
for idx, value in enumerate(n):
    if value > 0:
        plt.text(xticks[idx], value+1, int(value), ha='center')

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Number of days since a rainfall event of >0.1')
plt.ylabel('Frequency of Data Collected')
plt.title('Number of days after a rainfall event (greater than .1 inches)\nthe data was gathered for Enterococci')
plt.savefig('Number of days after a Rainfall Event greater than .1 inches.png')
"""
plt.show()
