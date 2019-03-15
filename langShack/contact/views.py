from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from . import forms

# Create your views here.
def contactUs(request):
    form = forms.contactForm()
    if request.method == 'POST':
        form = forms.contactForm(request.POST)
        if form.is_valid():
            send_mail(
                'Message from {}'.format(form.cleaned_data['name']),
                form.cleaned_data['message'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['languageshack@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS,
                                 "Maururu for your message, we'll respond soon.")
            return HttpResponseRedirect(reverse('contact'))
    return render(request, 'contact.html', {'form': form})
