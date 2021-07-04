# Surfs Up
# Project Overview
Our assignment is to perform data analysis and data exploration on a weather dataset from the island of Oahu to determine if opening a surf shop is worth our time.

## Challenge Overview
After calculating some statistics on the precipitation and temperatures throughout the previous year, we generate the summary statistics of the temperatures for the months of June and December. 

## Resources
- Data Source: hawaii.sqlite
- Software: Python 3.7.6, SQLite, SQLAlchemy, Flask.

## June and December Temperatures Analysis Results
Below are the summary statistics for the June and December temperature data: 

  ![June Temperature Statistics](https://github.com/nhipqnguyen/surfs_up/blob/main/Data/june_temps.png)
  
  ![December Temperature Statistics](https://github.com/nhipqnguyen/surfs_up/blob/main/Data/december_temps.png)

- The average temperature in June is about 5 degrees higher than that in December (75 and 71, respectively).
- While we don't observe a big difference between the highest temperatures in June and December (85 and 83, respectively), the coldest day in December is significantly colder than that in June (56 and 64, respectively).
- The ways temperatures are spread out in both sets are not much different. The temperatures in both months are quite normally distributed. The means are equal to the median (50th percentile), the 25th percentiles are approximately 1 standard deviation lower than the means, and the 75th percentiles are approximately 1 standard deviation higher than the means.

## June and December Temperatures Analysis Summary
- Looking at the above statistics, we can see that in the summer (June) and winter (December), the weather in Oahu does change slightly but not to the point that it will significantly affect our surf and ice cream business. Most days in June are in the 75-80 range and most days in December will be in the 70-75 range, which could be considered good temperatures for surfing. With that range of temperature in June, we could sell more ice cream, and in December we might be able to increase sales on spring suit rentals.
- Below are the statistics for the precipitation for the months of June and December:

  ![June Precipitation Statistics](https://github.com/nhipqnguyen/surfs_up/blob/main/Data/june_prcp.png)
  
  ![December Precipitation Statistics](https://github.com/nhipqnguyen/surfs_up/blob/main/Data/dec_prcp.png)

- We can see that in December it rains a little more than June but the differene is not significant. 75% of June days' precipitation is less than 0.12 and that number in December is less than 0.15, which should not have a big impact on our surfing and ice cream sales.
- In general, our surf and ice cream shop business is sustainable year-round in the island of Oahu.

