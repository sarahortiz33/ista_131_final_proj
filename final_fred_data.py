import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def reserves_15_years():
    """
    This function creates a scatter plot with a regression line using the data
    from 2007 to 2022.

    return: Nothing is returned by this function as it creates a plot.
    """
    df = pd.read_csv('TOTRESNS.csv', index_col=0)

    # Changes the dates from the x-axis into datetime objects
    dt_index = []
    for i in df.index:
        date_splt = i.split('-')
        dt_index.append(datetime(int((date_splt[0])), int(date_splt[1]),
                                 int(date_splt[2])))

    x_temp = []
    count = 0

    # Loops through the datetime object list of the index of the DataFrame and
    # appends the year plus the month divided by 12 to a list that will be used
    # for the regression
    for i in range(len(dt_index)):
        if dt_index[i].year >= 2007:
            yr = float(dt_index[i].year)
            mon = float(dt_index[i].month)
            dec = mon / 12
            ans = yr + dec
            x_temp.append(ans)
        if dt_index[i].year == 2007 and count == 0:
            count += i

    # Declares x and y values for the plot so the linear regression line can be
    # calculated
    x = np.array(x_temp)
    new_vals = df.values[count:]
    y = np.array([n for n in new_vals.astype(float)])
    m, b = np.polyfit(x, y, 1)

    # Plots the figure
    plt.figure(facecolor='#c7ebcc')
    plt.plot(x, y, "o", color='g')
    plt.plot(x, m*x+b)
    plt.xlabel('Time in Years', fontsize=15)
    plt.xticks([num for num in range(2007, 2023)], fontsize=13)
    plt.xlim(2007, 2023)
    plt.ylabel('Money in Billions', fontsize=20)
    plt.title('Amount of Money in Reserves', fontsize=25)


def max_min_recession():
    """
    This function gets all instances of a recession from the MBCURRCIR.csv file
    and finds the most amount of money that was in circulation at the time, as
    well as the least amount of money. These are then plotted.

    return: Nothing is returned by this function as it creates a plot.
    """
    df = pd.read_csv('MBCURRCIR.csv', index_col=0, header=0)

    # Finds the least amount of money in circulation for each recession period
    r1_mini = min(df.loc['1960-04-01':'1961-02-01', 'MBCURRCIR'])
    r2_mini = min(df.loc['1969-12-01':'1970-11-01', 'MBCURRCIR'])
    r3_mini = min(df.loc['1973-11-01':'1975-03-01', 'MBCURRCIR'])
    r4_mini = min(df.loc['1980-01-01':'1980-07-01', 'MBCURRCIR'])
    r5_mini = min(df.loc['1981-07-01':'1982-11-01', 'MBCURRCIR'])
    r6_mini = min(df.loc['1990-07-01':'1991-03-01', 'MBCURRCIR'])
    r7_mini = min(df.loc['2001-03-01':'2001-11-01', 'MBCURRCIR'])
    r8_mini = min(df.loc['2007-12-01':'2009-06-01', 'MBCURRCIR'])
    r9_mini = min(df.loc['2020-02-01':'2020-04-01', 'MBCURRCIR'])

    # Finds the most amount of money in circulation for each recession period
    r1_max = max(df.loc['1960-04-01':'1961-02-01', 'MBCURRCIR'])
    r2_max = max(df.loc['1969-12-01':'1970-11-01', 'MBCURRCIR'])
    r3_max = max(df.loc['1973-11-01':'1975-03-01', 'MBCURRCIR'])
    r4_max = max(df.loc['1980-01-01':'1980-07-01', 'MBCURRCIR'])
    r5_max = max(df.loc['1981-07-01':'1982-11-01', 'MBCURRCIR'])
    r6_max = max(df.loc['1990-07-01':'1991-03-01', 'MBCURRCIR'])
    r7_max = max(df.loc['2001-03-01':'2001-11-01', 'MBCURRCIR'])
    r8_max = max(df.loc['2007-12-01':'2009-06-01', 'MBCURRCIR'])
    r9_max = max(df.loc['2020-02-01':'2020-04-01', 'MBCURRCIR'])

    width = .4
    bars1 = [r1_max, r2_max, r3_max, r4_max, r5_max, r6_max, r7_max, r8_max,
             r9_max]
    bars2 = [r1_mini, r2_mini, r3_mini, r4_mini, r5_mini, r6_mini, r7_mini,
             r8_mini, r9_mini]

    r1 = np.arange(len(bars1))
    r2 = [x + width for x in r1]

    bil_bars1 = [b/1000 for b in bars1]
    bil_bars2 = [b/1000 for b in bars2]

    # Creates each of the graphs
    plt.figure(facecolor='#c7ebcc')
    plt.bar(r1, bil_bars1, color='g', width=width, edgecolor='white',
            label='Maximum')
    plt.bar(r2, bil_bars2, color='b', width=width, edgecolor='white',
            label='Minimum')

    x_ticks = ['Apr 1960-Feb 1961', 'Dec 1969-Nov 1970', 'Nov 1973-Mar 1975',
               'Jan 1980-Jul 1980', 'Jul 1981-Nov 1982', 'Jul 1990-Mar 1991',
               'Mar 2001-Nov 2001', 'Dec 2007-Jun 2009', 'Feb 2020-Apr 2020']
    y_ticks = [i for i in range(30, 1900, 100)]

    # Adds in the x-label and the tick marks for the x-axis
    plt.title('Most and Least Amount of Money in Circulation during Recession',
              fontsize=20)
    plt.xlabel('Recession timeframe', fontsize=15)
    plt.xticks([r + width for r in range(9)], x_ticks, fontsize=8)
    plt.ylabel('Money in Circulation (in billions)', fontsize=15)
    plt.yticks(y_ticks, fontsize=10)
    plt.legend()


def mean_all_years():
    """
    This function plots a graph that shows the mean of the data for each year
    in the dataset, excluding the year 2023.

    return: Nothing is returned by this function as it creates a plot.
    """
    df = pd.read_csv('MBCURRCIR.csv', index_col=0, header=0)

    cur = []
    data = []

    # Loops through the data so that the mean amount of money from each year
    # can be calculated
    for i in df.index:
        for j in df.columns:
            if i[5:7] != '12' and i[:4] != '2023':
                cur.append(df.loc[i, j])
            elif i[5:7] == '12' and i[:4] != '2023':
                cur.append(df.loc[i, j])
                data.append(sum(cur) / len(cur))
                cur = []

    dates = [n for n in range(1959, 2023)]
    bil_data = [b / 1000 for b in data]

    # Adds labels to figure and formats it
    plt.figure(facecolor='#c7ebcc')
    plt.plot(dates, bil_data, color='g')
    plt.xlabel('Time in Years', fontsize=15)
    plt.ylabel('Money in Circulation (in billions)', fontsize=20)
    plt.title('Mean Amount of Money for each Year (excluding 2023)',
              fontsize=25)
    y_ticks = [i for i in range(30, 2300, 100)]
    plt.yticks(y_ticks)
    plt.xlim(1959)


def main():
    reserves_15_years()
    max_min_recession()
    mean_all_years()
    plt.show()


if __name__ == '__main__':
    main()
