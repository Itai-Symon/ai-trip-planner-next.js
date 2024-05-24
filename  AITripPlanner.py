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

            parsed_plan.append(day_info)

    except Exception as e:
        print("Error parsing the trip plan:", e)
    return parsed_plan

def display_options(hotels, destinations):
    for idx, destination in enumerate(destinations):
        print(f"Option {idx + 1}: {hotels[destination]} - {hotels[destination]['name']} - ${hotels[destination]['price']}")

    choice = int(input("Choose a destination (1-5): ")) - 1
    chosen_option = hotels[destinations[choice]]
    chosen_option['destination'] = destinations[choice]
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
    start_date, end_date, budget, trip_type = '2024-08-01', '2024-08-10', 1000, 'city'
    
    possible_destinations = []
    budgets = [budget] * 5

    going_flights_info = []
    returning_flights_info = []
    destinations_with_flights = []
    
    # allowing multiple tries to get the flights
    serapi_tries = 0
    number_of_missing_destinations = 5
    chosen_cities = []
   
    while number_of_missing_destinations > 0 and serapi_tries < 1:
        # possible_destinations = ChatGPTFetcher.get_possible_destinations(start_date, end_date, trip_type, number_of_missing_destinations, chosen_cities)
        # cities, destinations, airport_codes = parse_destinations(possible_destinations)
        
        # added_going_flights_info, added_returning_flights_info, chosen_cities, flight_prices, destinations_with_flights = FlightSearcher.get_flights(cities, airport_codes, start_date, end_date, budgets, destinations)
        # going_flights_info.append(added_going_flights_info)
        # returning_flights_info.append(added_returning_flights_info)

        going_flights_info = [[{'Reykjavik': {'price': 834, 'departure_token': 'WyJDalJJVnpoVlNVVkNURFV3UVVGQlJGaHNkRUZDUnkwdExTMHRMUzB0YjNsaVpIVXhNa0ZCUVVGQlIxcFJWMEpWU1dSWlkwRkJFaE5CUmprMk0zeEJSakV5TkRCOFNGWTJPRGcxR2dzSXlJc0ZFQUlhQTFWVFJEZ2NjTWlMQlE9PSIsW1siVExWIiwiMjAyNC0wOC0wMSIsIkNERyIsbnVsbCwiQUYiLCI5NjMiXSxbIkNERyIsIjIwMjQtMDgtMDIiLCJBTVMiLG51bGwsIkFGIiwiMTI0MCJdLFsiQU1TIiwiMjAyNC0wOC0wMiIsIktFRiIsbnVsbCwiSFYiLCI2ODg1Il1dXQ==', 'flights': {'AF 963': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-08-01 16:30', 'arrival_airport_name': 'Paris Charles de Gaulle Airport', 'arrival_time': '2024-08-01 20:15', 'duration': 285, 'airline': 'Air France', 'flight_number': 'AF 963'}, 'AF 1240': {'departure_airport_name': 'Paris Charles de Gaulle Airport', 'departure_time': '2024-08-02 07:10', 'arrival_airport_name': 'Amsterdam Airport Schiphol', 'arrival_time': '2024-08-02 08:35', 'duration': 85, 'airline': 'Air France', 'flight_number': 'AF 1240'}, 'HV 6885': {'departure_airport_name': 'Amsterdam Airport Schiphol', 'departure_time': '2024-08-02 17:55', 'arrival_airport_name': 'Keflavík International Airport', 'arrival_time': '2024-08-02 19:05', 'duration': 190, 'airline': 'Transavia', 'flight_number': 'HV 6885'}}}}, {'Barcelona': {'price': 347, 'departure_token': 'WyJDalJJZURCTlEyUlVRbGc0VjFsQlJFZENaMEZDUnkwdExTMHRMUzB0TFc5NVltTm9NMEZCUVVGQlIxcFJWRXBKUTNSemFFTkJFZzFKTWpNNU9ERjhTVUl6TURBeUdnc0lqSThDRUFJYUExVlRSRGdjY0l5UEFnPT0iLFtbIlRMViIsIjIwMjQtMDgtMDEiLCJNQUQiLG51bGwsIkkyIiwiMzk4MSJdLFsiTUFEIiwiMjAyNC0wOC0wMiIsIkJDTiIsbnVsbCwiSUIiLCIzMDAyIl1dXQ==', 'flights': {'I2 3981': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-08-01 18:35', 'arrival_airport_name': 'Adolfo Suárez Madrid–Barajas Airport', 'arrival_time': '2024-08-01 23:00', 'duration': 325, 'airline': 'Iberia Express', 'flight_number': 'I2 3981'}, 'IB 3002': {'departure_airport_name': 'Adolfo Suárez Madrid–Barajas Airport', 'departure_time': '2024-08-02 06:45', 'arrival_airport_name': 'Josep Tarradellas Barcelona-El Prat Airport', 'arrival_time': '2024-08-02 08:00', 'duration': 75, 'airline': 'Iberia', 'flight_number': 'IB 3002'}}}}]]
        returning_flights_info = [[{'Reykjavik': {'flights': {'BT 170': {'departure_airport_name': 'Keflavík International Airport', 'departure_time': '2024-08-10 12:30', 'arrival_airport_name': 'Riga Airport', 'arrival_time': '2024-08-10 19:05', 'duration': 215, 'airline': 'Air Baltic', 'flight_number': 'BT 170'}, 'BT 771': {'departure_airport_name': 'Riga Airport', 'departure_time': '2024-08-10 23:25', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-08-11 03:50', 'duration': 265, 'airline': 'Air Baltic', 'flight_number': 'BT 771'}}}}, {'Barcelona': {'flights': {'VY 7844': {'departure_airport_name': 'Josep Tarradellas Barcelona-El Prat Airport', 'departure_time': '2024-08-10 18:25', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-08-10 23:40', 'duration': 255, 'airline': 'Vueling', 'flight_number': 'VY 7844'}}}}]]
        destinations_with_flights = ['Iceland', 'Spain']
        print_flights_state(going_flights_info, returning_flights_info, serapi_tries)
        number_of_missing_destinations -= len(going_flights_info[0])

        serapi_tries += 1
        flight_prices = [834, 347, 0, 0, 0]
    
    
    new_budgets = []
    for index, price in enumerate(flight_prices):
        if price != 0:
            new_budgets.append(budgets[index] - price)

    budgets = new_budgets
    destinations = destinations_with_flights
    
    print("budgets", budgets)
    print("destinations_with_flights", destinations)
    print("finished getting flights") 
   
    hotels = HotelSearcher.get_hotels_in_budget(destinations, budgets, start_date, end_date)
    
    if not hotels:
        print("No suitable hotels found within the budget.")
        return
    print("budgets before subtraction", budgets)
    for index, destination in enumerate(destinations):
        budgets[index] -= hotels[destination]['price']
    print("budgets after subtraction", budgets)

    print("finished getting hotels")

    hotels = {'Iceland': {'name': 'Syðstibær Guesthouse - Double Room', 'price': 780, 'image_url': {'thumbnail': 'https://lh6.googleusercontent.com/proxy/25jsSNNJgs8-K7mhDH-Xy8sVflMwXvgQGnpZBL8Foa6eyFKD_KaIbjFRpMcgg6eSqtU2iCDqfozszHw9QmGKHO5j5OG9csGFfmAiMY2SgEruOnBUZwwU0NP3wL9OjuT4cDyc-evUQVOetmNpjlc00MS_kmLvtQ=s287-w287-h192-n-k-no-v1', 'original_image': 'https://q-xx.bstatic.com/xdata/images/hotel/max1024x768/309852219.jpg?k=c407f72fb1277ae1b5e64903faf08f380ba6f9c6eee9b4be7a328bda4502c442&o='}}, 'Netherlands': {'name': 'Trendy Tiny Houses Bovenweg', 'price': 977, 'image_url': {'thumbnail': 'https://lh5.googleusercontent.com/proxy/JFPUmM4Armxz0z9cp7SQfx7b8ncEmqq31r35PqW7HnsdBUGnNKpLpZhpsZFNhBgOZhIv_JTeiWkfrA02U5MKONss5-rcjdNE0kMAQNlb-6lTgzqfQdPHCHa_057i6eICyY9I354Ir8HsQe2-lF21Jz_8sSu1Iw=s287-w287-h192-n-k-no-v1', 'original_image': 'https://q-xx.bstatic.com/xdata/images/hotel/max1440x1080/208218765.jpg?k=d9cfd024a1a5e24831d4c0511fc365d93e98da3e2b8cfe3fb1ebc12981e95370&o='}}, 'Japan': {'name': "Hotel M's Plus Shijo Omiya", 'price': 474, 'image_url': {'thumbnail': 'https://lh6.googleusercontent.com/proxy/nqwH8kQm7R0G3YMN_z5wcauiK7278bvEXk2QSXm3FtgNml7vbtOCq3e_EDHNfSXmPvo3xxSrR-i5xWZ1k7pQe_RP5YX4quxLFV2vzcmPSA7vJFs2cdgtAFrvaEzdAZj-DT05Hexd56Lw7jiMp6L021Y7qTiomA=s287-w287-h192-n-k-no-v1', 'original_image': 'https://photos.hotelbeds.com/giata/original/63/637861/637861a_hb_a_003.jpg'}}, 'Canada': {'name': 'Pangea Pod Hotel', 'price': 875, 'image_url': {'thumbnail': 'https://lh5.googleusercontent.com/p/AF1QipNikPcbU7oLm4Yc7P-9QlC71pJ7Z_9AXIsDYx52=s287-w287-h192-n-k-no-v1', 'original_image': 'https://lh5.googleusercontent.com/p/AF1QipNikPcbU7oLm4Yc7P-9QlC71pJ7Z_9AXIsDYx52=s10000'}}, 'Spain': {'name': 'Beachfront studio apartment', 'price': 817, 'image_url': {'thumbnail': 'https://lh6.googleusercontent.com/proxy/Jy37xmRXalmXfsWbqx2-zqkf-5kpKD79rcmuJQm55lO7QkWPhAPLuHbiZpixY8MyUt2JSzoPiuECNQjddcIpPcmgXuI_KEnIiUXPIuKJ6iftrTx4ueyw96i4ZYSyYFM4NIbhs_1QldgBeeF-C4RF4xBcAwzFrg=s287-w287-h192-n-k-no-v1', 'original_image': 'https://media-cdn.tripadvisor.com/media/vr-splice-j/00/d5/ae/6e.jpg'}}}
    destinations = ['Iceland', 'Netherlands', 'Japan', 'Canada', 'Spain']

    chosen_option = display_options(hotels, destinations)
    print("chosen_option", chosen_option)

    trip_plan = ChatGPTFetcher.create_daily_plan(chosen_option['destination'], start_date, end_date, trip_type)
    parsed_plan = parse_trip_plan(trip_plan)
    print("parsed_plan", parsed_plan)

    trip_images = ChatGPTFetcher.generate_trip_images(chosen_option['destination'], trip_type)
    print("trip_images", trip_images)

    print("\nTrip Summary:")
    print(f"Destination: {chosen_option['destination']}")
    print(f"Hotel: {chosen_option['name']}")
    print(f"Hotel image: {chosen_option['image_url']['original_image']}")
    print(f"Total Cost: ${chosen_option['price']}")
    print(f"Trip Plan:\n{trip_plan}")
    print("\nTrip Images:")
    for idx, img_url in enumerate(trip_images):
        print(f"Image {idx + 1}: {img_url}")

if __name__ == "__main__":
    main()
