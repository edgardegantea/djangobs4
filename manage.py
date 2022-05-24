#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#!CODIGO NUEVO DE BEAUTIFUL SOUP
import requests
from bs4 import BeautifulSoup

url= "https://www.elsoldemexico.com.mx/metropoli/cdmx/mueren-tres-personas-por-balacera-en-colonia-la-roma-8324832.html"

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.59",
    "Agent-Languaje": "es",
}
r=requests.get(url,headers=headers)

soup = BeautifulSoup(r.text,"lxml")
#print(soup.prettify())

name = soup.select_one(selector=".title").getText()
name=name.strip()
print(name)

contenido=soup.select_one(selector="#content-body-225-8324832").getText()
contenido=contenido.strip()
print(contenido)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobs.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
