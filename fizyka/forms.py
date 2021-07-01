from django import forms


class Kwanty(forms.Form):   # klasa dla dwóch przyprostokątnych
    atomy = forms.FloatField(
        label="N - ilość atomów",
        min_value=1,
        required=True)
    kwanty = forms.FloatField(
        label="n - ilość kwantów",
        min_value=1,
        required=True)
