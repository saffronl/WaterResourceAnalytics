# Saffron Livaccari
# Email saffron.livaccari@gmail.com for inquiries.

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator)


# https://stackoverflow.com/questions/5938459/combining-plt-plotx-y-with-plt-boxplot

# Data with river mile info
file = r'/Users/saffron/PycharmProjects/PythonProject1/RawCentralChanneldataWithRainFall.xlsx'
data = pd.read_excel(file)
df = pd.DataFrame(data)
df = df.dropna(subset=['Data','Bacteria','Location','RiverMile'])

# Data with target percentiles
file2 = r'/Users/saffron/PycharmProjects/PythonProject1/WetandDryData_NoYears.xlsx'
data2 = pd.read_excel(file2)
df2 = pd.DataFrame(data2)

riverlocation = {100.2: 'Benjamin Franklin Br', 104.75: 'Betsy Ross Br',
                 117.8: 'Burlington Bristol Br', 71: 'Cherry Island',
                 84: 'Eddystone', 122.4: 'Florence Bend', 78.1: 'Marcus Hook',
                 93.2: 'Navy Yard', 74.9: 'Oldmans Point',
                 87.5: 'Paulsboro', 110.7: 'Torresdale'}

target = {"Fecal Coliform": 200, "Fecal coliform": 200,
          "Enterococci": 35, "Enterococcus":35,
          "E.coli": 126, "E.Coli": 126,"Escherichia coli":126}

RiverList = df['RiverMile'].unique().tolist()
BacteriaList = df['Bacteria'].unique().tolist()

print('RiverMile List:\n',RiverList)
print('BacteriaList:\n',BacteriaList)


riverbacteria_dict = {}
riverpercent_dict = {}

# ['Fecal Coliform', 'Escherichia coli', 'Enterococcus']
bacteria = 'Escherichia coli'

for L in range(len(RiverList)):
    DATA = (df.loc[(df['Bacteria'] == (bacteria))
                   & (df['RiverMile'] == (RiverList[L]))])
    DataList = DATA['Data'].tolist()
    bacteriaconclist = {RiverList[L]:DataList}
    riverbacteria_dict.update(bacteriaconclist)
    print('River List ',RiverList[L])
    print('River location ',riverlocation[RiverList[L]])

    DATA2 = df2.loc[(df2['Data Type'] == ('Central Channel'))
                &(df2['Bacteria'] == (bacteria))
                &(df2['Location'] == (riverlocation[RiverList[L]]))]
    DataList2 = float(DATA2['Percent that meet the Target'])
    targetperclist = {RiverList[L]:DataList2}
    riverpercent_dict.update(targetperclist)

print('KEYS ',sorted(riverbacteria_dict.keys()))
print(riverbacteria_dict)
print(riverpercent_dict)




fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
ax2 = ax.twinx()


line_props = dict(color="b",linewidth=1)
medianprops = dict(color="black",linewidth=1.5)
ax.boxplot(riverbacteria_dict.values(),positions=[*riverbacteria_dict.keys()],showfliers=False,
           boxprops=line_props,whiskerprops=line_props,medianprops=medianprops,widths=.6)

ax.set_xticks(range(70, 126, 5))
ax.set_xticklabels(range(70, 126, 5))

ax.set_ylim(bottom=0)
# For entrococcus:  ax.set_yticks(range(0,101,20))
# For fecal: ax.set_yticks(range(0,1001,200))
# For ecoli: ax.set_yticks(range(0,601,120))
ax.set_yticks(range(0,601,120))
ax.xaxis.grid(True, which='major')
ax.yaxis.grid(True, which='major')
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', colors='blue')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.set_title(bacteria+" in the Delaware River",weight='bold')
ax.set_xlabel('River Mile')
ax.set_ylabel(bacteria+' concentration (CFU/100mL)',weight='bold')

ax2.plot(*zip(*sorted(riverpercent_dict.items())),color='red',marker = 'o')

ax2.annotate(str(riverpercent_dict[71.0]),xy=(71.0,riverpercent_dict[71.0]-5), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[74.9]),xy=(74.9-1,riverpercent_dict[74.9]-6), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[78.1]),xy=(78.1-1,riverpercent_dict[78.1]-6), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[84.0]),xy=(84.0-2,riverpercent_dict[84.0]-6), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[87.5]),xy=(87.5-2,riverpercent_dict[87.5]-5), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[93.2]),xy=(93.2-2,riverpercent_dict[93.2]-5), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[100.2]),xy=(100.2-2,riverpercent_dict[100.2]-5), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[104.75]),xy=(104.75,riverpercent_dict[104.75]-5), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[110.7]),xy=(110.7-1,riverpercent_dict[110.7]-6), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[117.8]),xy=(117.8-1,riverpercent_dict[117.8]-6), fontsize='9',rotation=45)
ax2.annotate(str(riverpercent_dict[122.4]),xy=(122.4-2,riverpercent_dict[122.4]-5), fontsize='9',rotation=45)

ax2.set_yticks(range(0,101,20))
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax2.set_ylabel('Percent of Samples that meet the Target: '+ str(target[bacteria]),weight='bold')
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', colors='red')

#plt.savefig('ecoli_centralchannel.png')
plt.show()
