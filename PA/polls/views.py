from django.shortcuts import render,get_object_or_404,redirect
from .models import Person
from .forms import PersonForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse


def home_create(request):
    if request.POST:
        form = PersonForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('list'))
    else:
        form = PersonForm()
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
    if request.POST:
        form = PersonForm(request.POST or None,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        return HttpResponseRedirect(reverse('detail', args=[instance.id]))
    else:
        form = PersonForm(instance=instance)

    data_employer = {
        "title" :  instance.personal_number,
        "instance": instance,
        "form" :  form,
    }
    return render (request, "Person_form.html" ,data_employer)


def home_delete(request,id=None):
    instance = get_object_or_404(Person,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('list'))
