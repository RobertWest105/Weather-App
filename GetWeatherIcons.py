import os
import urllib.request

def getWeatherIcons():
    day = ["01d.png", "02d.png", "03d.png", "04d.png", "09d.png", "10d.png", "11d.png", "13d.png", "50d.png"]
    night = ["01n.png", "02n.png", "03n.png", "04n.png", "09n.png", "10n.png", "11n.png", "13n.png", "50n.png"]

    baseURL = "https://openweathermap.org/img/w/"
    imgFolder = "./weatherIcons/"
    if not os.path.exists(imgFolder):
        os.makedirs(imgFolder)

        for name in day:
            fileName = imgFolder + name
            if not os.path.exists(fileName):
                urllib.request.urlretrieve(baseURL + name, fileName)

        for name in night:
            fileName = imgFolder + name
            if not os.path.exists(fileName):
                urllib.request.urlretrieve(baseURL + name, fileName)
