from django.contrib.contenttypes.fields \
	import GenericForeignKey
from django.db \
	import models

# Create your models here.

class VozUsuario(models.Model):

	vozusuario_padrao = models.ImageField(
			width_field = imagemusuario_padrao_width,
			height_field = imagemusuario_padrao_height,
		)

	vozusuario_padrao_width = models.IntegerField(
			default = 0
		)

	vozusuario_padrao_height = models.IntegerField(
			default = 0
		)

	imagemusuario_vozusuario = GenericForeignKey(
			null = True
		)