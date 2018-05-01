# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.views.generic import View, TemplateView
from django.views import generic
from django.core.mail import send_mail
from datetime import datetime

from catalog.models import Category, Product

class IndexView(TemplateView):
    model = Product
    template_name = 'index.html'
    # context_object_name = 'product_promotion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_promotion'] = Product.objects.filter(in_promotion='True')
        return context


index = IndexView.as_view()

# def index (request):
#     return render (request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def localization(request):
    return render(request, 'localization.html')

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
        success = True
        form = ContactForm()
    else:
        form = ContactForm()
    context = {
        'form': form,
        'success': success
    }

    return render(request, 'contact.html', context)
