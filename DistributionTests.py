import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#from scipy.stats import normaltest

## For other excel files - all of the column names will have to change to fit the new excel sheet
#   'sample.date', 'parameter', 'loc.ID', 'data.value'

#### Reading from the excel sheet
data = pd.read_excel(r'/Users/saffron/Documents/Howard_Neukrug_Water_Center_PWD_Shore_Grab_Bacteria_2019.xlsx')
#print(data)

## DRBC Data
#data = pd.read_excel(r'/Users/saffron/Downloads/Nearshore_Bacteria.xlsx',sheet_name = "Raw Data")

#### Create a pandas dataframe
df = pd.DataFrame(data)

#### Remove missing data from IMPORTANT columns
df = df.dropna(subset=['sample.date', 'parameter', 'loc.ID', 'data.value'])

## DRBC Data
#df = df.dropna(subset=['ActivityStartDate', 'CharacteristicName', 'Location', 'ResultMeasureValue'])

#& (df['loc.ID'] == ('SC_BANKS'))
Data = df.loc[(df['parameter'] == ('E.coli'))]
              #& (df['sample.date'].dt.month == (6))]
#Data = df.loc[(df['CharacteristicName'] == ('Fecal Coliform'))]


#print(Data)

DataList = []

for k in Data:
    DataList = Data['data.value'].tolist()
    #DataList = Data['ResultMeasureValue'].tolist()


LogData = []
for i in DataList:
    LogData = np.log(DataList).tolist()

#plt.hist(LogData, bins=25)
#plt.show()

DataList = LogData

#plt.hist(DataList, bins=100)
#plt.show()

list_of_dists = ['alpha', 'anglit', 'arcsine', 'beta', 'betaprime', 'bradford', 'burr', 'burr12', 'cauchy', 'chi',
                 'chi2', 'cosine', 'dgamma', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f',
                 'fatiguelife', 'fisk', 'foldcauchy', 'foldnorm', 'frechet_r', 'frechet_l', 'genlogistic', 'genpareto',
                 'gennorm', 'genexpon', 'genextreme', 'gausshyper', 'gamma', 'gengamma', 'genhalflogistic', 'gilbrat',
                 'gompertz', 'gumbel_r', 'gumbel_l', 'halfcauchy', 'halflogistic', 'halfnorm', 'halfgennorm',
                 'hypsecant', 'invgamma', 'invgauss', 'invweibull', 'johnsonsb', 'johnsonsu', 'kstwobign', 'laplace',
                 'levy', 'levy_l', 'logistic', 'loggamma', 'loglaplace', 'lognorm', 'lomax', 'maxwell', 'mielke',
                 'nakagami', 'ncx2', 'ncf', 'nct', 'norm', 'pareto', 'pearson3', 'powerlaw', 'powerlognorm',
                 'powernorm', 'rdist', 'reciprocal', 'rayleigh', 'rice', 'recipinvgauss', 'semicircular', 't', 'triang',
                 'truncexpon', 'truncnorm', 'tukeylambda', 'uniform', 'vonmises', 'vonmises_line', 'wald',
                 'weibull_min', 'weibull_max']

results = []

for i in list_of_dists:
    dist = getattr(stats, i)
    param = dist.fit(DataList)
    a = stats.kstest(DataList, i, args=param)
    results.append((i, a[0], a[1]))


results.sort(key=lambda x: float(x[2]), reverse=True)
for j in results:
    print("{}: statistic= {}, pvalue= {}".format(j[0], j[1], j[2]))

