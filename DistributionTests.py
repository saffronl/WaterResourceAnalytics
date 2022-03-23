import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#### Reading from the excel sheet
data = pd.read_excel(r'/Users/saffron/Documents/Water Research/DRBC 2019,2020,2021/DRBC 19,20,21.xlsx')
#print(data)

#### Create a pandas dataframe
df = pd.DataFrame(data)

# only get e.coli data
Data = df.loc[(df['Bacteria'] == ('E.Coli'))]
#print(Data)

# turn the bacteria data into a list
DataList = Data['Data'].tolist()

# take the log of every bacteria concentration
LogData = np.log10(DataList).tolist()

# option to plot the data on a histogram:
#plt.hist(LogData, bins=25)
#plt.show()

# list of distributions in scipy
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

# fit every distribution to the dataset
for i in list_of_dists:
    dist = getattr(stats, i)
    param = dist.fit(LogData)
    a = stats.kstest(LogData, i, args=param)
    results.append((i, a[0], a[1]))

# sort the results, best fitting is on the top
results.sort(key=lambda x: float(x[2]), reverse=True)
for j in results:
    print("{}: statistic= {}, pvalue= {}".format(j[0], j[1], j[2]))

