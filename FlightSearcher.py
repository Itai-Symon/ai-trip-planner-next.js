from openai import OpenAI
from serpapi import GoogleSearch
import airportsdata
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)


def get_cheapest_flight(flight_result, budget = 0, city = ''):
    
    lowest_price = flight_result.get('price_insights', {}).get('lowest_price', 0)
    print("-----------------------------------")
    print("lowest_price", lowest_price)
    print("-----------------------------------")
    
    cheapest_flight = None
    cheapest_flight_price = budget
    
    # find the cheapest flight
    for flight_category in ['best_flights', 'other_flights']:
        if flight_category in flight_result:
            for flight in flight_result[flight_category]:
                if flight['price'] == lowest_price:
                    cheapest_flight = flight
                    cheapest_flight_price = lowest_price
                    break
                elif flight['price'] < cheapest_flight_price:
                    cheapest_flight_price = flight['price']
                    cheapest_flight = flight
            
    flights_info = {city: {}}

    # add the cheapest flight details
    if cheapest_flight is not None:
        flights_info[city]['price'] = cheapest_flight['price']
        flights_info[city]['departure_token'] = cheapest_flight['departure_token']
        flights_info[city]['flights'] = {}
        for flight in cheapest_flight['flights']:
            flights_info[city]['flights'][flight['flight_number']] = {
                'departure_airport_name': flight['departure_airport']['name'],
                'departure_time': flight['departure_airport']['time'],
                'arrival_airport_name': flight['arrival_airport']['name'],
                'arrival_time': flight['arrival_airport']['time'],
                'duration': flight['duration'],
                'airline': flight['airline'],
                'flight_number': flight['flight_number'],
            }
            
    return flights_info, cheapest_flight_price

def get_return_flight(departure_token, params, city):
    flight = None

    params['departure_token'] = departure_token
    flight_search = GoogleSearch(params)
    flight_result = flight_search.get_dict()
    print("return_flights_result", flight_result)

    flight_raw = None
    if 'best_flights' in flight_result and flight_result['best_flights']:
        flight_raw = flight_result['best_flights'][0]
    elif 'other_flights' in flight_result and flight_result['other_flights']:
        flight_raw = flight_result['other_flights'][0]

    flights_info = {city: {}}

    if flight_raw and 'flights' in flight_raw:
        flights_info[city]['flights'] = {}
        for flight in flight_raw['flights']:
            flights_info[city]['flights'][flight['flight_number']] = {
                'departure_airport_name': flight['departure_airport']['name'],
                'departure_time': flight['departure_airport']['time'],
                'arrival_airport_name': flight['arrival_airport']['name'],
                'arrival_time': flight['arrival_airport']['time'],
                'duration': flight['duration'],
                'airline': flight['airline'],
                'flight_number': flight['flight_number'],
            }
    return flights_info

def get_flights(cities, airport_codes, start_date, end_date, budget):
    flights = []
    return_flights = []
    successfully_retrieved_flights = 0
    # validations
    if len(cities) != len(airport_codes):
        print("The number of cities and airport codes should be the same.")
        return flights, return_flights, []

    # each destination is a name
    for index, city in enumerate(cities):
        print(f"Searching for flights to {city}...")
        chosen_cities = []

        params = {
            "engine": "google_flights",
            "departure_id": "TLV",    #Tel Aviv
            "arrival_id": airport_codes[index],  #destination code
            "outbound_date": start_date,
            "return_date": end_date,
            "currency": "USD",
            "hl": "en",
            "max_price": budget[index],
            "api_key": SERPAPI_API_KEY
            }

        flight_search = GoogleSearch(params)
        flight_result = flight_search.get_dict()
        print("flight_result", flight_result)
        
        if 'error' in flight_result:
            print(f"Error: {flight_result['error']}")
            continue

        cheapest_flight, budget[index] = get_cheapest_flight(flight_result, budget[index], city)
    
        if cheapest_flight is None:
            print(f"No flights found for {city}.")
        else:
            print("-----------------------------------")
            print("cheapest_flight", cheapest_flight)
            print("-----------------------------------")    
            return_flight = get_return_flight(cheapest_flight[city]['departure_token'], params, city)
            if (return_flight is not None) and ('error' not in return_flight):
                flights.append(cheapest_flight)
                return_flights.append(return_flight)
                chosen_cities.append(city)
                successfully_retrieved_flights += 1
    
    print('='*50)
    print("flights", flights)
    print('*'*50)
    print("return_flights", return_flights)
    print('*'*50)
    print("chosen_cities", chosen_cities)
    print('='*50)

    return flights, return_flights, chosen_cities, successfully_retrieved_flights, budget

