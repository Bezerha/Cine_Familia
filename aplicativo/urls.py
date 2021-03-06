from django.conf.urls.static import static
from aplicativo.views import index, index_auth, filmes, sessoes, assentos, logar, deslogar, cadastro, administrador, indisponivel
from django.urls import path
from GerenciaCinema import settings

app_name = 'aplicativo'

urlpatterns = [
    path('', index),
    path('indisponivel', indisponivel, name='indisponivel'),
    path('index_auth', index_auth, name='index_auth'),
    path('filmes', filmes, name='filmes'),
    path('sessoes', sessoes, name='sessoes'),
    path('assentos', assentos, name='assentos'),
    path('logar', logar, name='logar'),
    path('deslogar', deslogar, name='deslogar'),
    path('cadastro', cadastro, name='cadastro'),
    path('administrador', administrador, name='administrador'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)