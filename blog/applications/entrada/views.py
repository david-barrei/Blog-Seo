from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import(
    ListView
)

from .models import Entry
# Create your views here.
class EntryListView(ListView):
    
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) :
        context ['']
        return super().get_context_data(**kwargs)

    def get_queryset(self) :
        kword = self.request.GET.get('kword','')
        categoria = self.request.GET.get('categoria','')
        #consulta de busqueda
        resultado = Entry.objects.buscar_entrada(kword, categoria)
        return resultado

