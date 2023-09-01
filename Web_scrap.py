import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.imdb.com/title/tt9179430/reviews/')
 
# Parsing the HTML
soup = BeautifulSoup(r.text, 'html.parser')
 
print(soup.findAll('div',attrs={"class":"lister-item-content"}))
# content = s.find_all('p')
# print(soup.find_all('div',class_='title'))
# print(soup.prettify())