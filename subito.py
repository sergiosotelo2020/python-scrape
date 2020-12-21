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
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%m%d%y_%H%M%S")
print(now)
output_file = "subito(" + current_time + ").json"
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
print(driver)

base_url = 'https://www.subito.it/annunci-toscana/affitto/camere-posti-letto/firenze/firenze/?o=9&advt=0'

driver.get(base_url)
time.sleep(15)
driver.implicitly_wait(50)

i=driver.find_elements_by_css_selector('button.pagination__btn')[2].text

print(i)
i=int(i)+1
j=9

stored_urls = [];
output_json=[];
while j<i:
    urls=driver.find_elements_by_css_selector('a.jsx-1356703816.link')
    time.sleep(5)
    driver.implicitly_wait(20)
    print(urls)

    for url in urls:
	    
        list_url=url.get_attribute('href')
        stored_urls.append(list_url)
        time.sleep(1)
	    # print(b_url)
    next_button=driver.find_elements_by_css_selector("button.UIElements__Button--icon-only-L2hvbWUv")[1]
    driver.execute_script("arguments[0].click();", next_button)
    time.sleep(10)
    j+=1;
for url in stored_urls:
    driver.get(url)
    time.sleep(8)

    title_pre=driver.find_element_by_css_selector("h1.ad-info__title").text
    print(title_pre)
    description=driver.find_element_by_css_selector("p.jsx-436795370").text
    name_of_owner=driver.find_element_by_css_selector("h6.weight-semibold").text
    try:
        phone_button=driver.find_element_by_css_selector("div.phone-icon")
        driver.execute_script("arguments[0].click();", phone_button)
        phone_number=driver.find_element_by_css_selector(".phone-number").text
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