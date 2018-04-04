# Developer name: Kaunda Michael Kabwe
# Project: Football site for Zambian first division league
# Date: 04/04/2018

from django import forms

# This is the forms script that will contain form classes
# It is very similar to the models class. It is not 
# created on project creation. The developer created this 
# file. Testing how forms work

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    