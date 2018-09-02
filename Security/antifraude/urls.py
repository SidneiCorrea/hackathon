
from . import views

from django.conf.urls \
    import url
from django.contrib \
    import admin
from django.urls \
    import path
from .views \
    import UsuarioCreateView

app_name = "antifraude"

admin.autodiscover()

urlpatterns = [    
    path('ajax/grava', 
    	UsuarioCreateView.get_ajax, 
    	name="AjaxGravaAudio"),
	path('ajax/salva', 
    	UsuarioCreateView.set_ajax, 
    	name="AjaxSalvaAudio"),
]
    