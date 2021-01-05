# Import libraries
import pandas as pd
import numpy as np
import statistics as st
import scipy.stats as stats
import matplotlib.pyplot as plt
from pandas.core.common import flatten

# Creating dataset
file = pd.read_excel(r'/Users/saffron/Documents/RawPWD2019datawithRainFall.xlsx')
dfPWD = pd.DataFrame(file)
# Washington Avenue Green , Independence Seaport Museum , Frankford Boat Launch
# E.coli , Enterococci
# Ind Seaport Museum / Penns Landing
file1 = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/RawDRBC2019dataWithRainFall.xlsx')
dfDRBC = pd.DataFrame(file1)
# Wash Ave Green , Penns Landing , Frankford Arsenal
# Escherichia coli , Enterococcus



DATA = (dfPWD.loc[(dfPWD['Bacteria'] == 'Fecal coliform')
               & (dfPWD['loc.descrip'] == 'Independence Seaport Museum')])
PWDDataList = DATA['Data'].tolist()
PWDmonths = DATA['Date'].dt.month.unique().tolist()
print(PWDmonths)

DRBCDataList = []
for i in PWDmonths:
    DATA1 = (dfDRBC.loc[(dfDRBC['Bacteria'] == 'Fecal Coliform')
                        & (dfDRBC['Location'] == 'Penns Landing')
                        & (dfDRBC['Date'].dt.month == i)])
    DataList = DATA1['Data'].tolist()
    DRBCDataList.append(DataList)
DRBCDataList = list(flatten(DRBCDataList))


fig = plt.figure(figsize=(10, 7))
# Create an axes instance
ax = fig.add_subplot(111)

x, y = stats.ttest_ind(PWDDataList, DRBCDataList)
print("T Test Results: t-value = "+str(round(x,5))+" p-value = "+str(round(y,5)))
data_to_plot = [PWDDataList, DRBCDataList]
ax.set_title('Ind Seaport Museum / Penns Landing - Fecal Coliform Data PWD vs DRBC\n'
             +"T Test Results: t-value = "+str(round(x,5))+" p-value = "+str(round(y,5)))
ax.set_xticklabels(['PWD Data\n'+'Frequency of data: ' + str(len(PWDDataList)),
                    'DRBC Data\n'+'Frequency of data: ' + str(len(DRBCDataList))])
ax.set_xlabel('\nRainfall Amount')
ax.set_ylabel('Fecal Coliform Amount')
bp = ax.boxplot(data_to_plot)


# Save the figure
fig.savefig('Ind Seaport Museum or Penns Landing - Fecal Coliform Data PWD vs DRBC BoxPlot.png')

plt.show()



