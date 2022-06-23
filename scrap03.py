import requests
from bs4 import BeautifulSoup

# extraer datos de una pagina
website = 'https://www.milenio.com'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# Entrar a seccion que contiene bloques
layout = soup.find('section', class_="row")
print(layout)

