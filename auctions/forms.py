from django import forms

from .models import Listing

INPUT_CLASSES = 'form-control w-60 rounded py-2 px-3 birder'

class AddListingForm(forms.ModelForm):
  class Meta:
    model = Listing
    fields = ('title', 'description', 'price', 'image_url', 'category',)

    widgets = {
      'title': forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Title'
      }),
      'description': forms.Textarea(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Description'
      }),
      'price': forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Price'
      }),
      'image_url': forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Image URL'
      }),
      'category': forms.Select(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Category'
      })
    }