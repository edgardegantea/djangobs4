import requests
from bs4 import BeautifulSoup

# extraer datos de una pagina
website = 'https://www.elfinanciero.com.mx'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# Entrar a seccion que contiene bloques
layout = soup.find('div', class_="row advanced-grid")
# print(layout)
# Entrar a seccion que contiene articulos y mostrar su cantidad
blocks = layout.find_all(class_='container-fluid medium-promo', recursive=True)
print(len(blocks))

for block in blocks:
    for href in block.find_all('a', href=True):
        print('Titulo: ' + href.get_text())

        Noticia = block.find('p', class_='secondary-font__SecondaryFontStyles-x1tol1-0 dhTDff description-text').get_text()
        print('Noticia: ' + Noticia)
        print()
