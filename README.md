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
  <li>First function -  universal_excelsheet - </br> 
  This function takes in the raw PWD or DRBC excel sheet and changes the column names into a standard ('Date', 'Bacteria', 'Location', 'Data'), so the later functions do not have to change.
  </li>
  <li></li>
  <li></li>
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
