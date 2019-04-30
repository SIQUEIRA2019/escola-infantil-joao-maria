from django.db import models

class cadastro(models.Model):
	nomecadastro = models.CharField("nomecadastro", max_length=50)
	siglacadastro= models.CharField("siglacadastro", max_length=5)
	emailcadastro = models.SlugField("emailcadastro", max_length=50)
		
	def __str__(self):
		return self.nome
# Create your models here.
