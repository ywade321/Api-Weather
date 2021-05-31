# Include requests to call openweather api
import requests
# Include JSON to parse the information from openweather
import json
api_key = '9c26fcd36ffa56a54fc35cd3cece35ae'

def k_to_f(k): 
    ''' Converts kelvin to fahrenheit '''
    f = (k - 273.15) * 9/5 + 32
    return f

def main():
    ''' Main/Driver function '''

    # Within a loop...
    again = "y"
    while again == "y":

        # Ask user for city or Zip
        entry = input("Please enter city or zip: ")

        # remove  whitespaces from entry
        entry = entry.strip()

        # Validate the input
        if len(entry) < 2:
            print("Please enter a valid city name or zip code")
            # Repeat request if input is invalid
            continue

        # Call the openweather API with the city or zip
        url=f"https://api.openweathermap.org/data/2.5/forecast?q={entry}&appid={api_key}"

        # Use try when attempting to access the weather server so that the program
        # doesn't crash if something goes wrong.
        print("Contacting the weather service....")
        try:
            r = requests.get(url)
        except Exception:
            # If the connection fails, notify the user and start the loop again.
            print("*** Unable to connect to Open Weather system. Try again later. ***")
            continue

        # Receive reply from openweather
        # convert text response to a python dictionary using json
        response = json.loads(r.text)
        # Indicate whether the connection was successful
        # if successful, openweather api respondes with cod=200
        if response['cod'] != "200":
            print("Received error response from OpenWeather API:", response["cod"])
            continue

        print("Response received... decoding...")

        weather_list = response['list']
        # Parse the received information
        # If an error was received, notify the user of the error
        # Display the information to the user
        print("\nCurrent weather for",response['city']['name'])
        temp_k = weather_list[0]['main']['temp'] # temp in kelvin
        fahr = k_to_f(temp_k)
        fahr = round(fahr,1)
        print("Temperature:",fahr)
        print("Pressure:",weather_list[0]['main']['pressure'])
        print("Weather:",weather_list[0]['weather'][0]['main'],"--",weather_list[0]['weather'][0]['description'])

        print("\nTomorrow's Forecast:")
        temp_k = weather_list[24]['main']['temp'] # temp in kelvin
        fahr = k_to_f(temp_k)
        fahr = round(fahr,1)
        print("Temperature:",fahr)
        print("Pressure:",weather_list[24]['main']['pressure'])
        print("Weather:",weather_list[24]['weather'][0]['main'],"--",weather_list[24]['weather'][0]['description'])


        # Ask the user if he or she would like to check weather again…
        again = input("\nThank you for using Open Weather would you like to try again (y or n): ")
        again = again.strip() #takes whitespace off of the entry
        if len(again) == 0:
            again = "n"
        again = again[0].lower() # get the first letter and convert to lowercase
        if again != "y":
            print("Have a nice day")

if __name__ == "__main__":
    main()