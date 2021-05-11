# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
# Import libraries
from GoogleImageScrapper import GoogleImageScraper
import os

# Define file path
webdriver_path = os.path.normpath('/usr/local/bin/chromedriver')
image_path = os.path.normpath(os.getcwd()+"/photos")

# Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
search_keys = ["sunglass"]

# Parameters
number_of_images = 20
headless = False
min_resolution = (0, 0)
max_resolution = (1000, 1000)

# Main program
for search_key in search_keys:
    image_scrapper = GoogleImageScraper(
        webdriver_path, image_path, search_key, number_of_images, headless, min_resolution, max_resolution)
    print('3')
    image_urls = image_scrapper.find_image_urls()
    print('4')
    image_scrapper.save_images(image_urls)
