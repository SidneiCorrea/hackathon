
from django.contrib.contenttypes.fields \
    import GenericForeignKey
from django.contrib.contenttypes.models \
    import ContentType
from django.db \
    import models

class GerenciadorImagemUsuario(models.Manager):

    def cria_imagem(self, imagemusuario_padrao):

        complemento = self.create(
            imagemusuario_padrao = imagemusuario_padrao, 
        )
        
        return complemento

class ImagemUsuario(models.Model):

    imagemusuario_padrao = models.ImageField(
            width_field = "imagemusuario_padrao_width",
            height_field = "imagemusuario_padrao_height",
        )

    imagemusuario_padrao_width = models.IntegerField(
            default = 0,
            null = True,
        )

    imagemusuario_padrao_height = models.IntegerField(
            default = 0,
            null = True,
        )

    objects = GerenciadorImagemUsuario()