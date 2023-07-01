from django import forms

class SubmitForm(forms.Form):
    name = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(
                              attrs={'class': 'form-control mb-3',
                                     'placeholder': 'Name'}))
    email = forms.EmailField(max_length=150,
                             required=True,
                             widget=forms.TextInput(
                              attrs={'class': 'form-control mb-3',
                                     'placeholder': 'Email Address'}))
    subject = forms.CharField(max_length=100,
                             required=True,
                             widget=forms.TextInput(
                              attrs={'class': 'form-control mb-3',
                                     'placeholder': 'Subject'})) 
    message = forms.CharField(max_length=2000,
                             required=True,
                             widget=forms.TextInput(
                              attrs={'class': 'form-control mb-3',
                                     'placeholder': 'Message'})) 