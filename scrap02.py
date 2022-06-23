import requests
from bs4 import BeautifulSoup

# extraer datos de una pagina
website = 'https://www.elsoldemexico.com.mx/mexico/sociedad/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# Entrar a seccion que contiene bloques
layout = soup.find('div', class_="container")
# print(layout)

# Entrar a seccion que contiene articulos y mostrar su cantidad
blocks = layout.find_all(class_='stories-list sports-description', recursive=True)
print(len(blocks))

for block in blocks:
    for href in block.find('a', href=True):
        print('Titulo: ' + href.get_text())

        Noticia = block.find('p', class_='leadtext').get_text()
        print('Noticia: ' + Noticia)
        print()