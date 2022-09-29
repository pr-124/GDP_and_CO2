import pandas as pd
import matplotlib.pyplot  as plt
wdi = pd.read_csv('https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')
wdi.head()
mortality = wdi['Mortality rate, infant (per 1,000 live births)']
GDP = wdi['GDP per capita (constant 2010 US$)']
country = wdi['Country Name']
plt.plot(GDP, mortality)