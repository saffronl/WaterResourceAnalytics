# Import libraries
import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

# Creating dataset
file = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/RainData.xlsx')
df = pd.DataFrame(file)

########################
DATA = (df.loc[(df['DATE'].dt.year == 2019)])
DataList = DATA['PRCP'].tolist()

binlist = list(np.arange(0,max(DataList)+.1,.1))

fig = plt.figure(figsize=(15, 8))
n, bins, patches = plt.hist(DataList,bins=binlist,color='lightskyblue',rwidth=.8)

xticks = [(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])]
xticks_labels = [ "{:.2f}\nto\n{:.2f}".format(value, bins[idx+1]) for idx, value in enumerate(bins[:-1])]
plt.xticks(xticks, labels = xticks_labels, fontsize = 8)

# plot values on top of bars
for idx, value in enumerate(n):
    if value > 0:
        plt.text(xticks[idx], value+1, int(value), ha='center')

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount\n(lower number is included, top number is excluded)')
plt.ylabel('Frequency of Rainfall')
plt.title('Frequency of Rainfall Events 2019')
plt.savefig('Frequency of Rainfall Events 2019.png')

########################
DATA = (df.loc[(df['DATE'].dt.month == 6)
               & (df['DATE'].dt.year == 2019)])
DataList = DATA['PRCP'].tolist()

binlist = list(np.arange(0,max(DataList)+.1,.1))

fig = plt.figure(figsize=(15, 8))
n, bins, patches = plt.hist(DataList,bins=binlist,color='lightskyblue',rwidth=.8)

xticks = [(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])]
xticks_labels = [ "{:.2f}\nto\n{:.2f}".format(value, bins[idx+1]) for idx, value in enumerate(bins[:-1])]
plt.xticks(xticks, labels = xticks_labels, fontsize = 9)

# plot values on top of bars
for idx, value in enumerate(n):
    if value > 0:
        plt.text(xticks[idx], value+.1, int(value), ha='center')

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount\n(lower number is included, top number is excluded)')
plt.ylabel('Frequency of Rainfall')
plt.title('Frequency of Rainfall in June')
plt.savefig('Frequency of Rainfall in June.png')

########################
DATA = (df.loc[(df['DATE'].dt.month == 7)
        & (df['DATE'].dt.year == 2019)])
DataList = DATA['PRCP'].tolist()

binlist = list(np.arange(0,max(DataList)+.1,.1))

fig = plt.figure(figsize=(12, 8))
n, bins, patches = plt.hist(DataList,bins=binlist,color='lightskyblue',rwidth=.8)

xticks = [(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])]
xticks_labels = [ "{:.2f}\nto\n{:.2f}".format(value, bins[idx+1]) for idx, value in enumerate(bins[:-1])]
plt.xticks(xticks, labels = xticks_labels, fontsize = 9)

# plot values on top of bars
for idx, value in enumerate(n):
    if value > 0:
        plt.text(xticks[idx], value+.1, int(value), ha='center')

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount\n(lower number is included, top number is excluded)')
plt.ylabel('Frequency of Rainfall')
plt.title('Frequency of Rainfall for July')
plt.savefig('Frequency of Rainfall for July.png')

########################
DATA = (df.loc[(df['DATE'].dt.month == 8)
        & (df['DATE'].dt.year == 2019)])
DataList = DATA['PRCP'].tolist()

binlist = list(np.arange(0,max(DataList)+.1,.1))

fig = plt.figure(figsize=(10, 8))
n, bins, patches = plt.hist(DataList,bins=binlist,color='lightskyblue',rwidth=.8)

xticks = [(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])]
xticks_labels = [ "{:.2f}\nto\n{:.2f}".format(value, bins[idx+1]) for idx, value in enumerate(bins[:-1])]
plt.xticks(xticks, labels = xticks_labels, fontsize = 9)

# plot values on top of bars
for idx, value in enumerate(n):
    if value > 0:
        plt.text(xticks[idx], value+.1, int(value), ha='center')

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount\n(lower number is included, top number is excluded)')
plt.ylabel('Frequency of Rainfall')
plt.title('Frequency of Rainfall for August')
plt.savefig('Frequency of Rainfall for August.png')

########################
DATA = (df.loc[(df['DATE'].dt.month == 9)
        & (df['DATE'].dt.year == 2019)])
DataList = DATA['PRCP'].tolist()

binlist = list(np.arange(0,max(DataList)+.1,.1))

fig = plt.figure(figsize=(10, 8))
n, bins, patches = plt.hist(DataList,bins=binlist,color='lightskyblue',rwidth=.5)

xticks = [(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])]
xticks_labels = [ "{:.2f}\nto\n{:.2f}".format(value, bins[idx+1]) for idx, value in enumerate(bins[:-1])]
plt.xticks(xticks, labels = xticks_labels, fontsize = 9)

# plot values on top of bars
for idx, value in enumerate(n):
    if value > 0:
        plt.text(xticks[idx], value+.1, int(value), ha='center')

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rainfall Amount\n(lower number is included, top number is excluded)')
plt.ylabel('Frequency of Rainfall')
plt.title('Frequency of Rainfall for September')
plt.savefig('Frequency of Rainfall for September.png')

########################

plt.show()