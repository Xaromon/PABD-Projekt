from django import forms
from .models import Person

class PersonForm (forms.ModelForm):
    class Meta:
        model = Person
        fields= [
        "personal_number",
        "first_name",
        "last_name",
        "adress"

        ]
