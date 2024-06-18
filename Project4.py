import datetime as dt
import requests
import tkinter as tk
from tkinter import messagebox

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "806f21a7bc8576b31293d0b2ced0cf21"

def getWeather():
    location = locationVar.get()
    system = measureSys.get()

    url = BASE_URL + "q=" + location + "&APPID=" + API_KEY
    response = requests.get(url).json()

    weather = response["weather"][0]["main"]
    temperature = response["main"]["temp"] - 273.15
    if(system == "I"):
        temperature *= 9/5
        temperature += 32
    humidity = response["main"]["humidity"]
    wind = response["wind"]["speed"]

    messagebox.showinfo("Weather", "The Temperature is:", temperature, 
                        "\nThe Sky is:", weather, "\nThe Humidity is:", humidity,
                        "\nThe Wind Speed is:", wind)

page = tk.Tk()
page.title("Weather App")
measureSys = tk.StringVar()
locationVar = tk.StringVar()
tk.Radiobutton(page, text='Imperial (Pounds/Inches)', variable=measureSys, value='I').grid(row = 0, column = 0)
tk.Radiobutton(page, text='Metric (Kilos/Meters)', variable=measureSys, value='M').grid(row = 0, column = 1)
tk.Label(page, text='City').grid(row = 0, pady = 5)
e1 = tk.Entry(page, textvariable = locationVar).grid(row = 0, column = 1)
button = tk.Button(page, text="Get Weather", command=getWeather).grid(row = 1, column = 1)
page.mainloop()