import datetime
from typing import Any
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)
#apps entrada
from applications.entrada.models import Entry
from .models import Home
from .forms import SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs: Any):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #cargamos el home
        context["home"] = Home.objects.latest('created')
        #conexto de portada
        context["portada"] =Entry.objects.entrada_en_portada()
        #contexto para los articulos en home
        context["entradas_home"] =Entry.objects.entradas_en_home()
        #entradas recientes
        context["entradas_resientes"] =Entry.objects.entradas_resientes()
        #enviamos formulario de suscripcion
        context["form"] = SuscribersForm

        return context
    

class Suscribers(CreateView):
    form_class = SuscribersForm
    success_url = '.'

class ContactForm(CreateView):
    
    form_class = ContactForm
    success_url = '.'

