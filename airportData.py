import airportsdata

# Load airport data
airports = airportsdata.load('IATA')  # Or 'ICAO'

city = input("Enter a city: ")
# Find the airport code according to the city
airport_code_according_to_city = None
for code, airport in airports.items():
    if airport['city'].lower() == city.lower():
        airport_code_according_to_city = code
        break

if airport_code_according_to_city:
    print(f"The airport code for {city} is {airport_code_according_to_city}.")
else:
    print(f"No airport found for the city: {city}.")