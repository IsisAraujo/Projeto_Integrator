from django.urls import include, path, re_path, register_converter

from . import views

app_name = 'seriados'

urlpatterns = [
    path('series/', views.series_lista, name='series_lista'),

    path('episodio/<int:pk>/', views.episodio_detalhes, name='episodio_detalhes'),

    path('episodios/nota/<str:nota>/',
         views.episodio_lista_nota, name='episodio_lista_nota'),
]
