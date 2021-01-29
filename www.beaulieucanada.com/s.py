import csv
from selenium import webdriver

import selenium.webdriver
from datetime import datetime
import selenium.webdriver
import time

now = datetime.now()
current_time = now.strftime("%m%d%y_%H%M%S")
print(now)
output_file = "products_detail_(" + current_time + ").csv"
print(output_file)


def add_csv_head():
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Description', 'Details', 'Pakaging', 'Modelings', 'Installations', 'Maintenance', 'Picture'])

def add_csv_row(title, description, details, pakaging, modelings, installations, maintenance, picture):

    with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([title, description, details, pakaging, modelings, installations, maintenance, picture])

driver = selenium.webdriver.Chrome()

base_url = 'https://www.beaulieucanada.com/en/retail/flooring/engineeredluxuryvinyl'

driver.get(base_url)
time.sleep(10)
driver.implicitly_wait(10)

liElement = driver.find_element_by_xpath('//footer')
driver.execute_script("arguments[0].scrollIntoView(true);", liElement)

states = driver.find_elements_by_xpath('//div[@class="card tw-w-full px-0 pt-0 pb-2 mb-3 tw-rounded product"]/a')
states_len = len(states)
# print(states)
page_urls = []

for state in states:
    page_url = state.get_attribute("href")
    page_urls.append(page_url)

page_count = len(page_urls)
print(page_count)
count = 1
add_csv_head()
for page_url in page_urls:
    driver.get(page_url)
    time.sleep(5)
    try:
        title = driver.find_element_by_xpath('//div[@class="card-header tw-rounded-tl-none tw-border-0 tw-pb-0 tw-bg-transparent"]/h1').text
    except:
        title = 'N/A'
    description = ''
    try:
        descriptions1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/div/p')
        for description1 in descriptions1:
            description += description1.text + " "
    except:
        print('No description1')
    try:
        descriptions2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/ul/li')
        for description2 in descriptions2:
            description += "~" + description2.text + " "
    except:
        print('No description2')
    try:
        descriptions3 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/dl/dt')
        descriptions4 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/dl/dd')
        length = len(descriptions3)
        i = 0
        while i < length:
            description += "~" + descriptions3[i].text + ":" + descriptions4[i].text + " "
            i += 1
    except:
        print('No description3')
    
    try:
        descriptions5 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/div[@class="my-3"]/h3')
        description += "1)" + descriptions5[0].text + ": "
        descriptions6 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/div[@class="my-3"]/dl/dt')
        descriptions7 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/section/div[@class="my-3"]/dl/dd')
        i = 0
        while i < 6:
            description += "~" + descriptions6[i].text + ":" + descriptions7[i].text + " "
            i += 1
        description += "2)" + descriptions5[1].text + ": "
        i = 6
        while i < 11:
            description += "~" + descriptions6[i].text + ":" + descriptions7[i].text + " "
            i += 1
    except:
        print("No description 5")
    description.replace(',', '.')
    
    navs = driver.find_elements_by_xpath('//ul[@class="nav"]/li[@class="nav-item"]')

    navs_length = len(navs)
    print("nav length: " + str(navs_length))
    if navs_length == 6:
        navs[1].click()
        details = ''
        try:
            details1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dt')
            details2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd')
            length = len(details1)
            i = 0
            while i < length:
                details += "~" + details1[i].text + ":" + details2[i].text + " "
                i += 1
        except:
            print("No details")

        navs[2].click()
        pakaging = ''
        try:
            pakaging1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dt')
            pakaging2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd')
            length = len(pakaging1)
            i = 0
            while i < length:
                pakaging += "~" + pakaging1[i].text + ":" + pakaging2[i].text + " "
                i += 1
        except:
            print("No pakaging")
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
                modelings += "~" + modelings1[i].text + ": " + modelings2[i].text + " " + modelings3[i].text + " " + modelings4[i+2].text + " "
                i += 1
        except:
            print("No modelings")

        navs[4].click()
        installations = ''
        try:
            installations1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/div[@class="col-12"]/p')
            installations2 = driver.find_elements_by_xpath('//div[@class="tw-w-full tw-flex tw-flex-wrap"]/div/p')
            installations3 = driver.find_elements_by_xpath('//div[@class="tw-flex tw-flex-wrap"]/div/p')
            installations += "-" + installations1[0].text + ": "
            for installation2 in installations2:
                installations += installation2.text + "|"
            installations += "-" + installations1[1].text + ": "
            for installation3 in installations3:
                installations += installation3.text + "|"
        except:
            print("No installations")
        
        navs[5].click()
        try:
            maintenance = driver.find_element_by_xpath('//div[@class="tab-pane active"]/div/div/div/div/p').text
        except:
            print("No maintenance")
    else:
        navs[1].click()
        details = ''
        try:
            details1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dt')
            details2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd')
            length = len(details1)
            i = 0
            while i < length:
                details += "~" + details1[i].text + ":" + details2[i].text + " "
                i += 1
        except:
            print("No details")

        navs[2].click()
        pakaging = ''
        try:
            pakaging1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dt')
            pakaging2 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/dl/dd')
            length = len(pakaging1)
            i = 0
            while i < length:
                pakaging += "~" + pakaging1[i].text + ":" + pakaging2[i].text + " "
                i += 1
        except:
            print("No pakaging")
        navs[3].click()
        
        installations = ''
        try:
            installations1 = driver.find_elements_by_xpath('//div[@class="tab-pane active"]/div/div/div/div[@class="col-12"]/p')
            installations2 = driver.find_elements_by_xpath('//div[@class="tw-w-full tw-flex tw-flex-wrap"]/div/p')
            installations3 = driver.find_elements_by_xpath('//div[@class="tw-flex tw-flex-wrap"]/div/p')
            installations += "-" + installations1[0].text + ": "
            for installation2 in installations2:
                installations += installation2.text + "|"
            installations += "-" + installations1[1].text + ": "
            for installation3 in installations3:
                installations += installation3.text + "|"
        except:
            print("No installations")
        
        navs[4].click()
        try:
            maintenance = driver.find_element_by_xpath('//div[@class="tab-pane active"]/div/div/div/div/p').text
        except:
            print("No maintenance")
        modelings = 'N/A'


    try:
        picture = driver.find_element_by_xpath('//div[@class="tw-relative"]/img').get_attribute("src")
    except:
        print('No picture')

    add_csv_row(title, description, details, pakaging, modelings, installations, maintenance, picture)

    print("detail page done")
    print(count)
    count += 1
driver.close()
print("please check file")


