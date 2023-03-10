from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date, datetime
from django.contrib import messages
import csv ,io
from django.http import FileResponse

def index(request):
    return render(request, 'index.html')

# =========== TODOLIST ==========================================

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

def todo_csv(request):
    show = ListModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'todo_csv.html' ,context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:todo_csv')

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
    return render(request,'todo_csv.html' ,context)


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


# =========== NEWS ==========================================


def news(request):
    if request.method == "POST":
        form = NewsModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = NewsModelForm()
    show = NewsModel.objects.all()
    
    context = {'form':form, 'show':show }
    return render(request,'news.html' ,context)

def deletenews(request, pk):
    data = NewsModel.objects.get(id=pk)
    data.delete()
    return redirect('website:news')

def updatenews(request, pk):
    list = NewsModel.objects.get(id=pk)
    form = NewsModelForm(instance=list )
    if request.method == 'POST':
        form = NewsModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:news')
    return render(request, 'update_news.html', {'form':form } )

def news_csv(request):
    show = NewsModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'news_csv.html' ,context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:news_csv')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = NewsModel.objects.update_or_create(
            title=column[0],
            detail=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show':show
    }
    return render(request,'news_csv.html' ,context)

def news_detail(request, pk):
    new = NewsModel.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "news_detail.html", context)

# =========== Document ==========================================


def document(request):
    if request.method == "POST":
        form = DocModelForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = DocModelForm()
    show = DocModel.objects.all()
    
    context = {'form':form, 'show':show }
    return render(request,'document.html' ,context)

def doc_detail(request, pk):
    pdf = DocModel.objects.filter(id=pk).first()
    context = {"pdf": pdf}
    return render(request, "doc_detail.html", context)

def deletedoc(request, pk):
    data = DocModel.objects.get(id=pk)
    data.delete()
    return redirect('website:document')



# =========== Prof ==========================================

def prof(request):
    if request.method == "POST":
        form = ProfModelForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = ProfModelForm()
    show = ProfModel.objects.all()
    
    context = {'form':form, 'show':show }
    return render(request,'professor.html' ,context)

def prof_csv(request):
    show = ProfModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'prof_csv.html' ,context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:prof_csv')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = ProfModel.objects.update_or_create(
            title = column[0],
            fname = column[1],
            lname = column[2],
            major = column[3],
            email = column[4],
            phone = column[5],

        )
    context = {
        'notify': 'CSV file is already upload', 'show':show
    }
    return render(request,'prof_csv.html' ,context)

def deleteprof(request, pk):
    data = ProfModel.objects.get(id=pk)
    data.delete()
    return redirect('website:prof')

def updateprof(request, pk):
    list = ProfModel.objects.get(id=pk)
    form = ProfModelForm(instance=list )
    if request.method == 'POST':
        form = ProfModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:prof')
    return render(request, 'update_prof.html', {'form':form } )

# =========== Other ==========================================

def other(request):
    if request.method == "POST":
        form = OtherModelForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = OtherModelForm()
    show = OtherModel.objects.all()
    
    context = {'form':form, 'show':show }
    return render(request,'other.html' ,context)

def other_csv(request):
    show = OtherModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'other_csv.html' ,context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:other_csv')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = OtherModel.objects.update_or_create(
            title = column[0],
            fname = column[1],
            lname = column[2],
            email = column[3],
            phone = column[4],

        )
    context = {
        'notify': 'CSV file is already upload', 'show':show
    }
    return render(request,'other_csv.html' ,context)

def deleteother(request, pk):
    data = OtherModel.objects.get(id=pk)
    data.delete()
    return redirect('website:other')

def updateother(request, pk):
    list = OtherModel.objects.get(id=pk)
    form = OtherModelForm(instance=list )
    if request.method == 'POST':
        form = OtherModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:other')
    return render(request, 'update_other.html', {'form':form } )


# =========== Student ==========================================

def std(request):
    if request.method == "POST":
        form = StdModelForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = StdModelForm()
    show = StdModel.objects.all()
    
    context = {'form':form, 'show':show }
    return render(request,'student.html' ,context)

def std_csv(request):
    show = StdModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'std_csv.html' ,context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:std_csv')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = StdModel.objects.update_or_create(
            stdid = column[0],
            title = column[1],
            fname = column[2],
            lname = column[3],
            email = column[4],
            phone = column[5],

        )
    context = {
        'notify': 'CSV file is already upload', 'show':show
    }
    return render(request,'std_csv.html' ,context)

def deletestd(request, pk):
    data = StdModel.objects.get(id=pk)
    data.delete()
    return redirect('website:std')

def updatestd(request, pk):
    list = StdModel.objects.get(id=pk)
    form = StdModelForm(instance=list )
    if request.method == 'POST':
        form = StdModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:std')
    return render(request, 'update_std.html', {'form':form } )


# =========== PLAN for Coordinator ==========================================

def coorplan(request):
    if request.method == "POST":
        form = CoorPlanModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = CoorPlanModelForm()
    show = CoorPlanModel.objects.all()
    
    context = {'form':form , 'show':show }
    return render(request,'coorplan.html' ,context)

def coorplan_csv(request):
    show = CoorPlanModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'coorplan_csv.html' ,context)

    if request.method == "POST":
        csv_file = request.FILES['file']
    

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:coorplan_csv')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = CoorPlanModel.objects.update_or_create(
            date=column[0],
            list=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show':show
    }
    return render(request,'coorplan_csv.html' ,context)


def deletecoorplan(request, pk):
    data = CoorPlanModel.objects.get(id=pk)
    data.delete()
    return redirect('website:coorplan')

def updatecoorplan(request, pk):
    list = CoorPlanModel.objects.get(id=pk)
    form = CoorPlanModelForm(instance=list )
    if request.method == 'POST':
        form = CoorPlanModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:coorplan')
    return render(request, 'update_coorplan.html', {'form':form } )


# =========== PLAN for Committee ==========================================

def complan(request):
    if request.method == "POST":
        form = ComPlanModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = ComPlanModelForm()
    show = ComPlanModel.objects.all()
    
    context = {'form':form , 'show':show }
    return render(request,'complan.html' ,context)

def complan_csv(request):
    show = ComPlanModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'complan_csv.html' ,context)

    if request.method == "POST":
        csv_file = request.FILES['file']
    

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:complan_csv')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = ComPlanModel.objects.update_or_create(
            date=column[0],
            list=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show':show
    }
    return render(request,'complan_csv.html' ,context)


def deletecomplan(request, pk):
    data = ComPlanModel.objects.get(id=pk)
    data.delete()
    return redirect('website:complan')

def updatecomplan(request, pk):
    list = ComPlanModel.objects.get(id=pk)
    form = ComPlanModelForm(instance=list )
    if request.method == 'POST':
        form = ComPlanModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:complan')
    return render(request, 'update_complan.html', {'form':form } )


# =========== PLAN for Consult ==========================================

def profplan(request):
    if request.method == "POST":
        form = ProfPlanModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = ProfPlanModelForm()
    show = ProfPlanModel.objects.all()
    
    context = {'form':form , 'show':show }
    return render(request,'profplan.html' ,context)

def profplan_csv(request):
    show = ProfPlanModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'profplan_csv.html' ,context)

    if request.method == "POST":
        csv_file = request.FILES['file']
    

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:profplan_csv')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = ProfPlanModel.objects.update_or_create(
            date=column[0],
            list=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show':show
    }
    return render(request,'profplan_csv.html' ,context)


def deleteprofplan(request, pk):
    data = ProfPlanModel.objects.get(id=pk)
    data.delete()
    return redirect('website:profplan')

def updateprofplan(request, pk):
    list = ProfPlanModel.objects.get(id=pk)
    form = ProfPlanModelForm(instance=list )
    if request.method == 'POST':
        form = ProfPlanModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:profplan')
    return render(request, 'update_profplan.html', {'form':form } )


# =========== PLAN for Student ==========================================

def stdplan(request):
    if request.method == "POST":
        form = StdPlanModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = StdPlanModelForm()
    show = StdPlanModel.objects.all()
    
    context = {'form':form , 'show':show }
    return render(request,'stdplan.html' ,context)

def stdplan_csv(request):
    show = StdPlanModel.objects.all()
    if request.method == "GET":
        context = {'show':show}
        return render(request, 'stdplan_csv.html' ,context)

    if request.method == "POST":
        csv_file = request.FILES['file']
    

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:stdplan_csv')

    data_set =csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = StdPlanModel.objects.update_or_create(
            date=column[0],
            list=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show':show
    }
    return render(request,'stdplan_csv.html' ,context)


def deletestdplan(request, pk):
    data = StdPlanModel.objects.get(id=pk)
    data.delete()
    return redirect('website:stdplan')

def updatestdplan(request, pk):
    list = StdPlanModel.objects.get(id=pk)
    form = StdPlanModelForm(instance=list )
    if request.method == 'POST':
        form = StdPlanModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:stdplan')
    return render(request, 'update_stdplan.html', {'form':form } )