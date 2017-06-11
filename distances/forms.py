from django import forms

AREAS_CHOICES = (
    ('blackrock', 'Blackrock'),
    ('booterstown', 'Booterstown'),
    ('dun-laoghaire', 'Dun-Laoghaire'),
    ('monkstown', 'Monkstown'),
    ('sandymount', 'Sandymount'),
)

PRICE_CHOICES = [(x, x) for x in range(1000, 3000, 100)]

class SearchCriteriaForm(forms.Form):
    #max_price = forms.IntegerField(label="Maximum Price", initial=1850)
    areas = forms.MultipleChoiceField(
        label="Select all areas for the house",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=AREAS_CHOICES,
    )
    max_price = forms.ChoiceField(
        required=True,
        label="Choose the maximum price",
        choices=PRICE_CHOICES
    )