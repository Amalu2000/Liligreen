from django import forms
from .models import Review,Products

class Productform(forms.ModelForm):
    class Meta:
        model=Products
        exclude=['us']



class Reviewform(forms.ModelForm):
    class Meta:
        model=Review
        fields=['review','rating']
       