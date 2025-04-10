from django import forms
from .models import Listing, Category, Bid

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

#In order to remove the fields labels in the UI
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name in self.fields:
      self.fields[field_name].label = False

  
class CategoryFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="All Categories",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control w-75 rounded py-2 px-3 border'})
    )

class BidForm(forms.Form):
    class Meta:
      model = Bid
      fields = ('amount')

      widgets = {
        'title': forms.TextInput(attrs={
          'class': INPUT_CLASSES,
          'placeholder': 'Bid Amount'
        })
      }

  # amount = forms.DecimalField(label="Bid Amount")
