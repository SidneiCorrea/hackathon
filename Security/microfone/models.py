import os.path

from django.contrib.contenttypes.fields \
    import GenericForeignKey
from django.contrib.contenttypes.models \
    import ContentType
from django.db \
    import models


class GerenciadorVozUsuario(models.Manager):

    def cria_voz(self, vozusuario_padrao):

        complemento = self.create(
            vozusuario_padrao = vozusuario_padrao, 
        )
        
        return complemento

class VozUsuario(models.Model):

    vozusuario_padrao = models.FileField()

    objects = GerenciadorVozUsuario()