import requests


apikey = "d0c3ba776d62e70712e741261cb43138"

city = input("enter your city : ")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={apikey}")

if response.status_code == 200 :
    weather = response.json()['weather'][0]['description']
    temp = round(response.json()['main']['temp'])

    celcius = round((temp - 32) * 5/9)

    print(f"weather condtion of {city} \nweather : {weather}\ntemperature is {temp}°F and {celcius}°c")
else:
    print("city not found")