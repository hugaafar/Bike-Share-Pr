import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/home/hussam/Downloads/Bikeshare/chicago.csv',
              'new york city': '/home/hussam/Downloads/Bikeshare/new_york_city.csv',
              'washington': '/home/hussam/Downloads/Bikeshare/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nPlease choose City name by writing it from the following : Chicago, New York City, Washington.\n").lower()
        if city not in CITY_DATA:
            print("\nYour choice is invalid as it isn't from above cities, Please try again refering to prior mentioned choices.\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
          month = input("\nWhich month would you like to filter your data with? January, February, March, April, May, June or type 'all' if you would like to view the whole date range the month.\n").lower()
          if month not in months:
            print("Oops,the filter you used seems invalid, please try again refering to prior mentioned choices.")
            continue
          else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
          day = input("\nWhich day would you like to filter your data with? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you would like to view the whole date range for the week.\n").lower()
          if day not in days:
            print("Oops,the filter you used seems invalid, please try again refering to prior mentioned choices.")
            continue
          else:
            break
    print(city)
    print(month)
    print(day)
    print('-'*40)
    return city, month, day

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month)+1

    if day != 'all':
       df = df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().index[0]
    print("\nThe most common month from fitered data you selected is: {}\n".format(common_month))
    # TO DO: display the most common day of week
    common_day_week = df['day_of_week'].value_counts().index[0]
    print("\nThe most common day from fitered data you selected is: {}\n".format(common_day_week))

    # TO DO: display the most common start hour
    common_hour = df['hour'].value_counts().index[0]
    print('The most common start hour from fitered data you selected is: {}\n'.format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station is: {}\n".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station is: {}\n".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = (df['Start Station'] + ' along with ' + df['End Station']).mode()[0]
    print("\nThe most frequent combination of start station and end station trip is: {}\n".format(common_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_sec = df['Trip Duration'].sum()
    print("\nThe mean travel time is: {} 'seconds' / {}  'hours' ".format(total_travel_time_sec , round(total_travel_time_sec/3600,3)))

    # TO DO: display mean travel time
    mean_travel_time_sec = df['Trip Duration'].mean()
    print("\nThe mean travel time is: {} 'seconds' / {} 'hours' ".format(mean_travel_time_sec , round(mean_travel_time_sec/3600,3)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe count of user types from the data you filtered is: \n"+str(user_types))
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("\nThe count of gender from the data you filtered is:\n"+str(gender))
    else:
        print("\nOops, There is no gender information in this city\n")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birthdate = df['Birth Year'].min()
        most_common_birthdate = df['Birth Year'].mode()[0]
        most_recent_birthdate = df['Birth Year'].max()
        print('\nThe earliest user birthdate from the data you filtered is: {}\n'.format(earliest_birthdate))
        print('\nThe most recent user birthdate from the data you filtered is: {}\n'.format(most_recent_birthdate))
        print('\nThe most common user birthdate from the data you filtered is: {}\n'.format(most_common_birthdate))
    else:
        print("\nOops, There is no birth year information in this city\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Asks if the user would like to see some lines of data from the filtered dataset.
    Displays 5 (show_rows) lines, then asks if they would like to see 5 more.
    Continues asking until they say stop.
    """
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1

    print('\nWould you like to view 5 rows of raw data from the current filtered dataset?')
    while True:
        raw_data = input('\n(yes or no):  \n')
        if raw_data.lower() == 'yes':
            # display show_rows number of lines, but display to user starting from 1

            print('\n    Displaying below rows from {} to {}:'.format(rows_start + 1, rows_end + 1))
            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows


            print('\nWould you like to see the next {} rows?\n'.format(show_rows))
            continue
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to check another city or try different filters? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
