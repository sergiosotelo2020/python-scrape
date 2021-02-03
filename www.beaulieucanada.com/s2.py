import csv
from typing import Collection
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
        writer.writerow(['Title'',sub-title','Description','Details','Brand','Collection','Style Name','Style Number','construction','Material','Backing','Wear Layer Thickness','Total Thickness','Width','Finish','Top' 'Surface','Interlayer','Design','Weight','Modelings','Installations','installation_method','Maintenance','Tile image'])

def add_csv_row(title,sub_title,description,details,brand,collection,style_name,style_number,construction,material,backing,wear_layer_thickness,total_thickness,width,finish,top_surface,interlayer,design,weight,modelings,installations,installation_method,maintenance,tile_image):

    with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([title,sub_title,description,details,brand,collection,style_name,style_number,construction,material,backing,wear_layer_thickness,total_thickness,width,finish,top_surface,interlayer,design,weight,modelings,installations,installation_method,maintenance,tile_image])

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
    try:
        sub_title = driver.find_element_by_xpath('//p/strong').text
    except:
        sub_title = 'N/A'

    try:
        description = driver.find_element_by_xpath('//div[@class="tab-pane active"]/section/div/p').text
    except:
        print('No description')
        description = 'N/A'

    details = ''
    try:
        details_tmp = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/ul/li')
        details += "'"
        for detail_tmp in details_tmp:
            description += detail_tmp.text + "\n"
        details += "'"
    except:
        print('No description2')
        details = 'N/A'
       
    navs = driver.find_elements_by_xpath('//ul[@class="nav"]/li[@class="nav-item"]')
    # Details scrape
    navs_length = len(navs)
    print("nav length: " + str(navs_length))

    nav_check = driver.find_elements_by_xpath('//ul[@class="nav"]/li/a')
    nav_checker = nav_check[3].text

    brand = ''
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
            maintenances = driver.find_element_by_xpath('//div[@class="tab-pane active"]/div/div/div/div/p').text
        except:
            print("No maintenance")
            maintenances = 'N/A'
    elif nav_checker == 'Moldings':
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
        
        maintenances = 'N/A'

    else:
        navs[1].click()
        try:
            details2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd')
            length = len(details2)
            i = 0
            brand = details2[0].text
            collection = details2[1].text
            style_name = details2[2].text
            style_number = details2[3].text
            construction = details2[4].text
            material = details2[5].text
            backing = details2[6].text
            wear_layer_thickness = details2[7].text
            total_thickness = details2[8].text
            width = details[9].text
            finish = details[10].text
            top_surface = details[11].text
            interlayer = details[12].text
            design = details[13].text

        except:
            print("No details")

        navs[2].click()
        try:
            weight = driver.find_element_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd').text
        except:
            print("No weight")
            weight = 'N/A'

        navs[3].click()
        
        installations = ''
        installation_method = ''
        try:
            installations2 = driver.find_elements_by_xpath('//div[@class="tw-w-full tw-flex tw-flex-wrap"]/div/p')
            installations3 = driver.find_elements_by_xpath('//div[@class="tw-flex tw-flex-wrap"]/div/p')
            for installation2 in installations2:
                installations += "<p>" + installation2.text + "</p>"
            installation_method += '"' 
            for installation3 in installations3:
                installation_method += installation3.text + ","
            installation_method += '"'
        except:
            print("No installations")
            installation_method = "N/A"
            installations = "N/A"
        
        navs[4].click()
        try:
            maintenance = driver.find_element_by_xpath('//div[@class="tab-pane active"]/div/div/div/div/p').text
        except:
            print("No maintenance")
        modelings = 'N/A'

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

    add_csv_row(title,sub_title, description, details, brand, collection, style_name, style_number, construction, material, backing, wear_layer_thickness, total_thickness, width, finish, top_surface, interlayer, design, weight, modelings, installations, installation_method, maintenance, tile_image) 

    print("detail page done")
    print(count)
    count += 1
driver.close()
print("please check file")


