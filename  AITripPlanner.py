import re
from openai import OpenAI
from serpapi import GoogleSearch
import requests
from datetime import datetime
import json
from dotenv import load_dotenv
import os
import FlightSearcher
import HotelSearcher
import ChatGPTFetcher
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def get_trip_details():
    start_date = input("Enter the start date of your trip (YYYY-MM-DD): ")
    end_date = input("Enter the end date of your trip (YYYY-MM-DD): ")
    budget = int(input("Enter your total budget in USD: "))
    trip_type = input("Enter the type of trip (ski/beach/city): ")

    return start_date, end_date, budget, trip_type

def parse_destinations(possible_destinations):
    # Split the response by newline character to get individual lines
    lines = possible_destinations.strip().split('\n')
    cities = []
    destinations = []
    airports = []

    # Iterate over each line and extract city, destination, airport, and alternative airport
    for line in lines:
        city_start_index = line.find('City: ') + len('City: ')
        city_end_index = line.find(', Destination: ')
        city_with_info = line[city_start_index:city_end_index].strip()

        # Strip additional information from the city
        city_parts = city_with_info.split(',')
        city = city_parts[0].strip()

        destination_start_index = line.find('Destination: ') + len('Destination: ')
        destination_end_index = line.find(', Airport: ')
        destination = line[destination_start_index:destination_end_index].strip()

        airport_start_index = line.find('Airport: ') + len('Airport: ')
        airport = line[airport_start_index:].strip()

        cities.append(city)
        destinations.append(destination)
        airports.append(airport)

    # Print the extracted cities, destinations, airports, and alternative airports
    for city, destination, airport in zip(cities, destinations, airports):
        print(f"City: {city}, Destination: {destination}, Airport: {airport}")

    return cities, destinations, airports

def parse_trip_plan(trip_plan):
    # Split the trip plan into individual days
    days = trip_plan.strip().split('\n\n')
    parsed_plan = []

    try:
        # Regular expression to match the day, date, and activities
        day_pattern = re.compile(r'Day (\d+|Last Day) \((\d{4}-\d{2}-\d{2})\):')
        activity_pattern = re.compile(r'- (Morning|Afternoon|Evening): (.+)')

        for day in days:
            lines = day.strip().split('\n')
            day_info = {}
            
            day_match = day_pattern.match(lines[0])
            if day_match:
                day_info['day'] = 'Last Day' if day_match.group(1) == 'Last Day' else int(day_match.group(1))
                day_info['date'] = day_match.group(2)
                day_info['activities'] = {'Morning': '', 'Afternoon': '', 'Evening': ''}
            
            for line in lines[1:]:
                activity_match = activity_pattern.match(line.strip())
                if activity_match:
                    period = activity_match.group(1)
                    activity = activity_match.group(2)
                    day_info['activities'][period] = activity
                    
            if 'date' in day_info:
                parsed_plan.append(day_info)

    except Exception as e:
        print("Error parsing the trip plan:", e)
    return parsed_plan

def display_options(hotels, destinations, going_flights_info, returning_flights_info, budgets):
    for idx, destination in enumerate(destinations):
        print(f"Option {idx + 1}: {going_flights_info[idx]} - {returning_flights_info[idx]}- {hotels[destination]} - {hotels[destination]['name']} - ${hotels[destination]['price']} - {budgets[idx]}")

    choice = int(input("Choose a destination (1-5): ")) - 1
    chosen_option = hotels[destinations[choice]]
    chosen_option['destination'] = destinations[choice]
    chosen_option['going_flight'] = going_flights_info[choice]
    chosen_option['returning_flight'] = returning_flights_info[choice]
    chosen_option['price'] = budgets[choice]

    return chosen_option

def print_flights_state(going_flights_info, returning_flights_info, serapi_tries):
    print('-' * 50)

    # Extract sublists for going and returning flight information
    going_info = going_flights_info[0]
    returning_info = returning_flights_info[0]

    # Print going flight information
    print("Going flight information, amount:", len(going_info))
    print(going_flights_info)

    print('#' * 50)

    # Print returning flight information
    print("Returning flight information, amount:", len(returning_info))
    print(returning_flights_info)

    print('-' * 50)

    # Print missing destinations and try number
    print('*' * 50)
    print("Missing destinations:", 5 - len(going_info))
    print("Try number:", serapi_tries)
    print('*' * 50)


def main():
    # start_date, end_date, budget, trip_type = get_trip_details()
    start_date, end_date, budget, trip_type = '2024-08-01', '2024-08-10', 10000, 'city'
    
    # possible_destinations = []
    # budgets = [budget] * 5
    # total_costs = [0] * 5

    # going_flights_info = []
    # returning_flights_info = []
    # destinations_with_flights = []
    
    # serapi_tries = 0
    # number_of_missing_destinations = 5
    # chosen_cities = []
   
    # while number_of_missing_destinations > 0 and serapi_tries < 1:
    #     possible_destinations = ChatGPTFetcher.get_possible_destinations(start_date, end_date, trip_type, number_of_missing_destinations, chosen_cities)
    #     cities, destinations, airport_codes = parse_destinations(possible_destinations)
        
    #     added_going_flights_info, added_returning_flights_info, chosen_cities, flight_prices, destinations_with_flights = FlightSearcher.get_flights(cities, airport_codes, start_date, end_date, budgets, destinations)
    #     going_flights_info.append(added_going_flights_info)
    #     returning_flights_info.append(added_returning_flights_info)

    #     print_flights_state(going_flights_info, returning_flights_info, serapi_tries)
    #     number_of_missing_destinations -= len(going_flights_info[0])

    #     serapi_tries += 1
    
    # new_budgets = []
    # for index, price in enumerate(flight_prices):
    #     if price != 0:
    #         new_budgets.append(budgets[index] - price)

    # budgets = new_budgets
    # destinations = destinations_with_flights
    
    # print("budgets", budgets)
    # print("destinations_with_flights", destinations)
    # print("finished getting flights") 
   
    # hotels = HotelSearcher.get_hotels_in_budget(destinations, budgets, start_date, end_date)
    
    # if not hotels:
    #     print("No suitable hotels found within the budget.")
    #     return
    
    # print("budgets before subtraction", budgets)
    # for index, destination in enumerate(destinations):
    #     if hotels[destination]['price'] == 0:
    #         del hotels[destination]
    #         del destinations[index]
    #         del budgets[index]
    #         del going_flights_info[0][index]
    #         del returning_flights_info[0][index]
    #     else:
    #         budgets[index] -= hotels[destination]['price']

    # print("budgets after subtraction", budgets)

    # print("hotels", hotels)
    # print("destinations", destinations)
    # print("going_flights_info", going_flights_info)
    # print("returning_flights_info", returning_flights_info)
    # print("finished getting hotels")

    # for index, complemet_cost in enumerate(budgets):
    #     total_costs[index] = budget - complemet_cost
    

    # chosen_option = display_options(hotels, destinations, going_flights_info[0], returning_flights_info[0], total_costs)
    # print("chosen_option", chosen_option)

    chosen_option = {'name': 'Lanzerac Wine Estate', 'price': 6378, 'image_url': {'thumbnail': 'https://lh3.googleusercontent.com/proxy/6KPWMK4_GyB8XKo03zGJS5x67qUHgqMFxeuifLWZ77fEv3WfjdVvdPfSvA8NxbXQeqqiUSgh5AIhcI3ZLp7V9PXkdUcQdBP7edosNAXV8jXoHS13rCbC2qYKFcpG1w8rHrD0tCslvPSw7FpZwjBxJaFjqWuclw=s287-w287-h192-n-k-no-v1', 'original_image': 'https://images.trvl-media.com/lodging/2000000/1180000/1179800/1179790/7fae941e_z.jpg'}, 'destination': 'Stellenbosch', 'going_flight': {'Cape Town': {'price': 1042, 'departure_token': 'WyJDalJJU0VWalZGOXZWWGxCZVVGQlFuaG9OMmRDUnkwdExTMHRMUzB0TFhCcWRHNHlNRUZCUVVGQlIxcFJaRU5yUlZGc04wVkJFZ3RGVkRReE9YeEZWRGcwTnhvTENNZXRCaEFDR2dOVlUwUTRISERIclFZPSIsW1siVExWIiwiMjAyNC0wOC0wMSIsIkFERCIsbnVsbCwiRVQiLCI0MTkiXSxbIkFERCIsIjIwMjQtMDgtMDIiLCJDUFQiLG51bGwsIkVUIiwiODQ3Il1dXQ==', 'flights': {'ET 419': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-08-01 15:35', 'arrival_airport_name': 'Bole Addis Ababa International Airport', 'arrival_time': '2024-08-01 19:50', 'duration': 255, 'airline': 'Ethiopian', 'flight_number': 'ET 419'}, 'ET 847': {'departure_airport_name': 'Bole Addis Ababa International Airport', 'departure_time': '2024-08-02 08:15', 'arrival_airport_name': 'Cape Town International Airport', 'arrival_time': '2024-08-02 13:45', 'duration': 390, 'airline': 'Ethiopian', 'flight_number': 'ET 847'}}}}, 'returning_flight': {'Cape Town': {'flights': {'ET 846': {'departure_airport_name': 'Cape Town International Airport', 'departure_time': '2024-08-10 14:35', 'arrival_airport_name': 'Bole Addis Ababa International Airport', 'arrival_time': '2024-08-10 22:00', 'duration': 385, 'airline': 'Ethiopian', 'flight_number': 'ET 846'}, 'ET 404': {'departure_airport_name': 'Bole Addis Ababa International Airport', 'departure_time': '2024-08-10 23:55', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-08-11 04:00', 'duration': 245, 'airline': 'Ethiopian', 'flight_number': 'ET 404'}}}}}
    
    trip_plan_tries = 0
    while trip_plan_tries < 3:
        trip_plan = ChatGPTFetcher.create_daily_plan(chosen_option['destination'], start_date, end_date, trip_type)
        parsed_plan = parse_trip_plan(trip_plan)
        print("parsed_plan", parsed_plan)

        # If the last date is missing, retry
        if parsed_plan[-1]['date'] != end_date:
            print("Last date missing in the trip plan. Retrying...")
            trip_plan_tries += 1
            continue
            
        # If the last date is present, break the loop
        break

    # trip_images = ChatGPTFetcher.generate_trip_images(chosen_option['destination'], trip_type)
    # print("trip_images", trip_images)

    print("\nTrip Summary:")
    print(f"Destination: {chosen_option['destination']}")
    print(f"flights: {[chosen_option['going_flight'], chosen_option['returning_flight']]}")
    print(f"Hotel: {chosen_option['name']}")
    print(f"Hotel image: {chosen_option['image_url']['original_image']}")
    print(f"Total Cost: ${chosen_option['price']}")
    print(f"Trip Plan:\n{trip_plan}")
    # print("\nTrip Images:")
    # for idx, img_url in enumerate(trip_images):
    #     print(f"Image {idx + 1}: {img_url}")

if __name__ == "__main__":
    main()
