# Saffron Livaccari

#pip install pandas
#pip install xlrd
#pip install openpyxl
import pandas as pd
import numpy as np
import statistics as st
import datetime as dt
import xlrd

## For other excel files - all of the column names will have to change to fit the new excel sheet
#   'sample.date', 'parameter', 'loc.ID', 'data.value'

#### Reading from the excel sheet

## PWD Data
#data = pd.read_excel(r'/Users/saffron/Documents/Howard_Neukrug_Water_Center_PWD_Shore_Grab_Bacteria_2019.xlsx')

## DRBC Data
data = pd.read_excel(r'/Users/saffron/Downloads/Nearshore_Bacteria.xlsx',sheet_name = "Raw Data")

#Excel sheet for the precipiation
raindata = pd.read_excel(r'/Users/saffron/Documents/Philadelphia Airport Precip data 2019.xlsx')

#### Create a pandas dataframe
df = pd.DataFrame(data)
df1 = pd.DataFrame(raindata)

#### Remove missing data from IMPORTANT columns

## PWD Data
#df = df.dropna(subset=['sample.date', 'parameter', 'loc.ID', 'data.value'])

## DRBC Data
df = df.dropna(subset=['ActivityStartDate', 'CharacteristicName', 'Location', 'ResultMeasureValue'])

def dataframe_to_dict(df, key_column, value_column):
    dict = df.set_index(key_column)[value_column].to_dict()
    return dict


rain_dict = dataframe_to_dict(df1,'DATE','PRCP')
print(rain_dict)


# Geometric Mean
def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

# Statistical Threshold Value
def stv(iterable):
    # log based 10 : STV = 10 ** ( avg(log values) + 1.282 * std(log values) )
    b = np.log10(iterable)
    eq = 10 ** (st.mean(b) + (1.282 * st.stdev(b)))
    return eq

# Create a list of lists for the bacteria, location, month, etc, to put into a pandas dataframe

LIST = []

#using the month, bacteria, and location, get the geometric mean
def pullingdata(month,year,bacteria,locationID):
    # Matching the correct columns with the parameters from the function

    ## PWD Data
    #DATA = (df.loc[(df['sample.date'].dt.month == (month))
     #                  & (df['sample.date'].dt.year == (year))
      #                 & (df['parameter'] == (bacteria))
       #                & (df['loc.ID'] == (locationID))])

    ## DRBC Data
    DATA = (df.loc[(df['ActivityStartDate'].dt.month == (month))
                   & (df['ActivityStartDate'].dt.year == (year))
                   & (df['CharacteristicName'] == (bacteria))
                   & (df['Location'] == (locationID))])

    #print(DATA)

    # Make a list of all of the data (MPN/100mL) with the same criteria (month, bacteria, and location iD

    ## PWD Data
    #DataList = DATA['data.value'].tolist()
    #DayList = DATA['sample.date'].dt.day.tolist()

    ## DRBC Data
    DataList = DATA['ResultMeasureValue'].tolist()
    DayList = DATA['ActivityStartDate'].dt.day.tolist()

    # If there is no data for the month, only print this statement and do nothing else
    if not DataList:
        print("No data for month " + str(month) + "\n")

    elif len(DataList) == 1:
        print("Bacteria: " + str(bacteria))
        print("Location ID: " + str(locationID))
        print("Month/Year: " + str(month) + "/" + str(year))
        print(DataList)
        print(DayList)
        print("Only one data point - cannot calculate STV, GM, or percentiles\n")
        x = 'NA'
        return LIST.append([month, year, locationID, bacteria,x,x,x,x,x,DataList[0],x,x,x,DataList,DayList])

    # If there is data for the month, make a list of the month, location, bacteria, and the geometric mean
    else:
        print("Bacteria: " + str(bacteria))
        print("Location ID: " + str(locationID))
        print("Month/Year: " + str(month) + "/" + str(year))
        print(DataList)
        print(DayList)
        print("Geometric Mean: " + str(geo_mean(DataList)))
        print("STV: " + str(stv(DataList)) + "\n")
        p0 = np.percentile(DataList, 0)
        p5 = np.percentile(DataList, 5)
        p25 = np.percentile(DataList, 25)
        p50 = np.percentile(DataList, 50)
        p75 = np.percentile(DataList, 75)
        p90 = np.percentile(DataList, 90)
        p100 = np.percentile(DataList, 100)
        return LIST.append([month, year, locationID, bacteria, float(geo_mean(DataList)), float(stv(DataList)),
                            float(p0),float(p5),float(p25),float(p50),float(p75),float(p90),float(p100),
                            DataList,DayList])

DAILYLIST = []

#using the month, bacteria, and location, get the RAINFALL VALUES
def dailydata(month,year,bacteria,locationID):
    # Matching the correct columns with the parameters from the function

    ## PWD Data
    #DATA = (df.loc[(df['sample.date'].dt.month == (month))
    #                   & (df['sample.date'].dt.year == (year))
    #                   & (df['parameter'] == (bacteria))
    #                   & (df['loc.ID'] == (locationID))])

    ## DRBC Data
    DATA = (df.loc[(df['ActivityStartDate'].dt.month == (month))
                   & (df['ActivityStartDate'].dt.year == (year))
                   & (df['CharacteristicName'] == (bacteria))
                   & (df['Location'] == (locationID))])

    # Make a list of all of the data (MPN/100mL) with the same criteria (month, bacteria, and location iD

    ## PWD Data
    #DataList2 = DATA['data.value'].tolist()
    #DayList2 = DATA['sample.date'].tolist()

    ## DRBC Data
    DataList2 = DATA['ResultMeasureValue'].tolist()
    DayList2 = DATA['ActivityStartDate'].tolist()

    # If there is no data for the month, only print this statement and do nothing else
    if not DataList2:
        print("No data for month " + str(month) + "\n")

    # If there is data for the month, make a list of the month, location, bacteria, and the geometric mean
    else:
        print(DataList2)
        print(DayList2)
        return DAILYLIST.append(DayList2)

# Make a list of only the unique locations and bacteria types

## PWD Data
#LocationList = df['loc.ID'].unique().tolist()
#BacteriaList = df['parameter'].unique().tolist()
#YearList = df['sample.date'].dt.year.unique().tolist()

## DRBC Data
LocationList = df['Location'].unique().tolist()
BacteriaList = df['CharacteristicName'].unique().tolist()
YearList = df['ActivityStartDate'].dt.year.unique().tolist()

i=0

#loop through all the years
for Y in range(len(YearList)):
    # outer loop is for all the months
    while i < 13:
        # middle loop is running through all the unique locations
        for L in range(len(LocationList)):
            # inner loop is running through all of the unique bacteria
            for B in range(len(BacteriaList)):
                # running the above function
                pullingdata(i,YearList[Y],BacteriaList[B],LocationList[L])
                dailydata(i,YearList[Y],BacteriaList[B],LocationList[L])
        i+=1


#make a list of lists for all of the rain values
totalrainlist = []
for NestedList in DAILYLIST:
    rainelements = []
    for DateInNestedList in NestedList:
        y = rain_dict.get(DateInNestedList)
        rainelements.append(y)
    totalrainlist.append(rainelements)


# get the longest list in the list of rain values
def longest(list):
    list_len = [len(i) for i in list]
    return (max(list_len))

# make a list of strings the length of rain values
columnsforrain = ["Rain"]*longest(totalrainlist)


#### Create a Pandas Dataframe of the data.
pwd_data = pd.DataFrame(columns = ["MONTH", "YEAR", "LocationID","Bacteria","GEO MEAN","STV",
                                   "P0","P5","P25","P50","P75","P90","P100",
                                   "Data List","Day List"])
#### Create a Pandas Dataframe of the RAIN data - columns automatically created for the length of the longest rain list
pwd2_data = pd.DataFrame(columns = columnsforrain)

# make the earlier defined list into a dataframe
pwd_data = pwd_data.append(pd.DataFrame(LIST, columns = pwd_data.columns))
pwd2_data = pwd2_data.append(pd.DataFrame(totalrainlist, columns = pwd2_data.columns))

# join the two data frames
pwd_data = pd.concat([pwd_data,pwd2_data],axis=1)



##### EXPORT TO EXCEL

# determining the name of the file
## PWD Data
#file_name = 'PWDdata.xlsx'

## DRBC Data
file_name = 'DRBC2data.xlsx'


# saving the excel
pwd_data.to_excel(file_name)

print('DataFrame is written to Excel File successfully.')



