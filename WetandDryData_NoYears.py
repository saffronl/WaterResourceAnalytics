# Saffron Livaccari
# Email saffron.livaccari@gmail.com for inquiries.

import pandas as pd
import numpy as np
from scipy.stats import gmean
import statistics as st

# Dictionary of Target Values
targetGM = {"Fecal Coliform": 200, "Fecal coliform": 200, "Fecal\nColiform":200,
          "Enterococci": 35, "Enterococcus":35,
          "E.coli": 126, "E.Coli": 126, "Ecoli": 126, "Escherichia coli":126, "Escherichia\nColi":126,
          "Total Coliform": 200}
targetSTV = {"Fecal Coliform": 770, "Fecal coliform": 770, "Fecal\nColiform":770,
          "Enterococci": 130, "Enterococcus":130,
          "E.coli": 410, "E.Coli": 410, "Ecoli": 410, "Escherichia coli":410, "Escherichia\nColi":410,
          "Total Coliform": 770}

def target_number(iterable, targetvalue):
    if len(iterable) < 1:
        return "NA"
    else:
        count = 0
        for i in iterable:
            if i > targetvalue:
                count = count + 1
        return count

def target_percentile(iterable, targetvalue):
    if len(iterable) < 1:
        return "NA"
    else:
        count = 0
        for i in iterable:
            if i >= targetvalue:
                count += 1
        totallist = len(iterable)
        return round((count / totallist) * 100, 1)

# Statistical Threshold Value
def stv(iterable):
    # log based 10 : STV = 10 ** ( avg(log values) + 1.282 * std(log values) )
    print("STV LIST: ",iterable)
    iterable = [i for i in iterable if i != 0]
    print("NEW STV LIST: ", iterable)
    if len(iterable) < 3:
        print("THIS IS HITTING THE <3 MARK")
        return "NA"
    else:
        b = np.log10(iterable)
        eq = 10 ** (st.mean(b) + (1.282 * st.stdev(b)))
        return round(eq,1)

def geomean(iterable):
    if len(iterable) < 5:
        return "NA"
    else:
        return round(float(gmean(iterable)),1)

def maxvalue(iterable):
    if len(iterable) < 2:
        return 'NA'
    else:
        return round(float(max(iterable)),2)

def minvalue(iterable):
    if len(iterable) < 2:
        return 'NA'
    else:
        return round(float(min(iterable)),2)

def gm_percentile(iterable, targetvalue):
    if len(iterable) < 1:
        return "NA"
    else:
        count = 0
        for i in iterable:
            if i <= targetvalue:
                count = count + 1
        totallist = len(iterable)
        return round((count / totallist) * 100, 1)


# Create a list of lists for the bacteria, location, month, etc
LIST = []


# Uses the month, bacteria, and location, get the geometric mean, STV, average, and percentiles
# and exports this information into a new pandas dataframe
def makingdatasheet(bacteria, locationID):
    # ALL DATA FIRST
    # Matching the correct columns with the parameters from the function
    DATA = (df.loc[(df['Bacteria'] == (bacteria))
                   & (df['Location'] == (locationID))])

    # Make a list of all of the data (MPN/100mL) with the same criteria (bacteria and location)
    DataList = DATA['Data'].tolist()


    print("\nBacteria: " + str(bacteria))
    print("Location ID: " + str(locationID))
    print("Data List for all values ",DataList)

    if not DataList:
        print("No data\n")

    else:
        # Print to check the loop
        print("Length of total data ",len(DataList))

        # Percentiles
        p0 = round(np.percentile(DataList, 0),1)
        p5 = round(np.percentile(DataList, 5),1)
        p25 = round(np.percentile(DataList, 25),1)
        p50 = round(np.percentile(DataList, 50),1)
        p75 = round(np.percentile(DataList, 75),1)
        p90 = round(np.percentile(DataList, 90),1)
        p100 = round(np.percentile(DataList, 100),1)

        # Target Value Caculations
        #print("DATA LIST NOW ",DataList)
        targetnumberGM = target_number(DataList, targetGM[str(bacteria)])
        targetpercentGM = target_percentile(DataList, targetGM[str(bacteria)])
        targetnumberSTV = target_number(DataList, targetSTV[str(bacteria)])
        targetpercentSTV = target_percentile(DataList, targetSTV[str(bacteria)])
        GM = geomean(DataList)
        STV = stv(DataList)
        print('scipy GM ',GM)
        print("Target GM",targetGM[str(bacteria)])
        print("Target STV", targetSTV[str(bacteria)])
        print("Target Number GM ",targetnumberGM)
        print("Target Percent GM ",targetpercentGM)
        print("Target Number STV ",targetnumberSTV)
        print("Target Percent STV ",targetpercentSTV)

        # DRY WEATHER DATA
        drydata = (df.loc[(df['Bacteria'] == (bacteria))
                          & (df['Location'] == (locationID))
                          & (df['Sum of Rain for Two Days'] < .1)])
        DryDataList = drydata['Data'].tolist()
        print("Length of dry data ", len(DryDataList))
        drytargetnumberGM = target_number(DryDataList, targetGM[str(bacteria)])
        drytargetpercentGM = target_percentile(DryDataList, targetGM[str(bacteria)])
        drytargetnumberSTV = target_number(DryDataList, targetSTV[str(bacteria)])
        drytargetpercentSTV = target_percentile(DryDataList, targetSTV[str(bacteria)])
        drySTV = stv(DryDataList)
        dryGM = geomean(DryDataList)
        drymin = minvalue(DryDataList)
        drymax = maxvalue(DryDataList)

        # WET WEATHER DATA
        wetdata = (df.loc[(df['Bacteria'] == (bacteria))
                          & (df['Location'] == (locationID))
                          & (df['Sum of Rain for Two Days'] >=.1)])
        WetDataList = wetdata['Data'].tolist()
        print("Length of wet data ", len(WetDataList))
        wettargetpercentGM = target_percentile(WetDataList, targetGM[str(bacteria)])
        wettargetnumberGM = target_number(WetDataList, targetGM[str(bacteria)])
        wettargetpercentSTV = target_percentile(WetDataList, targetSTV[str(bacteria)])
        wettargetnumberSTV = target_number(WetDataList, targetSTV[str(bacteria)])
        wetSTV = stv(WetDataList)
        wetGM = geomean(WetDataList)
        wetmin = minvalue(WetDataList)
        wetmax = maxvalue(WetDataList)

        return LIST.append([locationID, bacteria, targetGM[str(bacteria)], targetSTV[str(bacteria)],
                            len(DataList),
                            float(p0), float(p5), float(p25), float(p50), float(p75), float(p90), float(p100),
                            targetnumberGM, targetpercentGM,
                            targetnumberSTV, targetpercentSTV,
                            GM, STV,
                            len(DryDataList), len(WetDataList),
                            drytargetnumberGM, wettargetnumberGM,
                            drytargetnumberSTV, wettargetnumberSTV,
                            drytargetpercentGM, wettargetpercentGM,
                            drytargetpercentSTV, wettargetpercentSTV,
                            dryGM, wetGM,
                            drySTV, wetSTV,
                            drymin, drymax, wetmin, wetmax])



#### Create a Pandas Dataframe of the data.
exportingdata = pd.DataFrame(columns=["Location", "Bacteria", "Target Value for GM", "Target Value for STV",
                                      "Number of Observations",
                                      "P0", "P5", "P25", "P50", "P75", "P90", "P100",
                                      "Number Exceeding Target GM", "Percent that exceed the Target GM",
                                      "Number Exceeding Target STV", "Percent that exceed the Target STV",
                                      "Geo Mean", "STV",
                                      "Number of Dry Weather Samples", "Number of Wet Weather Samples",
                                      "Number Dry Samples Exceeding Target GM", "Number Wet Samples Exceeding Target GM",
                                      "Number Dry Samples Exceeding Target STV", "Number Wet Samples Exceeding Target STV",
                                      "Percent of Dry Samples that exceed the Target GM", "Percent of Wet Samples that exceed the Target GM",
                                      "Percent of Dry Samples that exceed the Target STV", "Percent of Wet Samples that exceed the Target STV",
                                      "Dry Samples GM", "Wet Samples GM", "Dry Samples STV", "Wet Samples STV",
                                      "Low of Dry Samples", "High of Dry Samples",
                                      "Low of Wet Samples","High of Wet Samples"])

"""
# Excel Sheet made from function
PWDdata = pd.read_excel(r'/Users/saffron/Documents/Water Research/2021 Data/2021datawithNOAARainFall.xlsx')
#### Create a pandas dataframe
df = pd.DataFrame(PWDdata)


# Make a list of only the unique locations and bacteria types
LocationList = df['Location'].unique().tolist()
BacteriaList = df['Bacteria'].unique().tolist()

print('Location List:\n', LocationList)
print('BacteriaList:\n', BacteriaList)

for L in range(len(LocationList)):
    for B in range(len(BacteriaList)):
        makingdatasheet(BacteriaList[B], LocationList[L])

"""


# Excel Sheet made from function
#DRBCdata = pd.read_excel(r'/Users/saffron/Documents/Water Research/DRBC 2019,2020,2021/DRBC 19,20,21.xlsx')
#PWDdata = pd.read_excel(r'/Users/saffron/Documents/Water Research/PWD Data With Rainfall/PWD2019Data_Rainfall.xlsx')
#Summerdata = pd.read_excel(r'/Users/saffron/Documents/Water Research/Summer Data Sampling/Summer2021Data_Rainfall.xlsx')
AllData = pd.read_excel(r'/Users/saffron/Documents/Water Research/All Data.xlsx')
#### Create a pandas dataframe
df = pd.DataFrame(AllData)

# Make a list of only the unique locations and bacteria types
LocationList = df['Location'].unique().tolist()
BacteriaList = df['Bacteria'].unique().tolist()

print('Location List:\n', LocationList)
print('BacteriaList:\n', BacteriaList)

for L in range(len(LocationList)):
    for B in range(len(BacteriaList)):
        makingdatasheet(BacteriaList[B], LocationList[L])



"""
# Excel Sheet made from function
Centraldata = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/RawCentralChanneldataWithRainFall.xlsx')
#### Create a pandas dataframe
df = pd.DataFrame(Centraldata)

# Make a list of only the unique locations and bacteria types
LocationList = df['Location'].unique().tolist()
BacteriaList = df['Bacteria'].unique().tolist()

print('Location List:\n', LocationList)
print('BacteriaList:\n', BacteriaList)

for L in range(len(LocationList)):
    for B in range(len(BacteriaList)):
        makingdatasheet(BacteriaList[B], LocationList[L], 'Central Channel')

"""


exportingdata = exportingdata.append(pd.DataFrame(LIST, columns=exportingdata.columns))

##### EXPORT TO EXCEL

### CHANGE THIS TO NAME
file_name = 'AllData_WetandDryData.xlsx'

# saving the excel
exportingdata.to_excel(file_name)
print('\nDataFrame is written to Excel File successfully.')
