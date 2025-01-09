from django import forms

from .models import Listing



class AddListingForm(forms.ModelForm):
  class Meta:
    model = Listing
    fields = ('title', 'description', 'price', 'image_url', 'category',)

    widgets = {
      'title': forms.TextInput(),
      'description': forms.Textarea(),
      'price': forms.NumberInput(),
      'image_url': forms.TextInput(),
      'category': forms.Select()
    }