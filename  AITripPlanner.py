from openai import OpenAI
from serpapi import GoogleSearch
import requests
from datetime import datetime
import json
from dotenv import load_dotenv
import os
import FlightSearcher
import HotelSearcher

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

def display_options(hotels, destinations):
    for idx, destination in enumerate(destinations):
        print(f"Option {idx + 1}: {hotels[destination]} - {hotels[destination]['name']} - ${hotels[destination]['price']}")

    choice = int(input("Choose a destination (1-5): ")) - 1
    return hotels[destinations[choice]]

def print_flights_state(going_flights_info, returning_flights_info, serapi_tries):
    print('-'*50)
    print("going flight information, amount:", len(going_flights_info))
    print(going_flights_info)
    print('#'*50)
    print("returning flight information, amount:", len(returning_flights_info))
    print(returning_flights_info)
    print('-'*50)

    print('*'*50)
    print("missing destinations:", 5 - len(going_flights_info))
    print("try number:", serapi_tries)
    print('*'*50)

def main():
    # start_date, end_date, budget, trip_type = get_trip_details()
    start_date, end_date, budget, trip_type = '2024-08-01', '2024-08-10', 1000, 'city'
    
    serapi_tries = 0
    number_of_missing_destinations = 5
    possible_destinations = []
    chosen_cities = []
    going_flights_info = []
    returning_flights_info = []
    budgets = [budget] * 5
   
    while number_of_missing_destinations > 0 and serapi_tries < 1:
        # possible_destinations = get_possible_destinations(start_date, end_date, trip_type, number_of_missing_destinations, chosen_cities)
        # cities, destinations, airport_codes = parse_destinations(possible_destinations)
        
        # added_going_flights_info, added_returning_flights_info, chosen_cities, successful_retrieved_flights, budgets = FlightSearcher.get_flights(cities, airport_codes, start_date, end_date, budgets)
        # going_flights_info.append(added_going_flights_info)
        # returning_flights_info.append(added_returning_flights_info)
        # print_flights_state(going_flights_info, returning_flights_info, serapi_tries)
        # number_of_missing_destinations -= successful_retrieved_flights

        serapi_tries += 1

    print("finished getting flights") 
   
    # hotels = HotelSearcher.get_hotels_in_budget(destinations, budgets, start_date, end_date)
    
    # if not hotels:
    #     print("No suitable hotels found within the budget.")
    #     return
    # print("budgets before subtraction", budgets)
    # for index, destination in enumerate(destinations):
    #     budgets[index] -= hotels[destination]['price']
    # print("budgets after subtraction", budgets)

    print("finished getting hotels")

    hotels = {'Iceland': {'name': 'Syðstibær Guesthouse - Double Room', 'price': 780, 'image_url': {'thumbnail': 'https://lh6.googleusercontent.com/proxy/25jsSNNJgs8-K7mhDH-Xy8sVflMwXvgQGnpZBL8Foa6eyFKD_KaIbjFRpMcgg6eSqtU2iCDqfozszHw9QmGKHO5j5OG9csGFfmAiMY2SgEruOnBUZwwU0NP3wL9OjuT4cDyc-evUQVOetmNpjlc00MS_kmLvtQ=s287-w287-h192-n-k-no-v1', 'original_image': 'https://q-xx.bstatic.com/xdata/images/hotel/max1024x768/309852219.jpg?k=c407f72fb1277ae1b5e64903faf08f380ba6f9c6eee9b4be7a328bda4502c442&o='}}, 'Netherlands': {'name': 'Trendy Tiny Houses Bovenweg', 'price': 977, 'image_url': {'thumbnail': 'https://lh5.googleusercontent.com/proxy/JFPUmM4Armxz0z9cp7SQfx7b8ncEmqq31r35PqW7HnsdBUGnNKpLpZhpsZFNhBgOZhIv_JTeiWkfrA02U5MKONss5-rcjdNE0kMAQNlb-6lTgzqfQdPHCHa_057i6eICyY9I354Ir8HsQe2-lF21Jz_8sSu1Iw=s287-w287-h192-n-k-no-v1', 'original_image': 'https://q-xx.bstatic.com/xdata/images/hotel/max1440x1080/208218765.jpg?k=d9cfd024a1a5e24831d4c0511fc365d93e98da3e2b8cfe3fb1ebc12981e95370&o='}}, 'Japan': {'name': "Hotel M's Plus Shijo Omiya", 'price': 474, 'image_url': {'thumbnail': 'https://lh6.googleusercontent.com/proxy/nqwH8kQm7R0G3YMN_z5wcauiK7278bvEXk2QSXm3FtgNml7vbtOCq3e_EDHNfSXmPvo3xxSrR-i5xWZ1k7pQe_RP5YX4quxLFV2vzcmPSA7vJFs2cdgtAFrvaEzdAZj-DT05Hexd56Lw7jiMp6L021Y7qTiomA=s287-w287-h192-n-k-no-v1', 'original_image': 'https://photos.hotelbeds.com/giata/original/63/637861/637861a_hb_a_003.jpg'}}, 'Canada': {'name': 'Pangea Pod Hotel', 'price': 875, 'image_url': {'thumbnail': 'https://lh5.googleusercontent.com/p/AF1QipNikPcbU7oLm4Yc7P-9QlC71pJ7Z_9AXIsDYx52=s287-w287-h192-n-k-no-v1', 'original_image': 'https://lh5.googleusercontent.com/p/AF1QipNikPcbU7oLm4Yc7P-9QlC71pJ7Z_9AXIsDYx52=s10000'}}, 'Spain': {'name': 'Beachfront studio apartment', 'price': 817, 'image_url': {'thumbnail': 'https://lh6.googleusercontent.com/proxy/Jy37xmRXalmXfsWbqx2-zqkf-5kpKD79rcmuJQm55lO7QkWPhAPLuHbiZpixY8MyUt2JSzoPiuECNQjddcIpPcmgXuI_KEnIiUXPIuKJ6iftrTx4ueyw96i4ZYSyYFM4NIbhs_1QldgBeeF-C4RF4xBcAwzFrg=s287-w287-h192-n-k-no-v1', 'original_image': 'https://media-cdn.tripadvisor.com/media/vr-splice-j/00/d5/ae/6e.jpg'}}}
    destinations = ['Iceland', 'Netherlands', 'Japan', 'Canada', 'Spain']

    chosen_option = display_options(hotels, destinations)
    
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
