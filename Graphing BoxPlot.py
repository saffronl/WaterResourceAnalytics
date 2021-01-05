# Import libraries
import pandas as pd
import numpy as np
import statistics as st
import scipy.stats as stats
import matplotlib.pyplot as plt

# Creating dataset
file = pd.read_excel(r'/Users/saffron/Documents/RawPWD2019datawithRainFall.xlsx')
df = pd.DataFrame(file)

# Make a list of only the unique locations and bacteria types
LocationList = df['loc.descrip'].unique().tolist()
BacteriaList = ['Enterococci','E.coli']
#RainfallList = ['Rain per Each Day','Sum of Rain for Two Days','Sum of Rain for Three Days','Sum of Rain for Six Days']

# middle loop is running through all the unique locations
for L in range(len(LocationList)):
    # inner loop is running through all of the unique bacteria
    for B in range(len(BacteriaList)):
        # running the above function
        i = 0
        list = []
        rain = [0, .101]
        rain1 = [.1, 10]
        print(list)
        print(BacteriaList[B])
        print(LocationList[L])
        while i < (len(rain)):
            DATA = (df.loc[(df['Bacteria'] == BacteriaList[B])
                           & (df['loc.descrip'] == LocationList[L])
                           & (df['Rain per Each Day'] >= rain[i])
                           & (df['Rain per Each Day'] <= rain1[i])])
            DataList = DATA['Data'].tolist()
            list.append(DataList)
            i += 1
        fig = plt.figure(figsize=(10, 7))
        # Create an axes instance
        ax = fig.add_subplot(111)
        print('List = ',list)
        #x = stats.ttest_ind(list[0], list[1])
        x, y = stats.ttest_ind(list[0], list[1])
        print("T Test Results: t-value = "+str(round(x,5))+" p-value = "+str(round(y,5)))
        data_to_plot = [list[0], list[1]]
        ax.set_title(LocationList[L]+' '+BacteriaList[B]+' Rainfall Total for One Day\n'
                     +"T Test Results: t-value = "+str(round(x,5))+" p-value = "+str(round(y,5)))
        ax.set_xticklabels([str(rain[0])+'-'+str(rain1[0])+'\n'+'Frequency of data: ' + str(len(list[0])),
                            str(rain[1])+'-'+str(rain1[1])+'\n'+'Frequency of data: ' + str(len(list[1]))])
        ax.set_xlabel('\nRainfall Amount')
        ax.set_ylabel(BacteriaList[B]+' Amount')
        bp = ax.boxplot(data_to_plot)
        #fig.savefig(LocationList[L]+' '+BacteriaList[B]+' Rainfall Total for One Day BoxPlot.png')
        plt.show()
