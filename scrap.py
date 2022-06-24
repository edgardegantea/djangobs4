import requests
from bs4 import BeautifulSoup

# extraer datos de una pagina
website = 'https://elpais.com/mexico/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# Entrar a seccion que contiene bloques
layout = soup.find('div', class_="")
# print(layout)

# Entrar a seccion que contiene articulos y mostrar su cantidad
blocks = layout.find_all(class_='', recursive=True)
print(len(blocks))

for block in blocks:
    for href in block.find('a', href=True):
        print('Titulo: ' + href.get_text())

        Noticia = block.find('p', class_='c_d').get_text()
        print('Noticia: ' + Noticia)

        print()
