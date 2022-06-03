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


class Websites(TemplateView):
    template_name = 'websites.html'


class Website1(TemplateView):
    template_name = 'website1.html'


class Website2(TemplateView):
    template_name = 'website2.html'


class Website3(TemplateView):
    template_name = 'website3.html'


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







