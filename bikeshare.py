import time
import pandas as pd
import numpy as np
from filters import get_filters
from data_loader import load_data
from stats import time_stats, station_stats, trip_duration_stats, user_stats, raw_data

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    
def main():
    while True:
        city, month, day = get_filters()
        city_data_frame = load_data(city, month, day)

        time_stats(city_data_frame)
        station_stats(city_data_frame)
        trip_duration_stats(city_data_frame)
        user_stats(city_data_frame)
        raw_data(city_data_frame)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
