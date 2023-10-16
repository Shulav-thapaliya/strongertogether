from atexit import register
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('test/',views.form,name = 'test'),
   path('story/',views.story,name = 'story'),
   path('newform/',views.comform,name = 'newform'),
   path('aboutus/',views.about,name = 'aboutus'),
   path('comment/<str:pk>/',views.com,name = 'comment'),
   

   
   
]