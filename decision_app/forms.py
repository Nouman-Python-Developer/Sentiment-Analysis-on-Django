from django import forms

class InputForm(forms.Form):
    input_field = forms.CharField(widget=forms.Textarea)

