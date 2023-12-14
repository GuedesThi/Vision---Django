from django.urls import path
from streaming.views import Begin, CriarConta, Login, IndexFilmes, DetalhesFilme

app_name = 'streaming'

urlpatterns = [
    path('', Begin.as_view(), name='index'),
    path('registrar/', CriarConta.as_view(), name='registrar'),
    path('login/', Login.as_view(), name='login'),
    path('inicio/', IndexFilmes.as_view(), name='inicio'),
    path('inicio/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),
]