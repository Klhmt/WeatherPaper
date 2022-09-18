from os import system, listdir
from random import randint
import requests
import json


#   All weather data come from Open-Meteo.com API: https://open-meteo.com
#   /!\ Please note that all data from this API is provided without any warranty /!\
#   /!\ Please note that the weather data intepretation into
#       weather description (like cloudy, rainy) is deliberately reductive       /!\
#   /!\ I'm not responsible for any consequences caused by weather predictions   /!\

#
#   Ajouter disclaimer
#   Ajouter gestion d'erreurs API
#   Ajouter gestion d'erreurs code Weather
#   Ajouter gestion d'erreurs fichiers wallpapers
#   Ajouter gestion d'erreurs changement wallpapers
#

# Set here your latitude value
LATITUDE = 45.800798

# Set here your longitude value
LONGITUDE = 4.822110

# If True, the weather code given by the API will be for the hour
# If False, the weather code given by the API will be for the whole day
hourly_update = True

# Generation of the URL according to the previous parameters
if hourly_update:
    URL = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&hourly=weathercode&timezone=auto"
else:
    URL = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&daily=weathercode&timezone=auto"


def getApiData(url: str, hourly_update: bool):
    """
    This function calls the weather API and returns the time code only
    Weather data are from Open-Meteo.com (https://open-meteo.com/)
    Please do not exceed 10.000 request a day and read the disclaimers at the
    beginning of the file. 
    Refer to the link for more information about the licence and contact of the
    API provider.

    Arg:
        url: url of the API
        hourly_update: if True, the function will return the weather code of
        the hour. Else the function will return the weather code of the day
    
    Return:
        time_code (float): time code for the hour/the day. Refer to the 
        following link for understanting the meaning of the codes: 
        https://open-meteo.com/en/docs
    
    """
    time_code = float
    api_response = requests.get(url)
    # If there is an error with the API an error is raised
    api_response.raise_for_status()
    
    response_data = json.loads(api_response.text)
    if hourly_update:
        time_code = response_data["hourly"]["weathercode"][0]
    else:
        time_code = response_data["daily"]["weathercode"][0]
    return time_code


def weatherCodeToDescription(weather_code: float):
    """
    This function returns the description of a given weather code. 
    /!\ Please note that this transformation is deliberately reductive /!\
    Please read the disclaimers at the beginning of the file.

    Arg:
        weather_code: weather code from weather API data
    
    Return:
        (string): approximative and possibly non representative description of 
                  the weather 
    
    """
    if weather_code == 0.0:
        return "clear"
    elif weather_code in (1, 2, 3, 45, 48):
        return "cloudy"
    elif weather_code in (51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82):
        return "rainy"
    elif weather_code in (71, 73, 75, 77, 85, 86):
        return "snowy"
    elif weather_code in (95, 96, 99):
        return "thunderstorm"


def changeWallpaper(wallpaper_path: str, weather_description: str, 
                    extensions: tuple = ("jpg", "png", "jpeg")):
    """
    This function changes the wallpaper of your Gnome desktop
        
    Arg:
        wallpaper_path (str): path of the a folder that contains your wallpaper
        force_new_one (bool): if True the previous wallpaper will be excluded 
                              from the list of possible wallpapers
        extensions (tuple): desired extensions
            
    """
    # Selection of images according to their extension
    wallpaper_images = [image for image in listdir(wallpaper_path) 
                        if image.split(".")[-1] in extensions 
                        and weather_description in image]
    # Random choice of an image
    selected_image = wallpaper_images[randint(0, len(wallpaper_images) - 1)]
    # Apply a new wallpaper
    system("gsettings set org.gnome.desktop.background picture-uri file:///{}".format(wallpaper_path + "/" + selected_image))

def main(wallpaper_path: str):
    """
    This function generates the API url, get the weather code and transform
    it and changes the wallpaper 

    Arg:
        wallpaper_path: path of the folder that contained your wallpaper 
    """
    # Check if the API url is for hourly or daily weather code
    hourly_update = True if "hourly" in URL else False
    # Get weather data from API
    weather_code = getApiData(URL, hourly_update)
    # Change weather code to weather description
    weather_description = weatherCodeToDescription(weather_code)
    # Change wallpaper according to the weather
    changeWallpaper(wallpaper_path, weather_description)


main("/home/klem/Images/wallpapers/Weather")
