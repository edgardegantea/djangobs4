from django.shortcuts import render
from .models import Contacto
from bs4 import BeautifulSoup
import requests

# Create your views here.
from django.views.generic import TemplateView

# extraer datos de una pagina
website = 'https://elpais.com/mexico/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')


# print(soup.prettify())


class IndexView(TemplateView):
    model = Contacto
    website = 'https://elpais.com/mexico/'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('section', class_='_g _g-md _g-o b b-d b--o')
    title = box.find('a').get_text()
    # scrip borra espacios en blanco al inicio y al final de una cadena de texto
    transcript = box.find('p', class_='c_d').get_text(strip=True, separator=' ')

    template_name = 'index.html'

    def get_context_data(self, t01=title, t02=transcript, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Extractor de noticias'
        # context['data'] = soup
        context['data2'] = t01
        context['data3'] = t02
        return context


class Websites(TemplateView):
    template_name = 'websites.html'


class Website1(TemplateView):
    template_name = 'website1.html'
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
    # print(len(blocks))

    for block in blocks:
        for href in block.find('a', href=True):
            # print('Titulo: ' + href.get_text())

            Noticia = block.find('p', class_='leadtext').get_text()
            # print('Noticia: ' + Noticia)
            # print()

            def get_context_data(self,t01=,t02=Noticia, **kwargs):
                context = super(IndexView, self).get_context_data(**kwargs)
                context['title'] = 'Extractor de noticias'
                #context['data2'] = t01
                context['data3'] = t02
                return context


class Website2(TemplateView):
    template_name = 'website2.html'


class Website3(TemplateView):
    template_name = 'website3.html'


class Website4(TemplateView):
    template_name = 'website4.html'


class Politics01(TemplateView):
    template_name = 'politics01.html'


class Sports01(TemplateView):
    template_name = 'sports01.html'


class Culture01(TemplateView):
    template_name = 'culture01.html'


class Politics02(TemplateView):
    template_name = 'politics02.html'


class Sports02(TemplateView):
    template_name = 'sports02.html'


class Culture02(TemplateView):
    template_name = 'culture02.html'


class Politics03(TemplateView):
    template_name = 'politics03.html'


class Sports03(TemplateView):
    template_name = 'sports03.html'


class Culture03(TemplateView):
    template_name = 'culture03.html'


class Prueba(TemplateView):
    template_name = 'prueba.html'
