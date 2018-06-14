
Observations :

1. Percent Change in Tumor Volume at the end of treatment/45 days: Capomulin ~ 20 % reduction >> Infubinol ~47% increase >> Placebo 51% increase >> Ketapril 57% increase

2. Number of Mice Survived at the end of treatment/45 days: Capomulin 21 alive out of 25 ;  Placebo 11 alive out of 25; Ketapril 11 alive out of 25; Infubinol 9 alive out of 25

3. Metastatic spread at the end of treatment/45 days: Capomulin restricted to 3 sites ; Infubinol, Ketapril, and Placebo spread to 4 sites.

4. Capomulin demonstrates to be better cure for cancer than the other 3 drugs - Infubinol, Ketapril, and Placebo. The observation is based on reduction of tumor volume, the survival rate of mice, and fewer number of metastatic sites.


```python
# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
```


```python
# Read CSV
Clinical_Trial_Data = pd.read_csv("clinicaltrial_data.csv")
Mouse_Drug_Data = pd.read_csv("mouse_drug_data.csv")
```


```python
# Data Exploration - Clinical Trial
Clinical_Trial_Data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1893 entries, 0 to 1892
    Data columns (total 4 columns):
    Mouse ID              1893 non-null object
    Timepoint             1893 non-null int64
    Tumor Volume (mm3)    1893 non-null float64
    Metastatic Sites      1893 non-null int64
    dtypes: float64(1), int64(2), object(1)
    memory usage: 59.2+ KB
    


```python
# Data Exploration - Drug
Mouse_Drug_Data.info()
Mouse_Drug_Data["Drug"].value_counts()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 250 entries, 0 to 249
    Data columns (total 2 columns):
    Mouse ID    250 non-null object
    Drug        250 non-null object
    dtypes: object(2)
    memory usage: 4.0+ KB
    




    Placebo      25
    Stelasyn     25
    Zoniferol    25
    Ketapril     25
    Ramicane     25
    Capomulin    25
    Ceftamin     25
    Infubinol    25
    Naftisol     25
    Propriva     25
    Name: Drug, dtype: int64




```python
# Merge our two data frames together on Mouse ID
Clinical_Trial_Combined = pd.merge(Clinical_Trial_Data,Mouse_Drug_Data,on = "Mouse ID")
Clinical_Trial_Combined.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mouse ID</th>
      <th>Timepoint</th>
      <th>Tumor Volume (mm3)</th>
      <th>Metastatic Sites</th>
      <th>Drug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b128</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b128</td>
      <td>5</td>
      <td>45.651331</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b128</td>
      <td>10</td>
      <td>43.270852</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b128</td>
      <td>15</td>
      <td>43.784893</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b128</td>
      <td>20</td>
      <td>42.731552</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Data Exploration - Check if any value in dataframe has NULL
Clinical_Trial_Combined.isnull().sum().sum()
```




    0




```python
# Dataframe filtered with drugs to analyze - "Capomulin","Infubinol","Ketapril","Placebo"
Clinical_Trial_4Drugs = Clinical_Trial_Combined.loc[Clinical_Trial_Combined["Drug"].isin(["Capomulin","Infubinol","Ketapril","Placebo"])]
Clinical_Trial_4Drugs
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mouse ID</th>
      <th>Timepoint</th>
      <th>Tumor Volume (mm3)</th>
      <th>Metastatic Sites</th>
      <th>Drug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b128</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b128</td>
      <td>5</td>
      <td>45.651331</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b128</td>
      <td>10</td>
      <td>43.270852</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b128</td>
      <td>15</td>
      <td>43.784893</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b128</td>
      <td>20</td>
      <td>42.731552</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>5</th>
      <td>b128</td>
      <td>25</td>
      <td>43.262145</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>6</th>
      <td>b128</td>
      <td>30</td>
      <td>40.605335</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>7</th>
      <td>b128</td>
      <td>35</td>
      <td>37.967644</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>8</th>
      <td>b128</td>
      <td>40</td>
      <td>38.379726</td>
      <td>2</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>9</th>
      <td>b128</td>
      <td>45</td>
      <td>38.982878</td>
      <td>2</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>10</th>
      <td>f932</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>11</th>
      <td>g107</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>12</th>
      <td>g107</td>
      <td>5</td>
      <td>48.791665</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>13</th>
      <td>g107</td>
      <td>10</td>
      <td>53.435987</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>14</th>
      <td>g107</td>
      <td>15</td>
      <td>58.135545</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>15</th>
      <td>g107</td>
      <td>20</td>
      <td>62.706031</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>16</th>
      <td>g107</td>
      <td>25</td>
      <td>64.663626</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>17</th>
      <td>g107</td>
      <td>30</td>
      <td>69.160520</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>18</th>
      <td>g107</td>
      <td>35</td>
      <td>71.905117</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>19</th>
      <td>a457</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>20</th>
      <td>a457</td>
      <td>5</td>
      <td>47.462891</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>21</th>
      <td>a457</td>
      <td>10</td>
      <td>49.783419</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>22</th>
      <td>c819</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>23</th>
      <td>c819</td>
      <td>5</td>
      <td>45.769249</td>
      <td>1</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>24</th>
      <td>c819</td>
      <td>10</td>
      <td>46.658395</td>
      <td>1</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>25</th>
      <td>c819</td>
      <td>15</td>
      <td>48.370999</td>
      <td>1</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>26</th>
      <td>c819</td>
      <td>20</td>
      <td>49.762415</td>
      <td>1</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>27</th>
      <td>c819</td>
      <td>25</td>
      <td>51.828357</td>
      <td>1</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>28</th>
      <td>c819</td>
      <td>30</td>
      <td>56.098998</td>
      <td>1</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>29</th>
      <td>c819</td>
      <td>35</td>
      <td>57.729535</td>
      <td>1</td>
      <td>Ketapril</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1876</th>
      <td>i557</td>
      <td>25</td>
      <td>44.596219</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1877</th>
      <td>i557</td>
      <td>30</td>
      <td>45.261384</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1878</th>
      <td>i557</td>
      <td>35</td>
      <td>45.941949</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1879</th>
      <td>i557</td>
      <td>40</td>
      <td>46.821070</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1880</th>
      <td>i557</td>
      <td>45</td>
      <td>47.685963</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1881</th>
      <td>m957</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1882</th>
      <td>m957</td>
      <td>5</td>
      <td>45.622381</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1883</th>
      <td>m957</td>
      <td>10</td>
      <td>46.414518</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1884</th>
      <td>m957</td>
      <td>15</td>
      <td>39.804453</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1885</th>
      <td>m957</td>
      <td>20</td>
      <td>38.909349</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1886</th>
      <td>m957</td>
      <td>25</td>
      <td>37.695432</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1887</th>
      <td>m957</td>
      <td>30</td>
      <td>38.212479</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1888</th>
      <td>m957</td>
      <td>35</td>
      <td>32.562839</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1889</th>
      <td>m957</td>
      <td>40</td>
      <td>32.947615</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1890</th>
      <td>m957</td>
      <td>45</td>
      <td>33.329098</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1891</th>
      <td>f966</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1892</th>
      <td>f966</td>
      <td>5</td>
      <td>38.796474</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1893</th>
      <td>f966</td>
      <td>10</td>
      <td>35.624403</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1894</th>
      <td>f966</td>
      <td>15</td>
      <td>32.623003</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1895</th>
      <td>f966</td>
      <td>20</td>
      <td>30.485985</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1896</th>
      <td>m601</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1897</th>
      <td>m601</td>
      <td>5</td>
      <td>41.408591</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1898</th>
      <td>m601</td>
      <td>10</td>
      <td>36.825367</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1899</th>
      <td>m601</td>
      <td>15</td>
      <td>35.464612</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1900</th>
      <td>m601</td>
      <td>20</td>
      <td>34.255732</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1901</th>
      <td>m601</td>
      <td>25</td>
      <td>33.118756</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1902</th>
      <td>m601</td>
      <td>30</td>
      <td>31.758275</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1903</th>
      <td>m601</td>
      <td>35</td>
      <td>30.834357</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1904</th>
      <td>m601</td>
      <td>40</td>
      <td>31.378045</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
    <tr>
      <th>1905</th>
      <td>m601</td>
      <td>45</td>
      <td>28.430964</td>
      <td>1</td>
      <td>Capomulin</td>
    </tr>
  </tbody>
</table>
<p>777 rows × 5 columns</p>
</div>




```python
# Pivot table to calculate Tumor Volume across the spectrum of drugs vs time(days) for treatment
Time_vs_Volume_DF = pd.pivot_table(Clinical_Trial_Combined, values = "Tumor Volume (mm3)",
                                   index =["Timepoint"],columns =["Drug"])
Time_vs_Volume_DF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Ceftamin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Naftisol</th>
      <th>Placebo</th>
      <th>Propriva</th>
      <th>Ramicane</th>
      <th>Stelasyn</th>
      <th>Zoniferol</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>44.266086</td>
      <td>46.503051</td>
      <td>47.062001</td>
      <td>47.389175</td>
      <td>46.796098</td>
      <td>47.125589</td>
      <td>47.248967</td>
      <td>43.944859</td>
      <td>47.527452</td>
      <td>46.851818</td>
    </tr>
    <tr>
      <th>10</th>
      <td>43.084291</td>
      <td>48.285125</td>
      <td>49.403909</td>
      <td>49.582269</td>
      <td>48.694210</td>
      <td>49.423329</td>
      <td>49.101541</td>
      <td>42.531957</td>
      <td>49.463844</td>
      <td>48.689881</td>
    </tr>
    <tr>
      <th>15</th>
      <td>42.064317</td>
      <td>50.094055</td>
      <td>51.296397</td>
      <td>52.399974</td>
      <td>50.933018</td>
      <td>51.359742</td>
      <td>51.067318</td>
      <td>41.495061</td>
      <td>51.529409</td>
      <td>50.779059</td>
    </tr>
    <tr>
      <th>20</th>
      <td>40.716325</td>
      <td>52.157049</td>
      <td>53.197691</td>
      <td>54.920935</td>
      <td>53.644087</td>
      <td>54.364417</td>
      <td>53.346737</td>
      <td>40.238325</td>
      <td>54.067395</td>
      <td>53.170334</td>
    </tr>
    <tr>
      <th>25</th>
      <td>39.939528</td>
      <td>54.287674</td>
      <td>55.715252</td>
      <td>57.678982</td>
      <td>56.731968</td>
      <td>57.482574</td>
      <td>55.504138</td>
      <td>38.974300</td>
      <td>56.166123</td>
      <td>55.432935</td>
    </tr>
    <tr>
      <th>30</th>
      <td>38.769339</td>
      <td>56.769517</td>
      <td>58.299397</td>
      <td>60.994507</td>
      <td>59.559509</td>
      <td>59.809063</td>
      <td>58.196374</td>
      <td>38.703137</td>
      <td>59.826738</td>
      <td>57.713531</td>
    </tr>
    <tr>
      <th>35</th>
      <td>37.816839</td>
      <td>58.827548</td>
      <td>60.742461</td>
      <td>63.371686</td>
      <td>62.685087</td>
      <td>62.420615</td>
      <td>60.350199</td>
      <td>37.451996</td>
      <td>62.440699</td>
      <td>60.089372</td>
    </tr>
    <tr>
      <th>40</th>
      <td>36.958001</td>
      <td>61.467895</td>
      <td>63.162824</td>
      <td>66.068580</td>
      <td>65.600754</td>
      <td>65.052675</td>
      <td>63.045537</td>
      <td>36.574081</td>
      <td>65.356386</td>
      <td>62.916692</td>
    </tr>
    <tr>
      <th>45</th>
      <td>36.236114</td>
      <td>64.132421</td>
      <td>65.755562</td>
      <td>70.662958</td>
      <td>69.265506</td>
      <td>68.084082</td>
      <td>66.258529</td>
      <td>34.955595</td>
      <td>68.438310</td>
      <td>65.960888</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Scatter plot  for Tumor Volume vs Timepoint using seaborn libraries
sns.pointplot(x="Timepoint", y="Tumor Volume (mm3)", data=Clinical_Trial_4Drugs,hue='Drug',
              markers =["o","x","*","^"],linestyles=["--","--","--","--"])
plt.title("Tumor Response To Treatment")
plt.xlabel("Time(Days)")
plt.legend(loc="best")
plt.show()
```


![png](output_9_0.png)



```python
# A factor plot  for Tumor Volume vs Timepoint using seaborn libraries provides insightful visualization on a single frame
sns.factorplot(x="Timepoint", y="Tumor Volume (mm3)", 
               data=Clinical_Trial_4Drugs,hue='Drug',col="Drug",kind="swarm")
plt.show()
```


![png](output_10_0.png)



```python
# Scatter plot  for Metastatic Sites vs Timepoint using seaborn libraries

sns.pointplot(x="Timepoint", y="Metastatic Sites", data=Clinical_Trial_4Drugs,hue='Drug',
              markers =["o","x","*","^"],linestyles=["--","--","--","--"])
plt.title("Metastatic Spread During Treatment")
plt.xlabel("Treatment Duration(Days)")
plt.ylabel("Met. Sites")
plt.legend(loc="best")
plt.show()
```


![png](output_11_0.png)



```python
# A factor plot  for Tumor Volume vs Timepoint using seaborn libraries provides insightful visualization on a single frame
sns.factorplot(x="Timepoint", y="Metastatic Sites", data=Clinical_Trial_4Drugs,hue='Drug',col="Drug",kind="swarm")
plt.show()
```


![png](output_12_0.png)



```python
#Pivot table to track the number of mice alive along the course of treatment 0 to 45 days
Time_vs_Survival = pd.pivot_table(Clinical_Trial_4Drugs,index=["Timepoint"],
                                  values=["Mouse ID"],columns=["Drug"],aggfunc='count')
Time_vs_Survival
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">Mouse ID</th>
    </tr>
    <tr>
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Placebo</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>25</td>
      <td>25</td>
      <td>25</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25</td>
      <td>25</td>
      <td>23</td>
      <td>24</td>
    </tr>
    <tr>
      <th>10</th>
      <td>25</td>
      <td>21</td>
      <td>22</td>
      <td>24</td>
    </tr>
    <tr>
      <th>15</th>
      <td>24</td>
      <td>21</td>
      <td>19</td>
      <td>20</td>
    </tr>
    <tr>
      <th>20</th>
      <td>23</td>
      <td>20</td>
      <td>19</td>
      <td>19</td>
    </tr>
    <tr>
      <th>25</th>
      <td>22</td>
      <td>18</td>
      <td>19</td>
      <td>17</td>
    </tr>
    <tr>
      <th>30</th>
      <td>22</td>
      <td>17</td>
      <td>18</td>
      <td>15</td>
    </tr>
    <tr>
      <th>35</th>
      <td>22</td>
      <td>12</td>
      <td>17</td>
      <td>14</td>
    </tr>
    <tr>
      <th>40</th>
      <td>21</td>
      <td>10</td>
      <td>15</td>
      <td>12</td>
    </tr>
    <tr>
      <th>45</th>
      <td>21</td>
      <td>9</td>
      <td>11</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plot to indicate the number of mice alive along the course of treatment 0 to 45 days

sns.set()
Plot = Time_vs_Survival.plot()

# Plot Notation
plt.title("Survival During Treatment")
plt.ylabel('Number of mice')
plt.xlabel('Time(Days)')
plt.legend(loc="best")
plt.show()
```


![png](output_14_0.png)



```python
# Extract 4 unique drugs from the dataframe Clinical_Trial_4Drugs and store in a list

Drugs = list(Clinical_Trial_4Drugs["Drug"].unique());Drugs

Tumor_Vol_Change =[]

# Loop to calculate the percent change of tumor volume for each drug
for x in Drugs:
    P1 = Time_vs_Volume_DF[x][0]
    P2 = Time_vs_Volume_DF[x][45]
    Percent_Change = (P2 - P1)/P1 * 100
    Tumor_Vol_Change.append(Percent_Change) # append the percent change to an empty list
    
Tumor_Vol_Change
```




    [-19.475302667894155,
     57.028794686606041,
     46.123471727851843,
     51.297960483151527]




```python
# Bar Plot to show  % change in tumor volume for 4 drugs

x_axis = np.arange(len(Drugs))

Plot_Drug_Tumor_Vol = plt.bar(x_axis, Tumor_Vol_Change, color=["r","b","b","b"], align="center")

# Plot Notation

tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, Drugs)
plt.title("Tumor Change Over 45 Day Treatment")
plt.xlabel("Drug")
plt.ylabel("% Tumor Volume Change")
plt.show()

```


![png](output_16_0.png)



```python

```
