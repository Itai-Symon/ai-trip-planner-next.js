import openai
import requests
from datetime import datetime
from serapi import SerapiClient

# Set up OpenAI API credentials
openai.api_key = "YOUR_OPENAI_API_KEY"

# Set up Serapi client for hotel search
serapi_client = SerapiClient("YOUR_SERAPI_API_KEY")

# Function to get destination suggestions from OpenAI
def get_destination_suggestions(trip_type, trip_month):
    prompt = f"Suggest 5 possible places in the world to travel to for a {trip_type} trip in {trip_month}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    suggestions = response.choices[0].text.strip().split("\n")
    return suggestions

# Function to find hotels for a given destination
def find_hotel(destination, budget):
    try:
        hotels = serapi_client.search_hotels(destination)
        sorted_hotels = sorted(hotels, key=lambda x: x.total_price, reverse=True)
        for hotel in sorted_hotels:
            if hotel.total_price <= budget:
                return hotel
    except Exception as e:
        print(f"Error finding hotel for {destination}: {e}")
    return None

# Function to create a trip plan using OpenAI
def create_trip_plan(destination, start_date, end_date, trip_type):
    duration = (end_date - start_date).days + 1
    prompt = f"Create a {duration}-day trip plan for a {trip_type} trip to {destination} from {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Function to generate trip images using OpenAI DALL-E
def generate_trip_images(destination, trip_type):
    images = []
    for prompt in [
        f"A {trip_type} trip to {destination}",
        f"Famous landmarks in {destination}",
        f"Scenic views of {destination}",
        f"Local cuisine in {destination}",
    ]:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
        )
        images.append(response["data"][0]["url"])
    return images

# Main function
def main():
    # Get user input
    start_date = input("Enter start date of your trip (YYYY-MM-DD): ")
    end_date = input("Enter end date of your trip (YYYY-MM-DD): ")
    budget = float(input("Enter your total budget in USD: "))
    trip_type = input("Enter the type of trip (ski/beach/city): ")

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    trip_month = start_date.strftime("%B")

    # Get destination suggestions
    suggestions = get_destination_suggestions(trip_type, trip_month)

    # Find hotels and create trip options
    options = []
    for destination in suggestions:
        hotel = find_hotel(destination, budget)
        if hotel:
            total_cost = hotel.total_price
            options.append(
                {
                    "destination": destination,
                    "hotel": hotel,
                    "total_cost": total_cost,
                }
            )

    # Show options to the user and let them choose
    print("\nHere are the trip options we found for you:\n")
    for i, option in enumerate(options, start=1):
        print(f"Option {i}:")
        print(f"Destination: {option['destination']}")
        print(f"Hotel: {option['hotel'].name}")
        print(f"Total Cost: ${option['total_cost']:.2f}\n")

    choice = int(input("Enter the option number you want to choose: "))
    chosen_option = options[choice - 1]

    # Create trip plan and generate images
    trip_plan = create_trip_plan(
        chosen_option["destination"],
        start_date,
        end_date,
        trip_type,
    )
    trip_images = generate_trip_images(
        chosen_option["destination"], trip_type
    )

    # Show the final trip plan
    print("\nHere's your trip plan:\n")
    print(f"Destination: {chosen_option['destination']}")
    print(f"Hotel: {chosen_option['hotel'].name}")
    print(f"Total Cost: ${chosen_option['total_cost']:.2f}\n")
    print("Daily Plan:\n")
    print(trip_plan)
    print("\nTrip Images:\n")
    for i, image_url in enumerate(trip_images, start=1):
        print(f"Image {i}: {image_url}")

if __name__ == "__main__":
    main()