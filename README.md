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
  <li><b>Start from this sheet.</b></li>
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
  <li>Each list that is created from above is added as a row to a pandas datafram.</li>
  <li>This dataframe is then exported into an excel sheet.</li>
</ul>
AddingRainData.py
<ul>
  <li><b>Start from this sheet.</b></li>
  <li></li>
</ul>
DistributionTests.py
<ul>
  <li><b>Start from this sheet.</b></li>
  <li></li>
</ul>
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
