from django.shortcuts import render
from django.views.generic import ListView,CreateView
from AppiCrudAPP.models import Persona
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request,"AppiCrudAPP/home.html")

class PersonaList(ListView):
    model = Persona
    template_name = "AppiCrudAPP/home.html"

class PersonaCreate(CreateView):
    model = Persona
    success_url = "AppiCrudApp/home"
    fields = ['nombre','apellido','edad']

    def get_success_url(self):
        return reverse('home')

        