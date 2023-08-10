# stats.py
import time
import pandas as pd


def time_stats(city_data_frame):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month_count = city_data_frame['month'].value_counts()
    most_common_month = most_common_month_count.idxmax()
    print("The most frequent month is: {},  Count: {}\n".format(most_common_month, most_common_month_count[most_common_month]))

    # TO DO: display the most common day of week
    most_common_day_count = city_data_frame['day'].value_counts()
    most_common_day = most_common_day_count.idxmax()
    print("The most frequent day is: {},  Count: {}\n".format(most_common_day, most_common_day_count[most_common_day]))

    # TO DO: display the most common start hour
    city_data_frame['hour'] = city_data_frame['Start Time'].dt.hour
    most_common_hour_count = city_data_frame['hour'].value_counts()
    most_common_hour = most_common_hour_count.idxmax()
    print("The most frequent hour is: {},  Count: {}\n".format(most_common_hour, most_common_hour_count[most_common_hour]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(city_data_frame):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_sstation_count = city_data_frame['Start Station'].value_counts()
    most_common_sstation = most_common_sstation_count.idxmax()
    most_common_sstation_max = most_common_sstation_count.max()
    print("The most used Start staion is:\n{},  Count: {}\n".format(most_common_sstation, most_common_sstation_max))

    # TO DO: display most commonly used end station
    most_common_estation_count = city_data_frame['End Station'].value_counts()
    most_common_estation = most_common_estation_count.idxmax()
    most_common_estation_max = most_common_estation_count.max()
    print("The most used End staion is:\n{},  Count: {}\n".format(most_common_estation, most_common_estation_max))

    # TO DO: display most frequent combination of start station and end station trip
    city_data_frame['Trip'] = city_data_frame['Start Station'] + " --> " + city_data_frame['End Station']
    most_common_trip_count = city_data_frame['Trip'].value_counts()
    most_common_trip = most_common_trip_count.idxmax()
    most_common_trip_max = most_common_trip_count.max()
    print("The most frequent trip is:\n{}, Count: {}\n".format(most_common_trip, most_common_trip_max))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(city_data_frame):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = city_data_frame['Trip Duration'].sum()
    print("Total trip duration: {}\n".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = city_data_frame['Trip Duration'].mean()
    print("Average duration: {}\n".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city_data_frame):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = city_data_frame['User Type'].value_counts()
    print("User types count:\n", user_type_count)

    # TO DO: Display counts of gender if available in the data
    if 'Gender' in city_data_frame.columns and 'Birth Year' in city_data_frame.columns:
        gender_count = city_data_frame['Gender'].value_counts()
        NaN_count = city_data_frame['Gender'].isna().sum()
        print("Users' gender count:\n{}, \nUnkown users gender: {}".format(gender_count, NaN_count))

    # TO DO: Display earliest, most recent, and most common year of birth if available
        earliest_birth_year = city_data_frame['Birth Year'].min()
        latest_birth_year = city_data_frame['Birth Year'].max()
        common_birth_year = city_data_frame['Birth Year'].value_counts().idxmax()
        print("Earliest birth year: {}\n Latest birth year: {}\n Most common birth year: {}\n".format(int(earliest_birth_year), int(latest_birth_year), int(common_birth_year)))
    else:
        print("\nGender and Birth Year data are not available for this city!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(city_data_frame):
    """Displays 5 lines of the data set upon the user's request"""
    #to display all columns
    pd.set_option("display.max_columns", 200)
    start_index = 0
    while True:
        answer = input("\nWould you like to see 5 lines of the raw data set? ('Yes' or 'No')\n").lower()
        if answer == 'yes':
            print(city_data_frame.iloc[start_index : start_index + 5])
            start_index += 5
        elif answer == 'no':
            break
        else:
            print("Invalid answer! Please enter either ('Yes' or 'No').")