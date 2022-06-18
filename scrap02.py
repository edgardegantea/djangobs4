import requests
from bs4 import BeautifulSoup

# extraer datos de una pagina

website = 'https://www.elsoldemexico.com.mx'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content)
print(soup.prettify())


#noticia 01
box = soup.find('h4', class_='tit-top-story')
title = box.find('a').get_text()
print(title)
box = soup.find('section', class_='mexico_justicia')
transcript = box.find('p', class_='extract').get_text(strip=True,separator=' ')
print(transcript)


#noticia02
box = soup.find('h4', class_='title')
title = box.find('a').get_text()
print(title)
box = soup.find('article', class_='col-sm-5 hard-news-1')
transcript = box.find('p', class_='summary').get_text(strip=True,separator=' ')
print(transcript)
