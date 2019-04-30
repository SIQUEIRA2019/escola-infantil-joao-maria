from django.db import models

class alunos(models.Model):
	nomealunos = models.CharField("Nome", max_length=50)
	siglaalunos = models.CharField("Sigla", max_length=5)
	etiquetaalunos = models.SlugField("Etiqueta", max_length=50)
		
	def __str__(self):
		return self.nome

# Create your models here.
