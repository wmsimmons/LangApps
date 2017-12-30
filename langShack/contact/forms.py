from django import forms


class contactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'style': 'margin-left: 20px'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'style': 'margin-left: 21px'}))
    message = forms.CharField(widget=forms.Textarea)
