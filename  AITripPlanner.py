import re
from openai import OpenAI
# from dotenv import load_dotenv
# import os
# import FlightSearcher
# import HotelSearcher
# import ChatGPTFetcher
from serpapi import GoogleSearch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# from typing import Optional

# Load environment variables from .env file
# load_dotenv()

# Retrieve the API key from the environment variables
OPENAI_API_KEY = 'sk-proj-yrEmjYbIFZ6gL86hSnATT3BlbkFJhfrAhqAPT4jZOFQ43UoO'
SERPAPI_API_KEY = 'd1c49ffa35ff5e629a81bb1365e6b6e13b62912262e12f0d067a656dd3a7d202'

client = OpenAI(api_key=OPENAI_API_KEY)



# Allow requests from the Next.js frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)




# ChatGPT
def get_possible_destinations(start_date, end_date, trip_type, numeber_of_destinations=5, chosen_cities=[]):
    prompt = (
        f"Suggest {numeber_of_destinations} possible places in the world for a {trip_type} trip "
        f"from {start_date} to {end_date}. Consider the season, weather, and activities "
        f"suitable for this type of trip during this time."
    )
    
    if chosen_cities is not None and len(chosen_cities) > 0:
        prompt += f" Exclude the following cities: {', '.join(chosen_cities)}."
        
    prompt += (
        f" For each destination, provide the closest city with an airport and the airport code."
        f" Respond only with the city and destination names and airport code in the following format: "
        f"[index]. City: [city name], Destination: [destination name], Airport: [airport code]."
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a travel assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    print("prompt", prompt)
    destinations = response.choices[0].message.content
    print(destinations)
    return destinations

def create_daily_plan(destination, start_date, end_date, trip_type):
    prompt = (
        f"Create a daily plan for a {trip_type} trip to {destination} from {start_date} to {end_date}. "
        f"Consider the month of the trip and the local climate. Include a mix of activities that fit the trip type, "
        f"recommend places to eat for breakfast, lunch, and dinner, must-see attractions, and any special events happening during the trip dates. "
        f"Only provide an itinerary for each day of the trip in the following format:\n"
        f"Day X (YYYY-MM-DD):\n"
        f"- Morning: [Morning activities and places to eat breakfast]\n"
        f"- Afternoon: [Afternoon activities and places to eat lunch]\n"
        f"- Evening: [Evening activities and places to eat dinner]\n"
        f"- Attractions: [List of must-see attractions for the day]\n"
        f"- Special Events: [Any special events happening on that day]\n"
        f"Example:\n"
        f"Day 1 (2024-08-01):\n"
        f"- Morning: Arrival in Vancouver, check into your hotel and freshen up. Breakfast at Cafe Medina.\n"
        f"- Afternoon: Explore Stanley Park, visit the Vancouver Aquarium. Lunch at Stanley's Bar and Grill.\n"
        f"- Evening: Dinner at Miku Vancouver for delicious sushi. Stroll along the Vancouver Seawall.\n"
        f"- Attractions: Stanley Park, Vancouver Aquarium, Vancouver Seawall.\n"
        f"- Special Events: Summer Night Market.\n"
        f"Repeat this format for each day from {start_date} to {end_date}, ensuring that each day's plan is detailed and tailored to the specified trip type."
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a travel assistant. You are helping a user plan a trip with a detailed itinerary for each day."},
            {"role": "user", "content": prompt}
        ]
    )
    plan = response.choices[0].message.content.strip()
    return plan

def generate_trip_images(destination, trip_type):
    image_descriptions = [ "A popular tourist attraction or landmark.", "A scenic outdoor activity or natural landscape.", "A local restaurant or cuisine typical of the area.", "A cultural or special event happening in the area." ]
    image_urls = []
    for index in range(4):
        prompt = (
            f"Generate a high-quality image that represent a {trip_type} trip to {destination}. "
            f"Generte {image_descriptions[index]}\n"
            f"Ensure the image is visually appealing and accurately represent the destination."
        )
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_urls.append(response.data[0].url)
    
    return image_urls


# HotelSearcher
def get_most_expensive_hotel(data, budget):
    print("data", data)
    properties = data['properties']

    if not properties:
        return None

    print("properties", properties[0])
    chosen_hotel_data = {}
    name = properties[0]['name'] 
    current_max_price =  0 
    limited_price = budget
    image_url = properties[0]['images'][0]
    
    # print("*"*50)
    # print("properties", properties)
    # print("*"*50)
    
    for property in properties:
        # print("property", property)
        if ('total_rate' in property) and ('extracted_lowest' in property['total_rate']):
            print("property['total_rate']['extracted_lowest']", property['total_rate']['extracted_lowest'])
            price = property['total_rate']['extracted_lowest']
            if price > current_max_price and price <= limited_price:
                print("price", price, "max_price", current_max_price)
                current_max_price = price
                name = property['name']
                image_url = property['images'][0]
    
    chosen_hotel_data['name'] = name
    chosen_hotel_data['price'] = current_max_price
    chosen_hotel_data['image_url'] = image_url
    
    print(name)

    return chosen_hotel_data

def get_hotels_in_budget(destinations, budgets, start_date, end_date):
    hotels = {}
    for index, destination in enumerate(destinations):
        params = {
        "engine": "google_hotels",
        "q": f"hotels in {destination}",
        "check_in_date": start_date,
        "check_out_date": end_date,
        "adults": "1",
        "currency": "USD",
        "gl": "us",
        "hl": "en",
        "max_price": budgets[index],
        "api_key": SERPAPI_API_KEY,
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        print("results", results)
        chosen_hotel_data = get_most_expensive_hotel(results, budgets[index])
        print("&"*50)
        print("chosen_hotel_data", chosen_hotel_data, "budgets[index]", budgets[index])
        print("&"*50)
        if chosen_hotel_data is not None:
            print("inside the data")
            hotels[destination] = chosen_hotel_data
       
    return hotels


# FlightSearcher
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

def get_flights(cities, airport_codes, start_date, end_date, budget, destinations):
    flights = []
    return_flights = []
    flight_prices = [0, 0, 0, 0, 0]
    
    # validations
    if len(cities) != len(airport_codes):
        print("The number of cities and airport codes should be the same.")
        return flights, return_flights, []

    chosen_cities = []
    chosen_destinations = []
    
    # each destination is a name
    for index, city in enumerate(cities):
        print(f"Searching for flights to {city}...")

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

        cheapest_flight, flight_prices[index] = get_cheapest_flight(flight_result, budget[index], city)
    
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
                print("-"*50)
                print(f"Chosen destination: {destinations[index]}") 
                print("-"*50)
                chosen_destinations.append(destinations[index])
                print("-"*50)
                print("chosen_destinations", chosen_destinations)
                print("-"*50)
    
    print('='*50)
    print("flights", flights)
    print('*'*50)
    print("return_flights", return_flights)
    print('*'*50)
    print("chosen_cities", chosen_cities)
    print('='*50)
    print("flight_prices", flight_prices)
    print('='*50)
    print("chosen_destinations", chosen_destinations)
    print('='*50)

    return flights, return_flights, chosen_cities, flight_prices, chosen_destinations






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

@app.get("/search")
def planTrip():
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
        # trip_plan = ChatGPTFetcher.create_daily_plan(chosen_option['destination'], start_date, end_date, trip_type)
        trip_plan = create_daily_plan(chosen_option['destination'], start_date, end_date, trip_type)
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
    trip_images = generate_trip_images(chosen_option['destination'], trip_type)
    print("trip_images", trip_images)

    print("\nTrip Summary:")
    print(f"Destination: {chosen_option['destination']}")
    print(f"flights: {[chosen_option['going_flight'], chosen_option['returning_flight']]}")
    print(f"Hotel: {chosen_option['name']}")
    print(f"Hotel image: {chosen_option['image_url']['original_image']}")
    print(f"Total Cost: ${chosen_option['price']}")
    print(f"Trip Plan:\n{trip_plan}")
    print("\nTrip Images:")
    for idx, img_url in enumerate(trip_images):
        print(f"Image {idx + 1}: {img_url}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)