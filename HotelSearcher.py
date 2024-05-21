from openai import OpenAI
from serpapi import GoogleSearch
import airportsdata
from dotenv import load_dotenv
import os
import json


# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def get_most_expensive_hotel(data):
    most_expensive_hotel = {}
    max_price = 0
        
    for property in data['properties']:
        if 'total_rate' in property and 'extracted_lowest' in property['total_rate']:
            price = property['total_rate']['extracted_lowest']
            if price > max_price:
                print("price", price, "max_price", max_price)
                max_price = price
                most_expensive_hotel = property

    print(most_expensive_hotel['name'])
    return most_expensive_hotel, max_price

def get_hotel_in_budget(destinations, budget, start_date, end_date):
    hotels = []
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
        "max_price": budget[index],
        "api_key": SERPAPI_API_KEY,
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        print("results", json.dumps(results, indent=4))
        parse_results = json.dumps(results, indent=4)

        # retrieve the hotel with the maximum price that is within the budget[index]
        hotel_name, hotel_price = get_most_expensive_hotel(parse_results)
        if hotel_name and hotel_price < budget[index]:
            hotels.append({
                "destination": destination,
                "hotel": hotel_name,
                "price": hotel_price
            })

    return hotels
