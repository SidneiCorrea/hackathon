
from . import views

#DJANGO
from django.conf.urls \
    import url
from django.contrib \
    import admin
from django.urls \
    import path
from django.views.generic \
    import TemplateView

app_name = "frontend"

admin.autodiscover()

urlpatterns = [    
    path('', TemplateView.as_view(
        template_name="frontend/index.html")),

]
    