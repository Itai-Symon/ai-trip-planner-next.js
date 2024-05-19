from openai import OpenAI
import requests
from datetime import datetime
import json

# Replace with your actual API keys
OPENAI_API_KEY = 'sk-proj-yrEmjYbIFZ6gL86hSnATT3BlbkFJhfrAhqAPT4jZOFQ43UoO'
# SERPAPI_API_KEY = '5042931777b95a7ae2c59546a8a5b318c552478ed451ee0858c2c81b86287cdd'
client = OpenAI(api_key=OPENAI_API_KEY)

def get_trip_details():
    start_date = input("Enter the start date of your trip (YYYY-MM-DD): ")
    end_date = input("Enter the end date of your trip (YYYY-MM-DD): ")
    budget = float(input("Enter your total budget in USD: "))
    trip_type = input("Enter the type of trip (ski/beach/city): ")

    return start_date, end_date, budget, trip_type

def get_possible_destinations(start_date, end_date, trip_type):
    prompt = (
    f"Suggest 5 possible places in the world for a {trip_type} trip "
    f"from {start_date} to {end_date}. Consider the season, weather, and activities "
    f"suitable for this type of trip during this time."
    )
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a travel assistant."},
        {"role": "user", "content": prompt}
    ])
    destinations = response.choices[0].message.content.strip().split("\n")
    return destinations

def find_hotels(destinations, budget, start_date, end_date):
    hotels = []
    for destination in destinations:
        params = {
            "engine": "google_hotels",
            "q": destination,
            "start_date": start_date,
            "end_date": end_date,
            "api_key": SERPAPI_API_KEY
        }
        response = requests.get('https://serpapi.com/search', params=params)
        hotels_data = response.json()
        hotel = max(hotels_data['hotels_results'], key=lambda x: x['price'], default=None)
        if hotel and hotel['price'] <= budget:
            hotels.append({
                "destination": destination,
                "hotel": hotel['name'],
                "price": hotel['price']
            })
    return hotels

def get_trip_plan(destination, start_date, end_date):
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
    destinations = get_possible_destinations(start_date, end_date, trip_type)
    print("destinations", destinations)
    # hotels = find_hotels(destinations, budget, start_date, end_date)

    # if not hotels:
        # print("No suitable hotels found within the budget.")
        # return

    # chosen_option = display_options(hotels)
    # trip_plan = get_trip_plan(chosen_option['destination'], start_date, end_date)
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
