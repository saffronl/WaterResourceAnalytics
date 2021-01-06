# WaterResourceAnalytics
Code I wrote as a Data Analyst for the Water Center at Penn.


The city of Philadelphia has combined sewer overflows, meaning the sewer pipes carry stormwater and wastewater.
When the pipes are overloaded with water, they will empty into the river.

<b>This research project is aimed towards analyzing bacteria samples from the Delaware and Schuylkill River to better understand the affect of 
rain on bacteria samples.</b>

The samples were collected by both the Philadelphia Water Department and Delaware River Basin Commission for fecal coliform, enterococcus, and e.coli.
There are multiple locations of CSO's along the riverbanks from where the bacteria was sampled. 
Acceptable bacteria amounts for swimming is determined by the EPA.


ReadingFromExcel.py
<ul>
  <li><b>Start from this sheet</b></li>
  <li>Only have to change three lines</br>
  1. The excel file (excel = ......)</br>
  2. The column names in the above excel file (universal_excelsheet(Excel file, Column Name for Date, Column Name for Bacteria, Column Name for Location, Column for Data)</br>
  3. At the end of the script, change the file name to save the new excel sheet down to your computer. (file_name = ....)</br>
  </li>
  <li>Function -  universal_excelsheet - </br> 
  This function takes in the raw PWD or DRBC excel sheet and changes the column names into a standard ('Date', 'Bacteria', 'Location', 'Data'), so the later functions do not have to change.
  </li>
  <li>Function - geo_mean - </br> 
  Calculates the geometric mean for a list of values.
  </li>
  <li>Function - stv - </br>
  Calculates the statistical threshold value for a list of values.
  </li>
  <li>Function - average - </br>
  Calculates the average for a list of values.
  </li>
  <li>Function - pullingdata - </br>
  Finds a list of the data when the month, bacteria, and location are the same. Uses this list to calculate the geometric mean, STV, average, and percentiles. This information is exported as a list.
  </li>
  <li>Next, the location, bacteria, and year is compiled and only the unique values are added to a list.</li>
  <li>The unique value lists from the previous step is used to loop through every bacteria (fecal, enterococci, and ecoli) at every location, for every month, for every year. The function pullingdata creates a unique list for each bacteria, location, month, and year.</li>
  <li>Each list that is created from above is added as a row to a pandas dataframe.</li>
  <li>This dataframe is then exported into an excel sheet.</li>
</ul>

AddingRainData.py
<ul>
  <li><b>Second sheet</b></li>
  <li>Four lines to change are</br>
  1. The excel file for the PWD or DRBC data (excel = ......)</br>
  2. The column names in the above excel file (universal_excelsheet(Excel file, Column Name for Date, Column Name for Bacteria, Column Name for Location, Column for Data)</br>
  3. The excel file for the rain data (excel2019 = .... , excel2020 = ....)
  4. At the end of the script, change the file name to save the new excel sheet down to your computer. (file_name = ....)</br>
  <li>Function universal_excelsheet does the same as from ReadingFromExcel.py</li>
  <li>Function - RainExcelSheet - </br>
  The column names will have to be changed to fit your excel sheet. This function creats the rolling sum of the precipitation for 2, 3, 6, and 10 days and counts the number of days it has been since a rainfall event of >.1. This function returns a new excel sheet called RainData for the date, the amount of precipitation for each date, the cumulative precipitation for 2, 3, 6, and 10 days, the count of days after .1 rainfall event.
  </li>
  <li>Function - dataframe_to_dict - </br>
  This function creates a dictionary pair. The code after this function uses this function to create a dictionary pair for date and precipitation, date and sum for two days, ..., date and count of days after .1 rainfall event.
  </li>
  <li>DAILYLIST = (df['Date']) creates a list of all days in PWD or DRBC excel file.</li>
  <li>The next block of code (for DateInList in DAILYLIST:) creates a list of every date in PWD or DRBC excel file with the dictionary paired precipitation amount, the cumulative sum for two days, ..., and the count of days after .1 rainfall event.</li>
  <li>Next, (exportingrain = ...) creates a pandas data frame for every list created in the previous step.</li>
  <li>Next, (exportingdata = ...) this combines the PWD or DRBC data frame with the rain data frame created in the previous step.</li>
  <li>The data is saved down to an excel file.</li>
</ul>
DistributionTests.py
Graphing BoxPlot.py
<li>
</li>
Graphing Histograms.py
<li>
</li>
GraphingGeoMean.py
<li>
</li>
Histograms for Total Rainfall in Philly.py
<li>
</li>
Percentiles.py
<li>
</li>
T-Test.py
<li>
</li>
