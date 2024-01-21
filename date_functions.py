import datetime
import requests

def get_data():
    #Call the API and verify a response
    response = requests.get("http://numbersapi.com/random/math")
    return response.text

def date_to_string(date):
    ''' Takes an argument date and converts it to the string version of the date'''
    return date.strftime("%Y-%m-%d")

def get_first_date_of_last_month():
    '''Returns the first day of the prior month'''
    today = datetime.date.today()
    first_date_of_this_month = today.replace(day=1)
    last_date_of_last_month = first_date_of_this_month - datetime.timedelta(days=1)
    first_date_of_last_month = last_date_of_last_month.replace(day=1)
    return first_date_of_last_month


def get_last_date_of_last_month():
    '''Returns the last day of the prior month'''
    today = datetime.date.today()
    first_date_of_this_month = today.replace(day=1)
    last_date_of_last_month = first_date_of_this_month - datetime.timedelta(days=1)
    return last_date_of_last_month


def get_last_date_of_last_month():
    last_day_of_prior_month = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    return last_day_of_prior_month


def get_start_and_end_date():
    start_date = get_first_date_of_last_month()
    end_date = get_last_date_of_last_month()
    return date_to_string(start_date), date_to_string(end_date)

toDate = date_to_string(get_last_date_of_last_month())
print(toDate)

get_start_and_end_date()

start_date = get_first_date_of_last_month()
end_date = get_last_date_of_last_month()
new_start_date = get_last_date_of_last_month() + datetime.timedelta(days=1)
print(start_date, end_date, new_start_date)


new_start_date = datetime.date(2023, 3, 1) #get_last_date_of_last_month() + datetime.timedelta(days=1)
end_date = datetime.date(2023, 3, 30) #get_last_date_of_last_month()
if new_start_date < end_date:
    print("run script")
else:
    print("do not run script")

#What happens on May 1 - this will not run until the new_start_date is less than the end date
#What happens on M
new_start_date = datetime.date(2023, 4, 1) #get_last_date_of_last_month() + datetime.timedelta(days=1)
end_date = datetime.date(2023, 3, 31) #get_last_date_of_last_month()
if new_start_date < end_date:
    print("run script")
else:
    print("do not run script")

import datetime

def run_etl():
    today = datetime.date.today()
    if today.day <= 7:
        # Your ETL code here
        print("Running ETL process...")
    else:
        print("Current date is not within the first 7 days of the month. ETL process won't run.")
run_etl()

import datetime

def run_etl(get_last_date_of_last_month):
    today = datetime.date.today()
    if today.day <= 7 and get_last_date_of_last_month < today.replace(day=1):
        # Your ETL code here
        text_response = get_data()
        #print("Running ETL process...")
        return text_response

    else:
        return "Current date is not within the first 7 days of the month, or the last day of the prior month is after the first day of the current month. ETL process won't run."
run_etl(get_last_date_of_last_month)


def run_etl():
    today = datetime.date(2024,5,1)
    if today.day <= 7:
        # Your ETL code here
        text_response = get_data()
        print("Running ETL process...")
        return text_response
    else:
        print("Current date is not within the first 7 days of the month. ETL process won't run.")
run_etl()

last_day_of_prior_month = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
run_etl(last_day_of_prior_month)

