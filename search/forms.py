from django import forms
from .models import People


class DateInput(forms.DateInput):
	input_type = 'date'



class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('name','email','dob')
        widgets = {'dob': DateInput()}
    