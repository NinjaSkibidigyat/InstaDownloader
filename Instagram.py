from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import os

## Author = Sohaib

# Asking the user to input the url
link = input('Enter Instagram URL==> ')


# Create a webdriver chrome object by passing the path of chrimedriver.exe


driver = webdriver.Chrome('chromedriver')


# Open the instagram post on your chrome browser
driver.get(link)


# Fetching the source file of the html page using Beautifulsoup
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'lxml')

images = soup.find_all('img', class_='FFVAD')

# naming each image with numbers starting from 0
number = 0
for image in images:
    name = image['alt']
    img_url = image['src']
    with open(str(number) +".jpg",'wb') as f:
        im = requests.get(img_url)
        number += 1
        f.write(im.content)
        yourfile = os.getcwd()
        print('your photos are at ' + yourfile)
