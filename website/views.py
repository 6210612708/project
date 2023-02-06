from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date, datetime
from django.contrib import messages
import csv ,io


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def todolist(request):
    if request.method == "POST":
        form = ListModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = ListModelForm()
    show = ListModel.objects.all()
    
    context = {'form':form , 'show':show }
    return render(request,'todolist.html' ,context)

def upload_csv(request):
    show = ListModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'upload_csv.html' ,context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = ListModel.objects.update_or_create(
            date=column[0],
            list=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show':show
    }
    return render(request,'upload_csv.html' ,context)


def deletelist(request, pk):
    data = ListModel.objects.get(id=pk)
    data.delete()
    return redirect('website:todolist')

def updatelist(request, pk):
    list = ListModel.objects.get(id=pk)
    form = ListModelForm(instance=list )
    if request.method == 'POST':
        form = ListModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:todolist')
    return render(request, 'update_todo.html', {'form':form } )





