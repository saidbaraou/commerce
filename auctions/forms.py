from django import forms
from django.core.exceptions import ValidationError
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

class BidForm(forms.ModelForm):

    class Meta:
      model = Bid
      fields = ('bid_amount',)

      widgets = {
      'bid_amount': forms.NumberInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Bid'
      }),
      }
    

    #This method is to retrieve the Listing object from the view and make it available inside the form for validation
    def __init__(self, *args, **kwargs):
      self.listing = kwargs.pop('listing', None)
      super().__init__(*args, **kwargs)    
      # self.fields['bid_amount']

    #This method is to check the user's input for the bid_amount field and make sure it meets the business rules -here, that's bigger than current_highest_price- before it's saved to the db
    def clean_bid_amount(self):
      bid_amount = self.cleaned_data.get("bid_amount")

      if self.listing.current_bid:
            # If a bid exists, the minimum price is the current highest bid
            min_price = self.listing.current_bid
            
            if bid_amount <= min_price:
                raise ValidationError(
                    f"Your bid of ${bid_amount} must be greater than the current highest bid of ${min_price}."
                )
      else:
            # If no bid exists, the minimum price is the starting price
            min_price = self.listing.price

            if bid_amount < min_price:
                raise ValidationError(
                    f"Your bid of ${bid_amount} must be at least as large as the initial price of ${min_price}."
                )
      return bid_amount