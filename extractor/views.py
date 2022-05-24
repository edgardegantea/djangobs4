from django.shortcuts import render
from .models import Contacto

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    model = Contacto
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Extractor de noticias'
        return context
