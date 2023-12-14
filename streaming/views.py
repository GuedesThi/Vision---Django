from django.shortcuts import render
from .models import Filmeserie
from django.views.generic import TemplateView, ListView, DetailView


# def begin(request):
#     return render(request, 'index.html')
class Begin(TemplateView):
    template_name = 'index.html'


# def criar_conta(request):
#     return render(request, 'criar_conta.html')
class CriarConta(TemplateView):
    template_name = 'criar_conta.html'

# def login(request):
#     return render(request, 'login.html')
class Login(TemplateView):
    template_name = 'login.html'


# def indexConta(request):
#      filmes_e_series = {}
#      filmes = list(Filme.objects.all())
#      series = list(Serie.objects.all())
#      filmes_e_series['lista_fs'] = filmes + series 
#      return render(request, 'index_conta.html', context=filmes_e_series)
class IndexFilmes(ListView):
    template_name = 'index_conta.html'
    model = Filmeserie
    
    
class DetalhesFilme(DetailView):
    template_name = 'detalhes.html'
    model = Filmeserie