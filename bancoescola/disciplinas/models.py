from django.db import models

class disciplinas(models.Model):
	nomedisciplinas = models.CharField("Nomedisciplinas", max_length=50)
	sigladisciplinas = models.CharField("Sigladisciplinas", max_length=5)
	etiquetadisciplinas = models.SlugField("Etiquetadisciplinas", max_length=50)
	descricaodisciplinas = models.CharField("Descricaodisciplinas", max_length=60)
	
	def __str__(self):
		return self.nome
# Create your models here.
