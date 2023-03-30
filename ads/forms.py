from django import forms
from ads.models import Ad

class CreateForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'text','price']  # Picture is manual

