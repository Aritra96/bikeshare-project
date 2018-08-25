import time
import pandas as pd
import numpy as np

#Credits: Pandas Documentation was SUPER helpful when dealing with combining two columsn and applying functions like mode.
#Credits: Additionally, github repos of xhlow and philribbens were helpful in exploring different structures to the same problem statement.
#Credits: Udacity's 3 Problems in this project, namely user type, load data and popular hour, were immensely helpful.
#Credits: Final credit goes to my college classes, econometrics courses and professors and familiarity with R programming.

CITY_DATA = { 'chicago': 'chicago.csv', 'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv', 'New york city': 'new_york_city.csv',
              'new york city': 'new_york_city.csv', 'washington': 'washington.csv',
             'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    while city not in ['chicago', 'Chicago', 'new york city', 'New York City', 'New york city', 'washington', 'Washington']:
        print("\nWelcome to this program. Please choose your city:")
        print("\n1. Chicago 2. New York City 3. Washington")
        print("\nAccepted input:\nFull name of city in lowercase (e.g. chicago).\nFull name in title case (e.g. Chicago).")
        city = input()
        city = city.lower()
        if city not in ['chicago', 'Chicago', 'new york city', 'New York City', 'New york city', 'washington', 'Washington']:
            print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")
            print("\nRestarting...")

    print(f"\nYou have chosen {city} as your city.")

    month = ''
    while month not in {'january': 1, 'January': 1, 'february': 2, 'February': 2, 'march': 3, 'March': 3, 'april': 4, 'April': 4, 'may': 5, 'May': 5, 'june': 6, 'June': 6, 'all': 7, 'All': 7}.keys():
        print("\nPlease enter the month, between January to June, for which you're seeking data:")
        print("\nAccepted input:\nFull month name in lower case(e.g. january).\nFull month name in title case (e.g. April).")
        print("\n(You may also opt to view data for all months, please type 'all' or 'All' for that.)")
        month = input()
        month = month.lower()
        if month not in {'january': 1, 'January': 1, 'february': 2, 'February': 2, 'march': 3, 'March': 3, 'april': 4, 'April': 4, 'may': 5, 'May': 5, 'june': 6, 'June': 6, 'all': 7, 'All': 7}.keys():
            print("\nInvalid input. Please try again in the accepted input format.")
            print("\nRestarting...")
    print(f"\nYou have chosen {month} as your month.")

    day = ''
    while day not in ['all', 'All', 'monday', 'Monday', 'tuesday', 'Tuesday', 'wednesday', 'Wednesday', 'thursday', 'Thursday', 'friday', 'Friday', 'saturday', 'Saturday', 'sunday', 'Sunday']:
        print("\nPlease enter a day in the week of your choice for which you're seeking the data:")
        print("\nAccepted input:\nDay name in lowercase (e.g. monday).\nDay name in title case (e.g. Monday).")
        print("\n(You can also put 'all' or 'All' to view data for all days in a week.)")
        day = input()
        day = day.lower()
        if day not in ['all', 'All', 'monday', 'Monday', 'tuesday', 'Tuesday', 'wednesday', 'Wednesday', 'thursday', 'Thursday', 'friday', 'Friday', 'saturday', 'Saturday', 'sunday', 'Sunday']:
            print("\nInvalid input. Please try again in one of the accepted input formats.")
            print("\nRestarting...")
    print(f"\nYou have chosen {day} as your day.")
    print(f"\nYou have chosen to view data for city: {city}, month/s: {month} and day/s: {day}.")
    print('-'*100)
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
    #Load data for city
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    popular_month = df['month'].mode()[0]

    print('Most Popular Month (1 = January,...,6 = June):', popular_month)


    popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Day:', popular_day)

    # Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # Find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]

    print(f"The most commonly used start station: {common_start_station}")

    common_end_station = df['End Station'].mode()[0]

    print(f"The most commonly used end station: {common_end_station}")

    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print(f"The most frequent combination of trips are from {combo}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type = df['User Type'].value_counts()

    print(f"The types of users by number are given below:\n\n{user_type}")

    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\nThe most recent year of birth: {recent}\nThe most common year of birth:       {common_year}")
    except:
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city."""
    rdata = ''
    counter = 0
    while rdata not in ['yes', 'no', 'Yes', 'No']:
        print("\nDo you wish to view the raw data?")
        print("Accepted responses:\nYes or yes\nNo or no")
        rdata = input()
        rdata = rdata.lower()
        if rdata == "yes":
            print(df.head())
        elif rdata not in ['yes', 'no']:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    while True:
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input()
        rdata = rdata.lower()
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
