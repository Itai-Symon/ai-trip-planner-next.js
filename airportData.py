# # # import airportsdata

# # # # Load airport data
# # # airports = airportsdata.load('IATA')  # Or 'ICAO'

# # # city = input("Enter a city: ")
# # # # Find the airport code according to the city
# # # airport_code_according_to_city = None
# # # for code, airport in airports.items():
# # #     if airport['city'].lower() == city.lower():
# # #         airport_code_according_to_city = code
# # #         break

# # # if airport_code_according_to_city:
# # #     print(f"The airport code for {city} is {airport_code_according_to_city}.")
# # # else:
# # #     print(f"No airport found for the city: {city}.")


# # # response = """
# # # 1. City: Tokyo, Destination: Cherry Blossom Viewing in Shinjuku Gyoen Park
# # # 2. City: Sydney, Destination: Bondi Beach for Surfing and Sunbathing
# # # 3. City: Rio de Janeiro, Destination: Hiking to the Christ the Redeemer Statue
# # # 4. City: Cape Town, Destination: Wine Tasting in Stellenbosch Winelands
# # # 5. City: Reykjavik, Destination: Northern Lights Viewing in Thingvellir National Park
# # # """
# # # print(response)

# # # # Split the response by newline character to get individual lines
# # # lines = response.strip().split('\n')
# # # cities = []
# # # destinations = []
# # # # Iterate over each line and extract city and destination
# # # for line in lines:
# # #     parts = line.split(', Destination: ')
# # #     city = parts[0].split('City: ')[1].strip()
# # #     destination = parts[1].strip()
# # #     cities.append(city)
# # #     destinations.append(destination)

# # # # Print the extracted cities and destinations
# # # for i in range(len(cities)):
# # #     print(f"City: {cities[i]}, Destination: {destinations[i]}")

# # # print(cities)
# # # print(destinations)
# # import json
# # flight_result = {'search_metadata': {'id': '664b5b382bc7d8cb353faa62', 'status': 'Success', 'json_endpoint': 'https://serpapi.com/searches/0285cad94af724c6/664b5b382bc7d8cb353faa62.json', 'created_at': '2024-05-20 14:16:24 UTC', 'processed_at': '2024-05-20 14:16:24 UTC', 'google_flights_url': 'https://www.google.com/travel/flights?hl=en&gl=us&curr=USD&q=Flights+to+NRT+from+TLV+on+2024-06-01+through+2024-07-01', 'raw_html_file': 'https://serpapi.com/searches/0285cad94af724c6/664b5b382bc7d8cb353faa62.html', 'prettify_html_file': 'https://serpapi.com/searches/0285cad94af724c6/664b5b382bc7d8cb353faa62.prettify', 'total_time_taken': 1.16}, 'search_parameters': {'engine': 'google_flights', 'hl': 'en', 'gl': 'us', 'departure_id': 'TLV', 'arrival_id': 'NRT', 'outbound_date': '2024-06-01', 'return_date': '2024-07-01', 'currency': 'USD'}, 'best_flights': [{'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 13:25'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 17:45'}, 'duration': 200, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1212', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 149 kg'], 'often_delayed_by_over_30_min': True{'departure_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 02:40'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 17:35'}, 'duration': 595, 'airplane': 'Airbus A380', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 318', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 671 kg'], 'overnight': True'name': 'Dubai International Airport', 'id': 'DXB', 'overnight': True{'this_flight': 820000, 'typical_for_this_route': 895000, 'difference_percent': -8}, 'price': 1219, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ3hHV2pFeU1USjhSVXN6TVRnYUN3anJ0d2NRQWhvRFZWTkVPQnh3NjdjSCIsW1siVExWIiwiMjAyNC0wNi0wMSIsIkRYQiIsbnVsbCwiRloiLCIxMjEyIl0sWyJEWEIiLCIyMDI0LTA2LTAyIiwiTlJUIixudWxsLCJFSyIsIjMxOCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 23:30'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 17:05'}, 'duration': 695, 'airplane': 'Boeing 787', 'airline': 'El Al', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LY.png', 'travel_class': 'Economy', 'flight_number': 'LY 91', 'legroom': '31 in', 'extensions': ['Average legroom (31 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 634 kg'], 'overnight': True'often_delayed_by_over_30_min': True'typical_for_this_route': 895000, 'difference_percent': -29}, 'price': 1661, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LY.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ1JNV1RreEdnc0lrNUVLRUFJYUExVlRSRGdjY0pPUkNnPT0iLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJOUlQiLG51bGwsIkxZIiwiOTEiXV1d'}], 'other_flights': [{'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 15:20'}, 'arrival_airport': {'name': 'Vienna International Airport', 'id': 'VIE', 'time': '2024-06-01 18:05'}, 'duration': 225, 'airplane': 'Airbus A321', 'airline': 'Austrian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/OS.png', 'travel_class': 'Economy', 'flight_number': 'OS 858', 'legroom': '29 in', 'extensions': ['Below average legroom (29 in)', 'Wi-Fi for a fee', 'In-seat USB outlet', 'Carbon emissions estimate: 208 kg'], 'often_delayed_by_over_30_min': TrueInternational Airport', 'id': 'VIE', 'time': '2024-06-02 13:30'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 08:50'}, 'duration': 740, 'airplane': 'Boeing 777', 'airline': 'Austrian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/OS.png', 'travel_class': 'Economy', 'flight_number': 'OS 51', 'ticket_also_sold_by': ['ANA'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 668 kg'], 'overnight': True[{'duration': 1165, 'name': 'Vienna International Airport', 'id': 'VIE', 'overnight': True'carbon_emissions': {'this_flight': 877000, 'typical_for_this_route': 895000, 'difference_percent': -2}, 'price': 785, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/OS.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ3BQVXpnMU9IeFBVelV4R2dzSW4rVUVFQUlhQTFWVFJEZ2NjSi9sQkE9PSIsW1siVExWIiwiMjAyNC0wNi0wMSIsIlZJRSIsbnVsbCwiT1MiLCI4NTgiXSxbIlZJRSIsIjIwMjQtMDYtMDIiLCJOUlQiLG51bGwsIk9TIiwiNTEiXV1d'}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 17:05'}, 'arrival_airport': {'name': 'Munich International Airport', 'id': 'MUC', 'time': '2024-06-01 20:15'}, 'duration': 250, 'airplane': 'Airbus A321neo', 'airline': 'Lufthansa', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LH.png', 'travel_class': 'Economy', 'flight_number': 'LH 681', 'legroom': '29 in', 'extensions': ['Below average legroom (29 in)', 'In-seat USB outlet', 'Carbon emissions estimate: 187 kg']}, {'departure_airport': {'name': 'Munich International Airport', 'id': 'MUC', 'time': '2024-06-02 11:55'}, 'arrival_airport': {'name': 'Kansai International Airport', 'id': 'KIX', 'time': '2024-06-03 06:55'}, 'duration': 720, 'airplane': 'Airbus A350', 'airline': 'Lufthansa', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LH.png', 'travel_class': 'Economy', 'flight_number': 'LH 742', 'ticket_also_sold_by': ['ANA'], 'legroom': '31 in', 'extensions': ['Average legroom (31 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 543 kg'], 'overnight': True'ITM', 'time': '2024-06-03 14:15'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 15:40'}, 'duration': 85, 'airplane': 'Boeing 737', 'airline': 'ANA', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/NH.png', 'travel_class': 'Economy', 'flight_number': 'NH 2178', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Free Wi-Fi', 'Stream media to your device', 'Carbon emissions estimate: 82 kg']}], 'layovers': [{'duration': 940, 'name': 'Munich International Airport', 'id': 'MUC', 'overnight': TrueInternational Airport (Itami Airport)', 'id': 'KIX'}], 'total_duration': 2435, 'carbon_emissions': {'this_flight': 813000, 'typical_for_this_route': 895000, 'difference_percent': -9}, 'price': 809, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEpNU0RZNE1YeE1TRGMwTW54T1NESXhOemdhQ3dqMTl3UVFBaG9EVlZORU9CeHc5ZmNFIixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiTVVDIixudWxsLCJMSCIsIjY4MSJdLFsiTVVDIiwiMjAyNC0wNi0wMiIsIktJWCIsbnVsbCwiTEgiLCI3NDIiXSxbIklUTSIsIjIwMjQtMDYtMDMiLCJOUlQiLG51bGwsIk5IIiwiMjE3OCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 18:15'}, 'arrival_airport': {'name': 'Zurich Airport', 'id': 'ZRH', 'time': '2024-06-01 21:35'}, 'duration': 260, 'airplane': 'Airbus A320neo', 'airline': 'SWISS', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LX.png', 'travel_class': 'Economy', 'flight_number': 'LX 253', 'legroom': '29 in', 'extensions': ['Below average legroom (29 in)', 'Carbon emissions estimate: 179 kg']}, {'departure_airport': {'name': 'Zurich Airport', 'id': 'ZRH', 'time': '2024-06-02 13:05'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 08:50'}, 'duration': 765, 'airplane': 'Boeing 777', 'airline': 'SWISS', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LX.png', 'travel_class': 'Economy', 'flight_number': 'LX 160', 'ticket_also_sold_by': ['ANA'], 'legroom': '31 in', 'extensions': ['Average legroom (31 in)', 'Wi-Fi for a fee', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 759 kg'], 'overnight': True'name': 'Zurich Airport', 'id': 'ZRH', 'overnight': True'typical_for_this_route': 895000, 'difference_percent': 5}, 'price': 856, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/LX.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ3RNV0RJMU0zeE1XREUyTUJvTENKR2NCUkFDR2dOVlUwUTRISENSbkFVPSIsW1siVExWIiwiMjAyNC0wNi0wMSIsIlpSSCIsbnVsbCwiTFgiLCIyNTMiXSxbIlpSSCIsIjIwMjQtMDYtMDIiLCJOUlQiLG51bGwsIkxYIiwiMTYwIl1dXQ=='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 15:35'}, 'arrival_airport': {'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'time': '2024-06-01 19:50'}, 'duration': 255, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 419', 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'Stream media to your device', 'Carbon emissions estimate: 188 kg']}, {'departure_airport': {'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'time': '2024-06-02 22:35'}, 'arrival_airport': {'name': 'Incheon International Airport', 'id': 'ICN', 'time': '2024-06-03 16:00'}, 'duration': 685, 'airplane': 'Boeing 787', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 672', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 664 kg'], 'overnight': True17:40'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 20:05'}, 'duration': 145, 'airplane': 'Boeing 787', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 672', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 118 kg']}], 'layovers': [{'duration': 1605, 'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'overnight': True'ICN'}], 'total_duration': 2790, 'carbon_emissions': {'this_flight': 971000, 'typical_for_this_route': 895000, 'difference_percent': 8}, 'price': 1018, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEZGVkRReE9YeEZWRFkzTW54RlZEWTNNaG9MQ01tYUJoQUNHZ05WVTBRNEhIREptZ1k9IixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiQUREIixudWxsLCJFVCIsIjQxOSJdLFsiQUREIiwiMjAyNC0wNi0wMiIsIklDTiIsbnVsbCwiRVQiLCI2NzIiXSxbIklDTiIsIjIwMjQtMDYtMDMiLCJOUlQiLG51bGwsIkVUIiwiNjcyIl1dXQ=='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 00:50'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 05:10'}, 'duration': 200, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1808', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 156 kg'], 'overnight': True{'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 09:40'}, 'arrival_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-01 19:15'}, 'duration': 395, 'airplane': 'Airbus A380', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 372', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 418 kg']}, {'departure_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-01 22:10'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 06:20'}, 'duration': 370, 'airplane': 'Airbus A350', 'airline': 'THAI', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/TG.png', 'travel_class': 'Economy', 'flight_number': 'TG 640', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 341 kg'], 'overnight': True[{'duration': 270, 'name': 'Dubai International Airport', 'id': 'DXB'}, {'duration': 175, 'name': 'Suvarnabhumi Airport', 'id': 'BKK'}], 'total_duration': 1410, 'carbon_emissions': {'this_flight': 917000, 'typical_for_this_route': 895000, 'difference_percent': 2}, 'price': 1346, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEpHV2pFNE1EaDhSVXN6TnpKOFZFYzJOREFhQ3dpdm13Z1FBaG9EVlZORU9CeHdyNXNJIixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiRFhCIixudWxsLCJGWiIsIjE4MDgiXSxbIkRYQiIsIjIwMjQtMDYtMDEiLCJCS0siLG51bGwsIkVLIiwiMzcyIl0sWyJCS0siLCIyMDI0LTA2LTAxIiwiTlJUIixudWxsLCJURyIsIjY0MCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 00:50'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 05:10'}, 'duration': 200, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1808', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 156 kg'], 'overnight': True{'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-01 09:00'}, 'arrival_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-01 18:25'}, 'duration': 385, 'airplane': 'Boeing 777', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 370', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 414 kg']}, {'departure_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-01 22:10'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 06:20'}, 'duration': 370, 'airplane': 'Airbus A350', 'airline': 'THAI', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/TG.png', 'travel_class': 'Economy', 'flight_number': 'TG 640', 'ticket_also_sold_by': ['ANA'], 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 341 kg'], 'overnight': True'name': 'Suvarnabhumi Airport', 'id': 'BKK'}], 'total_duration': 1410, 'carbon_emissions': {'this_flight': 913000, 'typical_for_this_route': 895000, 'difference_percent': 2}, 'price': 1346, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEpHV2pFNE1EaDhSVXN6TnpCOFZFYzJOREFhQ3dpdm13Z1FBaG9EVlZORU9CeHdyNXNJIixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiRFhCIixudWxsLCJGWiIsIjE4MDgiXSxbIkRYQiIsIjIwMjQtMDYtMDEiLCJCS0siLG51bGwsIkVLIiwiMzcwIl0sWyJCS0siLCIyMDI0LTA2LTAxIiwiTlJUIixudWxsLCJURyIsIjY0MCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 23:55'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 04:15'}, 'duration': 200, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1626', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 149 kg'], 'overnight': True{'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 09:00'}, 'arrival_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-02 18:25'}, 'duration': 385, 'airplane': 'Boeing 777', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 370', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 414 kg']}, {'departure_airport': {'name': 'Suvarnabhumi Airport', 'id': 'BKK', 'time': '2024-06-02 22:10'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 06:20'}, 'duration': 370, 'airplane': 'Airbus A350', 'airline': 'THAI', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/TG.png', 'travel_class': 'Economy', 'flight_number': 'TG 640', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 341 kg'], 'overnight': True[{'duration': 285, 'name': 'Dubai International Airport', 'id': 'DXB', 'overnight': True'Suvarnabhumi Airport', 'id': 'BKK'}], 'total_duration': 1465, 'carbon_emissions': {'this_flight': 905000, 'typical_for_this_route': 895000, 'difference_percent': 1}, 'price': 1346, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaEpHV2pFMk1qWjhSVXN6TnpCOFZFYzJOREFhQ3dpdm13Z1FBaG9EVlZORU9CeHdyNXNJIixbWyJUTFYiLCIyMDI0LTA2LTAxIiwiRFhCIixudWxsLCJGWiIsIjE2MjYiXSxbIkRYQiIsIjIwMjQtMDYtMDIiLCJCS0siLG51bGwsIkVLIiwiMzcwIl0sWyJCS0siLCIyMDI0LTA2LTAyIiwiTlJUIixudWxsLCJURyIsIjY0MCJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 15:35'}, 'arrival_airport': {'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'time': '2024-06-01 19:50'}, 'duration': 255, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 419', 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'Stream media to your device', 'Carbon emissions estimate: 188 kg']}, {'departure_airport': {'name': 'Bole Addis Ababa International Airport', 'id': 'ADD', 'time': '2024-06-01 22:35'}, 'arrival_airport': {'name': 'Incheon International Airport', 'id': 'ICN', 'time': '2024-06-02 16:00'}, 'duration': 685, 'airplane': 'Boeing 787', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 672', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 664 kg'], 'overnight': True{'name': 'Incheon International Airport', 'id': 'ICN', 'time': '2024-06-02 17:40'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 20:05'}, 'duration': 145, 'airplane': 'Boeing 787', 'airline': 'Ethiopian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'travel_class': 'Economy', 'flight_number': 'ET 672', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 118 kg']}], 'layovers': [{'duration': 165, 'name': 'Bole Addis Ababa International Airport', 'id': 'ADD'}, {'duration': 100, 'name': 'Incheon International Airport', 'id': 'ICN'}], 'total_duration': 1350, 'carbon_emissions': {'this_flight': 971000, 'typical_for_this_route': 895000, 'difference_percent': 8}, 'price': 1395, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/ET.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFaE5GVkRReE9YeEZWRFkzTW54RlZEWTNNaU14R2dzSXY4RUlFQUlhQTFWVFJEZ2NjTC9CQ0E9PSIsW1siVExWIiwiMjAyNC0wNi0wMSIsIkFERCIsbnVsbCwiRVQiLCI0MTkiXSxbIkFERCIsIjIwMjQtMDYtMDEiLCJJQ04iLG51bGwsIkVUIiwiNjcyIl0sWyJJQ04iLCIyMDI0LTA2LTAyIiwiTlJUIixudWxsLCJFVCIsIjY3MiJdXV0='}, {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 19:50'}, 'arrival_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 00:05'}, 'duration': 195, 'airplane': 'Boeing 737MAX 8 Passenger', 'airline': 'flydubai', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/FZ.png', 'travel_class': 'Economy', 'flight_number': 'FZ 1126', 'ticket_also_sold_by': ['Emirates'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 149 kg'], 'often_delayed_by_over_30_min': True{'departure_airport': {'name': 'Dubai International Airport', 'id': 'DXB', 'time': '2024-06-02 02:40'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-02 17:35'}, 'duration': 595, 'airplane': 'Airbus A380', 'airline': 'Emirates', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png', 'travel_class': 'Economy', 'flight_number': 'EK 318', 'legroom': '32 in', 'extensions': ['Above average legroom (32 in)', 'Wi-Fi for a fee', 'In-seat power & USB outlets', 'On-demand video', 'Carbon emissions estimate: 671 kg'], 'overnight': True'name': 'Dubai International Airport', 'id': 'DXB', 'overnight': True{'this_flight': 820000, 'typical_for_this_route': 895000, 'difference_percent': -8}, 'price': 2134, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/multi.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ3hHV2pFeE1qWjhSVXN6TVRnYUN3alhnZzBRQWhvRFZWTkVPQnh3MTRJTiIsW1siVExWIiwiMjAyNC0wNi0wMSIsIkRYQiIsbnVsbCwiRloiLCIxMTI2Il0sWyJEWEIiLCIyMDI0LTA2LTAyIiwiTlJUIixudWxsLCJFSyIsIjMxOCJdXV0='}], 'price_insights': {'lowest_price': 785, 'price_level': 'low', 'typical_price_range': [790, 1100], 'price_history': [[1710972000, 827], [1711058400, 827], [1711144800, 828], [1711231200, 829], [1711317600, 829], [1711404000, 825], [1711490400, 825], [1711576800, 826], [1711663200, 826], [1711746000, 825], [1711832400, 825], [1711918800, 825], [1712005200, 825], [1712091600, 824], [1712178000, 873], [1712264400, 873], [1712350800, 835], [1712437200, 835], [1712523600, 835], [1712610000, 877], [1712696400, 877], [1712782800, 877], [1712869200, 875], [1712955600, 872], [1713042000, 872], [1713128400, 869], [1713214800, 865], [1713301200, 865], [1713387600, 887], [1713474000, 887], [1713560400, 888], [1713646800, 889], [1713733200, 889], [1713819600, 888], [1713906000, 816], [1713992400, 816], [1714078800, 815], [1714165200, 837], [1714251600, 843], [1714338000, 843], [1714424400, 842], [1714510800, 803], [1714597200, 802], [1714683600, 801], [1714770000, 801], [1714856400, 804], [1714942800, 804], [1715029200, 804], [1715115600, 781], [1715202000, 781], [1715288400, 780], [1715374800, 780], [1715461200, 780], [1715547600, 780], [1715634000, 779], [1715720400, 779], [1715806800, 780], [1715893200, 806], [1715979600, 809], [1716066000, 785], [1716152400, 785]]}}


# # # for flight in flight_result['best_flights']:
# # #     print(flight['price'])
# # # # print(flight_result['best_flights'][0]['price'])

# # # # get the cheapest flight
# # # cheapest_price = flight_result.get('price_insights', {}).get('lowest_price', float('inf'))
# # # print(cheapest_price)

# # # # cheapest_price = flight_result['price_insights']['lowest_price']
# # # # print(cheapest_price)

# # # # find flight according to price
# # # best_flights = flight_result['best_flights']
# # # for flight in best_flights:
# # #     if flight['price'] == cheapest_price:
# # #         print(flight)
# # # other_flights = flight_result['other_flights']
# # # for flight in other_flights:
# # #     if flight['price'] == cheapest_price:
# # #         print(flight)

# # # # cheapest_flight = min(flight_result[best_flights]['flights'], key=lambda f: f.price)
# # # # print(cheapest_flight)



# # lowest_price = flight_result.get('price_insights', {}).get('lowest_price', float('inf'))
    
# # # Initialize variable to keep track of the cheapest flight
# # cheapest_flight = None
    
 

# # # Check in both best_flights and other_flights for the lowest price
# # for flight_category in ['best_flights', 'other_flights']:
# #     for flight in flight_result.get(flight_category, []):
# #         if flight['price'] == lowest_price:
# #             cheapest_flight = flight

# # print(cheapest_flight)
# # # display the flight details
# # flights_info = []
# # flights_info.append({
# #     'price': cheapest_flight['price'],
# #     'departure_token': cheapest_flight['departure_token']
# # })
# # for flight in cheapest_flight['flights']:
# #     flight_details = {
# #         'departure_airport_name': flight['departure_airport']['name'],
# #         'departure_time': flight['departure_airport']['time'],
# #         'arrival_airport_name': flight['arrival_airport']['name'],
# #         'arrival_time': flight['arrival_airport']['time'],
# #         'duration': flight['duration'],
# #         'airline': flight['airline'],
# #         'flight_number': flight['flight_number'],
# #         'often_delayed_by_over_30_min': flight['often_delayed_by_over_30_min'],
# #     }
# #     if 'ticket_also_sold_by' in flight:
# #         flight_details['ticket_also_sold_by'] = flight['ticket_also_sold_by']
# #     if 'overnight' in flight:
# #         flight_details['overnight'] = flight['overnight']
    
# #     flights_info.append(flight_details)

# # for curly_brackets in flights_info:
# #     print(curly_brackets)
   

# possible_destinations = """
#         1. City: Queenstown, New Zealand, Destination: The Remarkables
#         2. City: Innsbruck, Austria, Destination: Nordkette
#         3. City: Ushuaia, Argentina, Destination: Cerro Castor
#         4. City: Park City, Utah, USA, Destination: Park City Mountain Resort
#         5. City: Zermatt, Switzerland, Destination: Matterhorn Glacier Paradise
# """
# # lines = possible_destinations.strip().split('\n')
# # cities = []
# # destinations = []
# # # Iterate over each line and extract city and destination
# # for line in lines:
# #     city_start_index = line.find('City: ') + len('City: ')
# #     city_end_index = line.find(', Destination: ')
# #     city_with_info = line[city_start_index:city_end_index].strip()

# #     # Strip additional information from the city
# #     city_parts = city_with_info.split(',')
# #     city = city_parts[0].strip()

# #     destination_start_index = line.find('Destination: ') + len('Destination: ')
# #     destination = line[destination_start_index:].strip()

# #     cities.append(city)
# #     destinations.append(destination)

# # # Print the extracted cities and destinations
# # for city, destination in zip(cities, destinations):
# #     print(f"City: {city}, Destination: {destination}")


# flight_result = {
#     "search_metadata": {
#         "id": "664c8a4e2c08448c104bfffe",
#         "status": "Success",
#         "json_endpoint": "https://serpapi.com/searches/f4a5f15de56c10b4/664c8a4e2c08448c104bfffe.json",
#         "created_at": "2024-05-21 11:49:34 UTC",
#         "processed_at": "2024-05-21 11:49:34 UTC",
#         "google_flights_url": "https://www.google.com/travel/flights?hl=en&gl=us&curr=USD&q=Flights+to+DXB+from+TLV+on+2024-06-01+through+2024-07-01",
#         "raw_html_file": "https://serpapi.com/searches/f4a5f15de56c10b4/664c8a4e2c08448c104bfffe.html",
#         "prettify_html_file": "https://serpapi.com/searches/f4a5f15de56c10b4/664c8a4e2c08448c104bfffe.prettify",
#         "total_time_taken": 2.39
#     },
#     "search_parameters": {
#         "engine": "google_flights",
#         "hl": "en",
#         "gl": "us",
#         "departure_id": "TLV",
#         "arrival_id": "DXB",
#         "outbound_date": "2024-06-01",
#         "return_date": "2024-07-01",
#         "departure_token": "WyJDalJJUm1sU2FreFJUM2R6TjI5QlJFWmFhRkZDUnkwdExTMHRMUzB0TFMxMWFtbHROMEZCUVVGQlIxcE5abk5OUm5wdGVIRkJFZ1pHV2pFMU5UQWFDd2kzNHdJUUFob0RWVk5FT0J4d3QrTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXV0=",
#         "currency": "USD"
#     },
#     "best_flights": [
#         {
#             "flights": [
#                 {
#                     "departure_airport": {
#                         "name": "Dubai International Airport",
#                         "id": "DXB",
#                         "time": "2024-07-01 16:05"
#                     },
#                     "arrival_airport": {
#                         "name": "Ben Gurion Airport",
#                         "id": "TLV",
#                         "time": "2024-07-01 18:40"
#                     },
#                     "duration": 215,
#                     "airplane": "Boeing 737MAX 8 Passenger",
#                     "airline": "flydubai",
#                     "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#                     "travel_class": "Economy",
#                     "flight_number": "FZ 1125",
#                     "ticket_also_sold_by": [
#                         "Emirates"
#                     ],
#                     "legroom": "30 in",
#                     "extensions": [
#                         "Average legroom (30 in)",
#                         "In-seat USB outlet",
#                         "On-demand video",
#                         "Carbon emissions estimate: 156 kg"
#                     ]
#                 }
#             ],
#             "total_duration": 215,
#             "carbon_emissions": {
#                 "this_flight": 157000,
#                 "typical_for_this_route": 157000,
#                 "difference_percent": 0
#             },
#             "price": 455,
#             "type": "Round trip",
#             "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#             "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFeE1qVWFDd2lkNHdJUUFob0RWVk5FT0J4d25lTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjExMjUiXV1d"
#         },
#         {
#             "flights": [
#                 {
#                     "departure_airport": {
#                         "name": "Dubai International Airport",
#                         "id": "DXB",
#                         "time": "2024-07-01 12:30"
#                     },
#                     "arrival_airport": {
#                         "name": "Ben Gurion Airport",
#                         "id": "TLV",
#                         "time": "2024-07-01 15:30"
#                     },
#                     "duration": 240,
#                     "airline": "El Al",
#                     "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/LY.png",
#                     "travel_class": "Economy",
#                     "flight_number": "LY 972",
#                     "legroom": "30 in",
#                     "extensions": [
#                         "Average legroom (30 in)",
#                         "In-seat USB outlet",
#                         "Stream media to your device",
#                         "Carbon emissions estimate: 188 kg"
#                     ],
#                     "often_delayed_by_over_30_min": True
#                 }
#             ],
#             "total_duration": 240,
#             "carbon_emissions": {
#                 "this_flight": 188000,
#                 "typical_for_this_route": 157000,
#                 "difference_percent": 20
#             },
#             "price": 477,
#             "type": "Round trip",
#             "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/LY.png",
#             "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1ZNV1RrM01ob0xDTWYwQWhBQ0dnTlZVMFE0SEhESDlBST0iLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJMWSIsIjk3MiJdXV0="
#         }
#     ],
#     "other_flights": [
#         {
#             "flights": [
#                 {
#                     "departure_airport": {
#                         "name": "Dubai International Airport",
#                         "id": "DXB",
#                         "time": "2024-07-01 09:50"
#                     },
#                     "arrival_airport": {
#                         "name": "Ben Gurion Airport",
#                         "id": "TLV",
#                         "time": "2024-07-01 12:20"
#                     },
#                     "duration": 210,
#                     "airplane": "Boeing 737MAX 8 Passenger",
#                     "airline": "flydubai",
#                     "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#                     "travel_class": "Economy",
#                     "flight_number": "FZ 1211",
#                     "ticket_also_sold_by": [
#                         "Emirates"
#                     ],
#                     "legroom": "30 in",
#                     "extensions": [
#                         "Average legroom (30 in)",
#                         "In-seat USB outlet",
#                         "On-demand video",
#                         "Carbon emissions estimate: 149 kg"
#                     ],
#                     "often_delayed_by_over_30_min": True
#                 }
#             ],
#             "total_duration": 210,
#             "carbon_emissions": {
#                 "this_flight": 149000,
#                 "typical_for_this_route": 157000,
#                 "difference_percent": -5
#             },
#             "price": 455,
#             "type": "Round trip",
#             "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#             "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFeU1URWFDd2lkNHdJUUFob0RWVk5FT0J4d25lTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjEyMTEiXV1d"
#         },
#         {
#             "flights": [
#                 {
#                     "departure_airport": {
#                         "name": "Dubai International Airport",
#                         "id": "DXB",
#                         "time": "2024-07-01 20:10"
#                     },
#                     "arrival_airport": {
#                         "name": "Ben Gurion Airport",
#                         "id": "TLV",
#                         "time": "2024-07-01 22:35"
#                     },
#                     "duration": 205,
#                     "airplane": "Boeing 737MAX 8 Passenger",
#                     "airline": "flydubai",
#                     "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#                     "travel_class": "Economy",
#                     "flight_number": "FZ 1625",
#                     "ticket_also_sold_by": [
#                         "Emirates"
#                     ],
#                     "legroom": "30 in",
#                     "extensions": [
#                         "Average legroom (30 in)",
#                         "In-seat USB outlet",
#                         "On-demand video",
#                         "Carbon emissions estimate: 149 kg"
#                     ],
#                     "often_delayed_by_over_30_min": True
#                 }
#             ],
#             "total_duration": 205,
#             "carbon_emissions": {
#                 "this_flight": 149000,
#                 "typical_for_this_route": 157000,
#                 "difference_percent": -5
#             },
#             "price": 455,
#             "type": "Round trip",
#             "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#             "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFMk1qVWFDd2lkNHdJUUFob0RWVk5FT0J4d25lTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjE2MjUiXV1d"
#         },
#         {
#             "flights": [
#                 {
#                     "departure_airport": {
#                         "name": "Dubai International Airport",
#                         "id": "DXB",
#                         "time": "2024-07-01 21:00"
#                     },
#                     "arrival_airport": {
#                         "name": "Ben Gurion Airport",
#                         "id": "TLV",
#                         "time": "2024-07-01 23:30"
#                     },
#                     "duration": 210,
#                     "airplane": "Boeing 737MAX 8 Passenger",
#                     "airline": "flydubai",
#                     "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#                     "travel_class": "Economy",
#                     "flight_number": "FZ 1807",
#                     "ticket_also_sold_by": [
#                         "Emirates"
#                     ],
#                     "legroom": "30 in",
#                     "extensions": [
#                         "Average legroom (30 in)",
#                         "In-seat USB outlet",
#                         "On-demand video",
#                         "Carbon emissions estimate: 156 kg"
#                     ]
#                 }
#             ],
#             "total_duration": 210,
#             "carbon_emissions": {
#                 "this_flight": 157000,
#                 "typical_for_this_route": 157000,
#                 "difference_percent": 0
#             },
#             "price": 455,
#             "type": "Round trip",
#             "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#             "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFNE1EY2FDd2lkNHdJUUFob0RWVk5FT0J4d25lTUMiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjE4MDciXV1d"
#         },
#         {
#             "flights": [
#                 {
#                     "departure_airport": {
#                         "name": "Dubai International Airport",
#                         "id": "DXB",
#                         "time": "2024-07-01 07:05"
#                     },
#                     "arrival_airport": {
#                         "name": "Ben Gurion Airport",
#                         "id": "TLV",
#                         "time": "2024-07-01 09:35"
#                     },
#                     "duration": 210,
#                     "airplane": "Boeing 737MAX 8 Passenger",
#                     "airline": "flydubai",
#                     "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#                     "travel_class": "Economy",
#                     "flight_number": "FZ 1549",
#                     "ticket_also_sold_by": [
#                         "Emirates"
#                     ],
#                     "legroom": "30 in",
#                     "extensions": [
#                         "Average legroom (30 in)",
#                         "In-seat USB outlet",
#                         "On-demand video",
#                         "Carbon emissions estimate: 149 kg"
#                     ],
#                     "often_delayed_by_over_30_min": True
#                 }
#             ],
#             "total_duration": 210,
#             "carbon_emissions": {
#                 "this_flight": 149000,
#                 "typical_for_this_route": 157000,
#                 "difference_percent": -5
#             },
#             "price": 531,
#             "type": "Round trip",
#             "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FZ.png",
#             "booking_token": "WyJDalJJTTBkdlJuUnFjMDVYU25OQlF5MUxWMUZDUnkwdExTMHRMUzB0YjJ0aWFXWTBNRUZCUVVGQlIxcE5hV3hCUTNWYVVWVkJFZ1pHV2pFMU5Ea2FDd2lmbmdNUUFob0RWVk5FT0J4d241NEQiLFtbIlRMViIsIjIwMjQtMDYtMDEiLCJEWEIiLG51bGwsIkZaIiwiMTU1MCJdXSxbWyJEWEIiLCIyMDI0LTA3LTAxIiwiVExWIixudWxsLCJGWiIsIjE1NDkiXV1d"
#         }
#     ]
# }
# flight = None
# if 'best_flights' in flight_result:
#         flight = flight_result.get('best_flights', [])[0]
    
# if 'error' in flight_result:
#     print(f"Error: {flight_result['error']}")

# print(flight)

# params = {
#             "engine": "google_flights",
#             "departure_id": "TLV",    #Tel Aviv
#             "arrival_id": "airport_codes[index]",  #destination code
#             "outbound_date": "start_date",
#             "return_date": "end_date",
#             "currency": "USD",
#             "hl": "en",
#             "max_price": "budget",
#             "api_key": "SERPAPI_API_KEY"
#             }

# params['departure_token'] = "eceqwegewthn3jymjmeyumr"

# print(params)
# budget = 1000
# budget = [budget] * 5
# print("buget", budget)

import json


# results = {'flights': [{'departure_airport': {'name': 'Ben Gurion Airport', 'id': 'TLV', 'time': '2024-06-01 15:20'}, 'arrival_airport': {'name': 'Vienna International Airport', 'id': 'VIE', 'time': '2024-06-01 18:05'}, 'duration': 225, 'airplane': 'Airbus A321', 'airline': 'Austrian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/OS.png', 'travel_class': 'Economy', 'flight_number': 'OS 858', 'legroom': '29 in', 'extensions': ['Below average legroom (29 in)', 'Wi-Fi for a fee', 'In-seat USB outlet', 'Carbon emissions estimate: 208 kg'], 'often_delayed_by_over_30_min': True}, {'departure_airport': {'name': 'Vienna International Airport', 'id': 'VIE', 'time': '2024-06-02 13:30'}, 'arrival_airport': {'name': 'Narita International Airport', 'id': 'NRT', 'time': '2024-06-03 08:50'}, 'duration': 740, 'airplane': 'Boeing 777', 'airline': 'Austrian', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/OS.png', 'travel_class': 'Economy', 'flight_number': 'OS 51', 'ticket_also_sold_by': ['ANA'], 'legroom': '30 in', 'extensions': ['Average legroom (30 in)', 'In-seat USB outlet', 'On-demand video', 'Carbon emissions estimate: 668 kg'], 'overnight': True, 'often_delayed_by_over_30_min': True}], 'layovers': [{'duration': 1165, 'name': 'Vienna International Airport', 'id': 'VIE', 'overnight': True}], 'total_duration': 2130, 'carbon_emissions': {'this_flight': 877000, 'typical_for_this_route': 895000, 'difference_percent': -2}, 'price': 785, 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/OS.png', 'departure_token': 'WyJDalJJVFdvMlVXRnBkMEZNZVRSQlIwNHdkbEZDUnkwdExTMHRMUzB0TFMxNWJIQnpNMEZCUVVGQlIxcE1WM3ByUmkxM2RFVkJFZ3BQVXpnMU9IeFBVelV4R2dzSW4rVUVFQUlhQTFWVFJEZ2NjSi9sQkE9PSIsW1siVExWIiwiMjAyNC0wNi0wMSIsIlZJRSIsbnVsbCwiT1MiLCI4NTgiXSxbIlZJRSIsIjIwMjQtMDYtMDIiLCJOUlQiLG51bGwsIk9TIiwiNTEiXV1d'}
# parse_results = json.dumps(results, indent=4)
# print(parse_results)


data = {
    "search_metadata": {
        "id": "664d15e214b24563e99d65e6",
        "status": "Success",
        "json_endpoint": "https://serpapi.com/searches/cb6790b886ee06dd/664d15e214b24563e99d65e6.json",
        "created_at": "2024-05-21 21:45:06 UTC",
        "processed_at": "2024-05-21 21:45:06 UTC",
        "google_hotels_url": "https://www.google.com/_/TravelFrontendUi/data/batchexecute?rpcids=AtySUc&source-path=/travel/search&hl=en&gl=us&rt=c&soc-app=162&soc-platform=1&soc-device=1",
        "raw_html_file": "https://serpapi.com/searches/cb6790b886ee06dd/664d15e214b24563e99d65e6.html",
        "prettify_html_file": "https://serpapi.com/searches/cb6790b886ee06dd/664d15e214b24563e99d65e6.prettify",
        "total_time_taken": 2.6
    },
    "search_parameters": {
        "engine": "google_hotels",
        "q": "Playa del Carmen",
        "gl": "us",
        "hl": "en",
        "currency": "USD",
        "check_in_date": "2024-06-01",
        "check_out_date": "2024-07-01",
        "adults": 2,
        "children": 0,
        "max_price": "10000"
    },
    "brands": [
        {
            "id": 33,
            "name": "Accor Live Limitless",
            "children": [
                {
                    "id": 67,
                    "name": "Banyan Tree"
                },
                {
                    "id": 8,
                    "name": "Fairmont Hotels and Resorts"
                }
            ]
        },
        {
            "id": 182,
            "name": "Barceló Hotel Group",
            "children": [
                {
                    "id": 186,
                    "name": "Allegro"
                },
                {
                    "id": 183,
                    "name": "Royal Hideaway"
                }
            ]
        },
        {
            "id": 211,
            "name": "Fiesta Inn"
        },
        {
            "id": 28,
            "name": "Hilton Honors",
            "children": [
                {
                    "id": 151,
                    "name": "Curio Collection"
                },
                {
                    "id": 54,
                    "name": "Hilton Hotels & Resorts"
                },
                {
                    "id": 285,
                    "name": "Tapestry Collection"
                }
            ]
        },
        {
            "id": 37,
            "name": "Hyatt",
            "children": [
                {
                    "id": 117,
                    "name": "Grand Hyatt"
                },
                {
                    "id": 384,
                    "name": "Secrets Resorts and Spas"
                }
            ]
        },
        {
            "id": 17,
            "name": "IHG Hotels & Resorts",
            "children": [
                {
                    "id": 56,
                    "name": "Holiday Inn Express"
                },
                {
                    "id": 100,
                    "name": "Iberostar Hotels and Resorts"
                }
            ]
        },
        {
            "id": 207,
            "name": "Live Aqua"
        },
        {
            "id": 46,
            "name": "Marriott Bonvoy",
            "children": [
                {
                    "id": 60,
                    "name": "Aloft Hotels"
                },
                {
                    "id": 216,
                    "name": "City Express Hotels"
                },
                {
                    "id": 218,
                    "name": "City Express Suites"
                },
                {
                    "id": 75,
                    "name": "Residence Inn by Marriott"
                }
            ]
        },
        {
            "id": 174,
            "name": "Melia Hotels International",
            "children": [
                {
                    "id": 177,
                    "name": "Paradisus by Melia"
                }
            ]
        },
        {
            "id": 214,
            "name": "ONE"
        },
        {
            "id": 353,
            "name": "OYO",
            "children": [
                {
                    "id": 99,
                    "name": "OYO Rooms"
                }
            ]
        },
        {
            "id": 323,
            "name": "Princess Hotels & Resorts"
        },
        {
            "id": 163,
            "name": "RIU Hotels & Resorts",
            "children": [
                {
                    "id": 165,
                    "name": "Palace by RIU"
                },
                {
                    "id": 166,
                    "name": "RIU Hotels"
                }
            ]
        },
        {
            "id": 53,
            "name": "Wyndham Hotels & Resorts",
            "children": [
                {
                    "id": 284,
                    "name": "Trademark"
                },
                {
                    "id": 150,
                    "name": "Wyndham"
                },
                {
                    "id": 141,
                    "name": "Wyndham Garden"
                }
            ]
        }
    ],
    "properties": [
        {
            "type": "vacation rental",
            "name": "Top Location Condo Infinity Oceanview Pool and Gym",
            "link": "https://www.pdccondorentals.com/listing/en/336618",
            "gps_coordinates": {
                "latitude": 20.62751007080078,
                "longitude": -87.07704162597656
            },
            "check_in_time": "4:00 PM",
            "check_out_time": "11:00 AM",
            "rate_per_night": {
                "lowest": "$52",
                "extracted_lowest": 52,
                "before_taxes_fees": "$40",
                "extracted_before_taxes_fees": 40
            },
            "total_rate": {
                "lowest": "$1,569",
                "extracted_lowest": 1569,
                "before_taxes_fees": "$1,200",
                "extracted_before_taxes_fees": 1200
            },
            "prices": [
                {
                    "source": "www.pdccondorentals.com",
                    "logo": "https://www.gstatic.com/travel-hotels/branding/icon_default.png",
                    "official": True,
                    "num_guests": 2,
                    "rate_per_night": {
                        "lowest": "$52",
                        "extracted_lowest": 52,
                        "before_taxes_fees": "$40",
                        "extracted_before_taxes_fees": 40
                    }
                }
            ],
            "nearby_places": [
                {
                    "name": "Playa del Carmen Alterna",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "6 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "47 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 6 min"
                        }
                    ]
                },
                {
                    "name": "El Fogón",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "3 min"
                        }
                    ]
                }
            ],
            "images": [
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/Mqjnm_RPxtUeizHrzcrXTb4-7R0vd5ej7Rr3AgIdXsib9tBUuEYJSj7WkoZY_zUIq4-bbD2LN4-Bym7LNlzOvRBPMUyvkcq9aiRbD9coDbXTozziGJ6Q1zoTeLtRTceNQJa5UgGKeq6ZneoRJr8Lz9RsWpzC9g0=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://l.icdbcdn.com:443/oh/84a9fa26-cdae-4bd3-8691-07b83d84f672.png?f=32&h=1440&w=1920&scale=both"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/HMNwwjErtfSep5VlyexWqwbr4sTnAfIywcPZRjHK2V8-dPLgeKJhsBQcFGKCUr2sPv-uOkxRsvgCAkEWgwbl0-lIo93DB_j4KyOuvfT-2uHx3N-9zvQgIzVrV5WrDoYhrA_p2Qubd8jSqSzEiL92e2_ac7b5YkA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://l.icdbcdn.com:443/oh/f6b60a4f-3263-4b43-a7c8-b7129995e10c.png?f=32&h=1440&w=1920&scale=both"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/O7vDGsUEEyayQGVErvoy2c7rSYlfKeEEn1i_5KlTbtpotXRbTjssS1pIK-iBvvpJLynsrLqp8RCN5-MHU7KI99OMoE2H_JsGpM8Xs8FyoeE4RG-t-dp-PQBzmG52o-wRNDTF_Uvv3PIOeAvhvoY7T8xYae6xxtI=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://l.icdbcdn.com:443/oh/21f43e7d-84ff-414b-8fc9-6b33aa043970.jpg?f=32&h=1440&w=1920&scale=both"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/NOOP6vW5GUIh2cMRisOZ1Q70dpjGcbiUcJ5c3_7fCvoaSjqkjlCFYTDpOI6ESaQZlMr6nHgOYgmv1y117DnSO2phlW7ZViv5WFcPTSU7YJc3nHdUgzucMC_lquwHA1TpTQKqnJn2skaLWn3eL6FNuf20j5dP-iE=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://l.icdbcdn.com:443/oh/14c01080-470a-4e63-ae27-e7dbe6219229.jpg?f=32&h=1440&w=1920&scale=both"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/z19Qo9BbvOpB-v86ZpIWvtumNnUnvWHa_ffaTDlbxLLkii5accJHsykBI3E1lkvRBEY1a8s7ac2AR0CZNZuM1ROk1V31DdXzS4gvdacgQ_Tu1U2kktl9HKnrIlY7Jug13thhQxFBp32f7hJqLlusZgaVqTrzm94=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://l.icdbcdn.com:443/oh/e6c6aa53-3bf6-4f8c-8e3c-319e23d16f45.png?f=32&h=1440&w=1920&scale=both"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/RiPIYp--0-t3kKqP-HJSnCrc9LN0wgRJ5Nxug35SAUHsGuF23CHgLmKPJNLDRmY--jSZEAXR8O3VTaTdyKIDzKWZmzb6LpL4a0ZTINAthbpbaSAEyqg2GYoASIWAncQ6sOlGqejGPpLZTBoD9jvIMMEwBKjHClk=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://l.icdbcdn.com:443/oh/60d31c14-1544-440a-b0ac-21a76ecb9176.png?f=32&h=1440&w=1920&scale=both"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/fa4vcYHY402qr_DEzM6Kdc5DN92VzdEMaguGAAmvQzP9-T5-ndZHtXmmo3ibVzkWs0tZwJA_fF46J4cf1xgm_43KLAerBROOqtcv1FrzbGfOShiQ1SAH2e_DdnuE5-_CS8jPhYfz7EDAoGQC9Hhm6TiclnYnQQ=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://l.icdbcdn.com:443/oh/3970f264-83a7-40c9-8247-abbc880c9bfe.png?f=32&h=1440&w=1920&scale=both"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/7WtM2qlo322lTlveOUhs4SAVVaoIvUGGUoGH2V5btQfC0bQ7VuS_7Z4CH4G9QsQJ2mvfIZYHK24Fjfh9RKUa_q9zkTp2IeO1Y30o2looTm9HrTgvYsqTJ2RDxdsiw1ydOLsJdHwmYH9v5zLMEQf4x3yafj2KIVk=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://l.icdbcdn.com:443/oh/13506237-7384-438e-8a67-43db218a9c99.png?f=32&h=1440&w=1920&scale=both"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/oviPF_jFa6gfMF_rRcM8NsQhQ4cZhHm5bLCqor17i3kNPutSoz73ZoAdT9BfatSwM8iMEZRfFOzCHUAx7v3NSilfxSpwA26aBiqVLZ6Try3bsOT9oGaHVW1l_SyobuBXxhMNEIqT1Pf79gvoqxrjdOfXKmRvKg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://l.icdbcdn.com:443/oh/42e2c266-632e-44b3-91d9-8cc5f6a439ac.png?f=32&h=1440&w=1920&scale=both"
                }
            ],
            "location_rating": 4.7,
            "amenities": [
                "Air conditioning",
                "Balcony",
                "Kid-friendly",
                "Elevator",
                "Ironing board",
                "Kitchen",
                "Microwave",
                "Outdoor grill",
                "Outdoor pool",
                "Oven stove",
                "Smoke-free",
                "Cable TV",
                "Free parking",
                "Free Wi-Fi"
            ],
            "excluded_amenities": [
                "No crib",
                "No indoor pool"
            ],
            "essential_info": [
                "Entire apartment",
                "Sleeps 4",
                "1 bedroom",
                "1 bathroom",
                "2 beds"
            ],
            "property_token": "ChkQrq2s-v79gJ04Gg0vZy8xMXZqam1uZ3lnEAI",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkQrq2s-v79gJ04Gg0vZy8xMXZqam1uZ3lnEAI&q=Playa+del+Carmen"
        },
        {
            "type": "vacation rental",
            "name": "Penthouse with Private Roof Jacuzzi, Beach 10 mins",
            "link": "https://booking.stella.rentals/properties/65e2010d8291c80017ac3ec8",
            "gps_coordinates": {
                "latitude": 20.632850646972656,
                "longitude": -87.07330322265625
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "10:00 AM",
            "rate_per_night": {
                "lowest": "$51",
                "extracted_lowest": 51,
                "before_taxes_fees": "$36",
                "extracted_before_taxes_fees": 36
            },
            "total_rate": {
                "lowest": "$1,529",
                "extracted_lowest": 1529,
                "before_taxes_fees": "$1,068",
                "extracted_before_taxes_fees": 1068
            },
            "prices": [
                {
                    "source": "Stella Rentals",
                    "logo": "https://www.gstatic.com/travel-hotels/branding/icon_default.png",
                    "official": True,
                    "num_guests": 2,
                    "rate_per_night": {
                        "lowest": "$51",
                        "extracted_lowest": 51,
                        "before_taxes_fees": "$36",
                        "extracted_before_taxes_fees": 36
                    }
                }
            ],
            "nearby_places": [
                {
                    "name": "Playa del Carmen Alterna",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "10 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "50 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 10 min"
                        }
                    ]
                },
                {
                    "name": "La Ceiba de la 30",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "5 min"
                        }
                    ]
                }
            ],
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/4wIeb3OMzxbFdeobXH_CN3fJEzbp2hSMaHzPCnCILSEk-3qGUALTc3PE2g47AkY5_lI-AIe0QRbdLKL5PKTH3qopzE0GphaFftMEW4POBVsPgx4rloshYeGR9r00UzEYV3uDOHDI3hsO7LAIW9gmQYDO-7W8aA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://res.cloudinary.com/guesty-test/image/upload/v1710430653/lygxgjt90aulifseg5e9.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/cvfPW3I20scOE7RxHv7CNeRW2Zemu38SHw_XkXmugbB4fvYfB8YTQUCGvIy0r33mpDX8BVCcZAqCnozdDCOA9rJStQljym7j-ohtNjmPf8vGRFUuifbmhiiA-EVoqsoid1hErkC2ZbXYZfI9sMkqAlGpWllesg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://res.cloudinary.com/guesty-test/image/upload/v1710430653/ysx8mumzf8yzsdayp5pn.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/M06CzlZGrf1yMrT0tjvyLzXjJSbQK9JJofjaGR2d4kK42oFjIkdbpLRcMLVg7-Ck0FdDu-Oy-YfFYOHgs4q-Pl8lEaM6Xn1_RybFNMK6-fAvzkHe_gAdfkj7wLBxfotZnGpD8yUsyyApeDs9yWemp8C3Sz_qaho=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://res.cloudinary.com/guesty-test/image/upload/v1710430654/ibxwtaaj8dgaxgxd0hrt.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/FutvT4L3XYFTuVvy4eZvdY8lLitKqjFqgMgWC0Ae3Wxyrt4vLcsM1JagP5AO02jtmkHPtmXVBLM8S_Q-PjRElhIhAxCPbwE31O2Lf7qQr5p5wOJD8fLBvssXp7f2jdV4nmqAsl1r9x-UcGnKFeM5tgq_2By8Fg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://res.cloudinary.com/guesty-test/image/upload/v1710430653/r8c5oolxj9tlatqxwrgm.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/o590fUMCtKvVkFtXTf8TggWoJR48GQ6mygdBErpOTJb229I2MNuK8a6eHPWWiOh64HSH4Cp5ziQp6yERTWuGAgnnqQUTpOxqBqWknDlqMn-T5TEUPc8YiLoix9tdOM_QGlzgdnyJkP4xOyWyVBKJPG-flvY1ug=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://res.cloudinary.com/guesty-test/image/upload/v1710430654/xsmi9lirbix0nyw6y5df.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/dPQB-lt9BlgZRnea4Rm-gQe8hXi_rSt6aRzSj0nstzZD4YCu5y6ultUh0HOMXCYkBX_F3Zhbhqh7zQRS7A5sRzvbXg8tgGZ2OzRViB5ue26QrnxPN7c-Ea15dA9MSmJEFYafLg-QGAKJgX0AdetB4WrqjHsc6Q=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://res.cloudinary.com/guesty-test/image/upload/v1710430654/uyslltudfxa7xmwsfuom.jpg"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/Z2qocxSckfZxyQl7e_5hAaNby4sEwx0-sjLmPNHUCfxvh-WahH2W7T36IStAELSmskTdkbXBwvu35VDYehal9_M2CMLBag5ghoOnfJwpsh2_Bpb4AaKVGTtO9VHaANFUUDtlEdZJBRSU4s82zhAK69E4LNkkFis=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://res.cloudinary.com/guesty-test/image/upload/v1710430654/b3mtwbzyhg1xseque5ll.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/2X4aFggVjHx-Jav9YIcJpYrhK850oxiZRLlxr2MH7H6PojjhUNAQn4C0PoMNPVXGo98VEEeliyrx4DCYh5PJmdXIk6fnPLlLJFQdBVV6bnhUjFH22KyHetIqcnNB_-fD92O6QLAFH2dzJRyXTxr9Ib0RKg85aF8=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://res.cloudinary.com/guesty-test/image/upload/v1710430653/y5zxm2zwb6ddqjjxjjn2.jpg"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/mVUqNYXBlnEmCOAIs1RqFddRxjd1zyw3qSSd3EM8NT02M6W0naXVK4GBNgC_tnaXuqpnQsdmtWLbErmTQxpD4PKPWos_ZACLi6gYFw_0SzwwwrvyIguXeFhH9EvnTkEQhcWURmQ6kEEuauSy1j2ydg7FCvMp9Uc=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://res.cloudinary.com/guesty-test/image/upload/v1710430653/bfbf6tn2djoyy5wm1j65.jpg"
                }
            ],
            "location_rating": 4.5,
            "amenities": [
                "Air conditioning",
                "Balcony",
                "Elevator",
                "Heating",
                "Indoor pool",
                "Kitchen",
                "Microwave",
                "Outdoor pool",
                "Patio",
                "Smoke-free",
                "Cable TV",
                "Paid parking"
            ],
            "excluded_amenities": [
                "Not kid-friendly",
                "No crib",
                "No fireplace",
                "No fitness center",
                "No hot tub",
                "No ironing board",
                "No outdoor grill",
                "No oven stove",
                "Not pet-friendly",
                "No washer",
                "Not wheelchair accessible"
            ],
            "essential_info": [
                "Entire apartment",
                "Sleeps 2",
                "1 bedroom",
                "1 bathroom",
                "1 bed"
            ],
            "property_token": "ChkQzeXVgZfv7tMfGg0vZy8xMXZ3bHh6eXYzEAI",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkQzeXVgZfv7tMfGg0vZy8xMXZ3bHh6eXYzEAI&q=Playa+del+Carmen"
        },
        {
            "type": "vacation rental",
            "name": "Menesse Midtown 2 Unit 208",
            "link": "https://www.vacasa.com/unit/104836",
            "gps_coordinates": {
                "latitude": 20.626943588256836,
                "longitude": -87.0771484375
            },
            "check_in_time": "4:00 PM",
            "check_out_time": "10:00 AM",
            "rate_per_night": {
                "lowest": "$46",
                "extracted_lowest": 46,
                "before_taxes_fees": "$31",
                "extracted_before_taxes_fees": 31
            },
            "total_rate": {
                "lowest": "$1,384",
                "extracted_lowest": 1384,
                "before_taxes_fees": "$921",
                "extracted_before_taxes_fees": 921
            },
            "prices": [
                {
                    "source": "Vacasa.com",
                    "logo": "https://www.gstatic.com/travel-hotels/branding/545799de-fc37-408e-88d1-fe60e131f551.png",
                    "official": True,
                    "num_guests": 2,
                    "rate_per_night": {
                        "lowest": "$50",
                        "extracted_lowest": 50,
                        "before_taxes_fees": "$35",
                        "extracted_before_taxes_fees": 35
                    }
                }
            ],
            "nearby_places": [
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "55 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 10 min"
                        }
                    ]
                },
                {
                    "name": "Esquina thai restaurant",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "5 min"
                        }
                    ]
                }
            ],
            "images": [
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/YXald3vhS3xCPF5LmTf9JV8Ego-QWKI5YDkN5eVO1SOcb1-9GfX6LNZqu5rG8EUTrf1RtYG-130jfiiESDM5nTJxsOd-3OUOs6ZwX3gJ4VFnP1uaiUPndZABUrjveNAlgE0Fz6XNGA-KQoje1LsPN5KzbZtY0Xk=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5137865.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/laL6pxpRI5Dmo1PmdHlWRC7i2wWLjybPvbF8vN7Nhfo9GUT07LlKnAIOoAo5880BOHUixIMc-OzvzmMbXASGZMjoeeLuLvG9CvuWt2sLsILAtc9j81I15Zl8jhdSWsC8CFR1LdQoDWYlQmMzLitNp6-NIdDN1Q=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5137861.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/eUe503kmmxgVVNHEVy9JahVhBsCZUzqOzYO2gi9P0ipjZo3OdmVpCope7Lrvkvi_GNMNE8nf6ciKAQ8hvZE8gCqfS6z_8l-BM5xsF87eI41t8BH1FSMZqcZ-6KKgApJ862mnASnhre7uLCnbNLlqBRjAc9P3cA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5137863.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/hvc2eAmLpBb1Mg45BDw_dV3NhYvjjOlDsqE73FNCBFoHNBRABxuYX4zpy02PXqkRtCsAkqNrCyCcQbEG2CQdlaI-rkV73KkIJLH0n23TRUlA-MtbzvV7Gnert9UngpuxeXZqsCAm5ljyT5MkIxVCCRqejzWhTg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://assets.whimstay.com/4915961/94459/343c6fd3d2ebf8e5cacae6e3c532fd07-5"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/7fWs6F87psVvvvd0wx-z75joSrPYy-kFrg_7aPp6FdCTNu_s6cdMp7QmLRt3oIC6FiQ6-h_hh_WyiPUefpkVKzG78dh4S8dgrkAfsG2jmqRApMVrifS0SOtTnOgm7T48ZWon0fPQJTUgb0MiTO-FjWPQGhOT46E=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://assets.whimstay.com/4915961/94459/56a369d96d84f60eb65df9062bebe29f-1"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/uEwB-YybKShr9dJxY_f31ZWQ9BYo29-o1CrhxO83ipZMS_-V6SH9DezPA-zQIFENgkhG41zk1nRMx-nS-R1QmAJ2R7_lOOK4CnOJVX1Ic5fOmgvh7zWpsgqdtdo5a-Citt0nxNYsJxIWcDaWP1Ee8edD3_-yGw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://assets.whimstay.com/4915961/94459/c892e30b7a2d4fe43b3470a89c794d53-6"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/KU1Wv1slfVROIl2T-wV6xhoDk2IpAhvI_-Kb0NcjTuiVXWc4F9aEPShXpDlvqFlWv7cHHiPj2nexGchEqPqBK3z9XjcSmWq8rsJ_UY836PTiOhP2as9sro8mmFXaQmYtuYolba96PlPlwpUylOF-_GUmkL4CfA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://assets.whimstay.com/4915961/94459/02957af15f9bf71a71e4d6dcda015a09-3"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/VIMCFOd66By0EpG4_QpoIKV3cgvJRrHtI2ESkAS9RquSrV5UBMXcjNWhJS-zKO6l6xvI70ZzaaA2hu-J75pGx0oArGSMewptLfDtbpt1yW0qB0R0oPSkd-IWq7eKqPRQnVOsZvthPDG-Pn8XcZjIRvu9HtLuOSY=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5137870.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/N4THnr8qkdatrn5hkwMhJ7uVC1cPSfXM0WoLYOHGilGaHUFSLBwvhV7njlHu5-Wp8J2EqohrJD7GXNymZSrzy6b0rZjx8Tu9fFvMy9Pyle5_6r5PkcSZ3E6HghPGUmQbyR-avhkVNsoPCG7f1VSK5kV0tixIijg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5137864.jpg"
                }
            ],
            "overall_rating": 5,
            "reviews": 7,
            "location_rating": 4.7,
            "amenities": [
                "Air conditioning",
                "Balcony",
                "Kid-friendly",
                "Elevator",
                "Heating",
                "Ironing board",
                "Kitchen",
                "Microwave",
                "Outdoor pool",
                "Oven stove",
                "Smoke-free",
                "Cable TV",
                "Paid parking",
                "Free Wi-Fi"
            ],
            "excluded_amenities": [
                "No airport shuttle",
                "No beach access",
                "No crib",
                "No fireplace",
                "No free breakfast",
                "No fitness center",
                "No hot tub",
                "No indoor pool",
                "No outdoor grill",
                "No patio",
                "Not pet-friendly",
                "No washer",
                "Not wheelchair accessible"
            ],
            "essential_info": [
                "Entire apartment",
                "Sleeps 2",
                "1 bedroom",
                "1 bathroom",
                "1 bed"
            ],
            "property_token": "ChoQ2uXap_zzu6XCARoNL2cvMTF5M2o1emcybRAC",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChoQ2uXap_zzu6XCARoNL2cvMTF5M2o1emcybRAC&q=Playa+del+Carmen"
        },
        {
            "type": "vacation rental",
            "name": "Perfect Place # 301",
            "link": "https://www.vacasa.com/unit/101003",
            "gps_coordinates": {
                "latitude": 20.628740310668945,
                "longitude": -87.07148742675781
            },
            "check_in_time": "4:00 PM",
            "check_out_time": "10:00 AM",
            "rate_per_night": {
                "lowest": "$48",
                "extracted_lowest": 48,
                "before_taxes_fees": "$32",
                "extracted_before_taxes_fees": 32
            },
            "total_rate": {
                "lowest": "$1,436",
                "extracted_lowest": 1436,
                "before_taxes_fees": "$957",
                "extracted_before_taxes_fees": 957
            },
            "prices": [
                {
                    "source": "Vacasa.com",
                    "logo": "https://www.gstatic.com/travel-hotels/branding/545799de-fc37-408e-88d1-fe60e131f551.png",
                    "official": True,
                    "num_guests": 2,
                    "rate_per_night": {
                        "lowest": "$51",
                        "extracted_lowest": 51,
                        "before_taxes_fees": "$36",
                        "extracted_before_taxes_fees": 36
                    }
                }
            ],
            "nearby_places": [
                {
                    "name": "Playa del Carmen Alterna",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "10 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "50 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 10 min"
                        }
                    ]
                },
                {
                    "name": "La Caprichoza",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "5 min"
                        }
                    ]
                }
            ],
            "images": [
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/Ol09wiOzlAXBZTxaad3d4vIyW3wRlnzHI5MqRzgNuuzqKu6xcNjf_Y3qwZQnSFxF1KVKF9XACj5Z-KBH_iJfSO-aEC1z0a8EfxPdlt8PH7N88Vv7DqWl5otwOuP_79TFhI37N8Vrm7gQ_Oj3GplB4NdzBq1acfw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://p.fih.io/v2/nSr0o-3gbZN8o1xMecXCcG-BkDeQVo3k-wOeVogkTe7ajuFOX7O-WA8aRWhXz1jsToZif_TsA_xCWfhWRa0ZmYiFn30y2EVmMhKhbb1gtWfGpXvQTo2OmBzNN4XOuLmgKT5H9JLdC13TfjF4en3ketkYyx1j1dLbUfhlOgkNcIcn9PwNtk_AU2csbUk6dd9sGo49Qn31qiMVOoIxofR_2o8VcZA3AAhCPReYBoJ8vY2Gq2593GaA4qMOT9Db2nQda_hJpgMz3IWqqItHLkiogoG54aTRYWZy9f9Ay66Ya2o8FxN_WzehAb09VepiRB9P7xJOPltJaDWrUUZGpVzU5xdsyqRpfTLBJuhq1NcKUvg"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/bt0YRctvLUOIFBvotFhshq7cJzTIy0hCPFRZAUTLYNgBT97XSo_OHXAOMz8PKDJe5bEUBl_LIO4F62tUu8ezxAxAURKVkh2OX1jQyBc3kl_sQ-Q-HmQoo3fQrZ_TswWoYGFf7CRDk2Ju774HUaBV5QKZdtBVLko=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/4948068.jpg"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/nSsbnc17QAwLSm00vb3AkbgOgs4y1NZDPy0P2oP3WN-ir6C4cIvlB3Vqr_LGhWJFhiSMGycErREpPVgLy-jL0KKLusHK2d9Trj_srXn7m4KlQ-m_ba01AiM4Pl92mONQPEJRZHZ0SLGtmRK1Em7HBCvDbJNohw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/4948070.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/Kq3EomTm3F-P1tFtNlJ4q4OkPT8QUb-QUlM3idm9bnqOVACXmdGYkLjREj1UqSPq_W9uFEUtv6KOVcyDfIVK2NN6nZUdfuRtTc2mCYbqHVh-4crzp13kyZ13nhEDBfSK56ZI3m3AK_-If5yat3en6JjzGAx19w=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://q-xx.bstatic.com/xdata/images/hotel/max1440x1080/432623620.jpg?k=bc9f8b89121f59bad2dfa161ca7d42f34c76a7c9e80bd062f1b3bff9c426ccb7&o="
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/0_VdlbCeSYVJGcQSgYvu6jrlzf4SXv7WFN9UUgxLWV-8nCN9wlE8PZIWZkcS6ygbVIwmbBS20DMwzhWpus2NCil0tCkQgceJdPBh5azg0RngdL_HdoAjYcf5kZMLC_6P7OzLZ6M1yOpxtb0HH_uG-Lizzwpu4nc=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/4960456.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/UY9EZssX8rcvQgdmeCNfVCEbhjNwJ3Vl1YwKf8TZ-5LvoJKHeK8vQhVxdCVJjTPelC4fVbfXs4MUIwo__jyNRlgBAYkL-Ly7xCojNMTy939P_4VkqyBNeThR5RF6S29Hb9jQWzUORONeW0v52WyUFN_MxBJjUA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://p.fih.io/v2/nSr0o-3gbZN8o1xMecXCcG-BkDeQVo3k-wOeVogkTe7ajuFOX7O-WA8aRWhXz1jsToZif_TsA_xCWfhWRa0Zj8Szmxw7wSM_NQ6xR7lnsz30rVrDHuyhmA_cH5DgmoqWCgUT74jXDWD-DzF4en3ketkYyx1j1dLbUfhlOgkNcIcn9PwNtk_AU2csbUk6dd9sGo49Qn31qiMVOoIxofR_2o8VcZA3AAhCPReYBoJ8vY2Gq2593GaA4qMOT9Db2nQda_hJpgMz3IWqqItHLkiogoG54aTRYWZy9f9Ay66Ya2o8FxN_WzehAbwqe-F2Uw9TohE5PltJaDWrUUZGpVzU59xoSYen8gMCekYBTKrR5OY"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/4zZRyVvpriqzE3l0Z2zueVEkBQQmrogKy0kjTy0ZXJ3svXMyPb6_FsU6Y3hszEeu9Aa3UJbtCgJ78KGEqSs_9MoL4hqckIUwXT3SCa21RLQX6RVFdFfpdOJ7XK-cU66_biw5bWlFsVblfwHJ1D-7lwOS1m1gIbU=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/4948065.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/_NirfOjWhWsbPRCy8H4a-NarZh1S9zsq7-FvpBJylpCLaDo7AGvGjun6u1cqqUX9CYYVuSXvytm_U81Ek_p-aSvD6dB4YMMtnWJQnF1QuRnDDluvYt6UMF-oJZoVrSOAfgJRvRv5_vCBGg8wZrPPQ6Kld62eewk=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://q-xx.bstatic.com/xdata/images/hotel/max1440x1080/432623605.jpg?k=ab3dc0cc73170c89e92a8b2ab42d65dc2eac7a274ea3bdd3fe2a62d5f4ce7509&o="
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/yGfCSpgD0IyjplJmCu1k7pHMVyxOtOdQePsXg8IjL3Qxd2RkvCSNqPMeQG4PgJCU05X9-qlENO9-OvGNneCZRIqpQ7k5X1w_6TO1Hm1hvx77xzHlhUdAcoaRbQgGu840OP1leO6cu3rEKYjkmVKIgH5b33aGZNM=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/4960461.jpg"
                }
            ],
            "overall_rating": 5,
            "reviews": 6,
            "location_rating": 4.7,
            "amenities": [
                "Air conditioning",
                "Balcony",
                "Kid-friendly",
                "Elevator",
                "Fitness center",
                "Heating",
                "Hot tub",
                "Ironing board",
                "Kitchen",
                "Microwave",
                "Outdoor pool",
                "Oven stove",
                "Smoke-free",
                "Cable TV",
                "Free parking",
                "Free Wi-Fi"
            ],
            "excluded_amenities": [
                "No airport shuttle",
                "No beach access",
                "No crib",
                "No fireplace",
                "No free breakfast",
                "No indoor pool",
                "No outdoor grill",
                "No patio",
                "Not pet-friendly",
                "No washer",
                "Not wheelchair accessible"
            ],
            "essential_info": [
                "Entire apartment",
                "Sleeps 2",
                "1 bedroom",
                "1 bathroom",
                "1 bed",
                "330 sq ft"
            ],
            "property_token": "ChkQobndvd62mJUIGg0vZy8xMWtqNW5tcG02EAI",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkQobndvd62mJUIGg0vZy8xMWtqNW5tcG02EAI&q=Playa+del+Carmen"
        },
        {
            "type": "vacation rental",
            "name": "Menesse One Paralia # 405",
            "link": "https://www.vacasa.com/unit/101456",
            "gps_coordinates": {
                "latitude": 20.629587173461914,
                "longitude": -87.06973266601562
            },
            "check_in_time": "4:00 PM",
            "check_out_time": "10:00 AM",
            "rate_per_night": {
                "lowest": "$48",
                "extracted_lowest": 48,
                "before_taxes_fees": "$32",
                "extracted_before_taxes_fees": 32
            },
            "total_rate": {
                "lowest": "$1,433",
                "extracted_lowest": 1433,
                "before_taxes_fees": "$950",
                "extracted_before_taxes_fees": 950
            },
            "prices": [
                {
                    "source": "whimstay.com",
                    "logo": "https://www.gstatic.com/travel-hotels/branding/47baa73a-d952-4f12-b216-932d02f65d3a.png",
                    "num_guests": 2,
                    "rate_per_night": {
                        "lowest": "$48",
                        "extracted_lowest": 48,
                        "before_taxes_fees": "$32",
                        "extracted_before_taxes_fees": 32
                    }
                }
            ],
            "nearby_places": [
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "55 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 15 min"
                        }
                    ]
                },
                {
                    "name": "Los Aguachiles",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "5 min"
                        }
                    ]
                }
            ],
            "images": [
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/ofV_aj0Y10dRFPPDmZtqNvqp6z4ZSkDm6YjuZ03xbeKWm_6PeiI8bUylWVFUnU4bP-HT5xPgKXg-WlKndUgUiwZLU_mupPKEUNuQLQRa81dxPmRaCr1BReF4rWb5khtlNnLA4csBWB72CycJEnqmaxfBc_rm1A=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5211911.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/LfoEmy4-E2HdWag4SJihqzfukj6cTf6qOMxZgtBB38KZEV8cD19LRdNfBOHdjiVKCwhsyWp7xot4iFOJwcuf4Quz-b9ATbkvbRdlZHpCbE3rpSJTGRUjOhwAZANTFj-pKtUndjtEXgjAb-PrIGN6iJJeKAvVlA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://assets.whimstay.com/4915961/89237/6730edf69bba555d4088e3a392f47e8e-16"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/h_PhGhgznwPrGBh3uReE-F6bS_yovUntZLpAMyimTat-VA399IH8xYV9IBr_cjdQu4wyLF_Hirf4XJ9OEPHUvT5rjkzxm976COX33CEzw10hsbzYuwXQSI0JIxs3RT05IcLryGjZLZwwcoK_CBCqtsJGt8kXkg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5006224.jpg"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/m5Mqv_Y4SAoxmLug_TiTNW6q2miO8njM-o4vDO2vzlI09B6lEh9HuA1gf-11mvFVLCVSqHcHlax3Oz5ewcud68RYOZHX3sLBZ4NtShGQdOdVrHW8V6Rh-6-ul084SLKfNppI2dVtHkZh-1aR7ySkYZR-JaXsJg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://assets.whimstay.com/4915961/89237/282618c8ad7b4aabb93fb84a754921d5-1"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/hbMAbPTodcm7qujJG5D3SkIWp1HS1R6lLQRJD143JhsdXM7MCRcLyDpUoTvpY7gAvcIG3dQbS0ydjgLMgpjiooCSSOSUEBuBj-c6rmGML7lfnhf0ol_v8DK-j-zr87of9bbBJsV11PEzKbFg8lV3VZBVWOPGJQ=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5006227.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/w8cMjAWqxbpFS8gX3IQgvpSXJAhr7h8u0ajEl3AsSDPSUaCNb3Vxro8A1NxLTAk7S3lgT0bTf6JVNgTFdyfuqZZAx3_h5aJfdpUa0KpprhC7tAWhB6dlKM7UVY2m0i304pjGH74g6ADCbZ177Vb2wBbndWLsc1A=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://assets.whimstay.com/4915961/89237/7d2655e41b8ae76caa597fc0a3630b33-5"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/ouxaJR4pK6C7HaAspuisa0UbcX6qifQtxmuVXVebAzfLefrI-DTFHG_IdigpmQmjsETBbn9lOl36v2crn-abcqtLz3zmUtq6k2-gW0gzZHMl0BkZ5Q98KSCJyOBEAIkrUqm1ImDxA4m0bf2YwQwBPOOaRRCyuOo=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://assets.whimstay.com/4915961/89237/81c28829f7e50e9d315d4c9e9c056fe3-3"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/Htr8cDlspHt-rh7IIlYiFg6z9RvshDLe7KPCcYZ1DjOZZRayfHrL5JQRrlztRe9sYXmV3V9j1r3GZdjJ28krrulV1To60Qq18eHixFrywWMKnfG0u980JVHnlN9ugWPSKAOGiTrkLXfwGR1nbLFc9v2b125mpw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5211909.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/K4x2-ctqR20fmqIS8Xqfajw990EoiqYU0yNC7C8Ar2n9OjtRBUbfoH8QaqeNXXDjN0egaMdBhikJoLgmMbZFo3WHsTzmjue-ZiH5Qzu7boatvvgpkEY-g5LkUMG3bejewGKhYdKlwskIdOoHPKPCtD7YKJXq_8Q=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://vacasa-units.imgix.net/5211906.jpg"
                }
            ],
            "overall_rating": 4.93,
            "reviews": 20,
            "location_rating": 4.7,
            "amenities": [
                "Air conditioning",
                "Balcony",
                "Kid-friendly",
                "Elevator",
                "Heating",
                "Kitchen",
                "Microwave",
                "Outdoor pool",
                "Oven stove",
                "Smoke-free",
                "Cable TV",
                "Free parking",
                "Free Wi-Fi"
            ],
            "excluded_amenities": [
                "No airport shuttle",
                "No beach access",
                "No crib",
                "No fireplace",
                "No free breakfast",
                "No fitness center",
                "No hot tub",
                "No indoor pool",
                "No ironing board",
                "No outdoor grill",
                "No patio",
                "Not pet-friendly",
                "No washer",
                "Not wheelchair accessible"
            ],
            "essential_info": [
                "Entire apartment",
                "Sleeps 2",
                "1 bedroom",
                "1 bathroom",
                "1 bed",
                "484 sq ft"
            ],
            "property_token": "ChkQ5e7h76mrpNwiGg0vZy8xMXNzZ2NrOXo1EAI",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkQ5e7h76mrpNwiGg0vZy8xMXNzZ2NrOXo1EAI&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "SC Hotel Playa del Carmen",
            "description": "Traditional rooms with kitchenettes in a Spanish Colonial-style building offering dining & a pool.",
            "link": "https://www.playa-del-carmen-hotel.com.mx/",
            "gps_coordinates": {
                "latitude": 20.625462,
                "longitude": -87.07669299999999
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$40",
                "extracted_lowest": 40,
                "before_taxes_fees": "$38",
                "extracted_before_taxes_fees": 38
            },
            "total_rate": {
                "lowest": "$1,199",
                "extracted_lowest": 1199,
                "before_taxes_fees": "$1,140",
                "extracted_before_taxes_fees": 1140
            },
            "deal": "40% less than usual",
            "deal_description": "Great Deal",
            "nearby_places": [
                {
                    "name": "3D Museum of Wonders",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "8 min"
                        }
                    ]
                },
                {
                    "name": "Playa Del Carmen",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "7 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "48 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 9 min"
                        }
                    ]
                },
                {
                    "name": "Restaurante Casa 8",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "3 min"
                        }
                    ]
                }
            ],
            "hotel_class": "3-star hotel",
            "extracted_hotel_class": 3,
            "images": [
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/1X8XVpIL5bH9wtvJK-2jO6tpOv40AQD1zg7rZGK2yWqxmVYff6b381EXLNtInRwAlrzWhuOP1ST_PqOl9Gft7Dj3CHHAVt8g9n4fGlgjZYFvnLENIBQJVqmFVC4iMfxi9w13Zz_6NNcQ-mOcAeJCrRV7OwMvjQ=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/12000000/11630000/11620500/11620473/2dbbbef7_z.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/JzEb8ashy4pFDQE4lMFiG43SFGpMLSWsJ8j-DYjomOrMsmQUW7p9zXtqYq_uCO7QF-UIPDJIYKPTpFr2pEo4jJbz6KeQEcbB6ULlFEDYVT0KR11aFfeKddUIvGVZ_5FT8Np6r6_yPFia5bMc6nulQKaS91dqpA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/7/0/149/645/289/Pool_O.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/8LKZ1o9KQ9i3JwlbxYJGBumzz4jzVA9rZbpeX06qoaD0gOVU8ES-XssZWOLkKR6R1Me0s6T88naJG6Qrz_IzSv--0kqG19zKCCEucWyC5Kob18k-_o97WQ9c39MrcBYydHYhpMl-4qfG7Ary9rr5RfE7pN5cwxE=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/49/496141/496141a_hb_p_002.jpg"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/hGlxnQs_PbelFmWpalfnULNvYEzOBSrKzquNvPvSeTDPWS0ZzXTw3Qov4uBQXZwAYb_Ql45RyTwbp4EdutR7zlvNMKYB4x_1pOTyHwqdoQU3kVhroDYDsugJ8W6QxrTi99IN7upGC3Rwytgz_t9yHiXyWtTfBw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/7/0/149/585/712/Private_Family_Room_4_S.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/vO0AneCS3mBREugOrV3y8Trj0K8iy-NTTA_4z9BIRikxy5Igh921Wj0RJeMPKiuRgAWK4v5KTbvoL8g7ZN7a8B95bS6TaiAWnpempf7Vor0zGhO9wvRIzqmywdlMY-DsqHQ3WpTb8ukNLXo8ekqFG4lWHhrlHgo=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/7/0/149/585/880/Shared_8_Bed_Community_Room_2_S.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/vXcJ8l6bjDv6-jrcMnVLuQHT74lptB4_yr-2OaUl3w7VuQS8w37_2ypUtoTxI6NeM9hAOeKvzfaa-hg22Dn7qXdezRoR3rRLjZzfExP17P9rj1naGE48x-44ibsIW9rSuTq5bN4WPBd2IsbGwo8bhZk9NJOJDg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/7/0/149/645/297/Interior_O.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/LugArXyt5hWZlw2GxG-jalOWhZ8XQ1tNRBC8i6fYPr_yZtuaHHl360m5b5hkevaOX7fDtU1mfeqXtcbwxn_qBk8cao6Hzb22P4RrQkYp6LCQrqF0wQMbyKg5Sv_D1KRbsJtgLsuDLiOw2zSFLhU5PzCrb3__Ww=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/7/0/149/645/321/Hotel_Front_O.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/0sE6qwwmXq-0Nf4npYY8nBYHvDvPf2isOuuZyI3Urak3zE-ESF4EPFkvu8mKHxiba61vjUVgxlQvwdeSKWz0f6apcxC-7vVfB3Vvn7Gl3n3q1aUgaX6xR2im7Pe5WivjLqwH_8OtRsmDALBJ3cadg1zBwksQCA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/49/496141/496141a_hb_a_002.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/CXn5Mwo5EUvM5Gz6SRX_ywAZVle0qgczE5SR9mW0fr774hHX0EEZHmi9P4E_gYG5zeFTfEBVAVZGqNxX0WHCUFgbocqWSr4uPAXuQq_9BDX_6D5yuuDZfjrjyFe36TcrhiRAnW502JToypf_PLxYYL3kroYJzA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/7/0/149/585/936/Private_The_Standard_S.jpg"
                }
            ],
            "overall_rating": 4,
            "reviews": 1068,
            "ratings": [
                {
                    "stars": 5,
                    "count": 481
                },
                {
                    "stars": 4,
                    "count": 307
                },
                {
                    "stars": 3,
                    "count": 141
                },
                {
                    "stars": 2,
                    "count": 51
                },
                {
                    "stars": 1,
                    "count": 88
                }
            ],
            "location_rating": 4.8,
            "reviews_breakdown": [
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 149,
                    "positive": 105,
                    "negative": 42,
                    "neutral": 2
                },
                {
                    "name": "Room",
                    "description": "Room amenities",
                    "total_mentioned": 87,
                    "positive": 24,
                    "negative": 50,
                    "neutral": 13
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 84,
                    "positive": 62,
                    "negative": 11,
                    "neutral": 11
                },
                {
                    "name": "Location",
                    "description": "Location",
                    "total_mentioned": 140,
                    "positive": 123,
                    "negative": 7,
                    "neutral": 10
                },
                {
                    "name": "Wi-Fi",
                    "description": "Wi-Fi",
                    "total_mentioned": 49,
                    "positive": 10,
                    "negative": 32,
                    "neutral": 7
                },
                {
                    "name": "Bathroom",
                    "description": "Bathroom and toiletries",
                    "total_mentioned": 60,
                    "positive": 9,
                    "negative": 46,
                    "neutral": 5
                }
            ],
            "amenities": [
                "Breakfast ($)",
                "Free Wi-Fi",
                "Free parking",
                "Pool",
                "Air conditioning",
                "Restaurant",
                "Child-friendly"
            ],
            "property_token": "ChkI3f23zc_iqalzGg0vZy8xMWMxeHNqanR5EAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkI3f23zc_iqalzGg0vZy8xMWMxeHNqanR5EAE&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "Winday Hotel - Playa Del Carmen",
            "link": "https://beds24.com/booking2.php?propid=176670",
            "gps_coordinates": {
                "latitude": 20.6398471,
                "longitude": -87.0682164
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$29",
                "extracted_lowest": 29,
                "before_taxes_fees": "$22",
                "extracted_before_taxes_fees": 22
            },
            "total_rate": {
                "lowest": "$862",
                "extracted_lowest": 862,
                "before_taxes_fees": "$654",
                "extracted_before_taxes_fees": 654
            },
            "deal": "28% less than usual",
            "deal_description": "Great Deal",
            "nearby_places": [
                {
                    "name": "Parque Los Fundadores",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "10 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "44 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 22 min"
                        }
                    ]
                },
                {
                    "name": "Mia's HomeMade",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "1 min"
                        }
                    ]
                }
            ],
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMYHenZFhVk2p62Vdt9N5TPa_wonDVXbLxjPbjT=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMYHenZFhVk2p62Vdt9N5TPa_wonDVXbLxjPbjT=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPO4M9IQZL2Kadn_j5R6FNq1QVgRS81NVfBvwkv=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPO4M9IQZL2Kadn_j5R6FNq1QVgRS81NVfBvwkv=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMjTjukKjRgRvMfhqxsPF2s5-ryy5L3GfNIkTCk=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMjTjukKjRgRvMfhqxsPF2s5-ryy5L3GfNIkTCk=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMw2siyFci1cGo3J46jBFt1df5P6fP00vEE1VjD=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMw2siyFci1cGo3J46jBFt1df5P6fP00vEE1VjD=s10000"
                },
                {
                    "thumbnail": "https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=MDlKUotC5RqD-PezX0ypsA&cb_client=search.estubs.gps&w=287&h=192&yaw=283.5108&pitch=0&thumbfov=100&scale=2",
                    "original_image": "https://lh5.googleusercontent.com/p/MDlKUotC5RqD-PezX0ypsA=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipM2kFOgTCMEVrw1UcMw-gz-9k1abvxSqAXkBBM2=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipM2kFOgTCMEVrw1UcMw-gz-9k1abvxSqAXkBBM2=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNJGHUudBIyIl-3idlJsAbj8ltCpNE_baYyKd4=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNJGHUudBIyIl-3idlJsAbj8ltCpNE_baYyKd4=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNaU7_uovNr3TMOJulyHiUn57gGilGZFH0HANIh=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNaU7_uovNr3TMOJulyHiUn57gGilGZFH0HANIh=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPXQV5lYwo5I3nZIPH-ke7axJlTBfJmoc3qbWh0=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPXQV5lYwo5I3nZIPH-ke7axJlTBfJmoc3qbWh0=s10000"
                }
            ],
            "overall_rating": 4.1,
            "reviews": 112,
            "ratings": [
                {
                    "stars": 5,
                    "count": 64
                },
                {
                    "stars": 4,
                    "count": 20
                },
                {
                    "stars": 3,
                    "count": 13
                },
                {
                    "stars": 2,
                    "count": 4
                },
                {
                    "stars": 1,
                    "count": 11
                }
            ],
            "location_rating": 3.7,
            "reviews_breakdown": [
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 17,
                    "positive": 13,
                    "negative": 3,
                    "neutral": 1
                },
                {
                    "name": "TV",
                    "description": "Room entertainment",
                    "total_mentioned": 8,
                    "positive": 5,
                    "negative": 2,
                    "neutral": 1
                },
                {
                    "name": "Pool",
                    "description": "Pool",
                    "total_mentioned": 14,
                    "positive": 12,
                    "negative": 1,
                    "neutral": 1
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 25,
                    "positive": 18,
                    "negative": 5,
                    "neutral": 2
                },
                {
                    "name": "Cleanliness",
                    "description": "Cleanliness",
                    "total_mentioned": 18,
                    "positive": 13,
                    "negative": 4,
                    "neutral": 1
                },
                {
                    "name": "Room",
                    "description": "Room amenities",
                    "total_mentioned": 12,
                    "positive": 7,
                    "negative": 4,
                    "neutral": 1
                }
            ],
            "amenities": [
                "Free Wi-Fi",
                "Parking",
                "Pool",
                "Air conditioning"
            ],
            "property_token": "ChoIpNGLmOWJkIyyARoNL2cvMTF0bXFxaHBfOBAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChoIpNGLmOWJkIyyARoNL2cvMTF0bXFxaHBfOBAB&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "Illusion Hotel Boutique by BFH",
            "description": "Bright quarters in a posh, adults-only hotel, plus a rooftop pool with a swim-up bar.",
            "link": "https://hotelillusion.com/",
            "gps_coordinates": {
                "latitude": 20.6255727,
                "longitude": -87.07255289999999
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$43",
                "extracted_lowest": 43,
                "before_taxes_fees": "$41",
                "extracted_before_taxes_fees": 41
            },
            "total_rate": {
                "lowest": "$1,285",
                "extracted_lowest": 1285,
                "before_taxes_fees": "$1,226",
                "extracted_before_taxes_fees": 1226
            },
            "deal": "26% less than usual",
            "deal_description": "Great Deal",
            "nearby_places": [
                {
                    "name": "Museo Frida Kahlo Playa Del Carmen",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "1 min"
                        }
                    ]
                },
                {
                    "name": "Playa Del Carmen",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "6 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "49 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 8 min"
                        }
                    ]
                },
                {
                    "name": "Tropical",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "1 min"
                        }
                    ]
                }
            ],
            "hotel_class": "4-star hotel",
            "extracted_hotel_class": 4,
            "images": [
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/TL2HfriRzzap2r6OuuWzBx_fTk_IGafzJ0ZZNtOPI_xaFn4x2hYA1RdnrsbByhqqbVe_6DEU5XvOi5mKajr9xl7YL6MMZUIh6FLm_yaj-_7kTnLtJq8kPs0xPobRFfar80baAO5z-7BOtPcf5uZwR83z2jA5bA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/20/6c/68/swimming-pool-view-from.jpg?w=1500&h=1000&s=1"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNhvjwT5OYGqg59Daoi8gdQF-ayCCa_Upctx_P9=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNhvjwT5OYGqg59Daoi8gdQF-ayCCa_Upctx_P9=s10000"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/t65C1pWBmfmV_M4BZBIuPTDXa1d3sC75_dvQ7rbuws1MdZHrVMkYFv9HC8U5_-NxdpqE6QY7hWixxMrpfdoxHj1i_kjUV9oTrD_qzvNI9CFF0KKeHl0uiaUtpkSS8dohidrmq3rSRJ-C2ypvEGefeD3xWbsZDAo=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/01/019358/019358a_hb_w_015.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/Xm78xvNJLvU_Y0SO0dwo3hXOx-1w6fmPBRBUaCAfN2Ij61DDPMQq55xBgZPUmg32DuoxLnmhLHfzOjyuo9fubZJlGXig804hmjb3Sym4jRoxD2WHVBWBlwrim8LeQkJeFbxaLgDBg9w-mZMaVe4wEgO4H216jdI=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KACvtdgIFAJqLSMQFWRZOpvNJb2l3S_U"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPge7GwEV1a7J81K_GvbGjSPlbGDRtJwYwh1Uxi=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPge7GwEV1a7J81K_GvbGjSPlbGDRtJwYwh1Uxi=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipN-bGqXja5oCN1CAs3NSdEddM5y_0kGjnaxh7rc=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipN-bGqXja5oCN1CAs3NSdEddM5y_0kGjnaxh7rc=s10000"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/wwzavuGksjY6Pt7zu4-zivEgaRU7J0y7-BuLd2GiJlcEMYtYitKorWDsLw9MT9w0YetTYUj7OZ78nbx5o1oJf2cl2SSYmRQytIgX26SCBkb8ETn4Aql4Lov72uEygWotSi7RBq96zt462O0lDF74BuvGxBM2uw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KAC_tdgIFAIVG2VXNkVaxG3hIX8qb1y4"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNnUGWsQeUYtnDqMUq8DV5srMj10XrlIAj_n-e2=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNnUGWsQeUYtnDqMUq8DV5srMj10XrlIAj_n-e2=s10000"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/ddVwDOOaORBtqTxOLL1NcdgHHKlrDXEKUli7MVYOvtceFqGQx8HDJDluvzM2a7YWcNUTgFrTJ9WNISPOQPPR2k2xI_LkH-zG-s8esmQrnl15cljywuVgtqJDz-XzuCyeK66xsoZcQig3nQuCHW3RYy0TbZgQOA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/01/019358/019358a_hb_ro_020.jpg"
                }
            ],
            "overall_rating": 3.9,
            "reviews": 740,
            "ratings": [
                {
                    "stars": 5,
                    "count": 336
                },
                {
                    "stars": 4,
                    "count": 190
                },
                {
                    "stars": 3,
                    "count": 79
                },
                {
                    "stars": 2,
                    "count": 46
                },
                {
                    "stars": 1,
                    "count": 89
                }
            ],
            "location_rating": 4.8,
            "reviews_breakdown": [
                {
                    "name": "Breakfast",
                    "description": "Breakfast",
                    "total_mentioned": 104,
                    "positive": 46,
                    "negative": 42,
                    "neutral": 16
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 167,
                    "positive": 123,
                    "negative": 34,
                    "neutral": 10
                },
                {
                    "name": "Accessibility",
                    "description": "Accessibility",
                    "total_mentioned": 45,
                    "positive": 4,
                    "negative": 37,
                    "neutral": 4
                },
                {
                    "name": "Location",
                    "description": "Location",
                    "total_mentioned": 150,
                    "positive": 121,
                    "negative": 14,
                    "neutral": 15
                },
                {
                    "name": "Sleep",
                    "description": "Sleep",
                    "total_mentioned": 78,
                    "positive": 21,
                    "negative": 47,
                    "neutral": 10
                },
                {
                    "name": "Restaurant",
                    "description": "Restaurant",
                    "total_mentioned": 49,
                    "positive": 21,
                    "negative": 21,
                    "neutral": 7
                }
            ],
            "amenities": [
                "Breakfast ($)",
                "Free Wi-Fi",
                "Outdoor pool",
                "Air conditioning",
                "Beach access",
                "Restaurant",
                "Room service",
                "Airport shuttle",
                "Full-service laundry"
            ],
            "property_token": "ChgIpf_XoNXP8aPGARoLL2cvMXRmbTJod3AQAQ",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChgIpf_XoNXP8aPGARoLL2cvMXRmbTJod3AQAQ&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "Ocean Riviera Paradise",
            "description": "Polished suites in an all-inclusive beachfront resort with 21 eateries & bars, plus a spa & pools.",
            "link": "https://www.oceanhotels.net/en/riviera-maya-hotels/ocean-riviera-paradise?utm_source=Google%20My%20Business&utm_medium=Boton%20sitio%20web&utm_campaign=ORP",
            "gps_coordinates": {
                "latitude": 20.6703485,
                "longitude": -87.03523919999999
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$247",
                "extracted_lowest": 247,
                "before_taxes_fees": "$210",
                "extracted_before_taxes_fees": 210
            },
            "total_rate": {
                "lowest": "$7,395",
                "extracted_lowest": 7395,
                "before_taxes_fees": "$6,294",
                "extracted_before_taxes_fees": 6294
            },
            "nearby_places": [
                {
                    "name": "Playa Xcalacoco",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "4 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "40 min"
                        }
                    ]
                },
                {
                    "name": "La Locanda",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "3 min"
                        }
                    ]
                }
            ],
            "hotel_class": "5-star hotel",
            "extracted_hotel_class": 5,
            "images": [
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/jCnKqoR0Ik8dJAya-Wn8QmF_NemBQ-hNbeRM2GkXVOf43jzYoN47504i_0HBAnhuYop90ZNrYJFEDT6JI0xzkY97USBANXRjsGzIaCWWg7_oGG57p7R0UsOAN7_SVDUONx3t0K4OID1tXG_dIPaejkZXgrJeVA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/16000000/15100000/15100000/15099921/a5a17208_z.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPGy3wIN9exiSAOiqNyLRybQ3Mw6v_2BFLW5MPg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPGy3wIN9exiSAOiqNyLRybQ3Mw6v_2BFLW5MPg=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipO-dx7oFWoFuS11GzA2DH_1975X7QShxV4tmiGf=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipO-dx7oFWoFuS11GzA2DH_1975X7QShxV4tmiGf=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipP573rTqrQ9f370CB0uzBe9y8K1IEvv7_bhtOn8=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipP573rTqrQ9f370CB0uzBe9y8K1IEvv7_bhtOn8=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMFAeFVIXAm49eEjin6NduOE7f9ppup7HYMEPwu=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMFAeFVIXAm49eEjin6NduOE7f9ppup7HYMEPwu=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMG8Ksjm5Im9akPutCuvwMmItiEwgOzFfGUKaDN=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMG8Ksjm5Im9akPutCuvwMmItiEwgOzFfGUKaDN=s10000"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/zHBk1aScCp0x3darvN3wZ5d8GRZqoOAyNizKI_Z3d4sck18-1wd-dvY_NVHXi2Kv3TD5VKWTQ8sCzzKvsdpI7z5SARU5yzCPiv2PdET202b_sTNHTOqRu8CG3rc31aYKmFtfh3nVBMWti5wspGVd-NMQVH5Cig=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/48/09/f3/ocean-riviera-paradise.jpg?w=2100&h=1400&s=1"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/gqzaLxGFnlUhQdH8gC10wFo10xTsNyAwsLnh6fIVY_eNMI2NGXSxvc5ejmUqEja5lvPxiw97Ldly52DMrhFgci_yPPqxWjTQZEmxpwxRqJpCMTIbnkN6F_o45Urv4T6RDjJEvSO1mioeqpr_3cLHYfWKIbSAy4c=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/48/0a/5e/ocean-riviera-paradise.jpg?w=2100&h=1400&s=1"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipN-OEl_CkNok10oEh-PBsfNVlZJRHPcfirkz4pd=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipN-OEl_CkNok10oEh-PBsfNVlZJRHPcfirkz4pd=s10000"
                }
            ],
            "overall_rating": 4.6,
            "reviews": 29343,
            "ratings": [
                {
                    "stars": 5,
                    "count": 23821
                },
                {
                    "stars": 4,
                    "count": 2890
                },
                {
                    "stars": 3,
                    "count": 968
                },
                {
                    "stars": 2,
                    "count": 567
                },
                {
                    "stars": 1,
                    "count": 1097
                }
            ],
            "location_rating": 3.7,
            "reviews_breakdown": [
                {
                    "name": "Dining",
                    "description": "Food and Beverage",
                    "total_mentioned": 6909,
                    "positive": 5959,
                    "negative": 649,
                    "neutral": 301
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 11762,
                    "positive": 10377,
                    "negative": 1060,
                    "neutral": 325
                },
                {
                    "name": "Bar",
                    "description": "Bar or lounge",
                    "total_mentioned": 2311,
                    "positive": 1757,
                    "negative": 392,
                    "neutral": 162
                },
                {
                    "name": "Family",
                    "description": "Family friendly",
                    "total_mentioned": 1786,
                    "positive": 1467,
                    "negative": 196,
                    "neutral": 123
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 2323,
                    "positive": 1776,
                    "negative": 351,
                    "neutral": 196
                },
                {
                    "name": "Nightlife",
                    "description": "Nightlife",
                    "total_mentioned": 1557,
                    "positive": 1325,
                    "negative": 138,
                    "neutral": 94
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Outdoor pool",
                "Hot tub",
                "Air conditioning",
                "Fitness centre",
                "All-inclusive available",
                "Spa",
                "Beach access",
                "Bar",
                "Restaurant",
                "Room service",
                "Full-service laundry",
                "Accessible",
                "Business centre",
                "Child-friendly"
            ],
            "eco_certified": True,
            "property_token": "ChoIk7DohaX4lteMARoNL2cvMTFjMXFrN2dqZhAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChoIk7DohaX4lteMARoNL2cvMTFjMXFrN2dqZhAB&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "The Palm at Playa",
            "description": "Modern hotel featuring free breakfast, parking & Wi-Fi, plus a restaurant, a spa & an outdoor pool.",
            "link": "https://www.thepalmatplaya.mx/?utm_medium=organic&utm_source=google-my-business&utm_campaign=google-local",
            "gps_coordinates": {
                "latitude": 20.626211599999998,
                "longitude": -87.0731799
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$78",
                "extracted_lowest": 78,
                "before_taxes_fees": "$71",
                "extracted_before_taxes_fees": 71
            },
            "total_rate": {
                "lowest": "$2,350",
                "extracted_lowest": 2350,
                "before_taxes_fees": "$2,142",
                "extracted_before_taxes_fees": 2142
            },
            "nearby_places": [
                {
                    "name": "Museo Frida Kahlo Playa Del Carmen",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "1 min"
                        }
                    ]
                },
                {
                    "name": "Playa Del Carmen",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "6 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "49 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 6 min"
                        }
                    ]
                },
                {
                    "name": "Don Mario",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "1 min"
                        }
                    ]
                }
            ],
            "hotel_class": "4-star hotel",
            "extracted_hotel_class": 4,
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMpldEChgeTVxAip27Njn4tPwnBAp8s5J2tvRLH=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMpldEChgeTVxAip27Njn4tPwnBAp8s5J2tvRLH=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipP_o9w1HO_GC0wLV4CmTr8E1HXZof74GBVMYutD=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipP_o9w1HO_GC0wLV4CmTr8E1HXZof74GBVMYutD=s10000"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/fwhdVboZBiOukNiO94uHzSz9W7y62_dYzGDEjm6HBp_ZWuAtznkWN-xuK3qc_JibmxvAb8vcgC5YS4rFU3w1HfBWB--ab_CJI5GGs0pFNslD1Sr5lK7oX7fagDA-PvBR9sEynNjTvrTVXprwtKVFVMEGNAyTSQ=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://cdn.worldota.net/t/1024x768/content/86/2e/862ebb5a0fa65f00865bb7aea63ce48ecb930992.jpeg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNvsM7lVuqKEC3qKuZWSsYgEnfqwYxRXXMSHMiC=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNvsM7lVuqKEC3qKuZWSsYgEnfqwYxRXXMSHMiC=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPf5vg7i9zc56B34VbhYd2em3-C2dAQxYTnR023=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPf5vg7i9zc56B34VbhYd2em3-C2dAQxYTnR023=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPearaKO8Jv9jjC9VjH21lNM76N_o5_7l_SoCSz=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPearaKO8Jv9jjC9VjH21lNM76N_o5_7l_SoCSz=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNhnng3ss84p_E5vOkfUoxxCZQTeYcBQwf3tjWg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNhnng3ss84p_E5vOkfUoxxCZQTeYcBQwf3tjWg=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPITJYSufoC-FcVRo7h0yZWefbiCIugiGeUzioB=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPITJYSufoC-FcVRo7h0yZWefbiCIugiGeUzioB=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMhzj_7Dq3vN_4etmJ79GYIoNcsd4jKf_iqWFOl=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMhzj_7Dq3vN_4etmJ79GYIoNcsd4jKf_iqWFOl=s10000"
                }
            ],
            "overall_rating": 4.3,
            "reviews": 1378,
            "ratings": [
                {
                    "stars": 5,
                    "count": 851
                },
                {
                    "stars": 4,
                    "count": 290
                },
                {
                    "stars": 3,
                    "count": 88
                },
                {
                    "stars": 2,
                    "count": 51
                },
                {
                    "stars": 1,
                    "count": 98
                }
            ],
            "location_rating": 4.8,
            "reviews_breakdown": [
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 268,
                    "positive": 212,
                    "negative": 47,
                    "neutral": 9
                },
                {
                    "name": "Bar",
                    "description": "Bar or lounge",
                    "total_mentioned": 104,
                    "positive": 79,
                    "negative": 13,
                    "neutral": 12
                },
                {
                    "name": "Nightlife",
                    "description": "Nightlife",
                    "total_mentioned": 78,
                    "positive": 36,
                    "negative": 27,
                    "neutral": 15
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 136,
                    "positive": 106,
                    "negative": 20,
                    "neutral": 10
                },
                {
                    "name": "Breakfast",
                    "description": "Breakfast",
                    "total_mentioned": 102,
                    "positive": 73,
                    "negative": 23,
                    "neutral": 6
                },
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 264,
                    "positive": 203,
                    "negative": 49,
                    "neutral": 12
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Outdoor pool",
                "Hot tub",
                "Air conditioning",
                "Fitness centre",
                "Spa",
                "Beach access",
                "Bar",
                "Restaurant",
                "Room service",
                "Kitchen in some rooms",
                "Airport shuttle",
                "Full-service laundry",
                "Accessible",
                "Business centre",
                "Smoke-free property"
            ],
            "property_token": "ChkIvdW38ajhmJSrARoML2cvMXBwMnZocjJqEAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkIvdW38ajhmJSrARoML2cvMXBwMnZocjJqEAE&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "La Pasión Hotel Boutique",
            "description": "Relaxed rooms in a casual pick with an outdoor pool, a hot tub & a tropical garden.",
            "link": "https://hotels.cloudbeds.com/reservation/zflEDk#promo=SUMMER23",
            "gps_coordinates": {
                "latitude": 20.6283264,
                "longitude": -87.07465540000001
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$50",
                "extracted_lowest": 50,
                "before_taxes_fees": "$48",
                "extracted_before_taxes_fees": 48
            },
            "total_rate": {
                "lowest": "$1,492",
                "extracted_lowest": 1492,
                "before_taxes_fees": "$1,433",
                "extracted_before_taxes_fees": 1433
            },
            "deal": "16% less than usual",
            "deal_description": "Deal",
            "nearby_places": [
                {
                    "name": "3D Museum of Wonders",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "3 min"
                        }
                    ]
                },
                {
                    "name": "Playa del Carmen Alterna",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "2 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "47 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 2 min"
                        }
                    ]
                }
            ],
            "hotel_class": "4-star hotel",
            "extracted_hotel_class": 4,
            "images": [
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/gKUtEcii4DnIFbXE47Qalt7YnFAJKnh2mvXqFdBxOOH-ll9rSorK5bkvGX19I5L-5_lbhBw5T2v4jrRo-B2kP3WZnsTg3m55CG736y2a8t2FbGeB5f7SN6wAMpPdXgKiQXqnegpf6JHDRB_V7__kdpL0g-Qyydg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://cdn.worldota.net/t/1024x768/content/53/7f/537f6e9d516a53e928de6142b0b947f3cfcde2a5.jpeg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/bZrYsGZlPyoq8WUNobnuG5cTuk_8rKKZrWZREqtptS2McmKZh74w6TjEfSinPxnHv3pUxmIgtQw7CRwZ13f7GRm20PX0pTXXfjiIRBwHTf2FbGw5JgUrHLVgutLW-rrXpa6PQIaV3QpkKN9SGm_Yp9IoZdz0cQ0=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/17/178342/178342a_hb_ro_003.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/O27dpF_BgxWOGmU0C9ozGqlXENzVXttrWQbBCi8_sDHCMvARvNKD0ARdQku4FWxTca3MA8QdSt1Dy6Wo6shBIqv4z_znyyysMA-OqMA5u_UCsod_mcCu53ydmddHkINCUSRZSz8Cl47xqfjLSA-4PCuPFJS7I1E=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/17/178342/178342a_hb_l_846.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPFjWxqSIc-wKHNvZU1lDNoAfC41jxCK4m0FPHO=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPFjWxqSIc-wKHNvZU1lDNoAfC41jxCK4m0FPHO=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/XFjqf948rwYlJzRaEOmcKmQlNZ6oIQELwBt1DkjP2GdNq4le5TVZPmb3gt8O660ZFZHXkgh_MU-s3BCBZ8QEYLwuDEDtngJnGFQXLacAZ0Bi_4JO3ncZJyLeeKzb_tlxhCcv4MDUwEIYVeI6rf40KbwVaw6vHg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/17/178342/178342a_hb_l_845.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMcwzJaT4uaFoCU1R3cawg3-fIyjyrZaoIVMnnB=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMcwzJaT4uaFoCU1R3cawg3-fIyjyrZaoIVMnnB=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipN6xBxieJicuT7nUoMxazNIh6sflermmhIXhlpH=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipN6xBxieJicuT7nUoMxazNIh6sflermmhIXhlpH=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOoiYEaBGd7UHi4KSAdHaSgOy6nH0WhBIW8FV6h=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOoiYEaBGd7UHi4KSAdHaSgOy6nH0WhBIW8FV6h=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPGw5gCjc63W-NkLxa6ry4W73QDMOW8_fibvJy1=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPGw5gCjc63W-NkLxa6ry4W73QDMOW8_fibvJy1=s10000"
                }
            ],
            "overall_rating": 4.6,
            "reviews": 1183,
            "ratings": [
                {
                    "stars": 5,
                    "count": 890
                },
                {
                    "stars": 4,
                    "count": 192
                },
                {
                    "stars": 3,
                    "count": 46
                },
                {
                    "stars": 2,
                    "count": 17
                },
                {
                    "stars": 1,
                    "count": 38
                }
            ],
            "location_rating": 4.7,
            "reviews_breakdown": [
                {
                    "name": "Breakfast",
                    "description": "Breakfast",
                    "total_mentioned": 201,
                    "positive": 165,
                    "negative": 18,
                    "neutral": 18
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 347,
                    "positive": 313,
                    "negative": 25,
                    "neutral": 9
                },
                {
                    "name": "Location",
                    "description": "Location",
                    "total_mentioned": 296,
                    "positive": 272,
                    "negative": 7,
                    "neutral": 17
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 157,
                    "positive": 136,
                    "negative": 11,
                    "neutral": 10
                },
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 323,
                    "positive": 279,
                    "negative": 36,
                    "neutral": 8
                },
                {
                    "name": "Restaurant",
                    "description": "Restaurant",
                    "total_mentioned": 94,
                    "positive": 79,
                    "negative": 7,
                    "neutral": 8
                }
            ],
            "amenities": [
                "Breakfast",
                "Free Wi-Fi",
                "Parking",
                "Outdoor pool",
                "Hot tub",
                "Air conditioning",
                "Restaurant",
                "Airport shuttle",
                "Full-service laundry"
            ],
            "property_token": "ChkInL-omZq8mvnWARoML2cvMTEzanowOXl6EAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkInL-omZq8mvnWARoML2cvMTEzanowOXl6EAE&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "La Quinta Caribeña",
            "link": "https://www.laquintacaribena.com/",
            "gps_coordinates": {
                "latitude": 20.648938899999997,
                "longitude": -87.05581120000001
            },
            "check_in_time": "2:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$37",
                "extracted_lowest": 37,
                "before_taxes_fees": "$37",
                "extracted_before_taxes_fees": 37
            },
            "total_rate": {
                "lowest": "$1,122",
                "extracted_lowest": 1122,
                "before_taxes_fees": "$1,122",
                "extracted_before_taxes_fees": 1122
            },
            "deal": "50% less than usual",
            "deal_description": "Great Deal",
            "nearby_places": [
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "43 min"
                        }
                    ]
                },
                {
                    "name": "Fuego",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "1 min"
                        }
                    ]
                }
            ],
            "hotel_class": "5-star hotel",
            "extracted_hotel_class": 5,
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPwKnoHfUm-t9cE27oK8OlbYNa8wqnEmn7bcYZP=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPwKnoHfUm-t9cE27oK8OlbYNa8wqnEmn7bcYZP=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMexhSYM574PeLHuwJcmVIy7Xxvo9NkxfwSwF7r=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMexhSYM574PeLHuwJcmVIy7Xxvo9NkxfwSwF7r=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPzrueOsv2uJeAEA043CO1Av10NRYkK4Qzb3kQ9=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPzrueOsv2uJeAEA043CO1Av10NRYkK4Qzb3kQ9=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOb6NcNdc-e9ly3jGDNnniQ8Eu2nxjLmmaRpNcS=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOb6NcNdc-e9ly3jGDNnniQ8Eu2nxjLmmaRpNcS=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipP4cYBR4U6C5jJ-TD-pZliuGwWfr2l8iFX7HyNK=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipP4cYBR4U6C5jJ-TD-pZliuGwWfr2l8iFX7HyNK=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPF-E0V6UudmW0L62mdKagce6wvY9v457Zd92YK=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPF-E0V6UudmW0L62mdKagce6wvY9v457Zd92YK=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMWTWBeMZLFdFBXLb9HnYbsTil7CWC61SQE7Y2z=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMWTWBeMZLFdFBXLb9HnYbsTil7CWC61SQE7Y2z=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNgifNzbs-nWyDZYExRWR6XOn0aepPQLXH8BkpM=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNgifNzbs-nWyDZYExRWR6XOn0aepPQLXH8BkpM=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipM9EHhNPRxd9J2iF9CzxKEI7i906fH1GC1cWljO=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipM9EHhNPRxd9J2iF9CzxKEI7i906fH1GC1cWljO=s10000"
                }
            ],
            "overall_rating": 4.9,
            "reviews": 258,
            "ratings": [
                {
                    "stars": 5,
                    "count": 247
                },
                {
                    "stars": 4,
                    "count": 8
                },
                {
                    "stars": 3,
                    "count": 0
                },
                {
                    "stars": 2,
                    "count": 1
                },
                {
                    "stars": 1,
                    "count": 2
                }
            ],
            "location_rating": 3.0,
            "reviews_breakdown": [
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 91,
                    "positive": 91,
                    "negative": 0,
                    "neutral": 0
                },
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 94,
                    "positive": 93,
                    "negative": 0,
                    "neutral": 1
                },
                {
                    "name": "Atmosphere",
                    "description": "Atmosphere",
                    "total_mentioned": 66,
                    "positive": 66,
                    "negative": 0,
                    "neutral": 0
                },
                {
                    "name": "Cleanliness",
                    "description": "Cleanliness",
                    "total_mentioned": 54,
                    "positive": 53,
                    "negative": 0,
                    "neutral": 1
                },
                {
                    "name": "Nature",
                    "description": "Nature and outdoor activities",
                    "total_mentioned": 40,
                    "positive": 37,
                    "negative": 1,
                    "neutral": 2
                },
                {
                    "name": "Location",
                    "description": "Location",
                    "total_mentioned": 59,
                    "positive": 53,
                    "negative": 2,
                    "neutral": 4
                }
            ],
            "amenities": [
                "Free Wi-Fi",
                "Free parking",
                "Outdoor pool",
                "Air conditioning",
                "Beach access",
                "Kitchen in some rooms",
                "Airport shuttle",
                "Child-friendly",
                "Smoke-free property"
            ],
            "property_token": "ChkIkcC36O-v1_0JGg0vZy8xMXM1djE3ZHdfEAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkIkcC36O-v1_0JGg0vZy8xMXM1djE3ZHdfEAE&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "The Reef Coco Beach Resort & Spa",
            "description": "Luxe all-inclusive retreat with 4 restaurants & 3 bars, plus a tennis court & a sophisticated spa.",
            "link": "https://www.thereefresorts.com/reefcocobeach?utm_source=google&utm_medium=organic&utm_campaign=gbp_listing",
            "gps_coordinates": {
                "latitude": 20.6366865,
                "longitude": -87.06118889999999
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$209",
                "extracted_lowest": 209,
                "before_taxes_fees": "$170",
                "extracted_before_taxes_fees": 170
            },
            "total_rate": {
                "lowest": "$6,276",
                "extracted_lowest": 6276,
                "before_taxes_fees": "$5,088",
                "extracted_before_taxes_fees": 5088
            },
            "nearby_places": [
                {
                    "name": "3D Museum of Wonders",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "9 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "48 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 26 min"
                        }
                    ]
                }
            ],
            "hotel_class": "4-star hotel",
            "extracted_hotel_class": 4,
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/OUMC2aQf1tbv3bb8G-2swndx7wdd8CPGhw-Wiso-gD9mjD_Wk6ffJdRIojfTzLAwgbJ2fyIsGBq_XSiS7b7WAxfqBg7uiOVhwJdzlxMituhvBK__fsse69BPAE3GaRbfl8vxPi3Q6RB_rzy2m90WziaVHNjbpw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KABRGJAUFAN7YrBWQrbq4ZbEUVTOs1xA"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/exsCw3W9sy8ok65eg3qK6e5AD0YNdazhdLLWdSA6vvh7SQ3qQx8M1B3rsgV259q-eXd9UVkGmWnVLK6nlSykEUlT_qI0cOJWTbGjGfhyrjinXgVnbjde6dXGflpaGqQJSy4L0fDsMaUz3mrt6ex5OP5kDEghXg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/00/008168/008168a_hb_p_021.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPW3x2-bl3Tg8FLIx5jt3mTxZrBGDEGeFbXlz-o=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPW3x2-bl3Tg8FLIx5jt3mTxZrBGDEGeFbXlz-o=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/wchNWSDc5Y8PfMuBJDzEThM94kDBni_kVuaHRPMqRQJ46DaLnczjgMh1DWVf8qSvIRy3EcfHM0zn1ShY266bnHdp05xBT1p2BY3nbH9QwbH-utjqkl5R33NRJ6qkjyqWCVCmJFHRlGQK-cXf1HBfvS9YdgEEMg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/00/008168/008168a_hb_l_008.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOZEibig-HkNTqjYyVA76pirXf0AZe6SVEBuEUI=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOZEibig-HkNTqjYyVA76pirXf0AZe6SVEBuEUI=s10000"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/xH8kbxvTQlSSBiY4UczIy-5xubIWHykYtRncg949FyZT9-IEDh6zIPyRWs4DEiAzPz0wN3-XHkD-1yEc4kcvDNHhABsnqxcNrU-F5Crs6czM1yjXIxouBUibWjk0i7D7_4ieoCvkgt2kdigU7eau2nw0R7CGdWU=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/00/008168/008168a_hb_s_022.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOAhvWLgDs9-KUWehjOqW7izVgN8pmhB9b3e-97=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOAhvWLgDs9-KUWehjOqW7izVgN8pmhB9b3e-97=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipN2v9C99cuBShnIJfrY-XNtdH2abjzWpyAwdjm0=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipN2v9C99cuBShnIJfrY-XNtdH2abjzWpyAwdjm0=s10000"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/blBpgOyxrhCi-TEKfiyQksFZ9M36qVdWKoaVbdU3Qqac6CR0GNvGHC9nS_kdCOwl7agldBgLbZ00AIy42vu9lzT14lX0vt58gpjbHODFgTZ4mqDwdXvFqA3qdhWvzvm48BpZg9BU5cQKDR5iIJMFWLtRhqTbuFI=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/00/008168/008168a_hb_r_018.jpg"
                }
            ],
            "overall_rating": 4.2,
            "reviews": 5131,
            "ratings": [
                {
                    "stars": 5,
                    "count": 2822
                },
                {
                    "stars": 4,
                    "count": 1227
                },
                {
                    "stars": 3,
                    "count": 530
                },
                {
                    "stars": 2,
                    "count": 201
                },
                {
                    "stars": 1,
                    "count": 351
                }
            ],
            "location_rating": 3.7,
            "reviews_breakdown": [
                {
                    "name": "Dining",
                    "description": "Food and Beverage",
                    "total_mentioned": 539,
                    "positive": 306,
                    "negative": 174,
                    "neutral": 59
                },
                {
                    "name": "Nature",
                    "description": "Nature and outdoor activities",
                    "total_mentioned": 623,
                    "positive": 362,
                    "negative": 163,
                    "neutral": 98
                },
                {
                    "name": "Bar",
                    "description": "Bar or lounge",
                    "total_mentioned": 333,
                    "positive": 172,
                    "negative": 128,
                    "neutral": 33
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 919,
                    "positive": 613,
                    "negative": 234,
                    "neutral": 72
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 340,
                    "positive": 206,
                    "negative": 90,
                    "neutral": 44
                },
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 683,
                    "positive": 479,
                    "negative": 150,
                    "neutral": 54
                }
            ],
            "amenities": [
                "Free Wi-Fi",
                "Free parking",
                "Outdoor pool",
                "Hot tub",
                "Air conditioning",
                "Fitness centre",
                "All-inclusive available",
                "Spa",
                "Beach access",
                "Child-friendly"
            ],
            "property_token": "ChgIt4uojYn-08gGGgwvZy8xeWZqbXk2MjkQAQ",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChgIt4uojYn-08gGGgwvZy8xeWZqbXk2MjkQAQ&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "The Fives Beach Hotel & Residences",
            "description": "Upscale resort featuring 9 restaurants, 6 bars & a spa, plus 5 pools connected by lazy rivers.",
            "link": "https://www.thefiveshotels.com/resorts/the-fives-beach?partner=7228&utm_source=google&utm_medium=gmb&utm_campaign=web_link",
            "gps_coordinates": {
                "latitude": 20.663562799999998,
                "longitude": -87.03426789999999
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$279",
                "extracted_lowest": 279,
                "before_taxes_fees": "$230",
                "extracted_before_taxes_fees": 230
            },
            "total_rate": {
                "lowest": "$8,363",
                "extracted_lowest": 8363,
                "before_taxes_fees": "$6,912",
                "extracted_before_taxes_fees": 6912
            },
            "deal": "45% less than usual",
            "deal_description": "Great Deal",
            "nearby_places": [
                {
                    "name": "Playa Xcalacoco",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "1 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "42 min"
                        }
                    ]
                }
            ],
            "hotel_class": "5-star hotel",
            "extracted_hotel_class": 5,
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMaCi3pwpZp-yYT0GFrcnOhQTCdmyb5121_1B1L=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMaCi3pwpZp-yYT0GFrcnOhQTCdmyb5121_1B1L=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMG--MEZSzfeG96i2ZvwuWPX7Kmrp53kY5BUnrw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMG--MEZSzfeG96i2ZvwuWPX7Kmrp53kY5BUnrw=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOG189zTAjvgXTyO1kQ-0yO8L_uqATj-BIMMNGv=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOG189zTAjvgXTyO1kQ-0yO8L_uqATj-BIMMNGv=s10000"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/a3WCgeHB0UEsZ9x9_w0xZFQhoDO0EqOagshbLgfK3bOn-ZSV3MN0gmibzbIS7MI9MPHmThpl6eEo5OfW7E4bhU0AcJ6ZO-riRSJeTqPe0LFCubiaoTu-UznN2Xg-VSVYn8mBL_agS-Gaz9wnEuvh_cvdjE9_mg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/http://media.staticontent.com/media/pictures/3291eb36-2560-41cd-a100-c4499cdea900=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMhPi9RD9ptjvoQLhzg2kqWRa1p4QcgXejm6EWy=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMhPi9RD9ptjvoQLhzg2kqWRa1p4QcgXejm6EWy=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPMBeywfJAheNeNrKJFhS_x8J-3FPVoWBFCLxvO=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPMBeywfJAheNeNrKJFhS_x8J-3FPVoWBFCLxvO=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOjzty4otBN_bJdgoLugKTfe_WDPorC8_8QBMco=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOjzty4otBN_bJdgoLugKTfe_WDPorC8_8QBMco=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/q7-BB7fbdFjdiiRpI26H0j9PRMHv7UAYYqkmgYkuoimBV4O3GuSKEBgYwNq7AwI0qLP34MbQO29CqLmkaaD_Y-S82XLD0iBd5cquxmTkqzouLv_ChBjIj4V4pUnmz5eew19WFVxGjY88Z1ELn4MelRf69DhSwpo=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/48/483101/483101a_hb_r_004.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipO29Bz3PSn4PGtr9f98s78VBa5XmuIWeOncCFNt=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipO29Bz3PSn4PGtr9f98s78VBa5XmuIWeOncCFNt=s10000"
                }
            ],
            "overall_rating": 4.5,
            "reviews": 8151,
            "ratings": [
                {
                    "stars": 5,
                    "count": 5974
                },
                {
                    "stars": 4,
                    "count": 1157
                },
                {
                    "stars": 3,
                    "count": 402
                },
                {
                    "stars": 2,
                    "count": 190
                },
                {
                    "stars": 1,
                    "count": 428
                }
            ],
            "location_rating": 3.7,
            "reviews_breakdown": [
                {
                    "name": "Dining",
                    "description": "Food and Beverage",
                    "total_mentioned": 1490,
                    "positive": 1168,
                    "negative": 222,
                    "neutral": 100
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 2312,
                    "positive": 1851,
                    "negative": 336,
                    "neutral": 125
                },
                {
                    "name": "Family",
                    "description": "Family friendly",
                    "total_mentioned": 689,
                    "positive": 552,
                    "negative": 84,
                    "neutral": 53
                },
                {
                    "name": "Bar",
                    "description": "Bar or lounge",
                    "total_mentioned": 789,
                    "positive": 575,
                    "negative": 144,
                    "neutral": 70
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 1095,
                    "positive": 891,
                    "negative": 115,
                    "neutral": 89
                },
                {
                    "name": "Nature",
                    "description": "Nature and outdoor activities",
                    "total_mentioned": 1006,
                    "positive": 742,
                    "negative": 147,
                    "neutral": 117
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Outdoor pool",
                "Hot tub",
                "Air conditioning",
                "Fitness centre",
                "All-inclusive available",
                "Spa",
                "Beach access",
                "Bar",
                "Restaurant",
                "Room service",
                "Kitchen in rooms",
                "Airport shuttle",
                "Full-service laundry",
                "Accessible",
                "Business centre",
                "Child-friendly",
                "Smoke-free property"
            ],
            "eco_certified": True,
            "property_token": "ChcIpd7Z7qDvkcgBGgsvZy8xdzk3dnR2chAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChcIpd7Z7qDvkcgBGgsvZy8xdzk3dnR2chAB&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "Thompson Playa Del Carmen Main House, by Hyatt",
            "description": "Luxe lodging featuring mid-century modern rooms & suites, plus sea views & a rooftop infinity pool.",
            "link": "https://www.hyatt.com/thompson-hotels/en-US/canth-thompson-playa-del-carmen-main-house/?src=corp_lclb_gmb_seo_canth",
            "gps_coordinates": {
                "latitude": 20.6278975,
                "longitude": -87.0720509
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$158",
                "extracted_lowest": 158,
                "before_taxes_fees": "$93",
                "extracted_before_taxes_fees": 93
            },
            "total_rate": {
                "lowest": "$4,734",
                "extracted_lowest": 4734,
                "before_taxes_fees": "$2,782",
                "extracted_before_taxes_fees": 2782
            },
            "nearby_places": [
                {
                    "name": "3D Museum of Wonders",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "3 min"
                        }
                    ]
                },
                {
                    "name": "Playa del Carmen Alterna",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "5 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "48 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 5 min"
                        }
                    ]
                },
                {
                    "name": "Catch",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "1 min"
                        }
                    ]
                }
            ],
            "hotel_class": "5-star hotel",
            "extracted_hotel_class": 5,
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOiR2pFt9LkDSwlvKLiMMEeyXfhqHBggPCh_QCm=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOiR2pFt9LkDSwlvKLiMMEeyXfhqHBggPCh_QCm=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPiQ6KTUCb0-K-D82g9Ah1q5VWGW7rL3mIgWFls=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPiQ6KTUCb0-K-D82g9Ah1q5VWGW7rL3mIgWFls=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOM-d6GYgUuxK5cQvzotYPkQxPqSFNfdEEgpbXI=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOM-d6GYgUuxK5cQvzotYPkQxPqSFNfdEEgpbXI=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMKdS_-PpXFcLsZH5AjmVNTr2VwvTZS0bMMMGGC=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMKdS_-PpXFcLsZH5AjmVNTr2VwvTZS0bMMMGGC=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOrELUHFo9R6c7HdU-fbfODtdVMg95lAyUDZM__=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOrELUHFo9R6c7HdU-fbfODtdVMg95lAyUDZM__=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNfe6Tn9cZl5fhMwBcSd2yrYYNnToX7QrTmqJEI=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNfe6Tn9cZl5fhMwBcSd2yrYYNnToX7QrTmqJEI=s10000"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/77dkJROcxqH5WJNpMhn10lLlKQhA4Y2R06qnhWr-e72EYj5JvGREXOL4bm4KPQbFfWBz0Rw4XpKJJOkdhtZf77pmI4D3AWRpOC3bKnHvF4ax6GvhwNGNIl0PBeLEKSkZtwZEXsXjjIBWBiyIAjKw1SiF6FoKdA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/42/425260/425260a_hb_w_008.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/ta3fzm1WFdzycFuYHQ1Cnsk0cNsD8kVwx72hvytzndcBmMLUtuKXB78Q7oZt1l9CzJcyOjqu90WKrSMqag5qMSU1JGmLYLo9BQamyvdpW136mtUpO2GlvX0adBDgFXk39ttOFb1tqWgZogyXVDQtaVulFz13Zw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/12000000/11630000/11620500/11620473/a39fa50a_z.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/cAd0wLt9zfeZrShxtTHXqN1SjMc_hXNYyOvvLymcr7I2QpqhvlwA5nv5Ll3KAyJB5Uh_EKLTopeZ-v472MYMCvJsAoG6KVUbsEKhhns2Hj3ueR7SwSTHllNeN9m5EbxmEgwE1PloJzOFEF5UwxgbgCYL_f74-Z4=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KADwcGQQFAIynTvjuaa4SYiYGeJAIoaU"
                }
            ],
            "overall_rating": 4.4,
            "reviews": 1278,
            "ratings": [
                {
                    "stars": 5,
                    "count": 857
                },
                {
                    "stars": 4,
                    "count": 236
                },
                {
                    "stars": 3,
                    "count": 68
                },
                {
                    "stars": 2,
                    "count": 34
                },
                {
                    "stars": 1,
                    "count": 83
                }
            ],
            "location_rating": 4.8,
            "reviews_breakdown": [
                {
                    "name": "Nightlife",
                    "description": "Nightlife",
                    "total_mentioned": 92,
                    "positive": 43,
                    "negative": 38,
                    "neutral": 11
                },
                {
                    "name": "Bar",
                    "description": "Bar or lounge",
                    "total_mentioned": 109,
                    "positive": 76,
                    "negative": 22,
                    "neutral": 11
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 227,
                    "positive": 155,
                    "negative": 61,
                    "neutral": 11
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 127,
                    "positive": 93,
                    "negative": 17,
                    "neutral": 17
                },
                {
                    "name": "Dining",
                    "description": "Food and Beverage",
                    "total_mentioned": 119,
                    "positive": 76,
                    "negative": 27,
                    "neutral": 16
                },
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 224,
                    "positive": 173,
                    "negative": 32,
                    "neutral": 19
                }
            ],
            "amenities": [
                "Breakfast ($)",
                "Wi-Fi ($)",
                "Parking ($)",
                "Pool",
                "Air conditioning",
                "Pet-friendly",
                "Fitness centre",
                "Beach access",
                "Bar",
                "Restaurant",
                "Room service",
                "Full-service laundry",
                "Accessible",
                "Smoke-free property"
            ],
            "property_token": "ChkIpKb6qfXn7JpBGg0vZy8xMWNqeTE2a3prEAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkIpKb6qfXn7JpBGg0vZy8xMWNqeTE2a3prEAE&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "Aspira Hotel Playa del Carmen by Tukan",
            "description": "Relaxed rooms in a laid-back hotel offering a free beach club shuttle & an outdoor pool.",
            "link": "https://tukanhotels.com/hoteles/hotel-aspira/?utm_source=google&utm_medium=gmb&utm_campaign=web_link",
            "gps_coordinates": {
                "latitude": 20.6302449,
                "longitude": -87.07155750000001
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$61",
                "extracted_lowest": 61,
                "before_taxes_fees": "$48",
                "extracted_before_taxes_fees": 48
            },
            "total_rate": {
                "lowest": "$1,832",
                "extracted_lowest": 1832,
                "before_taxes_fees": "$1,439",
                "extracted_before_taxes_fees": 1439
            },
            "nearby_places": [
                {
                    "name": "La Quinta Avenida",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "3 min"
                        }
                    ]
                },
                {
                    "name": "Playa del Carmen Alterna",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "6 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "47 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 5 min"
                        }
                    ]
                }
            ],
            "hotel_class": "4-star hotel",
            "extracted_hotel_class": 4,
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOWolFLwotnV01BLHNg1YSUpTVCNz----Z_0Fgf=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOWolFLwotnV01BLHNg1YSUpTVCNz----Z_0Fgf=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipP8oLqrcJDFNYvCYJS9xysSCbsi7lyTe64y0Z0H=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipP8oLqrcJDFNYvCYJS9xysSCbsi7lyTe64y0Z0H=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPQeWdpyx9iXqXRQ_mjjEIRor1bv2sbTvreV729=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPQeWdpyx9iXqXRQ_mjjEIRor1bv2sbTvreV729=s10000"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/N_6pNeC2c-zgEjevefKG0UNtRoau8FCjiXyXGLSqb0Ddd6oLCP7-7DcBgkCb8WZ2AbB55tkxfpIFhsEOWbL_tlJdsMHlVVIb25bttmt9CtD7TMNBcIBKNOTwgil6drx3gnWU8u2K0gDRhsbdyckv9v4HYICOhPA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/http://media.staticontent.com/media/pictures/f4bfa639-c992-4496-8139-f6f7ab3cb082=s10000"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/EpTwf3FaXp7R26ehTnjVDEXm2WxB-jWq7iwYMBmvF4rx9g1-9-HMCED3nu3j9-x0dToN5uMPgvVJ1ymA_HqYfffhY8N9iVRzCjRpf2TDbyy3lMkRjaFNKXbTzNGKOOiTZMp4sZJhR6k2D-K8ZzhkoRVA615Lag=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KAMSyJAQFAIVIGsdLpOM4KGQCvs9UnCY"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPFjwRmnZqYyK8CisOHpFSo1REf-2PvruVkkzhQ=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPFjwRmnZqYyK8CisOHpFSo1REf-2PvruVkkzhQ=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNJEt_Uxdywe3hvw-No0VKiKpNa4Mh75MIXCpyZ=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNJEt_Uxdywe3hvw-No0VKiKpNa4Mh75MIXCpyZ=s10000"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/ka-oWYwX8s7xgxTAHF1Tr0EI5ziuEeUhZsYW0IOYXwG642bSkanE7jFPxQCal1KqXdP6JhX9ckQN3lhladtomaU2PgG-El2mAQXKif0YXXxEvBnQ_KkeMRd2tMmf6hR21RBdsBYs03_Yx_Wn6p9eO2-85xYbpow=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/16000000/15370000/15360900/15360848/4d86601f_z.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOuTOXKW2hu6m00tVF1UOObdx0SP0sJb_RdWkRl=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOuTOXKW2hu6m00tVF1UOObdx0SP0sJb_RdWkRl=s10000"
                }
            ],
            "overall_rating": 4.2,
            "reviews": 431,
            "ratings": [
                {
                    "stars": 5,
                    "count": 230
                },
                {
                    "stars": 4,
                    "count": 111
                },
                {
                    "stars": 3,
                    "count": 45
                },
                {
                    "stars": 2,
                    "count": 21
                },
                {
                    "stars": 1,
                    "count": 24
                }
            ],
            "location_rating": 4.7,
            "reviews_breakdown": [
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 99,
                    "positive": 86,
                    "negative": 7,
                    "neutral": 6
                },
                {
                    "name": "Location",
                    "description": "Location",
                    "total_mentioned": 76,
                    "positive": 67,
                    "negative": 2,
                    "neutral": 7
                },
                {
                    "name": "Bathroom",
                    "description": "Bathroom and toiletries",
                    "total_mentioned": 34,
                    "positive": 4,
                    "negative": 28,
                    "neutral": 2
                },
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 93,
                    "positive": 82,
                    "negative": 8,
                    "neutral": 3
                },
                {
                    "name": "Accessibility",
                    "description": "Accessibility",
                    "total_mentioned": 21,
                    "positive": 4,
                    "negative": 14,
                    "neutral": 3
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 33,
                    "positive": 18,
                    "negative": 12,
                    "neutral": 3
                }
            ],
            "amenities": [
                "Breakfast ($)",
                "Free Wi-Fi",
                "Parking",
                "Pool",
                "Air conditioning",
                "Pet-friendly",
                "Bar",
                "Restaurant",
                "Full-service laundry",
                "Child-friendly"
            ],
            "property_token": "ChkItcODi7LUy9ppGg0vZy8xMWNucmRtdGIwEAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChkItcODi7LUy9ppGg0vZy8xMWNucmRtdGIwEAE&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "Hacienda Paradise by BFH",
            "description": "Informal property offering a spa, an outdoor pool & complimentary breakfast, plus a restaurant.",
            "link": "https://haciendaparadise.com/",
            "gps_coordinates": {
                "latitude": 20.6314535,
                "longitude": -87.0700257
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$38",
                "extracted_lowest": 38,
                "before_taxes_fees": "$36",
                "extracted_before_taxes_fees": 36
            },
            "total_rate": {
                "lowest": "$1,131",
                "extracted_lowest": 1131,
                "before_taxes_fees": "$1,072",
                "extracted_before_taxes_fees": 1072
            },
            "deal": "40% less than usual",
            "deal_description": "Great Deal",
            "nearby_places": [
                {
                    "name": "La Quinta Avenida",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "3 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "50 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 8 min"
                        }
                    ]
                },
                {
                    "name": "Mu. Burgerhouse",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "1 min"
                        }
                    ]
                }
            ],
            "hotel_class": "4-star hotel",
            "extracted_hotel_class": 4,
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/XsSAdTzqT6JrfLop31_bVIT6OXjtO92O-taetrAO91hFeqMCvMfupPPtOdZZsYdq1MW4-dRzSqLxg26kieJBPOdJCxmVWEadT58MCM_JLvxpfnstgAfgqNs5TgR1e8x-g8Uc1-p3i93GD0ltEJ1L7GlTPC61FA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/1000000/870000/862700/862618/307548cb_z.jpg"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/PdxIrB2rGwCjQkX9yrTS35Hy7gFEGLx0L5kgQV4cDAQQWNrsd1zC5ktp1f8FVX8hIHXv_QcKpA5e_GgS1pJNzjFqcOhvNH8Ny7PFjOPdVWGPh6EgmFIdqBjb1Y9XZedRY1V_l-wMmJPaeey-ieil97sJfDJ_mg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/1/0/29/652/271/Piscina_y_habitaciones_con_terrazas_2_O.jpg"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/bX7ESjMtjAVuAM1caHqHIgdTedOd1jy29R8oU7ZYhLMkGU7bmsIre5TS56J-Mib95baE_LvUtjvCHrkbuNEqQBkvI6k61k6f7c6LR2udqe4i0GK1Dwae9puLHutB4qKA6bl-U61UUhhhY72GfkC-Q9ZXgWDceD0=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/00/007921/007921a_hb_t_001.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMwZBwDANmx-KnDyxcq6fwqkJIIAOMOhUZNlc83=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMwZBwDANmx-KnDyxcq6fwqkJIIAOMOhUZNlc83=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/N8pXqD1hD7g_8kd61QRkJZjZb_eGcvAV8DPGvNegajI-mwMErnetum1NgY80Sb6zyV_a0pWA25HrlfPiRXngFpMR_VdKyjFfT2QQmDwaKQ42XrSGAj4IwxcdTSbQXclYcTZaVnS75TwVRpxA14GcK8f5YbYobg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/1/0/29/652/211/DSC_8590_O.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPjx31GxcqmxcglwRvqf9B3dJdzAbjp0VizUP1m=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPjx31GxcqmxcglwRvqf9B3dJdzAbjp0VizUP1m=s10000"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/zOxFwSVi3qjlknvjyp1NUj4sQEldp_Y61zM_koHQTTL2Tiih-zrhqETTvelZrFC2cL8MVcrAfLSp3Rw7BgtS95ntdTWlTI65_tL9A2hVVcfaDtIQ6JvmXpJ1vKS811_bv3QcC3VkL5rC-KzL7KA1x4IU_PZoQA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/1000000/870000/862700/862618/232a343a_z.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/IRoZBXlHQ-5sLl9EJdXH4kKaS2Y4Y8yS1cAY9rfbylVob2joOX1u0V5_-syHjXqwLJg9U9yt74GJmKKvY2uL2E0mFi-kLSqTEHe7Fd5BYeNJd6J2fncE8ymOUtu-1O9XXw5gAV6a1LNTKyx7dAiePK8FwgH8xg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/1000000/870000/862700/862618/9c2389f6_z.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipN9fIyBLJLIOPFlgJW9Nwr3FmjAztYzLEswTyoD=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipN9fIyBLJLIOPFlgJW9Nwr3FmjAztYzLEswTyoD=s10000"
                }
            ],
            "overall_rating": 4,
            "reviews": 493,
            "ratings": [
                {
                    "stars": 5,
                    "count": 249
                },
                {
                    "stars": 4,
                    "count": 109
                },
                {
                    "stars": 3,
                    "count": 65
                },
                {
                    "stars": 2,
                    "count": 24
                },
                {
                    "stars": 1,
                    "count": 46
                }
            ],
            "location_rating": 4.4,
            "reviews_breakdown": [
                {
                    "name": "Breakfast",
                    "description": "Breakfast",
                    "total_mentioned": 68,
                    "positive": 31,
                    "negative": 29,
                    "neutral": 8
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 142,
                    "positive": 117,
                    "negative": 17,
                    "neutral": 8
                },
                {
                    "name": "Location",
                    "description": "Location",
                    "total_mentioned": 93,
                    "positive": 83,
                    "negative": 2,
                    "neutral": 8
                },
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 122,
                    "positive": 87,
                    "negative": 21,
                    "neutral": 14
                },
                {
                    "name": "Restaurant",
                    "description": "Restaurant",
                    "total_mentioned": 31,
                    "positive": 14,
                    "negative": 12,
                    "neutral": 5
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 49,
                    "positive": 36,
                    "negative": 9,
                    "neutral": 4
                }
            ],
            "amenities": [
                "Breakfast ($)",
                "Free Wi-Fi",
                "Outdoor pool",
                "Hot tub",
                "Air conditioning",
                "Restaurant",
                "Airport shuttle",
                "Full-service laundry",
                "Accessible",
                "Child-friendly"
            ],
            "property_token": "ChcI8-Dt-uTfgOwYGgsvZy8xdmdfN24xMBAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChcI8-Dt-uTfgOwYGgsvZy8xdmdfN24xMBAB&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "Casa del Árbol | Casas In Playa",
            "description": "Laid-back hotel offering bright rooms with kitchenettes & free Wi-Fi, plus an outdoor pool.",
            "link": "https://www.casasinplaya.com/arbol",
            "gps_coordinates": {
                "latitude": 20.6260387,
                "longitude": -87.0950407
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$41",
                "extracted_lowest": 41,
                "before_taxes_fees": "$34",
                "extracted_before_taxes_fees": 34
            },
            "total_rate": {
                "lowest": "$1,230",
                "extracted_lowest": 1230,
                "before_taxes_fees": "$1,008",
                "extracted_before_taxes_fees": 1008
            },
            "nearby_places": [
                {
                    "name": "Xplor Park",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "8 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "49 min"
                        }
                    ]
                },
                {
                    "name": "Anafre cocina a la leña y vino",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "2 min"
                        }
                    ]
                }
            ],
            "hotel_class": "3-star hotel",
            "extracted_hotel_class": 3,
            "images": [
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/PX6-aqLYUWXAmkuSvKjAQt-fbeBI5e3pRklfIONo496HVE2Z3416AOQx9UYVz5L25vu9j4gTivujSA-G_aFHb-3ydDe6Fd9nUMEYtxK3IpNZMTUJaRcszFFzCMHh86kQrum6jNMUZ-wdY9P_wV1dIv_CSPyglg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/89/899061/899061a_hb_w_006.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/XWENlm1A9H9Q0Bq9K3nCrVzD6I-RA4su0mT058C8Pt3gS6NGgopl6emB89ahPUjD5hdx33mYq4Eck3cTIGOdJjPku4HzMxnTi4l10fE1bsfeWm65PT2MVPQOwyeD4dI841NpWJE0SCtMZrGeEAPZsvj5aCadXA=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/89/899061/899061a_hb_w_020.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/cbHRu_LITVb5G0bAJl486yLYRofFAh_t-9Y78lnHKZPozdsdPsrl9MEBQTsCvg6UPc3N3QygASMYgPtrzn48JgIEBl92CuGKix4PXFCaeThryd2Q8RuZXpsRxP53huD-_ZO0BHysuL7VrzAmLdNu4wsGh5Q6Sfk=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/89/899061/899061a_hb_a_009.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipO6CN3PLqdXV9qB-x9pM7qm8e3YlTwY4-Ms9IAe=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipO6CN3PLqdXV9qB-x9pM7qm8e3YlTwY4-Ms9IAe=s10000"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/OsPR3sv1IRbSh8F8VTk-QVo5Fy7n2xdmv6tqrngumeoPlly9wWUP5d3aq0IaBttp1kNItXykiFNor2KsWiKowQneOr5W-jtGeiaO6etLZyezGtJPoouWSCfAwej8C5kpJ7Jici1S0u6uY7BsN_3nWs80oWP7zw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/89/899061/899061a_hb_a_001.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/6XUG0WSJH5NxyoBN3U9tFc4Qe3HbtVA5pU5dRHtgLJcGEB8J9KGujrE2W4VjJ9y56QV-6k3VkL0wjA7AaRp7QJBti9xePF9_vq2VKluEzqn05giRMh7qXkauFVrwvsLO1MV3lYBVjjdakPTsbUHla4KdgtirlQ=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/23000000/22320000/22316500/22316404/0c72d587_z.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/8kIMnJsjK61SrN7rKDZsrmEUoyEsgRLhwexHbGtt5_RX9melrhP0PX8q9ZbGPiCT9RBdO9rRlfjkHAuLk6B_D4xQYJPk0-FUgP29EjsuVL2R0PqsDvZeFPKSLU_Yj6zgubb5_KxviS_v6U3xOGt290sMwHYJ4xQ=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/23000000/22320000/22316500/22316404/4c937a7a_z.jpg"
                },
                {
                    "thumbnail": "https://lh3.googleusercontent.com/proxy/BUzhZ85hNDPTJPsIdti8nBPO0uUMwo4AuWp-6NkZjMFG1MU329tihV4TsOjsK173GS7GaMZo0gtvjpRhICH-TrEv--7m2s1C82H4twZyn8tL2irHtQhfiHB_JzbEOXA1cDEUoDWV6FZSMW9TFI0c_6s-sfZV0A=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/25/da/8e/photo1jpg.jpg?w=1900&h=1400&s=1"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/8LthYUS0gwxSl70KJ_sHDR5IFq1RdhMtmWi3iSQYaI3fHJiBRMs0-CxzavKmuS9qu-mc1If_H4U8lnkAOvxKzngFoWlDxZWgz-aQLq_-w9pbt5R_VCHAmjCxRKsayX6aKrjKKE_MqVnL6Ye1bfHdApg6c0f3xg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/25/da/8f/photo2jpg.jpg?w=1900&h=1400&s=1"
                }
            ],
            "overall_rating": 4.3,
            "reviews": 355,
            "ratings": [
                {
                    "stars": 5,
                    "count": 222
                },
                {
                    "stars": 4,
                    "count": 72
                },
                {
                    "stars": 3,
                    "count": 26
                },
                {
                    "stars": 2,
                    "count": 12
                },
                {
                    "stars": 1,
                    "count": 23
                }
            ],
            "location_rating": 3.3,
            "reviews_breakdown": [
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 79,
                    "positive": 71,
                    "negative": 8,
                    "neutral": 0
                },
                {
                    "name": "Cleanliness",
                    "description": "Cleanliness",
                    "total_mentioned": 51,
                    "positive": 39,
                    "negative": 11,
                    "neutral": 1
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 49,
                    "positive": 36,
                    "negative": 9,
                    "neutral": 4
                },
                {
                    "name": "Kitchen",
                    "description": "Kitchen",
                    "total_mentioned": 14,
                    "positive": 11,
                    "negative": 3,
                    "neutral": 0
                },
                {
                    "name": "Safety",
                    "description": "Safety",
                    "total_mentioned": 11,
                    "positive": 9,
                    "negative": 1,
                    "neutral": 1
                },
                {
                    "name": "Parking",
                    "description": "Parking",
                    "total_mentioned": 9,
                    "positive": 4,
                    "negative": 5,
                    "neutral": 0
                }
            ],
            "amenities": [
                "Free Wi-Fi",
                "Free parking",
                "Outdoor pool",
                "Air conditioning",
                "Kitchen in rooms",
                "Child-friendly"
            ],
            "property_token": "ChoI0LvP5KeepYG4ARoNL2cvMTFnZjhnd2Z5axAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChoI0LvP5KeepYG4ARoNL2cvMTFnZjhnd2Z5axAB&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "Hotel Casaejido",
            "description": "Unfussy rooms, studios & apartments in a low-key hotel offering a garden & an outdoor pool.",
            "gps_coordinates": {
                "latitude": 20.6282337,
                "longitude": -87.08854219999999
            },
            "check_in_time": "2:00 PM",
            "check_out_time": "11:30 AM",
            "rate_per_night": {
                "lowest": "$28",
                "extracted_lowest": 28,
                "before_taxes_fees": "$21",
                "extracted_before_taxes_fees": 21
            },
            "total_rate": {
                "lowest": "$833",
                "extracted_lowest": 833,
                "before_taxes_fees": "$636",
                "extracted_before_taxes_fees": 636
            },
            "nearby_places": [
                {
                    "name": "Xplor Park",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "9 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "48 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 25 min"
                        }
                    ]
                }
            ],
            "hotel_class": "2-star hotel",
            "extracted_hotel_class": 2,
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipO0ar_1X3AV9B_qMzcQBoYIAvu1YdW8wM9PVLJ2=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipO0ar_1X3AV9B_qMzcQBoYIAvu1YdW8wM9PVLJ2=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPnDUJh1rVhCSmjJkikZ9Ul7evJpQDqhxdi3iup=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPnDUJh1rVhCSmjJkikZ9Ul7evJpQDqhxdi3iup=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNwCLXjnsKNwajBd6eioDn9D1o4Aoh5v2hLqquy=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNwCLXjnsKNwajBd6eioDn9D1o4Aoh5v2hLqquy=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOBrBteRam3c9_-kaDw7DWXl2tsijVUYcl1diuT=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOBrBteRam3c9_-kaDw7DWXl2tsijVUYcl1diuT=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipN4sYT_zeJutToI6eXTQ0ZxGfQi38EuVL9ECpy-=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipN4sYT_zeJutToI6eXTQ0ZxGfQi38EuVL9ECpy-=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNX80HuYoFpv3FC-fch2ULrPe7fN_z5M-oxEZ0d=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNX80HuYoFpv3FC-fch2ULrPe7fN_z5M-oxEZ0d=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPAc4S-7fm8mw_v3MUjfIF3PkIZRqZv4xpo4aXo=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPAc4S-7fm8mw_v3MUjfIF3PkIZRqZv4xpo4aXo=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/V6sWOhp-RQBlZh20EEg2AVtXqCiIgn7x_aq9NxkiHFu3ua5egPoUn-fASOodb55MtdKzxXaqeITwC_b7WsqCqqXPs26_kHJX-OOqklYglQ-5hj7QugMjaPEgurFB_hkIstByjFNebmz_dQKBky74PFzfhoFSG7Y=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/48/481581/481581a_hb_l_009.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipNTqwPBxupvcz5Z7-g4uzKVTDuxilzRaal5PTOn=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipNTqwPBxupvcz5Z7-g4uzKVTDuxilzRaal5PTOn=s10000"
                }
            ],
            "overall_rating": 4.4,
            "reviews": 936,
            "ratings": [
                {
                    "stars": 5,
                    "count": 634
                },
                {
                    "stars": 4,
                    "count": 180
                },
                {
                    "stars": 3,
                    "count": 62
                },
                {
                    "stars": 2,
                    "count": 20
                },
                {
                    "stars": 1,
                    "count": 40
                }
            ],
            "location_rating": 3.5,
            "reviews_breakdown": [
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 222,
                    "positive": 195,
                    "negative": 14,
                    "neutral": 13
                },
                {
                    "name": "Cleanliness",
                    "description": "Cleanliness",
                    "total_mentioned": 118,
                    "positive": 109,
                    "negative": 7,
                    "neutral": 2
                },
                {
                    "name": "Kitchen",
                    "description": "Kitchen",
                    "total_mentioned": 47,
                    "positive": 38,
                    "negative": 4,
                    "neutral": 5
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 134,
                    "positive": 120,
                    "negative": 9,
                    "neutral": 5
                },
                {
                    "name": "Atmosphere",
                    "description": "Atmosphere",
                    "total_mentioned": 93,
                    "positive": 89,
                    "negative": 1,
                    "neutral": 3
                },
                {
                    "name": "Location",
                    "description": "Location",
                    "total_mentioned": 88,
                    "positive": 62,
                    "negative": 9,
                    "neutral": 17
                }
            ],
            "amenities": [
                "Breakfast ($)",
                "Free Wi-Fi",
                "Parking ($)",
                "Outdoor pool",
                "Air conditioning",
                "Pet-friendly",
                "Restaurant",
                "Kitchen in some rooms",
                "Airport shuttle",
                "Full-service laundry",
                "Child-friendly",
                "Smoke-free property"
            ],
            "property_token": "ChgI5JGt-aubh6_PARoLL2cvMXRmeHoyanMQAQ",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChgI5JGt-aubh6_PARoLL2cvMXRmeHoyanMQAQ&q=Playa+del+Carmen"
        },
        {
            "type": "hotel",
            "name": "Magic Blue Spa Boutique Hotel Playa del Carmen",
            "description": "Tropically influenced hotel offering elegant quarters, a Brazilian restaurant & a pool, plus a spa.",
            "link": "https://magicbluespahotel.com/",
            "gps_coordinates": {
                "latitude": 20.6281088,
                "longitude": -87.0727151
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$111",
                "extracted_lowest": 111,
                "before_taxes_fees": "$90",
                "extracted_before_taxes_fees": 90
            },
            "total_rate": {
                "lowest": "$3,341",
                "extracted_lowest": 3341,
                "before_taxes_fees": "$2,710",
                "extracted_before_taxes_fees": 2710
            },
            "nearby_places": [
                {
                    "name": "3D Museum of Wonders",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "2 min"
                        }
                    ]
                },
                {
                    "name": "Playa del Carmen Alterna",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "3 min"
                        }
                    ]
                },
                {
                    "name": "Cancún International Airport",
                    "transportations": [
                        {
                            "type": "Taxi",
                            "duration": "48 min"
                        },
                        {
                            "type": "Public transport",
                            "duration": "1 hr 4 min"
                        }
                    ]
                },
                {
                    "name": "La Consentida",
                    "transportations": [
                        {
                            "type": "Walking",
                            "duration": "1 min"
                        }
                    ]
                }
            ],
            "hotel_class": "4-star hotel",
            "extracted_hotel_class": 4,
            "images": [
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPUUFvFZKIffFpBKcIme1oQHLspdPWxoQf9Ahx_=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPUUFvFZKIffFpBKcIme1oQHLspdPWxoQf9Ahx_=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipOud83PISC9WI6GKpTJFr4_zAkCDg9Cttzbpelb=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipOud83PISC9WI6GKpTJFr4_zAkCDg9Cttzbpelb=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/proxy/sPviViC5NeLNEu2V0lZFsEXUmMH4yKLxSXjNFCpt5n7n6W3y_lpdPkRz1Qr24_df0jJ5D4cTQdX3oDSSFNIHmp2Qxb6dE2slxuR6rKiZ5_oki_5sAq0tqDT9Cn6l5_AdwVVKbj14hGrxKkfP3QY-nG62W61MVQ=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/2000000/1680000/1671500/1671407/6284d7bd_z.jpg"
                },
                {
                    "thumbnail": "https://lh4.googleusercontent.com/proxy/sVVKve2v0lijmoxsw2Du6VAv-H47hlYw0QwEWKWsY4gLpHeRs9_eXAwuRqauyYwvSTlvUxTMATrbZmw6JJzdD7kBCeaMBzrTKtrCJbZ8kTn5DbbzwhwnaP6EaFuPppcksIkKsNOKc3OdHAwTBrRL0w9ES-fmpZ4=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://photos.hotelbeds.com/giata/original/00/008183/008183a_hb_a_001.jpg"
                },
                {
                    "thumbnail": "https://lh6.googleusercontent.com/proxy/ANrs8VIsivWHEXnSc3DGkk3DHUTej03Yrv_DJS4McF0nbPzl3iQpT_SkGWp6mQbImKxocIujNlFDel6LFZIIGBtt3xq0qWREOHE9eU6M6fi46NVwME94DtXidP1y0p7bTvlJsLdvkc2AubAgHsuOVooJphSPbw=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://images.trvl-media.com/lodging/2000000/1680000/1671500/1671407/9b56ece9_z.jpg"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMxpvWVQXVQwLJy3fLP3rblWQkotfQLijkUQMDy=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMxpvWVQXVQwLJy3fLP3rblWQkotfQLijkUQMDy=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipMqS3vurNqo93cxguMrODqTsNacj5Vy3UH2ZkuS=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipMqS3vurNqo93cxguMrODqTsNacj5Vy3UH2ZkuS=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPaB3P2RN3-a-eKphO0jEE1owvk9AKdDOzgJahk=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPaB3P2RN3-a-eKphO0jEE1owvk9AKdDOzgJahk=s10000"
                },
                {
                    "thumbnail": "https://lh5.googleusercontent.com/p/AF1QipPLETjlyLt5Ihh3D-RNavvzL4mJsTdpJWGzftAg=s287-w287-h192-n-k-no-v1",
                    "original_image": "https://lh5.googleusercontent.com/p/AF1QipPLETjlyLt5Ihh3D-RNavvzL4mJsTdpJWGzftAg=s10000"
                }
            ],
            "overall_rating": 4.4,
            "reviews": 770,
            "ratings": [
                {
                    "stars": 5,
                    "count": 507
                },
                {
                    "stars": 4,
                    "count": 174
                },
                {
                    "stars": 3,
                    "count": 41
                },
                {
                    "stars": 2,
                    "count": 8
                },
                {
                    "stars": 1,
                    "count": 40
                }
            ],
            "location_rating": 4.8,
            "reviews_breakdown": [
                {
                    "name": "Wellness",
                    "description": "Wellness",
                    "total_mentioned": 53,
                    "positive": 35,
                    "negative": 10,
                    "neutral": 8
                },
                {
                    "name": "Spa",
                    "description": "Spa",
                    "total_mentioned": 47,
                    "positive": 31,
                    "negative": 7,
                    "neutral": 9
                },
                {
                    "name": "Breakfast",
                    "description": "Breakfast",
                    "total_mentioned": 109,
                    "positive": 94,
                    "negative": 9,
                    "neutral": 6
                },
                {
                    "name": "Fitness",
                    "description": "Fitness",
                    "total_mentioned": 119,
                    "positive": 96,
                    "negative": 14,
                    "neutral": 9
                },
                {
                    "name": "Service",
                    "description": "Service",
                    "total_mentioned": 174,
                    "positive": 143,
                    "negative": 24,
                    "neutral": 7
                },
                {
                    "name": "Property",
                    "description": "Property",
                    "total_mentioned": 190,
                    "positive": 153,
                    "negative": 26,
                    "neutral": 11
                }
            ],
            "amenities": [
                "Breakfast ($)",
                "Free Wi-Fi",
                "Parking ($)",
                "Pool",
                "Air conditioning",
                "Spa",
                "Beach access",
                "Bar",
                "Restaurant",
                "Room service",
                "Airport shuttle",
                "Full-service laundry",
                "Child-friendly"
            ],
            "property_token": "ChgIgqTM0KSZ2YOUARoLL2cvMXRmYnBjeW0QAQ",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&property_token=ChgIgqTM0KSZ2YOUARoLL2cvMXRmYnBjeW0QAQ&q=Playa+del+Carmen"
        }
    ],
    "serpapi_pagination": {
        "current_from": 1,
        "current_to": 20,
        "next_page_token": "CBI=",
        "next": "https://serpapi.com/search.json?adults=2&check_in_date=2024-06-01&check_out_date=2024-07-01&children=0&currency=USD&engine=google_hotels&gl=us&hl=en&max_price=10000&next_page_token=CBI%3D&q=Playa+del+Carmen"
    }
}

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

