import requests
from datetime import datetime
from bs4 import BeautifulSoup
import re
#Get page url
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

content = soup.find_all()
# print(sentence)
result = sentence + results
result = result.replace("\n", "")
result = result.replace("]", "")
result = result.replace("[", "")
# print(result)
results = re.split('\.\s+|\.', result)
#Write contents into file
filename = date_time + ".txt"
f= open(filename,"w+", encoding='utf-8')
for result in results:
    f.write(result + ".\n\n")
    if (result.find(',') != -1): 
        tt = re.split(', ', result)

        for t in tt:
                f.write(t + "\n\n")
                
f.close() 
print('done!!!')





