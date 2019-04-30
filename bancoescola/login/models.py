from django.db import models

class login(models.Model):
	nomelogin = models.CharField("Nome", max_length=50)
	siglalogin= models.CharField("Sigla", max_length=5)
	senhalogin = models.SlugField("Etiqueta", max_length=50)
		
	def __str__(self):
		return self.nome
# Create your models here.
