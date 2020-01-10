from django import forms

class SearchInput(forms.Form):
    search_input = forms.CharField(max_length=30)