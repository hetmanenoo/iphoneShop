from django import forms

CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CHOICES, coerce=int, label="К-ст")
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartUpdateProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CHOICES, coerce=int, label="К-ст")
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
