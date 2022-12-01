from atexit import register
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home),
   path('test/',views.form,name = 'res'),
   path('story/',views.story,name = 'str'),
   path('newform/',views.comform,name = 'formpage'),


   
   
]