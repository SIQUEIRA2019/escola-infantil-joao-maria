from django.db import models

class professores(models.Model):
	nomeprofessores = models.CharField("Nome", max_length=50)
	siglaprofessores = models.CharField("Sigla", max_length=5)
	etiquetaprofessores = models.SlugField("Etiqueta", max_length=50)
		
	def __str__(self):
		return self.nome
# Create your models here.
