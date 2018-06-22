
Problem Statement:

I had to study and visualize the weather data from a randomly selected set of 500 cities. The parameters of visualization were -

* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude

Observations: (As of 6/20/2018)

1. One might assume that the hottest temperatures are at places on the equator or equatorial regions. However, the data suggests that the hottest temperatures are at placess slightly off the equator. On 6/20 - the highest temperature from a random sample of cities was recorded at Cuauhtemoc, MX which is situated at lat = 22.19 degrees N. However, the hotter temperatures are seen at places around the equator (N and S). Interestingly, Carhuaz in Peru being relatively closer to the equator reported the lowest temperature! The plot is shaped like a bell curve aligning with the theory that temperatures peak on/around equator and drops as we go farther away along N/S directions.

2. The plot between latitude and humidity indicates higher humidity % on and around the equator e.g. cities at 100 % humidity. The distrubution wasn't uniform. While the selection of cities was random, the distribution suggests more cities with higher humidity levels. The timing of the plot(6/20/2018) may be a factor as well - as heat waves are affecting many countries globally leading to record breaking temperatures.

3.The plot between latitude and cloudiness indicates low % of cloudiness for the data set - ~75 % of cities studied reported clear to partly cloudy skies.The timing of the plot(6/20/2018) may be a factor as well - as heat waves are affecting many countries globally leading to record breaking temperatures.

4.The plot between latitude and wind speed is interesting! The bulk of the cities studied reported low to medium wind speeds. The highest speed (31.09 MPH) was reported in Vestmanna, Faroe Islans. And islands experience stronger winds/windy conditions.



Outlined below are the steps that I followed to get to the output and observations (compiled above under Observations section)

Step 1 : 

I start by importing the libraries that I need to analyze and visualize the weather across the world at a varying distance from the equator.


Step 2: 

I create an empty dataframe with required columns to hold the values extracted from APIs from https://openweathermap.org/api. 

Columns - "City","Country","Latitude","Temperature","Humidity","Cloudiness","Wind Speed".


Step 3: 

I define a function to generate uniform and random sets of latitude and longitude.


Step 4: 

I use citipy library to pass the coordinates collected above and get the corresponding cities and country codes. I define the 

list of cities(Weather_Summary_Cities) randomly selected from the superset Weather_Summary.



Step 5: 

I define the base url -api.openweathermap.org/data/2.5/weather?q={city name},{country code} and pass city, country code to 

collect the attributes : "Temperature","Humidity","Cloudiness","Wind Speed". The objective is to perform a weather check on each 

city over the entire list using a series of successive API calls.

  

Step 6: 

I use data wrangling methods within pandas dataframe to make the data readable and presentable.


Step 7 :

I use seaborn libraries (lmplot) to plot the illustrate weather attributes vs Latitude.

City Latitude vs Max Temperature 

City Latitude vs Humidity 

City Latitude vs Cloudiness

City Latitude vs Wind Speed 


Also, I use pairplot from searborn library to look at the analysis in one canvas.

Step 8:

I saved the resulting data set and scatter plot images to Images and Resources folders respectively.

For questions on the problem statement or solution, please reach out to Supriya_Satpathy@outlook.com

