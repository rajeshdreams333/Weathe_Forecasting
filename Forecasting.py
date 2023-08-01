import requests
def get_weather_data():
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data. Please check your input or try again later.")
        return None
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius=kelvin-273.15
    fahrenheit=celsius*(9/5)+32
    return "{:.2f}".format(fahrenheit)

def get_weather_by_date(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].startswith(date):
            return kelvin_to_celsius_fahrenheit(forecast['main']['temp'])
    return None

def get_wind_speed_by_date(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].startswith(date):
            return forecast['wind']['speed']
    return None

def get_pressure_by_date(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].startswith(date):
            return forecast['main']['pressure']
    return None

if __name__ == "__main__":
    weather_data = get_weather_data()
    if not weather_data:
        exit()

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_by_date(weather_data, date)
            if temperature:
                print(f"Temperature on {date}: {temperature} °C")
            else:
                print("No weather data found for the given date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("No weather data found for the given date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No weather data found for the given date.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
