from django.shortcuts import render
from . models import Realtor
from .forms import RealtorForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic

# Create your views here.


class RealtorFormView(generic.edit.CreateView):

    def post(self, request, *args, **kwargs):
        form = RealtorForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)


def addrealtors(request):
    print('Inside realtor')

    if request.method == 'POST':
        print('Inside method')
        form = RealtorForm(request.POST or None)

        if form.is_valid():
            print('Inside form')
            form.save()
            print('After save')
            messages.success(request, "Registered Successfully !")
            return HttpResponseRedirect('/')
    else:

        print('Inside else ')
        form = RealtorForm()
    context = {'form': form}

    return render(request, 'realtors/addrealtors.html', context)


class RealtorFormView(generic.edit.CreateView):

    def post(self, request, *args, **kwargs):
        form = RealtorForm(request.POST)
        print(form.errors)
