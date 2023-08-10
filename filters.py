# filters.py
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose which city you would like to see analyzed (Chicago, New York City, Washington)\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name! Please choose a valid city name: (Chicago, New York City, Washington)\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose a month to filter on or 'All' for no filter\n").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid month! Please choose a valid month: (January, February, March, April, May, June, All)\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Choose a day to filter on or 'All' for no filter\n").lower()
        if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            break
        else:
            print("Invalid day! Please choose a valid day\n")

    print('-'*40)
    return city, month, day