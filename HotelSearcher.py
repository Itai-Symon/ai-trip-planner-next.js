from openai import OpenAI
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')    
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def get_most_expensive_hotel(data, budget):
    print("data", data)
    try:
        chosen_hotel_data = {}
        chosen_hotel_data['name'] = 'No hotel found'
        chosen_hotel_data['price'] = 0
        chosen_hotel_data['image_url'] = ''

        if 'properties' not in data or not data['properties']:
            return chosen_hotel_data
       
        properties = data['properties']
        

        print("properties", properties[0])
        
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
    except Exception as e:
        chosen_hotel_data['name'] = 'No hotel found'
        chosen_hotel_data['price'] = 0
        chosen_hotel_data['image_url'] = ''
    
    finally:
        return chosen_hotel_data

def get_hotels_in_budget(destinations, budgets, start_date, end_date):
    hotels = {}
    print("maximumprice for hotels", budgets)
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
        if chosen_hotel_data is not None and chosen_hotel_data['price'] > 0:
            print("inside the data")
            hotels[destination] = chosen_hotel_data

        if hotels is None or not hotels:
            hotels = []
       
    return hotels
