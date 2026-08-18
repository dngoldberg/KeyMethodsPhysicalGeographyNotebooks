import pandas as pd

flowdf = pd.read_csv('19006_gdf.csv')

import numpy as np

for year in np.arange(2001,2015):  # remember, 2015 will not be included
    # for each of years 2001 to 2014, we limit the dataframe to this year
    df_year = flowdf[flowdf.Date.str.contains(str(year))]
    # we now can save this data to its own .csv file
    df_year.to_csv('WoL_' + str(year) + '_flow.csv',index=False)
    
flowdf = pd.read_csv('19006_cdr.csv')
for year in np.arange(2001,2015):  # remember, 2015 will not be included
    # for each of years 2001 to 2014, we limit the dataframe to this year
    df_year = flowdf[flowdf.Date.str.contains(str(year))]
    # we now can save this data to its own .csv file
    df_year.to_csv('WoL_' + str(year) + '_rain.csv',index=False)    