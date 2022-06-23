from django.contrib import admin
from django.urls import path

from extractor.views import IndexView, Websites, Website1, Website2, Website3, Website4, Politics01, Politics02, \
    Politics03, \
    Sports01, Sports02, Sports03, Culture01, Culture02, Culture03, Prueba
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('websites/', Websites.as_view(), name='websites'),
    path('website1/', Website1.as_view(), name='el_sol_de_mexico'),
    path('website2/', Website2.as_view(), name='milenio'),
    path('website3/', Website3.as_view(), name='el_pais'),
    path('website4/', Website4.as_view(), name='el_financiero'),
    path('Politics01/', Politics01.as_view(), name='Politica'),
    path('Politics02/', Politics02.as_view(), name='Politica'),
    path('Politics03/', Politics03.as_view(), name='Politica'),
    path('Culture01/', Culture01.as_view(), name='Cultura'),
    path('Culture02/', Culture02.as_view(), name='Cultura'),
    path('Culture03/', Culture03.as_view(), name='Cultura'),
    path('Culture04/', Culture03.as_view(), name='Cultura'),
    path('Sports01/', Sports01.as_view(), name='Cultura'),
    path('Sports02/', Sports02.as_view(), name='Cultura'),
    path('Sports03/', Sports03.as_view(), name='Cultura'),
    path('Sports04/', Sports03.as_view(), name='Cultura'),
    path('Prueba/', Prueba.as_view(), name='prueba'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


