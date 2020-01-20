import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.tecmundo.com.br'

page = requests.get(url)

soup = BS(page.text, 'html.parser')

noticesFromPage = soup.find_all(class_='tec--card__title__link')

dataToSave = []

for notice in noticesFromPage:
    dataToSave.append({
        'titulo': BS.getText(notice).strip(),
        'link': BS.get(notice, 'href')
    })
