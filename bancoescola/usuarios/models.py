from django.db import models

class usuarios(models.Model):
	nome = models.CharField("Nome", max_length=50)
	sigla = models.CharField("Sigla", max_length=5)
	etiqueta = models.SlugField("Etiqueta", max_length=50)
	descricao = models.CharField("Descricao", max_length=60)
	
	def __str__(self):
		return self.nome
# Create your models here.
