from .models \
    import ImagemUsuario
from django \
    import forms
from django.core.exceptions \
    import ValidationError
from django.forms \
    import DateTimeField
from django.utils.html \
    import strip_tags

class FormCreateFoto(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(FormCreateFoto, self)\
            .__init__(*args, **kwargs)

    imagemusuario_padrao = forms.ImageField( 
        required=True,
        label="Foto do Usuário."
    ) 

    class Meta:

        model = ImagemUsuario

        fields = [
            'imagemusuario_padrao',
        ]