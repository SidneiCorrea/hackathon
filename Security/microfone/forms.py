from .models \
    import VozUsuario
from django \
    import forms
from django.core.exceptions \
    import ValidationError
from django.forms \
    import DateTimeField
from django.utils.html \
    import strip_tags

class FormCreateAudio(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(FormCreateAudio, self)\
            .__init__(*args, **kwargs)

    vozusuario_padrao = forms.FileField( 
        required=True,
        label="Voz do Usuário."
    ) 

    class Meta:

        model = VozUsuario

        fields = [
            'vozusuario_padrao',
        ]