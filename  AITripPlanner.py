import re
from openai import OpenAI
from dotenv import load_dotenv
import os
import FlightSearcher
import HotelSearcher
import ChatGPTFetcher
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List, Dict, Any

app = FastAPI()


# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

# Allow requests from the Next.js frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

def get_trip_details():
    start_date: str = Query(..., description="Start date of the trip (YYYY-MM-DD)"),
    end_date: str = Query(..., description="End date of the trip (YYYY-MM-DD)"),
    budget: int = Query(..., description="Total budget in USD"),
    trip_type: str = Query(..., description="Type of trip (ski/beach/city)"),

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
    trip_options = []
    #  hard coded example
    # hotels ={'Kyoto': {'name': 'The Celestine Hotel Gion', 'price': 7694, 'image_url': {'thumbnail': 'https://lh5.googleusercontent.com/p/AF1QipPhLoRD6w1C-CEFEmzEDgGdykS1lqc5kyHxJgo=s287-w287-h192-n-k-no-v1', 'original_image': 'https://lh5.googleusercontent.com/p/AF1QipPhLoRD6w1C-CEFEmzEDgGdykS1lqc5kyHxJgo=s10000'}}, 'Florence': {'name': 'Hotel La Scaletta Florence', 'price': 8634, 'image_url': {'thumbnail': 'https://lh5.googleusercontent.com/p/AF1QipN7jkFB_YwPBvl-VL9Oa6IQoQ-v7TKSfjXrAeN8=s287-w287-h192-n-k-no-v1', 'original_image': 'https://lh5.googleusercontent.com/p/AF1QipN7jkFB_YwPBvl-VL9Oa6IQoQ-v7TKSfjXrAeN8=s10000'}}, 'Whistler': {'name': 'Sundial Hotel', 'price': 8081, 'image_url': {'thumbnail': 'https://lh5.googleusercontent.com/p/AF1QipNZxEA26cbbl6FXEIDmDrK-Lc1lE4oWB9QmnHdA=s287-w287-h192-n-k-no-v1', 'original_image': 'https://lh5.googleusercontent.com/p/AF1QipNZxEA26cbbl6FXEIDmDrK-Lc1lE4oWB9QmnHdA=s10000'}}, 'Melbourne': {'name': 'Grand Hyatt Melbourne', 'price': 6012, 'image_url': {'thumbnail': 'https://lh5.googleusercontent.com/p/AF1QipNMxShKMTIHQplJbjUa5Q-FW8xTDk537lSjMRwJ=s287-w287-h192-n-k-no-v1', 'original_image': 'https://lh5.googleusercontent.com/p/AF1QipNMxShKMTIHQplJbjUa5Q-FW8xTDk537lSjMRwJ=s10000'}}, 'Valencia': {'name': 'The Westin Valencia', 'price': 9368, 'image_url': {'thumbnail': 'https://lh5.googleusercontent.com/p/AF1QipPLEnFVflGYJQ3F1qcLEcOXzr4ar-V6vgVuYSNf=s287-w287-h192-n-k-no-v1', 'original_image': 'https://lh5.googleusercontent.com/p/AF1QipPLEnFVflGYJQ3F1qcLEcOXzr4ar-V6vgVuYSNf=s10000'}}}
    # destinations = ['Kyoto', 'Florence', 'Whistler', 'Melbourne', 'Valencia']
    # going_flights_info = [[{'Tokyo': {'price': 1462, 'departure_token': 'WyJDalJJWlU1cmVqWnJTM0JYTWxsQlJrNW1OMUZDUnkwdExTMHRMUzB0ZFdwaloyTXhNRUZCUVVGQlIxcFJkRzV2U25ka1RtTkJFaEZGVkRReE9YeEZWRFkzTW54UFdqRTNPQm9MQ0xuMUNCQUNHZ05WVTBRNEhIQzU5UWc9IixbWyJUTFYiLCIyMDI0LTA3LTExIiwiQUREIixudWxsLCJFVCIsIjQxOSJdLFsiQUREIiwiMjAyNC0wNy0xMSIsIklDTiIsbnVsbCwiRVQiLCI2NzIiXSxbIklDTiIsIjIwMjQtMDctMTIiLCJITkQiLG51bGwsIk9aIiwiMTc4Il1dXQ==', 'flights': {'ET 419': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-07-11 15:35', 'arrival_airport_name': 'Bole Addis Ababa International Airport', 'arrival_time': '2024-07-11 19:50', 'duration': 255, 'airline': 'Ethiopian', 'flight_number': 'ET 419'}, 'ET 672': {'departure_airport_name': 'Bole Addis Ababa International Airport', 'departure_time': '2024-07-11 22:35', 'arrival_airport_name': 'Incheon International Airport', 'arrival_time': '2024-07-12 16:00', 'duration': 685, 'airline': 'Ethiopian', 'flight_number': 'ET 672'}, 'OZ 178': {'departure_airport_name': 'Incheon International Airport', 'departure_time': '2024-07-12 21:10', 'arrival_airport_name': 'Haneda Airport', 'arrival_time': '2024-07-12 23:30', 'duration': 140, 'airline': 'Asiana', 'flight_number': 'OZ 178'}}}}, {'Rome': {'price': 200, 'departure_token': 'WyJDalJJUVhOblpVNTRUbGxKYWxWQlJIRnhWSGRDUnkwdExTMHRMUzB0YjJ0aWEySXhNMEZCUVVGQlIxcFJkRzQ0UnpsV1IxVkJFZzFYTmpJek1qWjhWell5TXpReEdnc0lnSndCRUFJYUExVlRSRGdjY0lDY0FRPT0iLFtbIlRMViIsIjIwMjQtMDctMTEiLCJCVUQiLG51bGwsIlc2IiwiMjMyNiJdLFsiQlVEIiwiMjAyNC0wNy0xMSIsIkZDTyIsbnVsbCwiVzYiLCIyMzQxIl1dXQ==', 'flights': {'W6 2326': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-07-11 10:55', 'arrival_airport_name': 'Budapest Ferenc Liszt International Airport', 'arrival_time': '2024-07-11 13:30', 'duration': 215, 'airline': 'Wizz Air', 'flight_number': 'W6 2326'}, 'W6 2341': {'departure_airport_name': 'Budapest Ferenc Liszt International Airport', 'departure_time': '2024-07-11 20:10', 'arrival_airport_name': 'Leonardo da Vinci–Fiumicino Airport', 'arrival_time': '2024-07-11 22:00', 'duration': 110, 'airline': 'Wizz Air', 'flight_number': 'W6 2341'}}}}, {'Vancouver': {'price': 1522, 'departure_token': 'WyJDalJJT1hsdlZHVmlXVTVLYWtGQlJHbHlMWGRDUnkwdExTMHRMUzB0TFMxNWJHbHpOMEZCUVVGQlIxcFJkRzlOUzNKVFUxTkJFZ3RCUmprMk0zeEJSak0zTkJvTENMMmtDUkFDR2dOVlUwUTRISEM5cEFrPSIsW1siVExWIiwiMjAyNC0wNy0xMSIsIkNERyIsbnVsbCwiQUYiLCI5NjMiXSxbIkNERyIsIjIwMjQtMDctMTIiLCJZVlIiLG51bGwsIkFGIiwiMzc0Il1dXQ==', 'flights': {'AF 963': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-07-11 16:30', 'arrival_airport_name': 'Paris Charles de Gaulle Airport', 'arrival_time': '2024-07-11 20:15', 'duration': 285, 'airline': 'Air France', 'flight_number': 'AF 963'}, 'AF 374': {'departure_airport_name': 'Paris Charles de Gaulle Airport', 'departure_time': '2024-07-12 10:10', 'arrival_airport_name': 'Vancouver International Airport', 'arrival_time': '2024-07-12 11:10', 'duration': 600, 'airline': 'Air France', 'flight_number': 'AF 374'}}}}, {'Sydney': {'price': 1308, 'departure_token': 'WyJDalJJZVVsWFFtcGhOemROV1VsQlJISnJZWGRDUnkwdExTMHRMUzB0TFhaMGNYTXlORUZCUVVGQlIxcFJkRzlyUzBaMFdVOUJFaEZGVkRReE9YeEZWRFl6T0h4VFVUSXlNUm9MQ00zOUJ4QUNHZ05WVTBRNEhIRE4vUWM9IixbWyJUTFYiLCIyMDI0LTA3LTExIiwiQUREIixudWxsLCJFVCIsIjQxOSJdLFsiQUREIiwiMjAyNC0wNy0xMSIsIlNJTiIsbnVsbCwiRVQiLCI2MzgiXSxbIlNJTiIsIjIwMjQtMDctMTIiLCJTWUQiLG51bGwsIlNRIiwiMjIxIl1dXQ==', 'flights': {'ET 419': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-07-11 15:35', 'arrival_airport_name': 'Bole Addis Ababa International Airport', 'arrival_time': '2024-07-11 19:50', 'duration': 255, 'airline': 'Ethiopian', 'flight_number': 'ET 419'}, 'ET 638': {'departure_airport_name': 'Bole Addis Ababa International Airport', 'departure_time': '2024-07-11 23:50', 'arrival_airport_name': 'Singapore Changi Airport', 'arrival_time': '2024-07-12 14:50', 'duration': 600, 'airline': 'Ethiopian', 'flight_number': 'ET 638'}, 'SQ 221': {'departure_airport_name': 'Singapore Changi Airport', 'departure_time': '2024-07-12 20:20', 'arrival_airport_name': 'Sydney Airport', 'arrival_time': '2024-07-13 05:55', 'duration': 455, 'airline': 'Singapore Airlines', 'flight_number': 'SQ 221'}}}}, {'Barcelona': {'price': 261, 'departure_token': 'WyJDalJJU0d4dFFVVkNSbGs1UVc5QlEwcGlXbEZDUnkwdExTMHRMUzB0TFhCcWMyMHhNa0ZCUVVGQlIxcFJkRzg0U25kcGR6WkJFZzFYTkRjMU1URjhWbGs0TVRBMUdnc0l2Y3NCRUFJYUExVlRSRGdjY0wzTEFRPT0iLFtbIlRMViIsIjIwMjQtMDctMTEiLCJBVEgiLG51bGwsIlc0IiwiNzUxMSJdLFsiQVRIIiwiMjAyNC0wNy0xMiIsIkJDTiIsbnVsbCwiVlkiLCI4MTA1Il1dXQ==', 'flights': {'W4 7511': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-07-11 14:00', 'arrival_airport_name': 'Athens International Airport "Eleftherios Venizelos"', 'arrival_time': '2024-07-11 16:15', 'duration': 135, 'airline': 'Wizz Air', 'flight_number': 'W4 7511'}, 'VY 8105': {'departure_airport_name': 'Athens International Airport "Eleftherios Venizelos"', 'departure_time': '2024-07-12 03:40', 'arrival_airport_name': 'Josep Tarradellas Barcelona-El Prat Airport', 'arrival_time': '2024-07-12 05:50', 'duration': 190, 'airline': 'Vueling', 'flight_number': 'VY 8105'}}}}]]
    # returning_flights_info = [[{'Tokyo': {'flights': {'NH 847': {'departure_airport_name': 'Haneda Airport', 'departure_time': '2024-08-07 10:50', 'arrival_airport_name': 'Suvarnabhumi Airport', 'arrival_time': '2024-08-07 15:30', 'duration': 400, 'airline': 'ANA', 'flight_number': 'NH 847'}, 'ET 609': {'departure_airport_name': 'Suvarnabhumi Airport', 'departure_time': '2024-08-08 00:55', 'arrival_airport_name': 'Bole Addis Ababa International Airport', 'arrival_time': '2024-08-08 05:35', 'duration': 520, 'airline': 'Ethiopian', 'flight_number': 'ET 609'}, 'ET 418': {'departure_airport_name': 'Bole Addis Ababa International Airport', 'departure_time': '2024-08-08 10:25', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-08-08 14:35', 'duration': 250, 'airline': 'Ethiopian', 'flight_number': 'ET 418'}}}}, {'Rome': {'flights': {'W4 6041': {'departure_airport_name': 'Leonardo da Vinci–Fiumicino Airport', 'departure_time': '2024-08-07 15:15', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-08-07 19:45', 'duration': 210, 'airline': 'Wizz Air', 'flight_number': 'W4 6041'}}}}, {'Vancouver': {'flights': {'AF 375': {'departure_airport_name': 'Vancouver International Airport', 'departure_time': '2024-08-07 13:30', 'arrival_airport_name': 'Paris Charles de Gaulle Airport', 'arrival_time': '2024-08-08 08:15', 'duration': 585, 'airline': 'Air France', 'flight_number': 'AF 375'}, 'AF 958': {'departure_airport_name': 'Paris Charles de Gaulle Airport', 'departure_time': '2024-08-08 09:30', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-08-08 14:45', 'duration': 255, 'airline': 'Air France', 'flight_number': 'AF 958'}}}}, {'Sydney': {'flights': {'QF 295': {'departure_airport_name': 'Sydney Airport', 'departure_time': '2024-08-07 09:50', 'arrival_airport_name': 'Suvarnabhumi Airport', 'arrival_time': '2024-08-07 16:40', 'duration': 590, 'airline': 'Qantas', 'flight_number': 'QF 295'}, 'ET 609': {'departure_airport_name': 'Suvarnabhumi Airport', 'departure_time': '2024-08-08 00:55', 'arrival_airport_name': 'Bole Addis Ababa International Airport', 'arrival_time': '2024-08-08 05:35', 'duration': 520, 'airline': 'Ethiopian', 'flight_number': 'ET 609'}, 'ET 418': {'departure_airport_name': 'Bole Addis Ababa International Airport', 'departure_time': '2024-08-08 10:25', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-08-08 14:35', 'duration': 250, 'airline': 'Ethiopian', 'flight_number': 'ET 418'}}}}, {'Barcelona': {'flights': {'VY 6108': {'departure_airport_name': 'Josep Tarradellas Barcelona-El Prat Airport', 'departure_time': '2024-08-07 09:40', 'arrival_airport_name': 'Leonardo da Vinci–Fiumicino Airport', 'arrival_time': '2024-08-07 11:35', 'duration': 115, 'airline': 'Vueling', 'flight_number': 'VY 6108'}, 'W4 6041': {'departure_airport_name': 'Leonardo da Vinci–Fiumicino Airport', 'departure_time': '2024-08-07 15:15', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-08-07 19:45', 'duration': 210, 'airline': 'Wizz Air', 'flight_number': 'W4 6041'}}}}]]
    # budgets = [844, 1166, 397, 2680, 371]

    print("inside displaying trip options", hotels, destinations, going_flights_info, returning_flights_info, budgets)

    for idx, destination in enumerate(destinations):
        option = {
            "id": idx,
            "destination": destination,
            "going_flight": going_flights_info[idx],
            "returning_flight": returning_flights_info[idx],
            "hotel": hotels[destination]['name'],
            "hotel_price": hotels[destination]['price'],
            "hotel_image": hotels[destination]['image_url']['original_image'],
            "price": budgets[idx],

        }
        print("option", option)
        trip_options.append(option)

    return trip_options

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

@app.get("/possible-destinations")
def get_possible_destinations(
    start_date: str, end_date: str, budget: int, trip_type: str
) -> List[Dict[str, Any]]:
    try:
        possible_destinations = []
        budgets = [budget] * 5
        total_costs = [budget] * 5

        going_flights_info = []
        returning_flights_info = []
        destinations_with_flights = []
        trip_options = []
        
        serapi_tries = 0
        number_of_missing_destinations = 5
        chosen_cities = []
    
        while number_of_missing_destinations > 0 and serapi_tries < 1:
            possible_destinations = ChatGPTFetcher.get_possible_destinations(start_date, end_date, trip_type, number_of_missing_destinations, chosen_cities)
            cities, destinations, airport_codes = parse_destinations(possible_destinations)
            
            added_going_flights_info, added_returning_flights_info, chosen_cities, flight_prices, destinations_with_flights = FlightSearcher.get_flights(cities, airport_codes, start_date, end_date, budgets, destinations)
            going_flights_info.append(added_going_flights_info)
            returning_flights_info.append(added_returning_flights_info)

            print_flights_state(going_flights_info, returning_flights_info, serapi_tries)
            number_of_missing_destinations -= len(going_flights_info[0])

            serapi_tries += 1
        
        new_budgets = []
        for index, price in enumerate(flight_prices):
            if price != 0:
                new_budgets.append(budgets[index] - price)

        budgets = new_budgets
        destinations = destinations_with_flights

        # budgets = [9587, 8054, 8282, 8959, 8598]
        # destinations = ['Barcelona, Spain', 'Vancouver, Canada', 'Tokyo, Japan', 'Cape Town, South Africa', 'Sydney, Australia']
        
        print("budgets", budgets)
        print("destinations_with_flights", destinations)
        print("finished getting flights") 
        
        hotels = HotelSearcher.get_hotels_in_budget(destinations, budgets, start_date, end_date)
        
        if not hotels:
            print("No suitable hotels found within the budget.")
            return []
        
        print("budgets before subtraction", budgets)
        for index, destination in enumerate(destinations):
            if hotels[destination]['price'] == 0:
                del hotels[destination]
                del destinations[index]
                del budgets[index]
                del going_flights_info[0][index]
                del returning_flights_info[0][index]
            else:
                budgets[index] -= hotels[destination]['price']

        print("budgets after subtraction", budgets)

        print("hotels", hotels)
        print("destinations", destinations)
        print("going_flights_info", going_flights_info)
        print("returning_flights_info", returning_flights_info)
        print("finished getting hotels")

        # compute the total cost of the trip
        for idx, destination in enumerate(destinations):
            total_costs[idx] -= budgets[idx] 

        trip_options = display_options(hotels, destinations, going_flights_info[0], returning_flights_info[0], total_costs)
       
#  trip_options =  [ {'id': 0, 'destination': 'Barcelona, Spain', 'going_flight': {'Barcelona': {'price': 241, 'departure_token': 'WyJDalJJVlhsT2FYazRkWEpGYTNOQlFVaFRiMUZDUnkwdExTMHRMUzB0ZFdwalpXSXhORUZCUVVGQlIxcFVabUp6UlhscFEzTkJFZ3BCV2pnd04zeEJXamM0R2dzSWtyd0JFQUlhQTFWVFJEZ2NjSks4QVE9PSIsW1siVExWIiwiMjAyNC0xMS0wMSIsIkZDTyIsbnVsbCwiQVoiLCI4MDciXSxbIkZDTyIsIjIwMjQtMTEtMDEiLCJCQ04iLG51bGwsIkFaIiwiNzgiXV1d', 'flights': {'AZ 807': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-11-01 15:20', 'arrival_airport_name': 'Leonardo da Vinci–Fiumicino Airport', 'arrival_time': '2024-11-01 18:05', 'duration': 225, 'airline': 'ITA', 'flight_number': 'AZ 807'}, 'AZ 78': {'departure_airport_name': 'Leonardo da Vinci–Fiumicino Airport', 'departure_time': '2024-11-01 21:25', 'arrival_airport_name': 'Josep Tarradellas Barcelona-El Prat Airport', 'arrival_time': '2024-11-01 23:15', 'duration': 110, 'airline': 'ITA', 'flight_number': 'AZ 78'}}}}, 'returning_flight': {'Barcelona': {'flights': {'VY 7844': {'departure_airport_name': 'Josep Tarradellas Barcelona-El Prat Airport', 'departure_time': '2024-11-09 22:50', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-11-10 04:00', 'duration': 250, 'airline': 'Vueling', 'flight_number': 'VY 7844'}}}}, 'hotel': 'The Barcelona EDITION', 'hotel_price': 3855, 'hotel_image': 'https://lh5.googleusercontent.com/p/AF1QipO8lBbY5Ru08mUkpSYJhTrDBm44PtQwKG-I5J_q=s10000', 'price': 0},
#  {'id': 1, 'destination': 'Tokyo, Japan', 'going_flight': {'Tokyo': {'price': 1265, 'departure_token': 'WyJDalJJTmsxeGJYZzVXaTFQUVVWQlRrUTVMWGRDUnkwdExTMHRMUzB0TFc5NVltSmpOVUZCUVVGQlIxcFVabU5qVDI5UlQybEJFaEZNV1RrM01YeFFValkxT1h4UVVqUXlOQm9MQ01YYkJ4QUNHZ05WVTBRNEhIREYyd2M9IixbWyJUTFYiLCIyMDI0LTExLTAxIiwiRFhCIixudWxsLCJMWSIsIjk3MSJdLFsiRFhCIiwiMjAyNC0xMS0wMSIsIk1OTCIsbnVsbCwiUFIiLCI2NTkiXSxbIk1OTCIsIjIwMjQtMTEtMDIiLCJITkQiLG51bGwsIlBSIiwiNDI0Il1dXQ==', 'flights': {'LY 971': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-11-01 06:15', 'arrival_airport_name': 'Dubai International Airport', 'arrival_time': '2024-11-01 11:15', 'duration': 180, 'airline': 'El Al', 'flight_number': 'LY 971'}, 'PR 659': {'departure_airport_name': 'Dubai International Airport', 'departure_time': '2024-11-01 19:35', 'arrival_airport_name': 'Ninoy Aquino International Airport', 'arrival_time': '2024-11-02 08:40', 'duration': 545, 'airline': 'Philippine Airlines', 'flight_number': 'PR 659'}, 'PR 424': {'departure_airport_name': 'Ninoy Aquino International Airport', 'departure_time': '2024-11-02 19:00', 'arrival_airport_name': 'Haneda Airport', 'arrival_time': '2024-11-03 00:15', 'duration': 255, 'airline': 'Philippine Airlines', 'flight_number': 'PR 424'}}}}, 'returning_flight': {'Tokyo': {'flights': {'PR 423': {'departure_airport_name': 'Haneda Airport', 'departure_time': '2024-11-09 01:15', 'arrival_airport_name': 'Ninoy Aquino International Airport', 'arrival_time': '2024-11-09 04:50', 'duration': 275, 'airline': 'Philippine Airlines', 'flight_number': 'PR 423'}, 'PR 658': {'departure_airport_name': 'Ninoy Aquino International Airport', 'departure_time': '2024-11-09 13:00', 'arrival_airport_name': 'Dubai International Airport', 'arrival_time': '2024-11-09 18:05', 'duration': 545, 'airline': 'Philippine Airlines', 'flight_number': 'PR 658'}, 'LY 972': {'departure_airport_name': 'Dubai International Airport', 'departure_time': '2024-11-10 13:00', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-11-10 14:40', 'duration': 220, 'airline': 'El Al', 'flight_number': 'LY 972'}}}}, 'hotel': 'The Okura Tokyo', 'hotel_price': 5273, 'hotel_image': 'https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/7/0/118/351/410/cwh_P.jpg', 'price': 0},
#  {'id': 2, 'destination': 'Sydney, Australia', 'going_flight': {'Sydney': {'price': 1477, 'departure_token': 'WyJDalJJWVc1YVJGaEJSMnRKVW5kQlRVRlZPSGRDUnkwdExTMHRMUzB0TFhaMGNITXlNVUZCUVVGQlIxcFVabU56UzBGWVRubEJFaEZNV0RJMU0zeE1XREUzTm54VFVUSXdNUm9MQ05HQkNSQUNHZ05WVTBRNEhIRFJnUWs9IixbWyJUTFYiLCIyMDI0LTExLTAxIiwiWlJIIixudWxsLCJMWCIsIjI1MyJdLFsiWlJIIiwiMjAyNC0xMS0wMSIsIlNJTiIsbnVsbCwiTFgiLCIxNzYiXSxbIlNJTiIsIjIwMjQtMTEtMDIiLCJTWUQiLG51bGwsIlNRIiwiMjAxIl1dXQ==', 'flights': {'LX 253': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-11-01 18:20', 'arrival_airport_name': 'Zurich Airport', 'arrival_time': '2024-11-01 21:40', 'duration': 260, 'airline': 'SWISS', 'flight_number': 'LX 253'}, 'LX 176': {'departure_airport_name': 'Zurich Airport', 'departure_time': '2024-11-01 22:35', 'arrival_airport_name': 'Singapore Changi Airport', 'arrival_time': '2024-11-02 17:50', 'duration': 735, 'airline': 'SWISS', 'flight_number': 'LX 176'}, 'SQ 201': {'departure_airport_name': 'Singapore Changi Airport', 'departure_time': '2024-11-02 19:10', 'arrival_airport_name': 'Sydney Airport', 'arrival_time': '2024-11-03 05:55', 'duration': 465, 'airline': 'Singapore Airlines', 'flight_number': 'SQ 201'}}}}, 'returning_flight': {'Sydney': {'flights': {'QF 1': {'departure_airport_name': 'Sydney Airport', 'departure_time': '2024-11-09 16:20', 'arrival_airport_name': 'Singapore Changi Airport', 'arrival_time': '2024-11-09 21:25', 'duration': 485, 'airline': 'Qantas', 'flight_number': 'QF 1'}, 'LH 791': {'departure_airport_name': 'Singapore Changi Airport', 'departure_time': '2024-11-09 23:45', 'arrival_airport_name': 'Munich International Airport', 'arrival_time': '2024-11-10 05:50', 'duration': 785, 'airline': 'Lufthansa', 'flight_number': 'LH 791'}, 'LH 680': {'departure_airport_name': 'Munich International Airport', 'departure_time': '2024-11-10 11:20', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-11-10 16:05', 'duration': 225, 'airline': 'Lufthansa', 'flight_number': 'LH 680'}}}}, 'hotel': 'Four Seasons Hotel Sydney', 'hotel_price': 2760, 'hotel_image': 'https://lh5.googleusercontent.com/p/AF1QipNVXI3Zb1btWO543gAFTX7sHPD7SLmd3966dGXH=s10000', 'price': 0},
#  {'id': 3, 'destination': 'Miami, USA', 'going_flight': {'Miami': {'price': 730, 'departure_token': 'WyJDalJJZDBKWmNVbERMVlJSVkRCQlNGUnFXR2RDUnkwdExTMHRMUzB0Y0daaVpXWXlOMEZCUVVGQlIxcFVabVJOVEUxUlpFVkJFZ3BDUVRRd05YeEJRVFUzR2dzSXlia0VFQUlhQTFWVFJEZ2NjTW01QkE9PSIsW1siVExWIiwiMjAyNC0xMS0wMSIsIkxIUiIsbnVsbCwiQkEiLCI0MDUiXSxbIkxIUiIsIjIwMjQtMTEtMDEiLCJNSUEiLG51bGwsIkFBIiwiNTciXV1d', 'flights': {'BA 405': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-11-01 06:20', 'arrival_airport_name': 'Heathrow Airport', 'arrival_time': '2024-11-01 10:00', 'duration': 340, 'airline': 'British Airways', 'flight_number': 'BA 405'}, 'AA 57': {'departure_airport_name': 'Heathrow Airport', 'departure_time': '2024-11-01 11:45', 'arrival_airport_name': 'Miami International Airport', 'arrival_time': '2024-11-01 17:45', 'duration': 600, 'airline': 'American', 'flight_number': 'AA 57'}}}}, 'returning_flight': {'Miami': {'flights': {'AA 1293': {'departure_airport_name': 'Miami International Airport', 'departure_time': '2024-11-09 14:34', 'arrival_airport_name': 'Philadelphia International Airport', 'arrival_time': '2024-11-09 17:21', 'duration': 167, 'airline': 'American', 'flight_number': 'AA 1293'}, 'BA 66': {'departure_airport_name': 'Philadelphia International Airport', 'departure_time': '2024-11-09 18:35', 'arrival_airport_name': 'Heathrow Airport', 'arrival_time': '2024-11-10 06:30', 'duration': 415, 'airline': 'British Airways', 'flight_number': 'BA 66'}, 'BA 402': {'departure_airport_name': 'Heathrow Airport', 'departure_time': '2024-11-10 07:45', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-11-10 14:45', 'duration': 300, 'airline': 'British Airways', 'flight_number': 'BA 402'}}}}, 'hotel': 'Four Seasons Hotel Miami', 'hotel_price': 6882, 'hotel_image': 'https://lh5.googleusercontent.com/p/AF1QipOGVMOfYVuAcN7oHTMZClUSGNas7gIHGbUFXfFc=s10000', 'price': 0},

#  {'id': 4, 'destination': 'Cape Town, South Africa', 'going_flight': {'Cape Town': {'price': 810, 'departure_token': 'WyJDalJJZUhBd09FSk1kV1Z3VjBGQlNWSlFiRkZDUnkwdExTMHRMUzB0Y0dwaVpuWXhNRUZCUVVGQlIxcFVabVJyUlVKVFptVkJFZ3hHV2pFMk1qWjhSVXMzTnpBYUN3aTcrQVFRQWhvRFZWTkVPQnh3dS9nRSIsW1siVExWIiwiMjAyNC0xMS0wMSIsIkRYQiIsbnVsbCwiRloiLCIxNjI2Il0sWyJEWEIiLCIyMDI0LTExLTAyIiwiQ1BUIixudWxsLCJFSyIsIjc3MCJdXV0=', 'flights': {'FZ 1626': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-11-01 23:45', 'arrival_airport_name': 'Dubai International Airport', 'arrival_time': '2024-11-02 04:50', 'duration': 185, 'airline': 'flydubai', 'flight_number': 'FZ 1626'}, 'EK 770': {'departure_airport_name': 'Dubai International Airport', 'departure_time': '2024-11-02 09:10', 'arrival_airport_name': 'Cape Town International Airport', 'arrival_time': '2024-11-02 16:45', 'duration': 575, 'airline': 'Emirates', 'flight_number': 'EK 770'}}}}, 'returning_flight': {'Cape Town': {'flights': {'EK 773': {'departure_airport_name': 'Cape Town International Airport', 'departure_time': '2024-11-09 13:40', 'arrival_airport_name': 'Dubai International Airport', 'arrival_time': '2024-11-10 01:05', 'duration': 565, 'airline': 'Emirates', 'flight_number': 'EK 773'}, 'EK 931': {'departure_airport_name': 'Dubai International Airport', 'departure_time': '2024-11-10 14:30', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-11-10 16:15', 'duration': 225, 'airline': 'Emirates', 'flight_number': 'EK 931'}}}}, 'hotel': 'One&Only Cape Town', 'hotel_price': 9021, 'hotel_image': 'https://i.giatamedia.com/m.php?m=AQABAAAAla4KAIldQwUFAIPvHVJ7yOA0IbaaTU-DFCE', 'price': 0}]

        return trip_options
    
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate-itinerary-and-images")
def generate_itinerary_and_images(
    destination: str, start_date: str, end_date: str, trip_type:str
) -> List[Dict[str, Any]]:
    try:
        # chosen_option = {'name': 'Lanzerac Wine Estate', 'price': 6378, 'image_url': {'thumbnail': 'https://lh3.googleusercontent.com/proxy/6KPWMK4_GyB8XKo03zGJS5x67qUHgqMFxeuifLWZ77fEv3WfjdVvdPfSvA8NxbXQeqqiUSgh5AIhcI3ZLp7V9PXkdUcQdBP7edosNAXV8jXoHS13rCbC2qYKFcpG1w8rHrD0tCslvPSw7FpZwjBxJaFjqWuclw=s287-w287-h192-n-k-no-v1', 'original_image': 'https://images.trvl-media.com/lodging/2000000/1180000/1179800/1179790/7fae941e_z.jpg'}, 'destination': 'Stellenbosch', 'going_flight': {'Cape Town': {'price': 1042, 'departure_token': 'WyJDalJJU0VWalZGOXZWWGxCZVVGQlFuaG9OMmRDUnkwdExTMHRMUzB0TFhCcWRHNHlNRUZCUVVGQlIxcFJaRU5yUlZGc04wVkJFZ3RGVkRReE9YeEZWRGcwTnhvTENNZXRCaEFDR2dOVlUwUTRISERIclFZPSIsW1siVExWIiwiMjAyNC0wOC0wMSIsIkFERCIsbnVsbCwiRVQiLCI0MTkiXSxbIkFERCIsIjIwMjQtMDgtMDIiLCJDUFQiLG51bGwsIkVUIiwiODQ3Il1dXQ==', 'flights': {'ET 419': {'departure_airport_name': 'Ben Gurion Airport', 'departure_time': '2024-08-01 15:35', 'arrival_airport_name': 'Bole Addis Ababa International Airport', 'arrival_time': '2024-08-01 19:50', 'duration': 255, 'airline': 'Ethiopian', 'flight_number': 'ET 419'}, 'ET 847': {'departure_airport_name': 'Bole Addis Ababa International Airport', 'departure_time': '2024-08-02 08:15', 'arrival_airport_name': 'Cape Town International Airport', 'arrival_time': '2024-08-02 13:45', 'duration': 390, 'airline': 'Ethiopian', 'flight_number': 'ET 847'}}}}, 'returning_flight': {'Cape Town': {'flights': {'ET 846': {'departure_airport_name': 'Cape Town International Airport', 'departure_time': '2024-08-10 14:35', 'arrival_airport_name': 'Bole Addis Ababa International Airport', 'arrival_time': '2024-08-10 22:00', 'duration': 385, 'airline': 'Ethiopian', 'flight_number': 'ET 846'}, 'ET 404': {'departure_airport_name': 'Bole Addis Ababa International Airport', 'departure_time': '2024-08-10 23:55', 'arrival_airport_name': 'Ben Gurion Airport', 'arrival_time': '2024-08-11 04:00', 'duration': 245, 'airline': 'Ethiopian', 'flight_number': 'ET 404'}}}}}
        trip_plan = ChatGPTFetcher.create_daily_plan(destination, start_date, end_date, trip_type)
        parsed_plan = parse_trip_plan(trip_plan)
        print("parsed_plan", parsed_plan)

        trip_images = ChatGPTFetcher.generate_trip_images(destination, trip_type)
        # trip_images = ["https://oaidalleapiprodscus.blob.core.windows.net/private/org-2CwskBzgGP5OnJE5rJP2GrIS/user-8X3nxWNCXu17D1wEz6eRoTVq/img-M2FURHFwEo1ZRytNp3Yr9EL2.png?st=2024-05-25T20%3A53%3A58Z&se=2024-05-25T22%3A53%3A58Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-25T17%3A29%3A13Z&ske=2024-05-26T17%3A29%3A13Z&sks=b&skv=2021-08-06&sig=iEX5FJ8PQzP6gWyX8o5dD4Z32afKt7TiqfedfEFlbcw%3D","https://oaidalleapiprodscus.blob.core.windows.net/private/org-2CwskBzgGP5OnJE5rJP2GrIS/user-8X3nxWNCXu17D1wEz6eRoTVq/img-40o0DhgucbRc54xtfah4dhfx.png?st=2024-05-25T20%3A54%3A09Z&se=2024-05-25T22%3A54%3A09Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-25T18%3A36%3A17Z&ske=2024-05-26T18%3A36%3A17Z&sks=b&skv=2021-08-06&sig=B/0IaInDugr7u1N0i5sEUJlBt4S8nFliF9DHazNC3OI%3D","https://oaidalleapiprodscus.blob.core.windows.net/private/org-2CwskBzgGP5OnJE5rJP2GrIS/user-8X3nxWNCXu17D1wEz6eRoTVq/img-rlvJh5cG4FkWXdjMj6WBfGWx.png?st=2024-05-25T20%3A54%3A22Z&se=2024-05-25T22%3A54%3A22Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-25T17%3A36%3A21Z&ske=2024-05-26T17%3A36%3A21Z&sks=b&skv=2021-08-06&sig=8hn/95X0zfmeXiWsNJsfEXyiq/Qn4ZvadhJlOf3R258%3D","https://oaidalleapiprodscus.blob.core.windows.net/private/org-2CwskBzgGP5OnJE5rJP2GrIS/user-8X3nxWNCXu17D1wEz6eRoTVq/img-NECXuGsKNk1uUBDvX3ZeLBCU.png?st=2024-05-25T20%3A54%3A34Z&se=2024-05-25T22%3A54%3A34Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-25T17%3A37%3A51Z&ske=2024-05-26T17%3A37%3A51Z&sks=b&skv=2021-08-06&sig=z9%2B24DQ8Kk5Xm0EnM09RBDnoRujXoVfLwl2bqOTOD7Q%3D"]
        print("trip_images", trip_images)

        print("\nTrip Summary:")
        print(f"Destination: {destination}")
        print(f"Trip Plan:\n{trip_plan}")

        return [{
            "destination": destination,
            "trip_plan": trip_plan,
            "trip_images": trip_images
        }]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)