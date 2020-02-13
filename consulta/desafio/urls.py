from django.conf.urls import url
from .views import DadosList

urlpatterns = [
   url(r'dados/$', DadosList.as_view()),

]
