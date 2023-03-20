import requests
import json
import PyWallpaper

api_key = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

res = requests.get(api_key)

content = res.content.decode("UTF-8")

print(content)


# convert string to json

clearContent = json.loads(content)
# print(type(clearContent))

# get image
image_url = clearContent['url']
print(image_url)

# to download
response = requests.get(image_url)
print(response)

# save the image

with open('apod.png', 'wb') as image:
    image.write(response.content)

# set wallpaper

# PyWallpaper.change_wallpaper('apod.png')
PyWallpaper.change_wallpaper('G:/New_folder/python/apod.png')
