from django import forms
from .models import Listing

INPUT_CLASSES = 'form-control w-75 rounded py-2 px-3 border'

class AddListingForm(forms.ModelForm):
  class Meta:
    model = Listing
    fields = ('title', 'image_url', 'description', 'price', 'category')

    widgets = {
      'title': forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Title'
      }),
      'image_url': forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Image URL'
      }),
      'description': forms.Textarea(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Description'
      }),
      'price': forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Price'
      }),
      'category': forms.Select(attrs={
        'class': INPUT_CLASSES
      })
    }

#In order to remove the fields labels
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name in self.fields:
      self.fields[field_name].label = False