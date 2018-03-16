''# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm (forms.Form):
    name = forms.CharField (label='Nome')
    email = forms.EmailField (label='E-mail')
    telephone = forms.CharField (label='Telefone')
    message = forms.CharField (label='Mensagem', widget=forms.Textarea())

    # Controle de como o formulário deve ser exibido
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['telephone'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'

    def send_mail(self):
        name = self.cleaned_data ['name']
        email = self.cleaned_data ['email']
        telephone = self.cleaned_data ['telephone']
        message = self.cleaned_data ['message']
        message = 'Nome:{0}\nE-mail:{1}\nTelefone:{2}\n{3}'.format(name, email, telephone, message)
        send_mail('Website', message, settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_FROM_EMAIL])
