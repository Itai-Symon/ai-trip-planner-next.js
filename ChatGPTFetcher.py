from openai import OpenAI
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

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
        f" Morning: [Morning activities and places to eat breakfast]\n"
        f" Afternoon: [Afternoon activities and places to eat lunch]\n"
        f" Evening: [Evening activities and places to eat dinner]\n"
        f" Attractions: [List of must-see attractions for the day]\n"
        f" Special Events: [Any special events happening on that day]\n"
        f"Example:\n"
        f"Day 1 (2024-08-01):\n"
        f" Morning: Arrival in Vancouver, check into your hotel and freshen up. Breakfast at Cafe Medina.\n"
        f" Afternoon: Explore Stanley Park, visit the Vancouver Aquarium. Lunch at Stanley's Bar and Grill.\n"
        f" Evening: Dinner at Miku Vancouver for delicious sushi. Stroll along the Vancouver Seawall.\n"
        f" Attractions: Stanley Park, Vancouver Aquarium, Vancouver Seawall.\n"
        f" Special Events: Summer Night Market.\n"
        f"Repeat this format for each day from {start_date} to {end_date}."
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

