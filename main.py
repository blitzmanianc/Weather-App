import requests #You have to install it using pip

def fetch_weather(city):
    api_key = 'This is where you put your api key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found. Please enter a valid city name.") #If your output keeps being "City not found. Please enter a valid city name." then most likely you have a problem with your API key.

city = input("Enter city name: ")
weather_data = fetch_weather(city)
display_weather(weather_data)
