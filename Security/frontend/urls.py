
from . import views

from django.conf.urls \
    import url
from django.contrib \
    import admin
from django.urls \
    import path
from antifraude.views \
    import UsuarioCreateView, AntifraudeValidadorCreateView
from django.views.generic \
    import TemplateView
from watson_developer_cloud \
	import DiscoveryV1

app_name = "frontend"

admin.autodiscover()

urlpatterns = [    
    path('', AntifraudeValidadorCreateView.as_view(), 
    	name="AntiFraudeCreateView"),
    path('cadastro/reconhecimento-facial/', 
    	UsuarioCreateView.as_view(), 
    	name="FaceCreateView"),
]
    