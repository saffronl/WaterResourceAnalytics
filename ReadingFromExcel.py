#pip install pandas
#pip install xlrd
#pip install openpyxl
import pandas as pd
import numpy as np

## For other excel files - all of the column names will have to change to fit the new excel sheet
#   'sample.date', 'parameter', 'loc.ID', 'data.value'

#### Reading from the excel sheet
data = pd.read_excel(r'/Users/saffron/Documents/Howard_Neukrug_Water_Center_PWD_Shore_Grab_Bacteria_2019.xlsx')
#print(data)

#### Create a pandas dataframe
df = pd.DataFrame(data)

#### Remove missing data from IMPORTANT columns
df = df.dropna(subset=['sample.date', 'parameter', 'loc.ID', 'data.value'])

#geometric mean
def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

# Create a list of lists for the bacteria, location, month, etc, to put into a pandas dataframe
list = []

#using the month, bacteria, and location, get the geometric mean
def pullingdata(month,bacteria,locationID):
    # Matching the correct columns with the parameters from the function
    DATA = (df.loc[(df['sample.date'].dt.month == (month))
             & (df['parameter'] == (bacteria))
             & (df['loc.ID'] == (locationID))])

    # Make a list of all of the data (MPN/100mL) with the same criteria
                # (month, bacteria, and location iD)
    DataList = DATA['data.value'].tolist()

    # If there is no data for the month, only print this statement and do nothing else
    if not DataList:
        print("No data for month " + str(month) + "\n")

    # If there is data for the month, make a list of the month, location, bacteria, and the geometric mean
    else:
        print("Bacteria: " + str(bacteria))
        print("Location ID: " + str(locationID))
        print("Month: " + str(month))
        print(DataList)
        print("Geometric Mean: " + str(geo_mean(DataList)) + "\n")
        return list.append([month, locationID, bacteria, float(geo_mean(DataList))])
        #print(STV)


# Make a list of only the unique locations and bacteria types
LocationList = df['loc.ID'].unique().tolist()
BacteriaList = df['parameter'].unique().tolist()

i=1

# outer loop is for all the months
while i < 13:
    # middle loop is running through all the unique locations
    for L in range(len(LocationList)):
        # inner loop is running through all of the unique bacteria
        for B in range(len(BacteriaList)):
            # running the above function
            pullingdata(i,BacteriaList[B],LocationList[L])
    i+=1


#### Create a Pandas Dataframe of the data.
pwd_data = pd.DataFrame(columns = ["Month","Bacteria","Location ID","Geometric Mean"])

# make the earlier defined list into a dataframe
pwd_data = pwd_data.append(pd.DataFrame(list, columns=pwd_data.columns))

##### EXPORT TO EXCEL

# determining the name of the file
file_name = 'PWDdata.xlsx'

# saving the excel
pwd_data.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')
