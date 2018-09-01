from django.contrib.contenttypes.fields \
	import GenericForeignKey
from django.db \
	import models

# Create your models here.


class ImagemUsuario(models.Model):

	imagemusuario_padrao = models.ImageField(
			width_field = "imagemusuario_padrao_width",
			height_field = "imagemusuario_padrao_height",
		)

	imagemusuario_padrao_width = models.IntegerField(
			default = 0
		)

	imagemusuario_padrao_height = models.IntegerField(
			default = 0
		)

	imagemusuario_usuario = GenericForeignKey(
			null = True
		)