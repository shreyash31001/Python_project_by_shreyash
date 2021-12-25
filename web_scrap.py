import requests
from bs4 import BeautifulSoup
url = "https://www.udemy.com"
#Step 1 Get the Html
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
#Step 2 Parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)
#Step 3 Html tree traversal
title = soup.title
# print(title)
# paras = soup.findAll('p')
# print(paras)
# print(soup.find('div'))
# print(soup.find('div')['class'])

#Finding all the elements with following class
# print(soup.find_all("div",class_="udlite-container"))

#Getting all the texts from the tags/soup
# print(soup.find('div').get_text())

#Get all the links on the page:
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if (link != '#'):
        link = "https://www.udemy.com" + link.get('href')
        all_links.add(link)
        # print(link)
    # print(link.get('href'))
# print(anchors)

jssidenavpopulartopics = soup.find(id="8154")
print(jssidenavpopulartopics)