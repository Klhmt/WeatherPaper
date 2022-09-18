# WeatherPaper

Here you have a simple and straighforward Python script that allows you to change your Gnome wallpaper according to the current weather

## Disclaimer

Please note that weather indications are voluntarely reductive and provided without any warranty

## Configuration

First you need to have images stored in the same folder that correspond to the following weather states:
- "clear"
- "cloudy"
- "rainy"
- "snowy"
- "thunderstorm"

**You have to rename the images and include these weather states as written above because the program will search the name of the images to associate a weather state and an image.**

For example, if "IMG_6575.png" corresponds to a cloudy weather, you can name it "IMG_6575_cloudy.png"
or "IMG_cloudy.png" or "cloudy.png". 

Then you need to open the wallpaper.py file.

**You have to declare the LATITUDE and LONGITUDE variable with the latitude and longitude of your location. There are websites to find them, like https://www.latlong.net/**

After that you can change the value of the variable "hourly_update". Set it to True or False (True by default).   
If True, the weather code given by the API will be for the hour.   
If False, the weather code given by the API will be for the whole day.

That's it!

## Run automatically with systemd

Currently under test!

