# Saffron Livaccari
import pandas as pd

### Three Lines have to be changed - marked by ###

# To make the important column names universal
def ExcelSheet(file,ColumnNameforDate,ColumnNameforBacteria,ColumnNameforLocation,ColumnforData):
    data = pd.read_excel(file)
    df = pd.DataFrame(data)
    df.rename(columns={ColumnNameforDate:'Date',ColumnNameforBacteria:'Bacteria',
                         ColumnNameforLocation:'Location',ColumnforData:'Data'},inplace=True)
    df = df.dropna(subset=['Date','Bacteria','Location','Data'])
    df.to_excel('data.xlsx')
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
df = pd.DataFrame(data)

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


DAILYLIST = (df['Date'])

#make a list of lists for all of the rain values
totalrain = []
totaltwo = []
totalthree = []
totalsix = []
totalten = []
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
    totalrain.append(rain)
    totaltwo.append(two)
    totalthree.append(three)
    totalsix.append(six)
    totalten.append(ten)

exportingrain = (pd.DataFrame({'Rain per Each Day':totalrain,'Sum of Rain for Two Days':totaltwo,
                                                   'Sum of Rain for Three Days':totalthree,'Sum of Rain for Six Days':totalsix,
                                                  'Sum of Rain for Ten Days':totalten}))


# join the two data frames
exportingdata = pd.concat([df,exportingrain],axis=1)

##### EXPORT TO EXCEL

### CHANGE THIS TO NAME
file_name = 'RawDRBCdataWithRainFall.xlsx'

# saving the excel
exportingdata.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')




