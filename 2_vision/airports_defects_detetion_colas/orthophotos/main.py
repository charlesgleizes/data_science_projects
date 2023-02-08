import requests as r
import pandas as pd
import json
from PIL import Image
import geopandas as gpd
from shapely.geometry import Point
import pyproj
import os
import yaml
import warnings
from utils.request_helper import clean_coordinates, get_all_coor, construct_bbox, get_width_height, get_url

warnings.filterwarnings("ignore")

# Load yaml config file.
with open("config.yml") as f:
    config = yaml.safe_load(f)

# Load data.
data = gpd.read_file("airports/data/airports.geojson")

# Clean Coordinates - Pass Geopandas Geometry format to string format.
data = clean_coordinates(data)

# Construction of the bbox rectangles that contain each airport. Bbox will be used during WMS request.
data = construct_bbox(data)

# Define the width and height needed for each airport photo in order to have a 20cm per pixel resolution.
data = get_width_height(data)

# Check if there is a folder named image_folder. If not, create one. 
if os.path.exists(config["ROOT_DIR_PATH"] + "/orthophotos/image_folder") == True:
    print('image_folder already exists')
    
else: 
    os.mkdir(config["ROOT_DIR_PATH"] + "/orthophotos/image_folder")

# Download each photo in the image_folder folder.
i = 0

for row in data.iterrows():
    image_url = get_url(row[1]["bbox"], row[1]["height"], row[1]["width"])
    response = r.get(image_url) ## Making a variable to get image
    image_name = config["ROOT_DIR_PATH"] + "/orthophotos/image_folder/airport_" + str(i) + ".png" 
    file = open(image_name, "wb") ## Creates the file for image
    file.write(response.content) ## Saves file content
    file.close()
    i += 1