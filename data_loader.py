# data_lodaer.py
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading the data
    city_data_file = CITY_DATA[city]
    city_data_frame = pd.read_csv(city_data_file)
    
    #changing 'Start Time' column data type
    city_data_frame['Start Time'] = pd.to_datetime(city_data_frame['Start Time'])
                                                   
    #extracting the month and day
    city_data_frame['month'] = city_data_frame['Start Time'].dt.month
    city_data_frame['day'] = city_data_frame['Start Time'].dt.day_name()
    
    #applying filters
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month_number = months.index(month) + 1
       city_data_frame = city_data_frame[city_data_frame['month'] == month_number]
    
    if day != 'all':
       city_data_frame = city_data_frame[city_data_frame['day'] == day.title()]

    return city_data_frame