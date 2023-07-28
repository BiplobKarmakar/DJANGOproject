from django import forms
from . models import Realtor


class RealtorForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Realtor
        fields = "__all__"
