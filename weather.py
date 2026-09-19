import requests

# Target Dallas and request clean JSON format strings
url = "https://wttr.in"

print("Connecting to the weather station in Dallas...")
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(" Success! Data Received ")

    # Extract the current condition object
    current_condition = weather_data["current_condition"][0]

    # Look up the exact weather data metrics
    temp_f = current_condition["temp_F"]
    desc = current_condition["weatherDesc"][0]["value"]
    humidity = current_condition["humidity"]
    
    # Print the clean dashboard layout
    print("\n🌤️ --- DALLAS LIVE WEATHER DASHBOARD --- 🌤️")
    print(f"Current Condition: {desc}")
    print(f"Temperature:       {temp_f}°F")
    print(f"Humidity:          {humidity}%")
    print("-------------------------------------------\n")
else:
    print(f"Failed to connect. Status code: {response.status_code}")
