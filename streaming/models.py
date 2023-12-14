from django.db import models
from django.utils import timezone

categorias = (
    ('AVENTURA', 'Aventura'),
    ('ANIMACAO', 'Animação'),
    ('ACAO', 'Ação'),
    ('COMEDIA', 'Comédia'),
    ('DRAMA', 'Drama'),
    ('SUSPENSE', 'Suspense'),
    ('TERROR', 'Terror'),
    ('HISTORICO', 'Histórico'),
    ('CRIME', 'Crime'),
    ('FINANCAS', 'Finanças'),
    ('MARKETING', 'Marketing'),
    ('DOCUMENTARIO', 'Documentário'),
    ('MUSICAL', 'Musical')
)

class Filmeserie(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumbs')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=categorias)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    

class Episodio(models.Model):
    filme = models.ForeignKey('Filmeserie', related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " | " + self.titulo
     

