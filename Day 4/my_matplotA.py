#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""


from matplotlib import pyplot as plt
import pandas as pd




def first_matplotlib():
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.xlabel('this is the x label')
    plt.ylabel('this is the y label')
    plt.title('my first plot')
    plt.show()

def first_pandas():
    data = {'year': [2008, 2012, 2016],
            'attendess':[112, 321, 729],
            'average age': [24, 43, 31]}
    df = pd.DataFrame(data)
    print(df)

    print(df['year'])
    print(type(df['year']))
    # earlier_than_2013 = df['year'] < 2013
    plt.plot(df['year'], df['attendees'])
    plt.plot(df['year'], df['average age'])
    plt.legend(['attendees', 'average age'])
    plt.show()

def import_data_pandas():
    data = pd.read_csv('countries.csv')
    print(data.head())
    print(f'total of {len(set(data.country))} unique countries')
    afghanistan = data[data.country == 'Afghanistan']
    plt.plot(afghanistan.year, afghanistan.gdpPerCapital)
    plt.title("Afghanistan's GDP Per Capita")
    plt.show()

    def continent_data(data):

    # compare asia and europe's GDP per capita
    continents = set(data.continent)
    print(continents)
    data_2007 = data[data.year == 2007]
    asia_2007 = data_2007[data_2007.continent == 'Asia']
    europe_2007 = data_2007[data_2007.continent == 'Europe']

    print(f'Asia countries: {len(set(asia_2007.country))}')
    print(f'Europe countries: {len(set(europe_2007.country))}')
    # get mean and median
    print(f'Mean GDP in Asia {asia_2007.gdpPerCapita.mean()}')
    print(f'Median GDP in Asia {asia_2007.gdpPerCapita.median()}')
    print(f'Mean GDP in Europe {europe_2007.gdpPerCapita.mean()}')
    print(f'Median GDP in Europe {europe_2007.gdpPerCapita.median()}')

    #make subplots
    plt.subplot(2, 1, 1)
    plt.title('Distribution of GDP Per Capita')
    plt.hist(asia_2007.gdpPerCapita, 20, range=(0, 5000), edgecolor='black')
    plt.ylabel('Asia')
    plt.subplot(2, 1, 2)
    plt.hist(europe_2007.gdpPerCapita, 20, range=(0, 5000), edgecolor='black')
    plt.ylabel('Europe')
    plt.show()

def continent_data_le(data):
    """compare the life expectancy between
    europe and america in 1997"""
    life = set(data.LifeExpectancy)
    print(LifeExpectancy)
    data_1997 = data[data.year == 1997]
    americas_1997 = data_1997[data_1977.LifeExpectancy == 'America']
    europe_1997 = data_1997[data_1977.LifeExpectancy == 'Europe']

    print(f'America countries: {len(set(americas_1997.country))}')
    print(f'Europe countries: {len(set(europe_1997.country))}')
    # get mean and median
    print(f'Mean LE in Asia {americas_1997.LifeExpectancy.mean()}')
    print(f'Median LE in Asia {americas_1997.LifeExpectancy.median()}')
    print(f'Mean LE in Europe {europe_1997.LifeExpectancy.mean()}')
    print(f'Median LE in Europe {europe_1997.LifeExpectancy.median()}')

    plt.subplot(2, 1, 1)
    plt.title('Life Expectancy')
    plt.hist(america_1997.LifeExpectancy, 20, range=(0, 5000), edgecolor='black')
    plt.ylabel('America')
    plt.subplot(2, 1, 2)
    plt.hist(europe_1997.LifeExpectancy, 20, range=(0, 5000), edgecolor='black')
    plt.ylabel('Europe')
    plt.show()

def continent_data_gdp_growth(data):
    usa = data[data.country == 'United States']
    china = data[data.country == 'China']
    usa_growth = usa.gdpPerCapita / usa.gdpPerCapita.iloc[0]*100
    china_growth = china.gdpPerCapita / china.gdpPerCapita.iloc[0]*100

    plt.title('GDP per Capita Growth (first year = 100)')
    plt.plot(usa.year, usa_growth)
    plt.plot(china.year, china_growth)
    plt.legend(['United States', 'China'])



    plt.plot(usa.year, usa.gdpPerCapita)
    plt.plot(china.year, china.gdpPerCapita)

    plt.legend(['United States', 'China'])
    plt.xlabel('year')
    plt.ylabel('GDP')
    plt.show()


# --------------------------------------------------
def main():
    """Make your noise here"""
    # import_data_pandas()
    data = pd.read_csv('countries.csv')
    continent_data_gdp_growth(data)









# --------------------------------------------------
if __name__ == '__main__':
    main()
