import csv
from selenium import webdriver

import selenium.webdriver
from datetime import datetime
import selenium.webdriver
import time

now = datetime.now()
current_time = now.strftime("%m%d%y_%H%M%S")
print(now)
output_file = "company_detail_(" + current_time + ").csv"
print(output_file)


def add_csv_head():
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Primary Contact', 'Address', 'Phone', 'Professionals On Staff', 'Web', 'Specialties'])

def add_csv_row(title, primary_contact, address, phone, staff, web, specialties):

    with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([title, primary_contact, address, phone, staff, web, specialties])

driver = selenium.webdriver.Chrome()

base_url = 'https://remodelingdoneright.nari.org/remodelers/'

driver.get(base_url)
time.sleep(10)
driver.implicitly_wait(10)

states = driver.find_elements_by_xpath('//select[@id="p_lt_ctl05_pageplaceholder_p_lt_ctl02_WebPartZone4_WebPartZone4_zone_RemodelerListing_fltRemodelers_drpState"]//option')
states_len = len(states)
# print(states)
page_urls = []
j = 1
while j < 3:

    time.sleep(5)
    

    select_state = driver.find_element_by_xpath('//select[@id="p_lt_ctl05_pageplaceholder_p_lt_ctl02_WebPartZone4_WebPartZone4_zone_RemodelerListing_fltRemodelers_drpState"]')
    select_state.click()

    states = driver.find_elements_by_xpath('//select[@id="p_lt_ctl05_pageplaceholder_p_lt_ctl02_WebPartZone4_WebPartZone4_zone_RemodelerListing_fltRemodelers_drpState"]//option')[j]
    states.click()

    search_button = driver.find_element_by_xpath('//div/input[@type="submit"]')
    search_button.click()
    print('button click')
    j += 1
    time.sleep(5)
    try:
        page_tmp = driver.find_elements_by_xpath('//div[@class="filter-item"]/span')[1].text
    except:
        print("no list")
        continue
    page_tmps = page_tmp.split()
    page_number = int(page_tmps[1])
    print('page number:' + page_tmps[1])
    i = 0
    
    while i < page_number:
        page_urls_tmps = driver.find_elements_by_xpath('//div[@class="find-remodeler-footer"]/a')
        for page_urls_tmp in page_urls_tmps:
            page_url = page_urls_tmp.get_attribute("href")
            page_urls.append(page_url)
        next_button = driver.find_elements_by_xpath('//div[@class="filter-item"]/a')[1]
        next_button.click()
        time.sleep(5)
        print(page_urls)
        i += 1

    
    print("done state")
    
    time.sleep(5)

print("all done")

add_csv_head()
for page_url in page_urls:
    driver.get(page_url)
    time.sleep(5)
    try:
        title = driver.find_element_by_xpath('//div[@class="company-title-description"]/h1').text
    except:
        title = 'N/A'
    try:
        primary_contact = driver.find_element_by_xpath('//div[@class="contact-block"]/p').text
    except:
        primary_contact = 'N/A'
    try:
        address = driver.find_element_by_xpath('//div[@class="address-block"]/p').text
    except:
        address = 'N/A'
    try:
        phone = driver.find_element_by_xpath('//div[@class="phone-block"]/a').text
    except:
        phone = 'N/A'
    try:
        staff = driver.find_element_by_xpath('//div[@class="certified-block"]/p').text
    except:
        staff = primary_contact
    try:
        web = driver.find_element_by_xpath('//div[@class="web-block"]/a').text
    except:
        web = 'N/A'
    specialties = ''
    try:
        specialties_tmps = driver.find_elements_by_xpath('//div[@class="rail-navigation-wrapper"]/ul/li')
        for specialties_tmp in specialties_tmps:
            specialties += specialties_tmp.text + '|'
    except:
        specialties = 'N/A'

    add_csv_row(title, primary_contact, address, phone, staff, web, specialties)

    print("detail page done")
driver.close()
print("please check file")


