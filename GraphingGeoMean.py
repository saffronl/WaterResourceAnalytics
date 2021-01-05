#pip install pandas
#pip install xlrd
#pip install openpyxl
import pandas as pd
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

## For other excel files - all of the column names will have to change to fit the new excel sheet
#   'sample.date', 'parameter', 'loc.ID', 'data.value'

#### Reading from the excel sheet
data = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/PWDdata.xlsx')

#### Create a pandas dataframe
df = pd.DataFrame(data)

list = []
list1 = []

monthlist = ['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']

i = 6
while i < 10:
    x = df.loc[(df['Month'] == (i))
           & (df['Bacteria'] == ("Fecal coliform"))
           & (df['LocationID'] == ("DR_FRNKFD"))]
    y = x['Geometric Mean'].values[0]
    namemonth = monthlist[i-1]
    list1.append(namemonth)
    list.append(y)
    i += 1

print(list)
print(list1)

# naming the x-axis
plt.xlabel('x-axis')
# naming the y-axis
plt.ylabel('Geometric Mean')
# plot title
plt.title('Bar Chart for Fecal Coliform')

plt.bar(list1, list)

plt.show()


"""
x is location
why is the geometric mean for the months
"""



"""
# labels for bars
monthlist = ['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
locationlabel = ['Schuylkill River at Schuylkill Banks']

def creating_bar_graph(month,bacteria,locationID):
    DATA = (df.loc[(df['Month'] == (month))
                   & (df['LocationID'] == (locationID))
                   & (df['Bacteria'] == (bacteria))])
    geomean = DATA['Geometric Mean']
    return float(geomean)

fig = plt.figure()

monthforgraph = []
geomeanforgraph = []
width = 0.35
i = 0
while i < 13:
    creating_bar_graph(i,'Fecal coliform', 'DR_FRNKFD')
    geomeanforgraph.append(geomean)
    monthlabel = monthlist[i]
    monthforgraph.append(monthlabel)
    i += 1

ax.bar(monthforgraph,geomeanforgraph)
ax.set_ylabel('Geo Mean')
ax.set_title('Geomean for months')
ax.set_xlabel('DR_FRNKFD')
ax.legend()

#plt.bar(x = months , height= geomean, bottom = months)
fig.tight_layout()

plt.show()

plt.show()
"""

# plotting a bar chart
"""
DATA = (df.loc[(df['Month'] == (6))
               & (df['LocationID'] == ('DR_FRNKFD'))
               & (df['Bacteria'] == ('Fecal coliform'))])
geomean = DATA['Geometric Mean']

y = geomean
"""
listmonth =[]
listgeomean = []

i = 6
while i < 10:
    DATA = (df.loc[(df['Month'] == (i))
                   & (df['LocationID'] == ('DR_FRNKFD'))
                   & (df['Bacteria'] == ('Fecal coliform'))])
    geomean = DATA['Geometric Mean']
    listgeomean.append(geomean)
    listmonth.append(i)
    i+=1
print(listmonth)
print(listgeomean)
#plt.bar(, listgeomean)
#width=0.8, color=['red', 'green']

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
#plt.show()


"""
x = np.arange(10)
ax1 = plt.subplot(1,1,1)
w = 0.3
#plt.xticks(), will label the bars on x axis with the respective country names.
plt.xticks(, rotation='vertical')
month =ax1.bar(, width=w, color='b', align='center')

#We have calculated GDP by dividing gdpPerCapita to population.
gdp =ax2.bar(x + w, datasort['gdpPerCapita'] * datasort.population / 10**9, width=w,color='g',align='center')
#Set the Y axis label as GDP.
plt.ylabel('GDP')

#To set the legend on the plot we have used plt.legend()
plt.legend([pop, gdp],['Population in Millions', 'GDP in Billions'])
#To show the plot finally we have used plt.show().
plt.show()
"""