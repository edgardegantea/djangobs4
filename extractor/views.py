from django.shortcuts import render
from .models import Contacto
from bs4 import BeautifulSoup
import requests

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    model = Contacto
    template_name = 'index.html'

    def extraer(self):
        url = "https://www.tutorialspoint.com/index.htm"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        print(soup.title)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Extractor de noticias'
        context['req'] = requests.get("https://www.tutorialspoint.com/index.htm")

        return context
