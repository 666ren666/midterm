from django.forms import ModelForm
from .models import Car,Treatment

class CarForm(ModelForm):
    class Meta:
        model=Car
        fields='__all__'

        

class TreatmentForm(ModelForm):
    class Meta:
        model=Treatment
        fields='__all__'


# from django import forms
# from django.core.exceptions import ValidationError

# class ContactForm(forms.Form):
#     # Everything as before.
#     ...

#     def clean_recipients(self):
#         data = self.cleaned_data['recipients']
#         if "fred@example.com" not in data:
#             raise ValidationError("You have forgotten about Fred!")

