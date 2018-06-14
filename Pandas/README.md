
### Heroes Of Pymoli Data Analysis
* Of the 780 total purchases, the vast majority are by male (~84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (~47) with secondary groups falling between 25-29 (~13%) and 15-19 (~17.5%). The total purchase value by age also aligns to the peak age demographic.

* The top 5 spenders are - 
    Lisosia; 
    Idastidru ;
    Chamjask; 
    Iral; 
    Saistyphos.

* The top 5 items by popularity (i.e. purchase count) are  - 
    Oathbreaker, Last Hope of the Breaking Storm; 
    Fiery Glass Crusader; 
    Extraction, Quickblade Of Trembling Hands; 
    Nirvana	; 
    Pursuit, Cudgel of Necromancy
-----

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.


```python
# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase ID</th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Lisim78</td>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>$3.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Lisovynya38</td>
      <td>40</td>
      <td>Male</td>
      <td>143</td>
      <td>Frenzied Scimitar</td>
      <td>$1.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Ithergue48</td>
      <td>24</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>$4.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Chamassasya86</td>
      <td>24</td>
      <td>Male</td>
      <td>100</td>
      <td>Blindscythe</td>
      <td>$3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Iskosia90</td>
      <td>23</td>
      <td>Male</td>
      <td>131</td>
      <td>Fury</td>
      <td>$1.44</td>
    </tr>
  </tbody>
</table>
</div>



## Player Count

* Display the total number of players



```python
#A dictionary containing a single list element converted to a dataframe

Total_Players_DF = pd.DataFrame({"Total Players":[purchase_data["SN"].nunique()]})

Total_Players_DF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



```python
#A dictionary containing lists converted to a dataframe

Purchasing_Analysis_DF = pd.DataFrame(
                                    
    {"Number of Unique Items" : [purchase_data["Item Name"].nunique()],
                                     
     "Average Price" : [purchase_data["Price"].mean()],
     
     "Number of Purchases" : [purchase_data["Item ID"].count()],
     
      "Total Revenue" : [purchase_data["Price"].sum()]
    }
)


# Format float values to 2 decimal places,add a comma, and prefix amounts with $

Purchasing_Analysis_DF_Ordered = Purchasing_Analysis_DF[[
    "Number of Unique Items","Average Price","Number of Purchases","Total Revenue"]]

pd.options.display.float_format = '${:,.2f}'.format

Purchasing_Analysis_DF_Ordered
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$3.05</td>
      <td>780</td>
      <td>$2,379.77</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



```python

# Convert Gender value_counts()  to data frame, calculate percentage of players, and add a new column to data frame

Gender_Demo_DF = pd.DataFrame(purchase_data["Gender"].value_counts())

Gender_Demo_DF = Gender_Demo_DF.rename(columns = {"Gender": "Total Count"}); Gender_Demo_DF

Percentage_of_Players = (Gender_Demo_DF["Total Count"])/(purchase_data["Gender"].count()) * 100 

Gender_Demo_DF["Percentage of Players"] = Percentage_of_Players 

# Reformat and reorganize the columns

pd.options.display.float_format = '{:,.2f}%'.format

Gender_Demo_DF_Organized_Renamed = Gender_Demo_DF[["Percentage of Players","Total Count"]] ;Gender_Demo_DF_Organized_Renamed
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>83.59%</td>
      <td>652</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>14.49%</td>
      <td>113</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.92%</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, etc. by gender


* For normalized purchasing, divide total purchase value by purchase count, by gender


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
# Format float values to 2 decimal places,add a comma, and prefix amounts with $

pd.options.display.float_format = '${:,.2f}'.format

Purchasing_Analysis_Summary= purchase_data.groupby(["Gender"])

Total_Purchase_Value = Purchasing_Analysis_Summary["Price"].sum()

Average_Purchase_Price = Purchasing_Analysis_Summary["Price"].sum() / Purchasing_Analysis_Summary["Gender"].count()

# Creating a new dataframe

Purchasing_Analysis_Summary_Gender = pd.DataFrame({"Purchase Count" : Purchasing_Analysis_Summary["Gender"].count(),
                                             "Average Purchase Price" : Average_Purchase_Price,
                                             "Total Purchase Value" : Total_Purchase_Value,
                                             "Normalized Totals" : Average_Purchase_Price})

# Reorder columns of the dataframe and display

Purchasing_Analysis_Summary_Gender[["Purchase Count","Average Purchase Price","Total Purchase Value","Normalized Totals"]]

```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>113</td>
      <td>$3.20</td>
      <td>$361.94</td>
      <td>$3.20</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>652</td>
      <td>$3.02</td>
      <td>$1,967.64</td>
      <td>$3.02</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>15</td>
      <td>$3.35</td>
      <td>$50.19</td>
      <td>$3.35</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table



```python
# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["Age Range"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)
Age_Demographics = purchase_data.groupby("Age Range").count()
Age_Demographics = Age_Demographics.rename(columns = {"SN": "Total Count"})
Age_Demographics["Percentage of Players"] = (Age_Demographics["Total Count"] /Age_Demographics["Total Count"].sum()) * 100


pd.options.display.float_format = '{:,.2f}%'.format
Age_Demographics_DF = Age_Demographics[["Percentage of Players","Total Count"]]
Age_Demographics_DF.index.name = None
Age_Demographics_DF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>2.95%</td>
      <td>23</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>3.59%</td>
      <td>28</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.44%</td>
      <td>136</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>46.79%</td>
      <td>365</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>12.95%</td>
      <td>101</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>9.36%</td>
      <td>73</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>5.26%</td>
      <td>41</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.67%</td>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, etc. in the table below


* Calculate Normalized Purchasing


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
Purchasing_Analysis_Age = purchase_data.groupby(["Age Range"])
Total_Purchase_Value = Purchasing_Analysis_Age["Price"].sum()

Purchase_Count = Age_Demographics_DF["Total Count"]
Average_Purchase_Price = Total_Purchase_Value/Purchase_Count
Normalized_Totals = Average_Purchase_Price

Purchasing_Analysis_Age_DF = pd.DataFrame({
    "Purchase Count": Purchase_Count,
    "Average Purchase Price": Average_Purchase_Price,
    "Total Purchase Value": Total_Purchase_Value,
    "Normalized Totals": Normalized_Totals
    })

pd.options.display.float_format = '${:,.2f}'.format
Purchasing_Analysis_Age_DF.index.name = None
Purchasing_Analysis_Age_DF.reindex(index = ["10-14","15-19","20-24","25-29","30-34","35-39","40+","<10"])
Purchasing_Analysis_Age_DF[["Purchase Count","Average Purchase Price","Total Purchase Value","Normalized Totals"]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
      <td>$3.35</td>
      <td>$77.13</td>
      <td>$3.35</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>$2.96</td>
      <td>$82.78</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>$3.04</td>
      <td>$412.89</td>
      <td>$3.04</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>$3.05</td>
      <td>$1,114.06</td>
      <td>$3.05</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>$2.90</td>
      <td>$293.00</td>
      <td>$2.90</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>$2.93</td>
      <td>$214.00</td>
      <td>$2.93</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>$3.60</td>
      <td>$147.67</td>
      <td>$3.60</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>$2.94</td>
      <td>$38.24</td>
      <td>$2.94</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
Top_Spenders = pd.DataFrame(purchase_data["SN"].value_counts().head())
Top_Spenders = Top_Spenders.rename(columns = {"SN": "Purchase Count"})
Top_Spenders.index.name = "SN"
Top_Spenders["Total Purchase Value"] = purchase_data.groupby("SN")["Price"].sum()
Top_Spenders["Average Purchase Price"] = Top_Spenders["Total Purchase Value"] / Top_Spenders["Purchase Count"] 

Top_Spenders = Top_Spenders.sort_values("Total Purchase Value",ascending=False)
Top_Spenders[["Purchase Count","Average Purchase Price","Total Purchase Value"]]

```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lisosia93</th>
      <td>5</td>
      <td>$3.79</td>
      <td>$18.96</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>4</td>
      <td>$3.86</td>
      <td>$15.45</td>
    </tr>
    <tr>
      <th>Chamjask73</th>
      <td>3</td>
      <td>$4.61</td>
      <td>$13.83</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>4</td>
      <td>$3.40</td>
      <td>$13.62</td>
    </tr>
    <tr>
      <th>Saistyphos30</th>
      <td>3</td>
      <td>$3.44</td>
      <td>$10.33</td>
    </tr>
  </tbody>
</table>
</div>



## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
Popular_Items_Analysis = purchase_data[["Item ID","Item Name","Price"]].groupby(["Item ID","Item Name"])
Popular_Items_Analysis_DF = pd.DataFrame(Popular_Items_Analysis.sum())
Popular_Items_Analysis_DF = Popular_Items_Analysis_DF.rename(columns = {"Price": "Total Purchase Value"})
Popular_Items_Analysis_DF["Purchase Count"] = Popular_Items_Analysis.count()
Popular_Items_Analysis_DF["Item Price"] = Popular_Items_Analysis_DF["Total Purchase Value"] / Popular_Items_Analysis_DF["Purchase Count"]


Display_DF = Popular_Items_Analysis_DF.sort_values("Purchase Count",ascending=False).head()
Display_DF[["Purchase Count","Item Price","Total Purchase Value"]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>108</th>
      <th>Extraction, Quickblade Of Trembling Hands</th>
      <td>9</td>
      <td>$3.53</td>
      <td>$31.77</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>19</th>
      <th>Pursuit, Cudgel of Necromancy</th>
      <td>8</td>
      <td>$1.02</td>
      <td>$8.16</td>
    </tr>
  </tbody>
</table>
</div>



## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame




```python
Display_DF = Popular_Items_Analysis_DF.sort_values("Total Purchase Value",ascending=False).head()
Display_DF[["Purchase Count","Item Price","Total Purchase Value"]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>92</th>
      <th>Final Critic</th>
      <td>8</td>
      <td>$4.88</td>
      <td>$39.04</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>8</td>
      <td>$4.35</td>
      <td>$34.80</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
