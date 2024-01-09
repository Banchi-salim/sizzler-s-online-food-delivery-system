from django import forms

class OrderForm(forms.Form):
    meal = forms.ChoiceField(
        choices=[
            ('jollof', 'Jollof Rice'),
        ]
    )
    drink = forms.ChoiceField(
        choices=[
            ('coke', 'Coke'),
        ]
    )
    toppings = forms.MultipleChoiceField(
        choices=[
            ('meat', 'Extra Meat'),
            ('chicken', 'Chicken'),
            ('plantain', 'Plantain'),
        ],
        widget=forms.CheckboxSelectMultiple
    )
    side = forms.ChoiceField(
        choices=[
            ('c', 'C Clow'),
            ('coslow', 'Coslow'),
        ]
    )
    sauce = forms.ChoiceField(
        choices=[
            ('coslow', 'Coslow'),
            ('coslow', 'Coslow'),
        ]
    )
    extras = forms.ChoiceField(
        choices=[
            ('', 'None'),
            ('egg', 'Egg'),
        ]
    )
