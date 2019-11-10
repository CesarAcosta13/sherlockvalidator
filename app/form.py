from django import forms

class formVal(forms.Form):
    string = forms.CharField(label='',max_length=100000,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                             'placeholder': 'enter a strint please',
                              'autofocus':'autofocus'}))