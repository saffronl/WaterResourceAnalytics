# Saffron Livaccari

import pandas as pd
import numpy as np
import statistics as st
import datetime as dt

### Three Lines have to be changed - marked by ###

# To make the important column names universal
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
excel = '/Users/saffron/Downloads/Nearshore_Bacteria.xlsx'
#PWD
#excel = '/Users/saffron/Documents/Howard_Neukrug_Water_Center_PWD_Shore_Grab_Bacteria_2019.xlsx'
### CHANGE THIS TO FIT THE COLUMNS NAMES OF ABOVE EXCEL SHEET
#DRBC
ExcelSheet(excel,'ActivityStartDate','CharacteristicName','Location','ResultMeasureValue')
#PWD
#ExcelSheet(excel,'sample.date', 'parameter', 'loc.ID', 'data.value')

#Excel Sheet made from function
data = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/data.xlsx')
#Excel sheet for the precipiation
raindata = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/RainData.xlsx')
df1 = pd.DataFrame(raindata)

def dataframe_to_dict(df, key_column, value_column):
    dict = df.set_index(key_column)[value_column].to_dict()
    return dict

rain_dict = dataframe_to_dict(df1,'DATE','PRCP')
TwoDays_dict = dataframe_to_dict(df1,'DATE','SumTwoDays')
ThreeDays_dict = dataframe_to_dict(df1,'DATE','SumThreeDays')
SixDays_dict = dataframe_to_dict(df1,'DATE','SumSixDays')
TenDays_dict = dataframe_to_dict(df1,'DATE','SumTenDays')


#### Create a pandas dataframe
df = pd.DataFrame(data)
df1 = pd.DataFrame(raindata)


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

# Average
def average(iterable):
    a = np.array(iterable)
    eq = (a.sum())/(len(iterable))
    return eq

# Create a list of lists for the bacteria, location, month, etc
LIST = []

# using the month, bacteria, and location, get the geometric mean
def pullingdata(month,year,bacteria,locationID):
    # Matching the correct columns with the parameters from the function
    DATA = (df.loc[(df['Date'].dt.month == (month))
                   & (df['Date'].dt.year == (year))
                   & (df['Bacteria'] == (bacteria))
                   & (df['Location'] == (locationID))])

    # Make a list of all of the data (MPN/100mL) with the same criteria (month, bacteria, and location iD
    DataList = DATA['Data'].tolist()
    DayList = DATA['Date'].dt.day.tolist()

    # If there is no data for the month, only print this statement and do nothing else
    if not DataList:
        print("No data for month " + str(month) + "\n")

    elif len(DataList) == 1:
        print("Bacteria: " + str(bacteria))
        print("Location ID: " + str(locationID))
        print("Month/Year: " + str(month) + "/" + str(year))
        print(DataList)
        print(DayList)
        print(average(DataList))
        print("Only one data point - cannot calculate STV, GM, or percentiles\n")
        x = 'NA'
        return LIST.append([month, year, locationID, float(average(DataList)), bacteria,x,x,x,x,x,DataList[0],x,x,x,DataList,DayList])

    # If there is data for the month, make a list of the month, location, bacteria, and the geometric mean
    else:
        print("Bacteria: " + str(bacteria))
        print("Location ID: " + str(locationID))
        print("Month/Year: " + str(month) + "/" + str(year))
        print(DataList)
        print(DayList)
        print(average(DataList))
        print("Geometric Mean: " + str(geo_mean(DataList)))
        print("STV: " + str(stv(DataList)) + "\n")
        p0 = np.percentile(DataList, 0)
        p5 = np.percentile(DataList, 5)
        p25 = np.percentile(DataList, 25)
        p50 = np.percentile(DataList, 50)
        p75 = np.percentile(DataList, 75)
        p90 = np.percentile(DataList, 90)
        p100 = np.percentile(DataList, 100)
        return LIST.append([month, year, locationID, bacteria, float(average(DataList)), float(geo_mean(DataList)), float(stv(DataList)),
                            float(p0),float(p5),float(p25),float(p50),float(p75),float(p90),float(p100),
                            DataList,DayList])

# Make a list of only the unique locations and bacteria types
LocationList = df['Location'].unique().tolist()
BacteriaList = df['Bacteria'].unique().tolist()
YearList = df['Date'].dt.year.unique().tolist()

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
        i+=1


#### Create a Pandas Dataframe of the data.
exportingdata = pd.DataFrame(columns = ["MONTH", "YEAR", "LocationID","Bacteria","Average","GEO MEAN","STV",
                                   "P0","P5","P25","P50","P75","P90","P100",
                                   "Data List","Day List"])


# make the earlier defined list into a dataframe
exportingdata = exportingdata.append(pd.DataFrame(LIST, columns = exportingdata.columns))


##### EXPORT TO EXCEL

### CHANGE THIS TO NAME
#file_name = 'PWDdata.xlsx'
file_name = 'DRBC2data.xlsx'

# saving the excel
exportingdata.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')




