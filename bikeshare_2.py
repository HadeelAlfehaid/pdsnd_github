import time
import pandas as pd
import numpy as np



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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def picked_city():
     while True:
        city=input('please spicfy which city you like to explore (chicago, new york city or washington)?').lower()
        if city in (CITY_DATA.keys()):
            return city
        else:
            print(city.title(), ' is not valid input, please shoese on of (chicago, new york city or washington')

    # get user input for month (all, january, february, ... , june)
    def get_month():
     while True:
        month=input('please spicfy the month you lile to explore (all, january, february, april, may, june , june)').lower()
        if month in ('all', 'january', 'february', 'april', 'may', 'june', 'june'):
            return month
        else:
            print ('invalid entry!! please enter a valid month (all, january, february, april, may, june , june')


   # get user input for day of week (all, monday, tuesday, ... sunday)
    def get_day():
      while True:
        day = input('please enter the day of week you woukd like to explore(all, monday, tuesday, ... sunday)').lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
          return day
        else:
          print ('please enter valid day(all, monday, tuesday, ... sunday)')
    city= picked_city()
    month = get_month()
    day= get_day()



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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    df['trip_combination'] = df['Start Station']+'_'+ df['End Station']
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        if day !='all':
          df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(common_month))


    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('The most common day of the week is {}'.format(common_day))


    # TO DO: display the most common start hour
    common_st_hour = df['start_hour'].mode()[0]
    print('The most common start hour is: ',common_st_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_Start_Station = df['Start Station'].mode()[0]
    print('The most common start station is: ',common_Start_Station)


    # TO DO: display most commonly used end station
    common_end_Station = df['End Station'].mode()[0]
    print('The most common end station is: ',common_end_Station)


    # TO DO: display most frequent combination of start station and end station trip
    common_trip_combination=df['trip_combination'].mode()[0]

    print('The most frequent combination of start station and end station trip is: ',common_trip_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is: ',df['Trip Duration'].sum())


    # TO DO: display mean travel time
    average_duration =  np.mean(df['Trip Duration'])
    print("average travel time:",average_duration)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usr_type_count = df['User Type'].value_counts()
    print('the counts of user types is: ', usr_type_count)

    if city !='washington':
        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('the counts of gender is: ', gender_count)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('the earliest year of birth is: ', int(np.amin(df['Birth Year'])))
        print('the recent year of birth is: ',
              int(np.max(df['Birth Year'])))
        print('the most common year of birth is: ', int(df['Birth Year'].mode()[0]))
    else:
        print ('gender & year of birth information are not avalible for selected city..')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    i=0
    while True:
            row_data_usr_input = input('Would you like to see 5 rows of the raw data ? Please enter "yes" or "no".').lower()
            if row_data_usr_input =='yes':
                #i=0
                print (df.iloc[i:i+5])
                i=i+5
                print_more_data = input('Would you like to see the next five raws? Please enter "yes" or "no": ').lower()
                if  print_more_data != 'yes':
                    break
            else:
                break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

#get user input if he want to restart the program again
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
