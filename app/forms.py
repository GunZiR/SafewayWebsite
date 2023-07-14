from django import forms
from django.core import validators
from django.utils.translation import gettext_lazy as _

class SubmitForm(forms.Form):
    name = forms.CharField(max_length=100,
                            label=_('name'),
                            required=True,
                            widget=forms.TextInput(
                            attrs={'class': 'form-control mb-3',
                                   'placeholder': _('John Doe'),
                                   'id': 'form-name'}))
    email = forms.EmailField(max_length=150,
                            label=_('email'),
                            required=True,
                            widget=forms.TextInput(
                            attrs={'class': 'form-control mb-3',
                                   'placeholder': 'you@example.com',
                                   'id': 'form-email'}),
                            validators=[validators.EmailValidator(message="Invalid Email")])
    

    subject = forms.CharField(max_length=100,
                            label=_('subject'),
                            required=True,
                            widget=forms.TextInput(
                            attrs={'class': 'form-control mb-3',
                                   'placeholder': _('subject'),
                                   'id': 'form-subject'})) 
    message = forms.CharField(max_length=2000,
                            label=_('message'),
                            required=True,
                            widget=forms.TextInput(
                            attrs={'class': 'form-control mb-3',
                                   'placeholder': _('message'),
                                   'id': 'form-message'})) 