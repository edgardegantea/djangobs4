import requests
from bs4 import BeautifulSoup

#extraer datos de una pagina
website = 'https://elpais.com/mexico/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())



#noticia 01
box = soup.find('section', class_='_g _g-md _g-o b b-d b--o')
title = box.find('a').get_text()
print(title)
#scrip borra espacios en blanco al inicio y al final de una cadena de texto
transcript = box.find('p', class_='c_d').get_text(strip=True,separator=' ')
print(transcript)



#noticia 02

box = soup.find('div', class_='b-d_b b_op _g _g-md b_op-1-2')
title = box.find('h2', class_='c_t').get_text(strip=False, separator=' ')
print(title)
transcript = box.find('p', class_='c_d').get_text(strip=False, separator=' ')
print(transcript)

