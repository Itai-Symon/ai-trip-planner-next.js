# # import airportsdata

# # # Load airport data
# # airports = airportsdata.load('IATA')  # Or 'ICAO'

# # city = input("Enter a city: ")
# # # Find the airport code according to the city
# # airport_code_according_to_city = None
# # for code, airport in airports.items():
# #     if airport['city'].lower() == city.lower():
# #         airport_code_according_to_city = code
# #         break

# # if airport_code_according_to_city:
# #     print(f"The airport code for {city} is {airport_code_according_to_city}.")
# # else:
# #     print(f"No airport found for the city: {city}.")


# # response = """
# # 1. City: Tokyo, Destination: Cherry Blossom Viewing in Shinjuku Gyoen Park
# # 2. City: Sydney, Destination: Bondi Beach for Surfing and Sunbathing
# # 3. City: Rio de Janeiro, Destination: Hiking to the Christ the Redeemer Statue
# # 4. City: Cape Town, Destination: Wine Tasting in Stellenbosch Winelands
# # 5. City: Reykjavik, Destination: Northern Lights Viewing in Thingvellir National Park
# # """
# # print(response)

# # # Split the response by newline character to get individual lines
# # lines = response.strip().split('\n')
# # cities = []
# # destinations = []
# # # Iterate over each line and extract city and destination
# # for line in lines:
# #     parts = line.split(', Destination: ')
# #     city = parts[0].split('City: ')[1].strip()
# #     destination = parts[1].strip()
# #     cities.append(city)
# #     destinations.append(destination)

# # # Print the extracted cities and destinations
# # for i in range(len(cities)):
# #     print(f"City: {cities[i]}, Destination: {destinations[i]}")

# # print(cities)
# # print(destinations)
# import json
# flight_result = {'search_metadata': {'id': '664b5b382bc7d8cb353faa62', 'status': 'Success', 'json_endpoint': 'https://serpapi.com/searches/0285cad94af724c6/664b5b382bc7d8cb353faa62.json', 'created_at': '2024-05-20 14:16:24 UTC', 'processed_at': '2024-05-20 14:16:24 UTC', 'google_flights_url': 'https://www.google.com/travel/flights?hl=en&gl=us&curr=USD&q=Flights+to+NRT+from+TLV+on+2024-06-01+through+2024-07-01', 'raw_html_file': 'https://serpapi.com/searches/0285cad94af724c6/664b5b382bc7d8cb353faa62.html', 'prettify_html_file': 'https://serpapi.com/searches/0285cad94af724c6/664b5b382bc7d8cb353faa62.prettify', 'total_time_taken': 1.16}, 'search_parameters': {'engine': 'google_flights', 'hl': 'en', 'gl': 'us', 'departure_id': 'TLV', 'arrival_id': 'NRT', 'outbound_date': '2024-06-01', 'return_date': '2024-07-01', 'currency': 'USD'}, 'best_flights': [{'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 13:25'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 17:45'}, 'duration': 200, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1212', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 149 kg'], 'often_delayed_by_over_30_min': True{'departure_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 02:40'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 17:35'}, 'duration': 595, 'airplane': 'Airbus A380', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 318', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 671 kg'], 'overnight': True'name': 'Dubai International Airport', 'id': 'DXB', 'overnight': True{'this_flight': 820000, 'typical_for_this_route': 895000, 'difference_percent': -8}, 'price': 1219, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ3hHV2pFeU1USjhSVXN6TVRnYUN3anJ0d2NRQWhvRFZWTkVPQnh3NjdjSCIsW1siVExWIiwiMjAyNC0wNi0wMSIsIkRYQiIsbnVsbCwiRloiLCIxMjEyIl0sWyJEWEIiLCIyMDI0LTA2LTAyIiwiTlJUIixudWxsLCJFSyIsIjMxOCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 23:30'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 17:05'}, 'duration': 695, 'airplane': 'Boeing 787', 'airline': 'El Al', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LY.png', 'travel_class': 'Economy', 'flight_number': 'LY 91', 'legroom': '31 in', 'extensions': ['Average legroom (31 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 634 kg'], 'overnight': True'often_delayed_by_over_30_min': True'typical_for_this_route': 895000, 'difference_percent': -29}, 'price': 1661, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LY.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ1JNV1RreEdnc0lrNUVLRUFJYUExVlRSRGdjY0pPUkNnPT0iLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJOUlQiLG51bGwsIkxZIiwiOTEiXV1d'}], 'other_flights': [{'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 15:20'}, 'arrival_airport': {'name': 'Vienna International Airport', 'id': 'VIE', 'time': '2024-06-01 18:05'}, 'duration': 225, 'airplane': 'Airbus A321', 'airline': 'Austrian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/OS.png', 'travel_class': 'Economy', 'flight_number': 'OS 858', 'legroom': '29 in', 'extensions': ['Below average legroom (29 in)', 'Wi-Fi for a fee', 'In-seat USB outlet', 'Carbon emissions estimate: 208 kg'], 'often_delayed_by_over_30_min': TrueInternational Airport', 'id': 'VIE', 'time': '2024-06-02 13:30'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 08:50'}, 'duration': 740, 'airplane': 'Boeing 777', 'airline': 'Austrian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/OS.png', 'travel_class': 'Economy', 'flight_number': 'OS 51', 'ticket_also_sold_by': ['ANA'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 668 kg'], 'overnight': True[{'duration': 1165, 'name': 'Vienna International Airport', 'id': 'VIE', 'overnight': True'carbon_emissions': {'this_flight': 877000, 'typical_for_this_route': 895000, 'difference_percent': -2}, 'price': 785, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/OS.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ3BQVXpnMU9IeFBVelV4R2dzSW4rVUVFQUlhQTFWVFJEZ2NjSi9sQkE9PSIsW1siVExWIiwiMjAyNC0wNi0wMSIsIlZJRSIsbnVsbCwiT1MiLCI4NTgiXSxbIlZJRSIsIjIwMjQtMDYtMDIiLCJOUlQiLG51bGwsIk9TIiwiNTEiXV1d'}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 17:05'}, 'arrival_airport': {'name': 'Munich International Airport', 'id': 'MUC', 'time': '2024-06-01 20:15'}, 'duration': 250, 'airplane': 'Airbus A321neo', 'airline': 'Lufthansa', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LH.png', 'travel_class': 'Economy', 'flight_number': 'LH 681', 'legroom': '29 in', 'extensions': ['Below average legroom (29 in)', 'In-seat USB outlet', 'Carbon emissions estimate: 187 kg']}, {'departure_airport': {'name': 'Munich International Airport', 'id': 'MUC', 'time': '2024-06-02 11:55'}, 'arrival_airport': {'name': 'Kansai International Airport', 'id': 'KIX', 'time': '2024-06-03 06:55'}, 'duration': 720, 'airplane': 'Airbus A350', 'airline': 'Lufthansa', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LH.png', 'travel_class': 'Economy', 'flight_number': 'LH 742', 'ticket_also_sold_by': ['ANA'], 'legroom': '31 in', 'extensions': ['Average legroom (31 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 543 kg'], 'overnight': True'ITM', 'time': '2024-06-03 14:15'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 15:40'}, 'duration': 85, 'airplane': 'Boeing 737', 'airline': 'ANA', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/NH.png', 'travel_class': 'Economy', 'flight_number': 'NH 2178', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Free Wi-Fi', 'Stream media to your device', 'Carbon emissions estimate: 82 kg']}], 'layovers': [{'duration': 940, 'name': 'Munich International Airport', 'id': 'MUC', 'overnight': TrueInternational Airport (Itami Airport)', 'id': 'KIX'}], 'total_duration': 2435, 'carbon_emissions': {'this_flight': 813000, 'typical_for_this_route': 895000, 'difference_percent': -9}, 'price': 809, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEpNU0RZNE1YeE1TRGMwTW54T1NESXhOemdhQ3dqMTl3UVFBaG9EVlZORU9CeHc5ZmNFIixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiTVVDIixudWxsLCJMSCIsIjY4MSJdLFsiTVVDIiwiMjAyNC0wNi0wMiIsIktJWCIsbnVsbCwiTEgiLCI3NDIiXSxbIklUTSIsIjIwMjQtMDYtMDMiLCJOUlQiLG51bGwsIk5IIiwiMjE3OCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 18:15'}, 'arrival_airport': {'name': 'Zurich Airport', 'id': 'ZRH', 'time': '2024-06-01 21:35'}, 'duration': 260, 'airplane': 'Airbus A320neo', 'airline': 'SWISS', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LX.png', 'travel_class': 'Economy', 'flight_number': 'LX 253', 'legroom': '29 in', 'extensions': ['Below average legroom (29 in)', 'Carbon emissions estimate: 179 kg']}, {'departure_airport': {'name': 'Zurich Airport', 'id': 'ZRH', 'time': '2024-06-02 13:05'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 08:50'}, 'duration': 765, 'airplane': 'Boeing 777', 'airline': 'SWISS', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LX.png', 'travel_class': 'Economy', 'flight_number': 'LX 160', 'ticket_also_sold_by': ['ANA'], 'legroom': '31 in', 'extensions': ['Average legroom (31 in)', 'Wi-Fi for a fee', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 759 kg'], 'overnight': True'name': 'Zurich Airport', 'id': 'ZRH', 'overnight': True'typical_for_this_route': 895000, 'difference_percent': 5}, 'price': 856, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LX.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ3RNV0RJMU0zeE1XREUyTUJvTENKR2NCUkFDR2dOVlUwUTRISENSbkFVPSIsW1siVExWIiwiMjAyNC0wNi0wMSIsIlpSSCIsbnVsbCwiTFgiLCIyNTMiXSxbIlpSSCIsIjIwMjQtMDYtMDIiLCJOUlQiLG51bGwsIkxYIiwiMTYwIl1dXQ=='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 15:35'}, 'arrival_airport': {'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'time': '2024-06-01 19:50'}, 'duration': 255, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 419', 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'Stream media to your device', 'Carbon emissions estimate: 188 kg']}, {'departure_airport': {'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'time': '2024-06-02 22:35'}, 'arrival_airport': {'name': 'Incheon International Airport', 'id': 'ICN', 'time': '2024-06-03 16:00'}, 'duration': 685, 'airplane': 'Boeing 787', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 672', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 664 kg'], 'overnight': True17:40'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 20:05'}, 'duration': 145, 'airplane': 'Boeing 787', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 672', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 118 kg']}], 'layovers': [{'duration': 1605, 'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'overnight': True'ICN'}], 'total_duration': 2790, 'carbon_emissions': {'this_flight': 971000, 'typical_for_this_route': 895000, 'difference_percent': 8}, 'price': 1018, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEZGVkRReE9YeEZWRFkzTW54RlZEWTNNaG9MQ01tYUJoQUNHZ05WVTBRNEhIREptZ1k9IixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiQUREIixudWxsLCJFVCIsIjQxOSJdLFsiQUREIiwiMjAyNC0wNi0wMiIsIklDTiIsbnVsbCwiRVQiLCI2NzIiXSxbIklDTiIsIjIwMjQtMDYtMDMiLCJOUlQiLG51bGwsIkVUIiwiNjcyIl1dXQ=='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 00:50'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 05:10'}, 'duration': 200, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1808', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 156 kg'], 'overnight': True{'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 09:40'}, 'arrival_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-01 19:15'}, 'duration': 395, 'airplane': 'Airbus A380', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 372', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 418 kg']}, {'departure_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-01 22:10'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 06:20'}, 'duration': 370, 'airplane': 'Airbus A350', 'airline': 'THAI', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/TG.png', 'travel_class': 'Economy', 'flight_number': 'TG 640', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 341 kg'], 'overnight': True[{'duration': 270, 'name': 'Dubai International Airport', 'id': 'DXB'}, {'duration': 175, 'name': 'Suvarnabhumi Airport', 'id': 'BKK'}], 'total_duration': 1410, 'carbon_emissions': {'this_flight': 917000, 'typical_for_this_route': 895000, 'difference_percent': 2}, 'price': 1346, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEpHV2pFNE1EaDhSVXN6TnpKOFZFYzJOREFhQ3dpdm13Z1FBaG9EVlZORU9CeHdyNXNJIixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiRFhCIixudWxsLCJGWiIsIjE4MDgiXSxbIkRYQiIsIjIwMjQtMDYtMDEiLCJCS0siLG51bGwsIkVLIiwiMzcyIl0sWyJCS0siLCIyMDI0LTA2LTAxIiwiTlJUIixudWxsLCJURyIsIjY0MCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 00:50'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 05:10'}, 'duration': 200, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1808', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 156 kg'], 'overnight': True{'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 09:00'}, 'arrival_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-01 18:25'}, 'duration': 385, 'airplane': 'Boeing 777', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 370', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 414 kg']}, {'departure_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-01 22:10'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 06:20'}, 'duration': 370, 'airplane': 'Airbus A350', 'airline': 'THAI', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/TG.png', 'travel_class': 'Economy', 'flight_number': 'TG 640', 'ticket_also_sold_by': ['ANA'], 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 341 kg'], 'overnight': True'name': 'Suvarnabhumi Airport', 'id': 'BKK'}], 'total_duration': 1410, 'carbon_emissions': {'this_flight': 913000, 'typical_for_this_route': 895000, 'difference_percent': 2}, 'price': 1346, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEpHV2pFNE1EaDhSVXN6TnpCOFZFYzJOREFhQ3dpdm13Z1FBaG9EVlZORU9CeHdyNXNJIixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiRFhCIixudWxsLCJGWiIsIjE4MDgiXSxbIkRYQiIsIjIwMjQtMDYtMDEiLCJCS0siLG51bGwsIkVLIiwiMzcwIl0sWyJCS0siLCIyMDI0LTA2LTAxIiwiTlJUIixudWxsLCJURyIsIjY0MCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 23:55'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 04:15'}, 'duration': 200, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1626', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 149 kg'], 'overnight': True{'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 09:00'}, 'arrival_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-02 18:25'}, 'duration': 385, 'airplane': 'Boeing 777', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 370', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 414 kg']}, {'departure_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-02 22:10'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 06:20'}, 'duration': 370, 'airplane': 'Airbus A350', 'airline': 'THAI', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/TG.png', 'travel_class': 'Economy', 'flight_number': 'TG 640', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 341 kg'], 'overnight': True[{'duration': 285, 'name': 'Dubai International Airport', 'id': 'DXB', 'overnight': True'Suvarnabhumi Airport', 'id': 'BKK'}], 'total_duration': 1465, 'carbon_emissions': {'this_flight': 905000, 'typical_for_this_route': 895000, 'difference_percent': 1}, 'price': 1346, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEpHV2pFMk1qWjhSVXN6TnpCOFZFYzJOREFhQ3dpdm13Z1FBaG9EVlZORU9CeHdyNXNJIixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiRFhCIixudWxsLCJGWiIsIjE2MjYiXSxbIkRYQiIsIjIwMjQtMDYtMDIiLCJCS0siLG51bGwsIkVLIiwiMzcwIl0sWyJCS0siLCIyMDI0LTA2LTAyIiwiTlJUIixudWxsLCJURyIsIjY0MCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 15:35'}, 'arrival_airport': {'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'time': '2024-06-01 19:50'}, 'duration': 255, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 419', 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'Stream media to your device', 'Carbon emissions estimate: 188 kg']}, {'departure_airport': {'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'time': '2024-06-01 22:35'}, 'arrival_airport': {'name': 'Incheon International Airport', 'id': 'ICN', 'time': '2024-06-02 16:00'}, 'duration': 685, 'airplane': 'Boeing 787', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 672', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 664 kg'], 'overnight': True{'name': 'Incheon International Airport', 'id': 'ICN', 'time': '2024-06-02 17:40'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 20:05'}, 'duration': 145, 'airplane': 'Boeing 787', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 672', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 118 kg']}], 'layovers': [{'duration': 165, 'name': 'Bole Addis Ababa International Airport', 'id': 'ADD'}, {'duration': 100, 'name': 'Incheon International Airport', 'id': 'ICN'}], 'total_duration': 1350, 'carbon_emissions': {'this_flight': 971000, 'typical_for_this_route': 895000, 'difference_percent': 8}, 'price': 1395, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaE5GVkRReE9YeEZWRFkzTW54RlZEWTNNaU14R2dzSXY4RUlFQUlhQTFWVFJEZ2NjTC9CQ0E9PSIsW1siVExWIiwiMjAyNC0wNi0wMSIsIkFERCIsbnVsbCwiRVQiLCI0MTkiXSxbIkFERCIsIjIwMjQtMDYtMDEiLCJJQ04iLG51bGwsIkVUIiwiNjcyIl0sWyJJQ04iLCIyMDI0LTA2LTAyIiwiTlJUIixudWxsLCJFVCIsIjY3MiJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 19:50'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 00:05'}, 'duration': 195, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1126', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 149 kg'], 'often_delayed_by_over_30_min': True{'departure_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 02:40'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 17:35'}, 'duration': 595, 'airplane': 'Airbus A380', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 318', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 671 kg'], 'overnight': True'name': 'Dubai International Airport', 'id': 'DXB', 'overnight': True{'this_flight': 820000, 'typical_for_this_route': 895000, 'difference_percent': -8}, 'price': 2134, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ3hHV2pFeE1qWjhSVXN6TVRnYUN3alhnZzBRQWhvRFZWTkVPQnh3MTRJTiIsW1siVExWIiwiMjAyNC0wNi0wMSIsIkRYQiIsbnVsbCwiRloiLCIxMTI2Il0sWyJEWEIiLCIyMDI0LTA2LTAyIiwiTlJUIixudWxsLCJFSyIsIjMxOCJdXV0='}], 'price_insights': {'lowest_price': 785, 'price_level': 'low', 'typical_price_range': [790, 1100], 'price_history': [[1710972000, 827], [1711058400, 827], [1711144800, 828], [1711231200, 829], [1711317600, 829], [1711404000, 825], [1711490400, 825], [1711576800, 826], [1711663200, 826], [1711746000, 825], [1711832400, 825], [1711918800, 825], [1712005200, 825], [1712091600, 824], [1712178000, 873], [1712264400, 873], [1712350800, 835], [1712437200, 835], [1712523600, 835], [1712610000, 877], [1712696400, 877], [1712782800, 877], [1712869200, 875], [1712955600, 872], [1713042000, 872], [1713128400, 869], [1713214800, 865], [1713301200, 865], [1713387600, 887], [1713474000, 887], [1713560400, 888], [1713646800, 889], [1713733200, 889], [1713819600, 888], [1713906000, 816], [1713992400, 816], [1714078800, 815], [1714165200, 837], [1714251600, 843], [1714338000, 843], [1714424400, 842], [1714510800, 803], [1714597200, 802], [1714683600, 801], [1714770000, 801], [1714856400, 804], [1714942800, 804], [1715029200, 804], [1715115600, 781], [1715202000, 781], [1715288400, 780], [1715374800, 780], [1715461200, 780], [1715547600, 780], [1715634000, 779], [1715720400, 779], [1715806800, 780], [1715893200, 806], [1715979600, 809], [1716066000, 785], [1716152400, 785]]}}


# # for flight in flight_result['best_flights']:
# #     print(flight['price'])
# # # print(flight_result['best_flights'][0]['price'])

# # # get the cheapest flight
# # cheapest_price = flight_result.get('price_insights', {}).get('lowest_price', float('inf'))
# # print(cheapest_price)

# # # cheapest_price = flight_result['price_insights']['lowest_price']
# # # print(cheapest_price)

# # # find flight according to price
# # best_flights = flight_result['best_flights']
# # for flight in best_flights:
# #     if flight['price'] == cheapest_price:
# #         print(flight)
# # other_flights = flight_result['other_flights']
# # for flight in other_flights:
# #     if flight['price'] == cheapest_price:
# #         print(flight)

# # # cheapest_flight = min(flight_result[best_flights]['flights'], key=lambda f: f.price)
# # # print(cheapest_flight)



# lowest_price = flight_result.get('price_insights', {}).get('lowest_price', float('inf'))
    
# # Initialize variable to keep track of the cheapest flight
# cheapest_flight = None
    
 

# # Check in both best_flights and other_flights for the lowest price
# for flight_category in ['best_flights', 'other_flights']:
#     for flight in flight_result.get(flight_category, []):
#         if flight['price'] == lowest_price:
#             cheapest_flight = flight

# print(cheapest_flight)
# # display the flight details
# flights_info = []
# flights_info.append({
#     'price': cheapest_flight['price'],
#     'departure_token': cheapest_flight['departure_token']
# })
# for flight in cheapest_flight['flights']:
#     flight_details = {
#         'departure_airport_name': flight['departure_airport']['name'],
#         'departure_time': flight['departure_airport']['time'],
#         'arrival_airport_name': flight['arrival_airport']['name'],
#         'arrival_time': flight['arrival_airport']['time'],
#         'duration': flight['duration'],
#         'airline': flight['airline'],
#         'flight_number': flight['flight_number'],
#         'often_delayed_by_over_30_min': flight['often_delayed_by_over_30_min'],
#     }
#     if 'ticket_also_sold_by' in flight:
#         flight_details['ticket_also_sold_by'] = flight['ticket_also_sold_by']
#     if 'overnight' in flight:
#         flight_details['overnight'] = flight['overnight']
    
#     flights_info.append(flight_details)

# for curly_brackets in flights_info:
#     print(curly_brackets)
   

possible_destinations = """
        1. City: Queenstown, New Zealand, Destination: The Remarkables
        2. City: Innsbruck, Austria, Destination: Nordkette
        3. City: Ushuaia, Argentina, Destination: Cerro Castor
        4. City: Park City, Utah, USA, Destination: Park City Mountain Resort
        5. City: Zermatt, Switzerland, Destination: Matterhorn Glacier Paradise
"""
# lines = possible_destinations.strip().split('\n')
# cities = []
# destinations = []
# # Iterate over each line and extract city and destination
# for line in lines:
#     city_start_index = line.find('City: ') + len('City: ')
#     city_end_index = line.find(', Destination: ')
#     city_with_info = line[city_start_index:city_end_index].strip()

#     # Strip additional information from the city
#     city_parts = city_with_info.split(',')
#     city = city_parts[0].strip()

#     destination_start_index = line.find('Destination: ') + len('Destination: ')
#     destination = line[destination_start_index:].strip()

#     cities.append(city)
#     destinations.append(destination)

# # Print the extracted cities and destinations
# for city, destination in zip(cities, destinations):
#     print(f"City: {city}, Destination: {destination}")


flight_result = {
    "search_metadata": {
        "id": "664c8a4e2c08448c104bfffe",
        "status": "Success",
        "json_endpoint": "https://serpapi.com/searches/f4a5f15de56c10b4/664c8a4e2c08448c104bfffe.json",
        "created_at": "2024-05-21 11:49:34 UTC",
        "processed_at": "2024-05-21 11:49:34 UTC",
        "google_flights_url": "https://www.google.com/travel/flights?hl=en&gl=us&curr=USD&q=Flights+to+DXB+from+TLV+on+2024-06-01+through+2024-07-01",
        "raw_html_file": "https://serpapi.com/searches/f4a5f15de56c10b4/664c8a4e2c08448c104bfffe.html",
        "prettify_html_file": "https://serpapi.com/searches/f4a5f15de56c10b4/664c8a4e2c08448c104bfffe.prettify",
        "total_time_taken": 2.39
    },
    "search_parameters": {
        "engine": "google_flights",
        "hl": "en",
        "gl": "us",
        "departure_id": "TLV",
        "arrival_id": "DXB",
        "outbound_date": "2024-06-01",
        "return_date": "2024-07-01",
        "departure_token": "WyJDalJJUm1sU2FreFJUM2R6TjI5QlJFWmFhRkZDUnkwdExTMHRMUzB0TFMxMWFtbHROMEZCUVVGQlIxcE5abk5OUm5wdGVIRkJFZ1pHV2pFMU5UQWFDd2kzNHdJUUFob0RWVk5FT0J4d3QrTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXV0=",
        "currency": "USD"
    },
    "best_flights": [
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Dubai International Airport",
                        "id": "DXB",
                        "time": "2024-07-01 16:05"
                    },
                    "arrival_airport": {
                        "name": "Ben Gurion Airport",
                        "id": "TLV",
                        "time": "2024-07-01 18:40"
                    },
                    "duration": 215,
                    "airplane": "Boeing 737MAX 8 Passenger",
                    "airline": "flydubai",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
                    "travel_class": "Economy",
                    "flight_number": "FZ 1125",
                    "ticket_also_sold_by": [
                        "Emirates"
                    ],
                    "legroom": "30 in",
                    "extensions": [
                        "Average legroom (30 in)",
                        "In-seat USB outlet",
                        "On-demand video",
                        "Carbon emissions estimate: 156 kg"
                    ]
                }
            ],
            "total_duration": 215,
            "carbon_emissions": {
                "this_flight": 157000,
                "typical_for_this_route": 157000,
                "difference_percent": 0
            },
            "price": 455,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
            "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFeE1qVWFDd2lkNHdJUUFob0RWVk5FT0J4d25lTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjExMjUiXV1d"
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Dubai International Airport",
                        "id": "DXB",
                        "time": "2024-07-01 12:30"
                    },
                    "arrival_airport": {
                        "name": "Ben Gurion Airport",
                        "id": "TLV",
                        "time": "2024-07-01 15:30"
                    },
                    "duration": 240,
                    "airline": "El Al",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/LY.png",
                    "travel_class": "Economy",
                    "flight_number": "LY 972",
                    "legroom": "30 in",
                    "extensions": [
                        "Average legroom (30 in)",
                        "In-seat USB outlet",
                        "Stream media to your device",
                        "Carbon emissions estimate: 188 kg"
                    ],
                    "often_delayed_by_over_30_min": True
                }
            ],
            "total_duration": 240,
            "carbon_emissions": {
                "this_flight": 188000,
                "typical_for_this_route": 157000,
                "difference_percent": 20
            },
            "price": 477,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/LY.png",
            "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1ZNV1RrM01ob0xDTWYwQWhBQ0dnTlZVMFE0SEhESDlBST0iLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJMWSIsIjk3MiJdXV0="
        }
    ],
    "other_flights": [
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Dubai International Airport",
                        "id": "DXB",
                        "time": "2024-07-01 09:50"
                    },
                    "arrival_airport": {
                        "name": "Ben Gurion Airport",
                        "id": "TLV",
                        "time": "2024-07-01 12:20"
                    },
                    "duration": 210,
                    "airplane": "Boeing 737MAX 8 Passenger",
                    "airline": "flydubai",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
                    "travel_class": "Economy",
                    "flight_number": "FZ 1211",
                    "ticket_also_sold_by": [
                        "Emirates"
                    ],
                    "legroom": "30 in",
                    "extensions": [
                        "Average legroom (30 in)",
                        "In-seat USB outlet",
                        "On-demand video",
                        "Carbon emissions estimate: 149 kg"
                    ],
                    "often_delayed_by_over_30_min": True
                }
            ],
            "total_duration": 210,
            "carbon_emissions": {
                "this_flight": 149000,
                "typical_for_this_route": 157000,
                "difference_percent": -5
            },
            "price": 455,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
            "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFeU1URWFDd2lkNHdJUUFob0RWVk5FT0J4d25lTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjEyMTEiXV1d"
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Dubai International Airport",
                        "id": "DXB",
                        "time": "2024-07-01 20:10"
                    },
                    "arrival_airport": {
                        "name": "Ben Gurion Airport",
                        "id": "TLV",
                        "time": "2024-07-01 22:35"
                    },
                    "duration": 205,
                    "airplane": "Boeing 737MAX 8 Passenger",
                    "airline": "flydubai",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
                    "travel_class": "Economy",
                    "flight_number": "FZ 1625",
                    "ticket_also_sold_by": [
                        "Emirates"
                    ],
                    "legroom": "30 in",
                    "extensions": [
                        "Average legroom (30 in)",
                        "In-seat USB outlet",
                        "On-demand video",
                        "Carbon emissions estimate: 149 kg"
                    ],
                    "often_delayed_by_over_30_min": True
                }
            ],
            "total_duration": 205,
            "carbon_emissions": {
                "this_flight": 149000,
                "typical_for_this_route": 157000,
                "difference_percent": -5
            },
            "price": 455,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
            "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFMk1qVWFDd2lkNHdJUUFob0RWVk5FT0J4d25lTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjE2MjUiXV1d"
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Dubai International Airport",
                        "id": "DXB",
                        "time": "2024-07-01 21:00"
                    },
                    "arrival_airport": {
                        "name": "Ben Gurion Airport",
                        "id": "TLV",
                        "time": "2024-07-01 23:30"
                    },
                    "duration": 210,
                    "airplane": "Boeing 737MAX 8 Passenger",
                    "airline": "flydubai",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
                    "travel_class": "Economy",
                    "flight_number": "FZ 1807",
                    "ticket_also_sold_by": [
                        "Emirates"
                    ],
                    "legroom": "30 in",
                    "extensions": [
                        "Average legroom (30 in)",
                        "In-seat USB outlet",
                        "On-demand video",
                        "Carbon emissions estimate: 156 kg"
                    ]
                }
            ],
            "total_duration": 210,
            "carbon_emissions": {
                "this_flight": 157000,
                "typical_for_this_route": 157000,
                "difference_percent": 0
            },
            "price": 455,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
            "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFNE1EY2FDd2lkNHdJUUFob0RWVk5FT0J4d25lTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjE4MDciXV1d"
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Dubai International Airport",
                        "id": "DXB",
                        "time": "2024-07-01 07:05"
                    },
                    "arrival_airport": {
                        "name": "Ben Gurion Airport",
                        "id": "TLV",
                        "time": "2024-07-01 09:35"
                    },
                    "duration": 210,
                    "airplane": "Boeing 737MAX 8 Passenger",
                    "airline": "flydubai",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
                    "travel_class": "Economy",
                    "flight_number": "FZ 1549",
                    "ticket_also_sold_by": [
                        "Emirates"
                    ],
                    "legroom": "30 in",
                    "extensions": [
                        "Average legroom (30 in)",
                        "In-seat USB outlet",
                        "On-demand video",
                        "Carbon emissions estimate: 149 kg"
                    ],
                    "often_delayed_by_over_30_min": True
                }
            ],
            "total_duration": 210,
            "carbon_emissions": {
                "this_flight": 149000,
                "typical_for_this_route": 157000,
                "difference_percent": -5
            },
            "price": 531,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
            "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFMU5Ea2FDd2lmbmdNUUFob0RWVk5FT0J4d241NEQiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjE1NDkiXV1d"
        }
    ]
}
flight = None
if 'best_flights' in flight_result:
        flight = flight_result.get('best_flights', [])[0]
    
if 'error' in flight_result:
    print(f"Error: {flight_result['error']}")

print(flight)

params = {
            "engine": "google_flights",
            "departure_id": "TLV",    #Tel Aviv
            "arrival_id": "airport_codes[index]",  #destination code
            "outbound_date": "start_date",
            "return_date": "end_date",
            "currency": "USD",
            "hl": "en",
            "max_price": "budget",
            "api_key": "SERPAPI_API_KEY"
            }

params['departure_token'] = "eceqwegewthn3jymjmeyumr"

print(params)