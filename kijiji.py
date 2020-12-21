import csv
import sys
import re
import os
import json
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import InvalidArgumentException

from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver

import requests
from bs4 import BeautifulSoup

import time

now = datetime.now()
current_time = now.strftime("%m%d%y_%H%M%S")
print(now)
output_file = "kijiji(" + current_time + ").json"
print(output_file)


# def add_csv_head():
#     with open(output_file, 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(['Title', 'Description', 'Name of owner', 'phone number'])

# def add_csv_row(title_pre, description, name_of_owner, phone_number):

#     with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow([title_pre, description, name_of_owner, phone_number])

# add_csv_head()

driver = selenium.webdriver.Chrome()

base_url = 'https://www.kijiji.it/case/stanze-e-posti-letto/annunci-milano/privato/?entryPoint=sb'

driver.get(base_url)
time.sleep(20)
driver.implicitly_wait(70)

element=driver.find_element_by_xpath('//span[@class="last-page"]')

print(element.text)

# i=driver.find_elements_by_css_selector('span.last-page').text

i=int(element.text)+1
j=1
time.sleep(20)
stored_urls = [];
output_json=[];
while j<i:
    urls=driver.find_elements_by_xpath('//ul[@id="search-result"]/li[@data-id]')
    time.sleep(30)
    driver.implicitly_wait(30)
    print(urls)
    for url in urls:

        list_url=url.get_attribute('data-href')
        stored_urls.append(list_url)
        time.sleep(3)
    next_button = driver.find_element_by_css_selector("a.btn-pagination-forward")
    driver.execute_script("arguments[0].click();", next_button)
    time.sleep(30)
    j+=1;
for url in stored_urls:
    time.sleep(10)
    driver.get(url)
    time.sleep(20)

    title_pre=driver.find_elements_by_css_selector("h1.vip__title")[1].text
    description=driver.find_element_by_css_selector("p.vip__text-description").text
    name_of_owner=driver.find_elements_by_css_selector("div.title")[1].text
    try:
        phone_button=driver.find_element_by_css_selector("i.ki-icon-call-blue")
        driver.execute_script("arguments[0].click();", phone_button)
        phone_number=driver.find_element_by_css_selector("h3.modal-phone__text").text
    except:
        phone_number="N/A"
    
    my_details = {
        'title': title_pre,
        'description': description,
        'name of owner': name_of_owner,
        'phone number': phone_number
    }

    output_json.append(my_details)

with open('rome1.json', 'w') as json_file:
    json.dump(output_json, json_file)

    # add_csv_row(title_pre, description, name_of_owner, phone_number)

print("done")