# Saffron Livaccari
import pandas as pd

### FOUR Lines have to be changed - marked by ###

# To make the important column names universal
def universal_excelsheet(file,ColumnNameforDate,ColumnNameforBacteria,ColumnNameforLocation,ColumnforData):
    data = pd.read_excel(file)
    df = pd.DataFrame(data)
    df.rename(columns={ColumnNameforDate:'Date',ColumnNameforBacteria:'Bacteria',
                         ColumnNameforLocation:'Location',ColumnforData:'Data'},inplace=True)
    df = df.dropna(subset=['Date','Bacteria','Location','Data'])
    df.to_excel('data.xlsx')
    return df

### CHANGE THIS PATH TO FIT YOUR EXCEL SHEET
#DRBC
#excel = '/Users/saffron/Downloads/Nearshore_Bacteria.xlsx'
#PWD
excel = '/Users/saffron/Documents/Howard_Neukrug_Water_Center_PWD_Shore_Grab_Bacteria_2019.xlsx'
#DRBC 2020
#excel = '/Users/saffron/Downloads/DRBC 2020 nearshore.xlsx'

### CHANGE THIS TO FIT THE COLUMNS NAMES OF ABOVE EXCEL SHEET
#DRBC
#ExcelSheet(excel,'ActivityStartDate','CharacteristicName','Location','ResultMeasureValue')
#PWD
universal_excelsheet(excel,'sample.date', 'parameter', 'loc.ID', 'data.value')
#DRBC 2020
#ExcelSheet(excel,'CollectionDate','Parameter','SiteName','result')

#Excel Sheet made from function
data = pd.read_excel(r'/Users/saffron/PycharmProjects/PythonProject1/data.xlsx')
df = pd.DataFrame(data)

def RainExcelSheet(file2019,file2020):
    data2019 = pd.read_excel(file2019, usecols=["DATE", "PRCP"])
    data2020 = pd.read_excel(file2020, usecols=["DATE", "PRCP"])
    df2019 = pd.DataFrame(data2019)
    df2020 = pd.DataFrame(data2020)
    frames = [df2019,df2020]
    df = pd.concat(frames)
    df['SumTwoDays'] = round(df['PRCP'].rolling(window=2).sum(),4)
    df['SumThreeDays'] = round(df['PRCP'].rolling(window=3).sum(),4)
    df['SumSixDays'] = round(df['PRCP'].rolling(window=6).sum(),4)
    df['SumTenDays'] = round(df['PRCP'].rolling(window=10).sum(),4)
    df['Count of days after .1 Rainfall Event'] = df.groupby((df['PRCP'] >= .1).cumsum()).cumcount()
    df.to_excel('RainData.xlsx')
    return df

#Excel sheet for the precipiation
### CHANGE THIS TO FIT YOUR PATH FOR THE RAIN EXCEL SHEETS
excel2019 = r"/Users/saffron/Documents/Philadelphia Airport Precip data 2019.xlsx"
excel2020 = r"/Users/saffron/Documents/RainData2020.xlsx"
RainExcelSheet(excel2019,excel2020)
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
Count_dict = dataframe_to_dict(df1,'DATE','Count of days after .1 Rainfall Event')


DAILYLIST = (df['Date'])

#make a list of lists for all of the rain values
totalrain = []
totaltwo = []
totalthree = []
totalsix = []
totalten = []
totalcount = []
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
    totalrain.append(rain)
    totaltwo.append(two)
    totalthree.append(three)
    totalsix.append(six)
    totalten.append(ten)
    totalcount.append(count)


exportingrain = (pd.DataFrame({'Rain per Each Day':totalrain,'Sum of Rain for Two Days':totaltwo,
                               'Sum of Rain for Three Days':totalthree, 'Sum of Rain for Six Days':totalsix,
                               'Sum of Rain for Ten Days':totalten,'Count of days after .1 Rainfall Event': totalcount}))


# join the two data frames
exportingdata = pd.concat([df,exportingrain],axis=1)

##### EXPORT TO EXCEL

### CHANGE THIS TO NAME
file_name = 'RawPWD2019datawithRainFall.xlsx'

# saving the excel
exportingdata.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')

