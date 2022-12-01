from pyexpat import model


from django import forms


from django.forms import ModelForm,widgets
from .models import share ,comment 

class Phase1form(ModelForm):
    class Meta:
        model = share
        fields = '__all__'
        
class commentform(ModelForm):
    class Meta:
        model = comment 
        fields = '__all__'
        