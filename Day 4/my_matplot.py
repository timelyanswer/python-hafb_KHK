#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose: test matplotlib, and pandas
"""

from matplotlib import pyplot as plt


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



# --------------------------------------------------

def main():

    import_data_pandas()







# --------------------------------------------------
if __name__ == '__main__':
    main()
