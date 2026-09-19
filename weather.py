import requests

# Official National Weather Service (NWS) endpoint for Dallas coordinates
url = "https://weather.gov"

# Professional systems must include a User-Agent header so the server knows who is calling
headers = {
    "User-Agent": "(myportfolio-project, quatrellekanady@github.com)"
}

print("Connecting to the US National Weather Service...")
try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        weather_data = response.json()
        print(" Success! Data Received ")

        # Extract the very first hourly entry (Current Weather)
        current_period = weather_data["properties"]["periods"][0]
        
        temp = current_period["temperature"]
        unit = current_period["temperatureUnit"]
        desc = current_period["shortForecast"]
        humidity = current_period["relativeHumidity"]["value"]
        wind = current_period["windSpeed"]
        
        # Display the live dashboard layout
        print("\n🌤️ --- DALLAS LIVE WEATHER DASHBOARD --- 🌤️")
        print(f"Current Condition: {desc}")
        print(f"Temperature:       {temp}°{unit}")
        print(f"Humidity:          {humidity}%")
        print(f"Wind Speed:        {wind}")
        print("-------------------------------------------\n")
    else:
        print(f"\n❌ Server blocked the request. HTTP Status code: {response.status_code}")
        print("--- SERVER RESPONSE TEXT START ---")
        print(response.text[:500])  # Print the first 500 characters of the block page
        print("--- SERVER RESPONSE TEXT END ---\n")
except Exception as e:
    print(f"An error occurred while loading data: {e}")
