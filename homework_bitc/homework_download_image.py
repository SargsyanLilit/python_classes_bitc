import json
import requests
import os
from datetime import datetime


try:
    os.mkdir("image_folder")
except FileExistsError:
    print("The folder has been already created!")


try:
    with open("log_file.txt", "x") as txt_file:
        pass
except FileExistsError:
    print("The file has been already created!")


with open("img_links_json.json", "r") as json_file:
    image_list = json.load(json_file)


string_to_log_file = ""


for image in image_list:
    response = requests.get(image["img_url"])
    with open("image_folder/" + image["img_name"], 'wb') as new_image:
        new_image.write(response.content)
    string_to_log_file += f'{image["img_name"]} was successfully downloaded in image_folder at {datetime.now()}\n'


if string_to_log_file:
    with open("log_file.txt", "a") as txt_file:
        txt_file.write(string_to_log_file)