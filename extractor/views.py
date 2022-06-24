from django.shortcuts import render
from .models import Contacto
from bs4 import BeautifulSoup
import requests

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'



class Websites(TemplateView):
    template_name = 'websites.html'




class Website1(TemplateView):
    website = 'https://www.elsoldemexico.com.mx/mexico/sociedad/'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    template_name = 'website1.html'

    def get_context_data(self, soup=soup, **kwargs):
        context = super(Website1, self).get_context_data(**kwargs)
        context = {
            # "noticias": soup.find_all(class_='stories-list sports-description')
            "noticias": soup.find_all(class_='stories-list sports-description')
        }
        return context


class Website2(TemplateView):
    template_name = 'website2.html'
    website = 'https://www.milenio.com'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    template_name = 'website2.html'

    def get_context_data(self, soup=soup, **kwargs):
        context = super(Website2, self).get_context_data(**kwargs)
        context = {
            "noticias": soup.find_all(class_='sn-base-base-noheading')
        }
        return context


class Website3(TemplateView):
    template_name = 'website3.html'
    website = 'https://elpais.com/mexico/'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    template_name = 'website3.html'

    def get_context_data(self, soup=soup, **kwargs):
        context = super(Website3, self).get_context_data(**kwargs)
        context = {
            "noticias": soup.find_all(class_='c c-d c--m-n')
        }
        return context


class Website4(TemplateView):
    template_name = 'website4.html'
    website = 'https://www.elfinanciero.com.mx'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    template_name = 'website4.html'

    def get_context_data(self, soup=soup, **kwargs):
        context = super(Website4, self).get_context_data(**kwargs)
        context = {
            "noticias": soup.find_all(class_='container-fluid medium-promo')
        }
        return context


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
