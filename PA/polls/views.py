from django.shortcuts import render
from .models import Person
from .forms import PersonForm
from django.http import HttpResponse



def home_create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    data_employer = {
         "form" :  form,
        }
    return render (request, "Person_form.html" ,data_employer)

def home_detail(request):
    data_employer = {
     "title" :  "Detail"

    }
    return render (request, "index.html",data_employer)
def home_list(request):
    queryset = Person.objects.all()
    data_employer = {
     "object_list":queryset,
     "title" :"List"

    }
    return render (request, "index.html",data_employer)
def home_update(request):
    return HttpResponse("<h1>lista zmieniona<h1>")
def home_delete(request):
        return HttpResponse("<h1>usunieto pracownika<h1>")
