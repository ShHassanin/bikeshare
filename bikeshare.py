import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['January' , 'Febreuary' , 'March' , 'April' , 'May' , 'June' , 'All']
days = ['Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday' , 'All']



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
        city=input('Choose a city from these cities: chicago, new york city, washington : ')
        city=city.lower()
        
        if city not in CITY_DATA:
                                print('\n City not found, please enter a city from these cities: chicago, new york city, washington : ')
                                continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
        
    while True:
        month = input('choose one of these months:January , Febreuary , March , April , May , June , or choose All to explore all months : ')
        month = month.title()
        if month not in months:
                print('\n Month not found, please enter a valid month . ')
                continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        
        day = input('Choose one of days of the week:Monday , Tuesday , Wednesday , Thursday , Friday , Saturday , Sunday , or choose All to explore all the days of the week : ')
        day = day.title()
        if day not in days:
                print('\n Day not found , please enter a valid day of the week.')
                continue
        else:
            break

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
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    """get the day and month from the date"""
    df['month']= df['Start Time'].dt.month
    df['day'] =df['Start Time'].dt.day_name()
    """load the data"""
    
    if month != 'All':
        #convert the name of the months to numbers
        month = months.index(month) +1

        #filter by month
        df = df[df['month']==month]
    
    if day != 'All':
        #filter by day
        df =df[df['day']==day]
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_common = df['month'].mode()[0]
    print('The most common month is:{}'.format(months[month_common-1]))

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('The most common day of week is:{}'.format(common_day))


    # TO DO: display the most common start hour
    df['start hour'] = df['Start Time'].dt.hour
    common_start_hour=df['start hour'].mode()[0]
    print('The most common start hour is:{}'.format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:{}'.format(common_start_station))
          
    # TO DO: display most commonly used end station       
    common_end = df['End Station'].mode()[0]
    print('The most commonly used end station is:{}'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = (df['Start Station'] + " to " + df['End Station'])
          
    common_trip = df['Trip'].mode()[0]
          
    print('The most frequent combination of start station and end station trip is:{}'.format(common_trip ))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is : {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is : {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('The counts of user types is:\n {}'.format(counts_of_user_types))

    # TO DO: Display counts of gender
    if city != 'washington' :
        counts_of_gender = df['Gender'].value_counts()
        print('The counts of gender is :\n {}'.format(counts_of_gender))
                          
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('The earliest birth is : {} \n The most recent birth is : {} \n The most common year of birth is : {}'.format(earliest,most_recent,most_common_year_of_birth))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    
    display = input('\n would you like to display 5 rows of the filtered data? (yes/no) \n').lower()
    i=0
    
    while display == 'yes':
        try:
           if display == 'yes':
                print(df.iloc[i:i+5])
                i = i+5  
                display =input('\n would you like to display another 5 rows of the filtered data? (yes/no) \n').lower()
                continue
        except display == 'no':
            break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
