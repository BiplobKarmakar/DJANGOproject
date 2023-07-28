
from django import forms
from . models import Listings

# create a ModelForm


class ListingForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Listings
        fields = "__all__"
