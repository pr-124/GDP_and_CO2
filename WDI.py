import pandas as pd
import matplotlib.pyplot as plt
wdi = pd.read_csv(
    'https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')

wdi.head()
mortality = wdi['Mortality rate, infant (per 1,000 live births)']git
GDP = wdi['GDP per capita (constant 2010 US$)']
country = wdi['Country Name']
plt.plot(GDP, mortality)

plt.xlabel('GDP per capita (constant 2010 US$)')
plt.ylabel('Mortality rate, infant (per 1,000 live births)')
plt.title('Mortality rate vs. GDP per capita')
plt.show()

# GDP per capita vs. Mortality rate, infant (per 1,000 live births)
