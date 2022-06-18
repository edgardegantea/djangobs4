import requests
from bs4 import BeautifulSoup

# extraer datos de una pagina

website = 'https://www.milenio.com'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())


#noticia 01
box = soup.find('article', class_='oo-flat-background-base-large')
title = box.find('a').get_text()
print(title)
transcript = box.find('li', class_='oo-flat-background-base-large__abstract').get_text(strip=True,separator=' ')
print(transcript)



#noticia 02
box = soup.find('article', class_='sn-base-base-noheading')
title = box.find('a').get_text()
print(title)
transcript = box.find('li', class_='sn-base-base-noheading__abstract').get_text(strip=True,separator=' ')
print(transcript)



