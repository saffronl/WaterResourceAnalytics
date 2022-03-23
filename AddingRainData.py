# Saffron Livaccari
import pandas as pd


### Lines that have to be changed are marked by ###

# To make the important column names universal for all the bacterial data
def universal_excelsheet(file, ColumnNameforDate, ColumnNameforBacteria, ColumnNameforLocation, ColumnforData):
    data = pd.read_excel(file)
    df = pd.DataFrame(data)
    df.rename(columns={ColumnNameforDate: 'Date', ColumnNameforBacteria: 'Bacteria',
                       ColumnNameforLocation: 'Location', ColumnforData: 'Data'}, inplace=True)
    df = df.dropna(subset=['Date', 'Bacteria', 'Location', 'Data'])
    df.to_excel('data.xlsx')
    return df


### CHANGE THIS PATH TO FIT YOUR EXCEL SHEET
excel = '/Users/saffron/Documents/Water Research/Summer Data Sampling/Raw Data/FIB and Field Data.xlsx'

### CHANGE THIS TO FIT THE COLUMNS NAMES OF ABOVE EXCEL SHEET
universal_excelsheet(excel, 'Sample Date', 'Bacteria', 'Station', 'Result') 


# Excel Sheet made from function
data = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/data.xlsx')
df = pd.DataFrame(data) # turn into pandas dataframe


### Column names will have to be changed if using a different excel sheet - "DATE", "PRCP"
def RainExcelSheet(file1999,file2005,file2008,file2019, file2020, file2021): # creates a separate excel sheet of all the rainfall information
    # read in two columns date and prcp from each year rainfall data file
    data2005 = pd.read_excel(file2005, usecols=["DATE", "PRCP"])
    data1999 = pd.read_excel(file1999, usecols=["DATE", "PRCP"]) 
    data2008 = pd.read_excel(file2008, usecols=["DATE", "PRCP"])
    data2019 = pd.read_excel(file2019, usecols=["DATE", "PRCP"])
    data2020 = pd.read_excel(file2020, usecols=["DATE", "PRCP"])
    data2021 = pd.read_excel(file2021, usecols=["DATE", "PRCP"])
    # turn into a pandas dataframe
    df1999 = pd.DataFrame(data1999) 
    df2005 = pd.DataFrame(data2005)
    df2008 = pd.DataFrame(data2008)
    df2019 = pd.DataFrame(data2019)
    df2020 = pd.DataFrame(data2020)
    df2021 = pd.DataFrame(data2021)
    # combine all the data frames
    frames = [df1999, df2005, df2008, df2019, df2020, df2021]
    df = pd.concat(frames)
    # do the rolling sum of the rainfall
    df['SumTwoDays'] = round(df['PRCP'].rolling(window=2).sum(), 4) 
    df['SumThreeDays'] = round(df['PRCP'].rolling(window=3).sum(), 4)
    df['SumSixDays'] = round(df['PRCP'].rolling(window=6).sum(), 4)
    df['SumTenDays'] = round(df['PRCP'].rolling(window=10).sum(), 4)
    # count the number of days after a certain rainfall event amount
    df['Count of days after .1 Rainfall Event'] = df.groupby((df['PRCP'] >= .1).cumsum()).cumcount()
    df['Count of days after any rainfall event'] = df.groupby((df['PRCP'] > 0).cumsum()).cumcount()
    # put all this into one excel sheet
    df.to_excel('RainData.xlsx')
    return df


# Excel sheet for the precipiation
### CHANGE THIS TO FIT YOUR PATH FOR THE RAIN EXCEL SHEETS
excel1999 = r"/Users/saffron/Documents/Water Research/RawData/rain1999to2004.xlsx"
excel2005 = r"/Users/saffron/Documents/Water Research/RawData/rain2005to2007.xlsx"
excel2008 = r"/Users/saffron/Documents/Water Research/RawData/rain2008to2018.xlsx"
excel2019 = r"/Users/saffron/Documents/Water Research/RawData/Philadelphia Airport Precip data 2019.xlsx"
excel2020 = r"/Users/saffron/Documents/Water Research/RawData/RainData2020.xlsx"
excel2021 = r"/Users/saffron/Documents/Water Research/Summer Data Sampling/Raw Data/NOAARainfall2021.xlsx"

# combine all the rainfall datasheets I have into one complete excel file in using the RainExcelSheet function
RainExcelSheet(excel1999, excel2005, excel2008, excel2019, excel2020, excel2021)
raindata = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/RainData.xlsx')
df1 = pd.DataFrame(raindata)

# Function that gets a dataframe and turns it into a dictionary
def dataframe_to_dict(df, key_column, value_column):
    dict = df.set_index(key_column)[value_column].to_dict()
    return dict

# turns this information into a dictionary in order to add it into another dataset
rain_dict = dataframe_to_dict(df1, 'DATE', 'PRCP')
TwoDays_dict = dataframe_to_dict(df1, 'DATE', 'SumTwoDays')
ThreeDays_dict = dataframe_to_dict(df1, 'DATE', 'SumThreeDays')
SixDays_dict = dataframe_to_dict(df1, 'DATE', 'SumSixDays')
TenDays_dict = dataframe_to_dict(df1, 'DATE', 'SumTenDays')
Count_dict = dataframe_to_dict(df1, 'DATE', 'Count of days after .1 Rainfall Event')
Count_dict2 = dataframe_to_dict(df1, 'DATE', 'Count of days after any rainfall event')

DAILYLIST = (df['Date']) # makes a list of all the dates

# make a list of lists for all of the rain values
totalrain = []
totaltwo = []
totalthree = []
totalsix = []
totalten = []
totalcount = []
totalcount2 = []
for DateInList in DAILYLIST:
    print(DateInList)
    rain = rain_dict.get(DateInList)
    two = TwoDays_dict.get(DateInList)
    print(two)
    three = ThreeDays_dict.get(DateInList)
    print(three)
    six = SixDays_dict.get(DateInList)
    print(six)
    ten = TenDays_dict.get(DateInList)
    print(ten)
    count = Count_dict.get(DateInList)
    print(count)
    count2 = Count_dict2.get(DateInList)
    print(count2)
    totalrain.append(rain)
    totaltwo.append(two)
    totalthree.append(three)
    totalsix.append(six)
    totalten.append(ten)
    totalcount.append(count)
    totalcount2.append(count2)

# This makes the excel sheet into separate columns with the following titles, so each rainfall amount is its own column    
exportingrain = (pd.DataFrame({'Rain per Each Day': totalrain, 'Sum of Rain for Two Days': totaltwo,
                               'Sum of Rain for Three Days': totalthree, 'Sum of Rain for Six Days': totalsix,
                               'Sum of Rain for Ten Days': totalten,
                               'Count of days after .1 Rainfall Event': totalcount,
                               'Count of days after any rainfall event': totalcount2}))

# join the two data frames - rainfall and bacteria data, based on the date!
exportingdata = pd.concat([df, exportingrain], axis=1)

##### EXPORT TO EXCEL

### CHANGE THIS TO NAME
file_name = 'Summer2021Data_Rainfall.xlsx'

# saving the excel
exportingdata.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')
