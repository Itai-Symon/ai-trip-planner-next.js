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
    chosen_hotel_data = {}
    name = ''
    max_price = data['properties'][0]['total_rate']['extracted_lowest']
        
    for property in data['properties']:
        if 'total_rate' in property and 'extracted_lowest' in property['total_rate']:
            price = property['total_rate']['extracted_lowest']
            if price > max_price:
                print("price", price, "max_price", max_price)
                max_price = price
                name = property['name']
                check_in_time = property['check_in_time']
                check_out_time = property['check_out_time'] 
                image_url = property['images'][0]
                overall_rating = property['overall_rating']
    
    chosen_hotel_data['name'] = name
    chosen_hotel_data['price'] = max_price
    chosen_hotel_data['check_in_time'] = check_in_time
    chosen_hotel_data['check_out_time'] = check_out_time
    chosen_hotel_data['image_url'] = image_url
    chosen_hotel_data['overall_rating'] = overall_rating


    print(name)

    return chosen_hotel_data

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
        # retrieve the hotel with the maximum price that is within the budget[index]
        chosen_hotel_data = get_most_expensive_hotel(results)
        if chosen_hotel_data and chosen_hotel_data['price'] < budget[index]:
            hotels[chosen_hotel_data['name']] = chosen_hotel_data
        break

    return hotels
