import requests
import time
import threading

class Weather:
    def __init__(self):
        self.key = "2a28059edf09485791e110753240101"
        self.url = "https://api.weatherapi.com/v1/current.json"
        self.fav = []
        self.auto_refresh_thread = None 

    def get(self, city):
        params = {'key': self.key, 'q': city}
        response = requests.get(self.url, params=params)
        data = response.json()

        if 'error' in data:
            print(f"Error: {data['error']}")
        else:
            self.display(data)

    def display(self, data):
        print(f"Weather in {data['location']['name']}, {data['location']['region']}, {data['location']['country']}:")
        print(f"Condition: {data['current']['condition']['text']}")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Wind Speed: {data['current']['wind_kph']} km/h")
        print(f"Last Updated: {data['current']['last_updated']}")
        print("")

    def add(self, city):
        if city not in self.fav:
            self.fav.append(city)
            print(f"{city} added to favorites")
        else:
            print(f"{city} is already in favorites")

    def remove(self, city_to_remove):
        print("Favorite cities:")
        for city in self.fav:
            print(f"- {city}")
        if city_to_remove in self.fav:
            self.fav.remove(city_to_remove)
            print(f"{city_to_remove} removed from favorites")
        else:
            print(f"{city_to_remove} is not in favorites")
        print("")

    def list_favorite_cities(self):
        print("Favorite cities:")
        for city in self.fav:
            print(f"- {city}")
        print("")

    def auto_refresh(self, city):
        while True:
            print(f"Auto-refreshing weather for {city} ")
            self.get(city)
            time.sleep(100)  

    def start_auto_refresh_thread(self, city):
        self.auto_refresh_thread = threading.Thread(target=self.auto_refresh, args=(city,))
        self.auto_refresh_thread.daemon = True
        self.auto_refresh_thread.start()

    def run(self):
        while True:
            print("Options:")
            print("1. Check weather by city")
            print("2. Add city to favorites")
            print("3. Remove city from favorites")
            print("4. List favorite cities")
            print("5. Quit")

            choice = input("Enter option number: ")

            if choice == '1':
                city = input("Enter city name: ")
                self.get(city)
            elif choice == '2':
                city = input("Enter city name to add to favorites: ")
                self.add(city)
            elif choice == '3':
                self.list_favorite_cities()
                city_to_remove = input("Enter city name to remove from favorites: ")
                self.remove(city_to_remove)
            elif choice == '4':
                self.list_favorite_cities()
            elif choice == '5':
                print("Quitting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    weather_app = Weather()
    weather_app.run()
