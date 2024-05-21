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

# Load airport data
airports = airportsdata.load('IATA') 

def get_closest_city_with_airport(city):
    prompt = (
        f"Find the closest city with an airport to {city}."
        f"respond only with the city name."
    )
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a geographical assistant."},
        {"role": "user", "content": prompt}
    ])
    closest_city_with_airport = response.choices[0].message.content
    print(closest_city_with_airport)
    return closest_city_with_airport

def get_airport_code(city):
    airport_code_according_to_city = None

    for code, airport in airports.items():
        if airport['city'].lower() == city.lower():
            airport_code_according_to_city = code
            break

    if airport_code_according_to_city:
        print(f"The airport code for {city} is {airport_code_according_to_city}.")
    else:
        print(f"No airport found for the city: {city}.")
        get_airport_code(get_closest_city_with_airport(city))
    
    return airport_code_according_to_city

def get_cheapest_flight(flight_result, budget = float(0)):
    lowest_price = flight_result.get('price_insights', {}).get('lowest_price', float('inf'))
    print("-----------------------------------")
    print("lowest_price", lowest_price)
    print("-----------------------------------")
    # if lowest_price >= budget:
    #     print(f"No suitable flights found within the budget.")
    #     return None
    

    # Initialize variable to keep track of the cheapest flight
    cheapest_flight = None
    cheapest_flight_price = float('inf')
    # Check in both best_flights and other_flights for the lowest price
    for flight_category in ['best_flights', 'other_flights']:
        if flight_category in flight_result:
            for flight in flight_result.get(flight_category, []):
                if flight['price'] == lowest_price:
                    cheapest_flight = flight
                    break
                elif flight['price'] < cheapest_flight_price:
                    cheapest_flight_price = flight['price']
                    cheapest_flight = flight
        else:
            print(f"No {flight_category} found in the flight result.")
            continue

    flights_info = []

    if cheapest_flight is not None:
        flights_info.append({
        'price': cheapest_flight['price'],
        'departure_token': cheapest_flight['departure_token']
        })
        for flight in cheapest_flight['flights']:
            flight_details = {
                'departure_airport_name': flight['departure_airport']['name'],
                'departure_time': flight['departure_airport']['time'],
                'arrival_airport_name': flight['arrival_airport']['name'],
                'arrival_time': flight['arrival_airport']['time'],
                'duration': flight['duration'],
                'airline': flight['airline'],
                'flight_number': flight['flight_number'],
            }
            if 'ticket_also_sold_by' in flight:
                flight_details['ticket_also_sold_by'] = flight['ticket_also_sold_by']
            if 'overnight' in flight:
                flight_details['overnight'] = flight['overnight']
            
            flights_info.append(flight_details)

    return flights_info

def get_flights(cities, airport_codes, start_date, end_date, budget):
    flights = []
    return_flights = []
    
    # validations
    if len(cities) != len(airport_codes):
        print("The number of cities and airport codes should be the same.")
        return flights, return_flights
    if budget <= 0:
        print("The budget should be greater than 0.")
        return flights, return_flights

    # each destination is a name
    for index, city in enumerate(cities):
        # airport_code = get_airport_code(city)
        
        # if not airport_code:
        #     print(f"No airport found for the city: {city}.")
        #     continue

        params = {
            "engine": "google_flights",
            "departure_id": "TLV",    #Tel Aviv
            "arrival_id": airport_codes[index],  #destination code
            "outbound_date": start_date,
            "return_date": end_date,
            "currency": "USD",
            "hl": "en",
            "max_price": budget,
            "api_key": SERPAPI_API_KEY
            }

        flight_search = GoogleSearch(params)
        flight_result = flight_search.get_dict()
        print("flight_result", flight_result)
        
        if 'error' in flight_result:
            print(f"Error: {flight_result['error']}")
            continue

        cheapest_flight = get_cheapest_flight(flight_result)
    
        if cheapest_flight is None:
            print(f"No flights found for {city}.")
        else:
            print("cheapest_flight", cheapest_flight)
            flights.append(cheapest_flight)
            return_flights.append(get_return_flight(cheapest_flight[0]['departure_token'], params))

    return flights, return_flights

def get_return_flight(departure_token, params):
    flight = None

    params['departure_token'] = departure_token
    flight_search = GoogleSearch(params)
    flight_result = flight_search.get_dict()
    print("return_flights_result", flight_result)

    if 'best_flights' in flight_result:
        flight = flight_result.get('best_flights', [])[0]
    
    if 'error' in flight_result:
        print(f"Error: {flight_result['error']}")

    return flight

