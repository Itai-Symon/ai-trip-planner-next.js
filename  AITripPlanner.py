from openai import OpenAI
from serpapi import GoogleSearch
import requests
from datetime import datetime
import json
from dotenv import load_dotenv
import os
import FlightSearcher
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

def get_possible_destinations(start_date, end_date, trip_type, numeber_of_destinations=5):
    prompt = (
    f"Suggest {numeber_of_destinations} possible places in the world for a {trip_type} trip "
    f"from {start_date} to {end_date}. Consider the season, weather, and activities "
    f"suitable for this type of trip during this time."
    f"for each destination, provide the closest city with an airport and the airport code."
    f"respond only with the city and destination names and airport code in the following format: "
    f"[index]. City: [city name], Destination: [destination name], Airport: [airport code]."
    )
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a travel assistant."},
        {"role": "user", "content": prompt}
    ])
    destinations = response.choices[0].message.content
    print(destinations)
    return destinations

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

def get_hotel_in_budget(destinations, budget, start_date, end_date):
    hotels = []
    for destination in destinations:
        params = {
            "engine": "google_hotels",
            "q": destination,
            "start_date": start_date,
            "end_date": end_date,
            "api_key": SERPAPI_API_KEY
        }
        hotels_search = GoogleSearch(params)
        results = hotels_search.get_dict()
        hotel = max(results['hotels_results'], key=lambda x: x['price'], default=None)
        if hotel and hotel['price'] <= budget:
            hotels.append({
                "destination": destination,
                "hotel": hotel['name'],
                "price": hotel['price']
            })
    return hotels

def create_daily_plan(destination, start_date, end_date):
    prompt = f"Create a daily plan for a trip to {destination} from {start_date} to {end_date}."
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a travel assistant."},
        {"role": "user", "content": prompt}
    ])
    plan = response.choices[0].message.content.strip()
    return plan

def generate_trip_images(destination):
    prompt = f"Generate 4 images showing a {destination} trip."
    response = client.images.generate(model="dall-e",
    prompt=prompt,
    n=4)
    images = [img['url'] for img in response.data]
    return images

def display_options(hotels):
    for idx, hotel in enumerate(hotels):
        print(f"Option {idx + 1}: {hotel['destination']} - {hotel['hotel']} - ${hotel['price']}")

    choice = int(input("Choose a destination (1-5): ")) - 1
    return hotels[choice]

def main():
    start_date, end_date, budget, trip_type = get_trip_details()
    serapi_tries = 0
    possible_destinations = []
    print("buget", budget)
    while len(possible_destinations) < 5 and serapi_tries < 3:
        possible_destinations = get_possible_destinations(start_date, end_date, trip_type)
        cities, destinations, airport_codes = parse_destinations(possible_destinations)

        flights_info = FlightSearcher.get_flights(cities, airport_codes, start_date, end_date, budget)
        print('-'*50)
        print("flights_info", flights_info)
        print('-'*50)
        serapi_tries += 1

    # while len(flights_info) != 5:
    #     print("still need more flights...")
    #     numer_of_new_destinations = 5 - len(flights_info)
    #     new_destinations = get_possible_destinations(start_date, end_date, trip_type, numer_of_new_destinations)
    #     new_cities, new_destinations = parse_destinations(new_destinations)
    #     flights_info += FlightSearcher.get_flights(new_cities, start_date, end_date, budget)

    # print(" flights", flights_info)
    # for info in flights_info:
    #     print("info", info)

    # hotels = get_hotel_in_budget(destinations, budget, start_date, end_date)
    # print("hotels", hotels)
    # if not hotels:
        # print("No suitable hotels found within the budget.")
        # return

    # chosen_option = display_options(hotels)
    # trip_plan = create_daily_plan(chosen_option['destination'], start_date, end_date)
    # trip_images = generate_trip_images(chosen_option['destination'])

    # print("\nTrip Summary:")
    # print(f"Destination: {chosen_option['destination']}")
    # print(f"Hotel: {chosen_option['hotel']}")
    # print(f"Total Cost: ${chosen_option['price']}")
    # print(f"Trip Plan:\n{trip_plan}")
    # print("\nTrip Images:")
    # for idx, img_url in enumerate(trip_images):
    #     print(f"Image {idx + 1}: {img_url}")

if __name__ == "__main__":
    main()
