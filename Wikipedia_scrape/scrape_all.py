import requests
from datetime import datetime
from bs4 import BeautifulSoup
import re
import hashlib
import time

from requests.api import request
#Get page url
#https://en.wikipedia.org/wiki/International_Association_for_Cryptologic_Research#International_Cryptology_Conference
#https://en.wikipedia.org/wiki/Cryptanalysis
url = input("Enter the URL: ")
page = requests.get(url)

state = page.status_code
print(state)
# content = page.content
# print(content)
#Parse page by using Beautifulsoup
results = ""
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
#Get local time
now = datetime.now()
date_time = now.strftime("%m%d%Y_%H%M%S")
print("date and time:",date_time)
#Find title and contents
sentences = soup.find(class_='hatnote')
if (sentences):
    sentence = sentences.getText()
else:
    sentence = ""
contents = soup.find(class_='mw-parser-output')
texts = contents.find_all('p')
for text in texts:
    # print(text.getText())
    results += text.getText()

# content = soup.find_all()
# print(sentence)
result = sentence + results
result = result.replace("\n", "")
result = result.replace("]", "")
result = result.replace("[", "")
# result = result.replace(":", "")

# print(result)
results = re.split('\.\s+|\.|\:', result)
#Write contents into file
filename = date_time + ".txt"
f= open(filename,"w+", encoding='utf-8')
f.write("Main Article \n\n")
for result in results:
    # f.write(result + ".\n\n")
    if (result.find(',') != -1): 
        tt = re.split(', ', result)

        for t in tt:
            f.write(t + ",\n\n")
            # hash_object = hashlib.sha384(t.encode())
            # hex_dig = hash_object.hexdigest()
            # f.write(hex_dig + "\n\n")
    else:
        f.write(result + ".\n\n")
        # hash_object = hashlib.sha384(result.encode())
        # hex_dig = hash_object.hexdigest()
        # f.write(hex_dig + "\n\n")
lists = contents.find_all('ul')
for ul in lists:
    for li in ul.find_all('li'):
        result = li.getText()
        if (result.find(',') != -1):
            tt = re.split(', ', result)

            for t in tt:
                f.write(t + ",\n\n")
                # hash_object = hashlib.sha384(t.encode())
                # hex_dig = hash_object.hexdigest()
                # f.write(hex_dig + "\n\n")
        else:
            f.write(result + ".\n\n")
            # hash_object = hashlib.sha384(result.encode())
            # hex_dig = hash_object.hexdigest()
            # f.write(hex_dig + "\n\n")
history_url = "https://en.wikipedia.org/w/index.php?title=Cryptanalysis&offset=&limit=500&action=history"
print(history_url)
history_page = requests.get(history_url)
history_soup = BeautifulSoup(history_page.text, 'html.parser')
revision_urls = history_soup.find_all(class_='mw-changeslist-date')
links = []
for revision_url in revision_urls:
    revision_url = "https://en.wikipedia.org" + revision_url.get('href')
    links.append(revision_url)
# print(links)
x = len(links)
print(x)
i = 1
for link in links:
    results = ""
    revision_page = requests.get(link)
    time.sleep(2)
    revision_soup = BeautifulSoup(revision_page.text, 'html.parser')
    sentences = revision_soup.find(class_='hatnote')
    if (sentences):
        sentence = sentences.getText()
    else:
        sentence = ""
    contents = soup.find(class_='mw-parser-output')
    texts = contents.find_all('p')
    for text in texts:
        # print(text.getText())
        results += text.getText()

    # content = soup.find_all()

    result = sentence + results
    result = result.replace("\n", "")
    result = result.replace("]", "")
    result = result.replace("[", "")
    # result = result.replace(":", "")

    # print(result)
    results = re.split('\.\s+|\.|\:', result)
    time.sleep(2)
    f.write("-----------------------------------------------------------\n")
    date = revision_soup.find(id='mw-revision-date')
    date = date.getText()
    f.write(date + "(" + link + ")" + "\n")
    f.write("------------------------------------------------------------\n\n")
    for result in results:
        # f.write(result + ".\n\n")
        if (result.find(',') != -1): 
            tt = re.split(', ', result)

            for t in tt:
                f.write(t + "\n\n")
                # hash_object = hashlib.sha384(t.encode())
                # hex_dig = hash_object.hexdigest()
                # f.write(hex_dig + "\n\n")
        else:
            f.write(result + ".\n\n")
            # hash_object = hashlib.sha384(result.encode())
            # hex_dig = hash_object.hexdigest()
            # f.write(hex_dig + "\n\n")
    lists = contents.find_all('ul')
    for ul in lists:
        for li in ul.find_all('li'):
            result = li.getText()
            if (result.find(',') != -1):
                tt = re.split(', ', result)

                for t in tt:
                    f.write(t + "\n\n")
                    # hash_object = hashlib.sha384(t.encode())
                    # hex_dig = hash_object.hexdigest()
                    # f.write(hex_dig + "\n\n")
            else:
                f.write(result + ".\n\n")
                # hash_object = hashlib.sha384(result.encode())
                # hex_dig = hash_object.hexdigest()
                # f.write(hex_dig + "\n\n")
    time.sleep(3)

    print('done' + str(i))
    i += 1


f.close() 
print('done!!!')





