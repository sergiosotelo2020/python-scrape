import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import selenium.webdriver
from datetime import datetime
import selenium.webdriver
import time

now = datetime.now()
current_time = now.strftime("%m%d%y_%H%M%S")
print(now)


# Read and write into csv file
def add_csv_head():
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Description', 'Details', 'Pakaging', 'Modelings', 'Installations', 'Maintenance', 'Tile image'])

def add_csv_row(title, description, details, pakaging, modelings, installations, maintenance, tile_image):

    with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([title, description, details, pakaging, modelings, installations, maintenance, tile_image])

option = webdriver.ChromeOptions()
option.add_argument('headless')
# driver = selenium.webdriver.Chrome()
# driver = webdriver.Chrome('chromedriver', options = option)

base_url = input("Enter the category url: ")

# base_url = 'https://www.beaulieucanada.com/en/retail/flooring/luxuryvinyl'
driver = selenium.webdriver.Chrome()

driver.get(base_url)
time.sleep(5)
driver.implicitly_wait(5)
try:
    accept_button = driver.find_element_by_xpath('//button[@class="btn btn-secondary"]')
    accept_button.click()
except:
    print('No button')

# Scroll to bottom of page
liElement = driver.find_element_by_xpath('//footer')
driver.execute_script("arguments[0].scrollIntoView(true);", liElement)

states = driver.find_elements_by_xpath('//div[@class="card tw-w-full px-0 pt-0 pb-2 mb-3 tw-rounded product"]/a')
states_len = len(states)
# print(states)
page_urls = []
# Get page urls
for state in states:
    page_url = state.get_attribute("href")
    page_urls.append(page_url)
# Count of pages
page_count = len(page_urls)
print(page_count)
count = 1

title = driver.find_element_by_xpath('//div[@class="col"]/h1').text
# File name define
output_file = title + "(" + current_time + ").csv"
print(output_file)

add_csv_head()
for page_url in page_urls:
    try:
        driver.get(page_url)
    except:
        driver.close()
        driver = selenium.webdriver.Chrome()
        driver.get(page_url)
    time.sleep(5)
    # Title scrape
    try:
        title = driver.find_element_by_xpath('//div[@class="card-header tw-rounded-tl-none tw-border-0 tw-pb-0 tw-bg-transparent"]/h1').text
    except:
        title = 'N/A'
    # Description scrape
    description = ''
    try:
        descriptions1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/div/p')
        for description1 in descriptions1:
            description += "<p>" + description1.text + "</p> "
    except:
        print('No description1')
    try:
        descriptions2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/ul/li')
        description += "<ul>"
        for description2 in descriptions2:
            description += "<li>" + description2.text + "</li>"
        description += "</ul> "
    except:
        print('No description2')
    try:
        descriptions3 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/dl/dt')
        descriptions4 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/dl/dd')
        length = len(descriptions3)
        i = 0
        while i < length:
            description += "<dt>" + descriptions3[i].text + "</dt><dd>" + descriptions4[i].text + "</dd> "
            i += 1
    except:
        print('No description3')
    
    try:
        descriptions5 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/div[@class="my-3"]/h3')
        description += "<h3>" + descriptions5[0].text + "</h3> "
        descriptions6 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/div[@class="my-3"]/dl/dt')
        descriptions7 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/div[@class="my-3"]/dl/dd')
        ll = len(descriptions6)
        i = 0
        while i < 6:
            description += "<dt>" + descriptions6[i].text + "</dt><dd>" + descriptions7[i].text + "</dd> "
            i += 1
        description += "<h3>" + descriptions5[1].text + "</h3> "
        i = 6
        while i < ll:
            description += "<dt>" + descriptions6[i].text + "</dt><dd>" + descriptions7[i].text + "</dd> "
            i += 1
    except:
        print("No description 5")
    description.replace(',', '.')
    
    navs = driver.find_elements_by_xpath('//ul[@class="nav"]/li[@class="nav-item"]')
    # Details scrape
    navs_length = len(navs)
    print("nav length: " + str(navs_length))
    if navs_length == 6:
        navs[1].click()
        details = ''
        try:
            details1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dt')
            details2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd')
            length = len(details1) - 1
            i = 0
            while i < length:
                details += "<dt>" + details1[i].text + "</dt><dd>" + details2[i].text + "</dd> "
                i += 1
        except:
            print("No details")
            details = 'N/A'

        navs[2].click()
        pakaging = ''
        try:
            pakaging1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dt')
            pakaging2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd')
            length = len(pakaging1)
            i = 0
            while i < length:
                pakaging += "<dt>" + pakaging1[i].text + "</dt><dd>" + pakaging2[i].text + "</dd> "
                i += 1
        except:
            print("No pakaging")
            pakaging = 'N/A'
        navs[3].click()
        modelings = ''
        try:
            modelings1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/h5')
            modelings2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/p[@class="m-0"]')
            modelings3 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/p/small')
            modelings4 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/p')
            i = 0
            length = len(modelings1)
            while i < length:
                modelings += "<h5>" + modelings1[i].text + "</h5> <p>" + modelings2[i].text + "</p> <small>" + modelings3[i].text + "</small> <p>" + modelings4[i+2].text + "</p> "
                i += 1
        except:
            print("No modelings")
            modelings = 'N/A'

        navs[4].click()
        installations = ''
        try:
            installations1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/div[@class="col-12"]/p')
            installations2 = driver.find_elements_by_xpath('//div[@class="tw-w-full tw-flex tw-flex-wrap"]/div/p')
            installations3 = driver.find_elements_by_xpath('//div[@class="tw-flex tw-flex-wrap"]/div/p')
            installations += "<p>" + installations1[0].text + "</p>: "
            for installation2 in installations2:
                installations += "<p>" + installation2.text + "</p>"
            installations += "<p>" + installations1[1].text + "</p>: "
            for installation3 in installations3:
                installations += "<p>" + installation3.text + "</p>"
        except:
            print("No installations")
            installation = 'N/A'
        
        navs[5].click()
        try:
            maintenance = driver.find_element_by_xpath('//div[@class="tab-pane active"]/div/div/div/div/p').text
        except:
            print("No maintenance")
            maintenance = 'N/A'
    else:
        navs[1].click()
        details = ''
        try:
            details1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dt')
            details2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd')
            length = len(details1)
            i = 0
            while i < length:
                details += "<dt>" + details1[i].text + "</dt> <dd>" + details2[i].text + "<>/dd "
                i += 1
        except:
            print("No details")
            details = 'N/A'

        navs[2].click()
        pakaging = ''
        try:
            pakaging1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dt')
            pakaging2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd')
            length = len(pakaging1)
            i = 0
            while i < length:
                pakaging += "<dt>" + pakaging1[i].text + "</dt> <dd>" + pakaging2[i].text + "</dd> "
                i += 1
        except:
            print("No pakaging")
            pakaging = 'N/A'

        navs[3].click()
        modelings = ''
        try:
            modelings1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/h5')
            modelings2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/p[@class="m-0"]')
            modelings3 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/p/small')
            modelings4 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/p')
            i = 0
            length = len(modelings1)
            while i < length:
                modelings += "<h5>" + modelings1[i].text + "</h5> <p>" + modelings2[i].text + "</p> <small>" + modelings3[i].text + "</small> <p>" + modelings4[i+2].text + "</p> "
                i += 1
        except:
            print("No modelings")
            modelings = 'N/A'
        
        navs[4].click()
        
        installations = ''
        try:
            installations1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/div[@class="col-12"]/p')
            installations2 = driver.find_elements_by_xpath('//div[@class="tw-w-full tw-flex tw-flex-wrap"]/div/p')
            installations3 = driver.find_elements_by_xpath('//div[@class="tw-flex tw-flex-wrap"]/div/p')
            installations += "<p>" + installations1[0].text + "</p>: "
            for installation2 in installations2:
                installations += "<p>" + installation2.text + "</p>"
            installations += "<p>" + installations1[1].text + "</p>: "
            for installation3 in installations3:
                installations += "<p>" + installation3.text + "</p>"
        except:
            print("No installations")
        
        maintenance = 'N/A'

    try:
        liElement = driver.find_element_by_xpath('//div[@class="agile__list"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", liElement)
        tiles = driver.find_elements_by_xpath('//div[@class="agile__slides agile__slides--regular"]/div/img')
        tile_len = len(tiles) - 1
        tiles[tile_len].click()
        time.sleep(1)
        tile_image = driver.find_element_by_xpath('//div[@class="tw-relative"]/img').get_attribute("src")
    except:
        print("No tile_image")
        tile_image = 'N/A'

    add_csv_row(title, description, details, pakaging, modelings, installations, maintenance, tile_image)

    print("detail page done")
    print(count)
    count += 1
driver.close()
print("please check file")


