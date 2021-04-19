import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk
from GetWeatherIcons import getWeatherIcons

# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={your api key}

root = tk.Tk()

HEIGHT = 520
WIDTH = 680

def formatResponse(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]
        output = "City: %s \nConditions: %s \nTemperature (C): %s" % (name, desc, temp)
    except:
        output = "Cannot find weather data for that place"

    return output

def getWeather(city):
    entry.delete(0, 'end')
    if city:
        weatherKey = "<Insert your OpenWeatherMap key here>"
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"APPID": weatherKey, "q": city, "units": "metric"}
        response = requests.get(url, params=params)
        weather = response.json()

        results["text"] = formatResponse(weather)

        getWeatherIcons()
        imageName = weather["weather"][0]["icon"]
        openImage(imageName)

def openImage(fileName):
    size = int(lowerFrame.winfo_height()*0.25)
    icon = ImageTk.PhotoImage(Image.open("./weatherIcons/" + fileName + ".png").resize((size, size)))
    weatherIcon.delete("all")
    weatherIcon.create_image(0, 0, anchor='nw', image=icon)
    weatherIcon.image = icon

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

backgroundImage = ImageTk.PhotoImage(file="Background.jpg")
backgroundLabel = tk.Label(root, image=backgroundImage)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#85c2ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Courier", 18))
entry.bind("<Return>", lambda x: getWeather(entry.get()))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bg="gray", fg="red", font=("Courier", 12), command=lambda: getWeather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lowerFrame = tk.Frame(root, bg="#85c2ff", bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

results = tk.Label(lowerFrame, font=("Courier", 14), anchor="nw", justify="left", bd=4)
results.place(relwidth=1, relheight=1)

weatherIcon = tk.Canvas(results, bd=0, highlightthickness=0)
weatherIcon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
