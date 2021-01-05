# Saffron Livaccari

#pip install pandas
#pip install xlrd
#pip install openpyxl
import pandas as pd
import numpy as np
import sys
import math
import scipy.stats as scs

def ExcelSheet(file,ColumnNameforDate,ColumnNameforBacteria,ColumnNameforLocation,ColumnforData):
    data = pd.read_excel(file)
    df = pd.DataFrame(data)
    df.rename(columns={ColumnNameforDate:'Date',ColumnNameforBacteria:'Bacteria',
                         ColumnNameforLocation:'Location',ColumnforData:'Data'},inplace=True)
    df = df.dropna(subset=['Date','Bacteria','Location','Data'])
    df.to_excel('data.xlsx')
    print('DataFrame is written to Excel File successfully.')
    return df

### CHANGE THIS TO FIT EXCEL SHEET
#DRBC
#excel = '/Users/saffron/Downloads/Nearshore_Bacteria.xlsx'
#PWD
excel = '/Users/saffron/Documents/Howard_Neukrug_Water_Center_PWD_Shore_Grab_Bacteria_2019.xlsx'
### CHANGE THIS TO FIT THE COLUMNS NAMES OF ABOVE EXCEL SHEET
#DRBC
#ExcelSheet(excel,'ActivityStartDate','CharacteristicName','Location','ResultMeasureValue')
#PWD
ExcelSheet(excel,'sample.date', 'parameter', 'loc.ID', 'data.value')

#Excel Sheet made from function
data = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/data.xlsx')
df = pd.DataFrame(data)

Data = df.loc[(df['Bacteria'] == ('E.coli'))]
#Data = df.loc[(df['CharacteristicName'] == ('Fecal Coliform'))]

DataList = []

for k in Data:
    DataList = Data['Data'].tolist()



def johnsonsu_mean(a, b, loc, scale):
    """
    Johnson SU mean according to https://en.wikipedia.org/wiki/Johnson%27s_SU-distribution
    """
    v = loc - scale * math.exp(0.5 / b**2) * math.sinh(a/b)
    return v

def johnsonsu_var(a, b, loc, scale):
    """
    Johnson SU variance according to https://en.wikipedia.org/wiki/Johnson%27s_SU-distribution
    """
    t = math.exp(1.0 / b**2)
    v = 0.5*scale**2 * (t - 1.0) * (t * math.cosh(2.0*a/b) + 1.0)
    return v

def johnsonsu_median(a, b, loc, scale):
    """
    Johnson SU median according to https://en.wikipedia.org/wiki/Johnson%27s_SU-distribution
    """
    v = loc + scale * math.sinh(-a/b)
    return v

def main(r):
    sample_mean, sample_med, sample_var, sample_std, sample_skew, sample_kurt = r.mean(), r.median(), r.var(0), r.std(0), r.skew(), r.kurt()

    a, b, loc, scale = scs.johnsonsu.fit(r) # fit the data and get distribution parameters back

    # distribution mean and variance according to SciPy
    dist_mean = scs.johnsonsu.mean(a, b, loc, scale)
    dist_med  = scs.johnsonsu.median(a, b, loc, scale)
    dist_var  = scs.johnsonsu.var(a, b, loc, scale)

    # distribution mean, var vs sample ones
    print("{0} {1}".format(sample_mean, dist_mean))
    print("{0} {1}".format(sample_med, dist_med))
    print("{0} {1}".format(sample_var, dist_var))
    print("")

    # distribution mean and variance according to Wiki vs SciPy
    print("{0} {1}".format(dist_mean, johnsonsu_mean(a, b, loc, scale)))
    print("{0} {1}".format(dist_var, johnsonsu_var(a, b, loc, scale)))
    print("{0} {1}".format(dist_med, johnsonsu_median(a, b, loc, scale)))


for i in DataList:
    main(int(i))
