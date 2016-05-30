from django.shortcuts import render,get_object_or_404
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

def home_detail(request,id=None):
    instance = get_object_or_404(Person,id=id)
    data_employer = {
     "title" :  instance.personal_number,
     "instance": instance,

    }
    return render (request, "detail.html",data_employer)
def home_list(request):
    queryset = Person.objects.all()
    data_employer = {
     "object_list":queryset,
     "title" :"List"

    }
    return render (request, "index.html",data_employer)
def home_update(request,id=None):
    instance = get_object_or_404(Person,id=id)
    form = PersonForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    data_employer = {
    "title" :  instance.personal_number,
    "instance": instance,
    "form" :  form,
    }
    return render (request, "Person_form.html" ,data_employer)


def home_delete(request):
        return HttpResponse("<h1>usunieto pracownika<h1>")
