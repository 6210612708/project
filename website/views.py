from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date, datetime
from django.contrib import messages
import csv
import io
import os
from django.http import FileResponse, StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from .decorator import *
from django.db.models import Q
from django.contrib.auth.models import Group
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from wsgiref.util import FileWrapper
import mimetypes

@login_required(login_url='user:login')
def index(request):
    news = NewsModel.objects.all()
    doc = DocModel.objects.all()
    context = {'news': news ,'doc': doc}
    return render(request, 'index.html', context)

# =========== todolist ==========================================

# @allowed_users(allowed_roles=['admin'])


def setting(request):
    admin = User.objects.get(username=request.user)
    form = settingForm(instance=admin)
    if request.method == "POST":
        form = settingForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)

    return render(request, 'setting.html', {'form': form})


def todolist(request):
    if request.method == "POST":
        form = ListModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = ListModelForm()
    show = ListModel.objects.all()

    context = {'form': form, 'show': show}
    return render(request, 'todolist.html', context)


def todo_csv(request):
    show = ListModel.objects.all()
    if request.method == "GET":
        context = {'show': show}
        return render(request, 'todo_csv.html', context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:todo_csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        ListModel.objects.update_or_create(
            date=column[0],
            list=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show': show
    }
    return render(request, 'todo_csv.html', context)


def deletelist(request, pk):
    data = ListModel.objects.get(id=pk)
    data.delete()
    return redirect('website:todolist')


def updatelist(request, pk):
    list = ListModel.objects.get(id=pk)
    form = ListModelForm(instance=list)
    if request.method == 'POST':
        form = ListModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:todolist')
    return render(request, 'update_todo.html', {'form': form})


# =========== news ==========================================


def news(request):
    if request.method == "POST":
        form = NewsModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = NewsModelForm()
    show = NewsModel.objects.all()

    context = {'form': form, 'show': show}
    return render(request, 'news.html', context)


def deletenews(request, pk):
    data = NewsModel.objects.get(id=pk)
    data.delete()
    return redirect('website:news')


def updatenews(request, pk):
    list = NewsModel.objects.get(id=pk)
    form = NewsModelForm(instance=list)
    if request.method == 'POST':
        form = NewsModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:news')
    return render(request, 'update_news.html', {'form': form})


def news_csv(request):
    show = NewsModel.objects.all()
    if request.method == "GET":
        context = {'show': show}
        return render(request, 'news_csv.html', context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:news_csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = NewsModel.objects.update_or_create(
            title=column[0],
            detail=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show': show
    }
    return render(request, 'news_csv.html', context)


def news_detail(request, pk):
    new = NewsModel.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "news_detail.html", context)

# =========== document ==========================================


def dowloadfile(request, pk):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'test.text'
    file_path = base + '/Document/' + filename
    name = os.path.basename(file_path)
    response = StreamingHttpResponse(FileWrapper(open(file_path, 'rb')))
    

def document(request):
    if request.method == "POST":
        form = DocModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = DocModelForm()
    show = DocModel.objects.all()

    context = {'form': form, 'show': show}
    return render(request, 'document.html', context)


def doc_detail(request, pk):
    pdf = DocModel.objects.filter(id=pk).first()
    context = {"pdf": pdf}
    return render(request, "doc_detail.html", context)


def deletedoc(request, pk):
    data = DocModel.objects.get(id=pk)
    data.delete()
    return redirect('website:document')


# =========== consultant ==========================================

def deletecoor(request, pk):
    data = CoordinatorModel.objects.get(id=pk)
    data.delete()
    username = User.objects.get(username=data.user)
    group = Group.objects.get(name='coordinator')
    username.groups.remove(group)
    return redirect('website:prof')


def addcoor(request, pk):
    name = ProfModel.objects.get(id=pk)
    if name.user is not None:
        username = User.objects.get(username=name.user)
        group = Group.objects.get(name='coordinator')
        username.groups.add(group)
    list = ProfModel.objects.get(id=pk)
    if request.method == 'POST':
        form = coordinatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:prof')
    form = coordinatorForm(initial={'user': list})
    show = CoordinatorModel.objects.all()

    context = {'form': form, 'show': show}
    return render(request, 'coordinator.html', context)


def prof(request):
    if request.method == "POST":
        form = ProfModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = ProfModelForm()
    show = ProfModel.objects.all().order_by('major')
    coor = CoordinatorModel.objects.all()

    context = {'form': form, 'show': show, 'coor': coor}
    return render(request, 'professor.html', context)


def prof_csv(request):
    show = ProfModel.objects.all().order_by('major')
    if request.method == "GET":
        context = {'show': show}
        return render(request, 'prof_csv.html', context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:prof_csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = ProfModel.objects.update_or_create(
            title=column[0],
            fname=column[1],
            lname=column[2],
            major=column[3],
            email=column[4],
            phone=column[5],

        )
    context = {
        'notify': 'CSV file is already upload', 'show': show
    }
    return render(request, 'prof_csv.html', context)


def deleteprof(request, pk):
    data = ProfModel.objects.get(id=pk)
    data.delete()
    return redirect('website:prof')


def updateprof(request, pk):
    list = ProfModel.objects.get(id=pk)
    form = ProfModelForm(instance=list)
    if request.method == 'POST':
        form = ProfModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:prof')
    return render(request, 'update_prof.html', {'form': form})

# =========== Other ==========================================


# def other(request):
#     if request.method == "POST":
#         form = OtherModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         else:
#             print("Error", form.errors)
#     form = OtherModelForm()
#     show = OtherModel.objects.all()

#     context = {'form': form, 'show': show}
#     return render(request, 'other.html', context)


# def other_csv(request):
#     show = OtherModel.objects.all()
#     if request.method == "GET":
#         context = {'show': show}
#         return render(request, 'other_csv.html', context)

#     csv_file = request.FILES['file']

#     if not csv_file.name.endswith('.csv'):
#         messages.error(request, 'Please upload only CSV file')
#         return redirect('website:other_csv')

#     data_set = csv_file.read().decode('UTF-8')
#     io_string = io.StringIO(data_set)


#     for column in csv.reader(io_string, delimiter=',', quotechar='|'):
#         _, created = OtherModel.objects.update_or_create(
#             title=column[0],
#             fname=column[1],
#             lname=column[2],
#             email=column[3],
#             phone=column[4],

#         )
#     context = {
#         'notify': 'CSV file is already upload', 'show': show
#     }
#     return render(request, 'other_csv.html', context)


# def deleteother(request, pk):
#     data = OtherModel.objects.get(id=pk)
#     data.delete()
#     return redirect('website:other')


# def updateother(request, pk):
#     list = OtherModel.objects.get(id=pk)
#     form = OtherModelForm(instance=list)
#     if request.method == 'POST':
#         form = OtherModelForm(request.POST, instance=list)
#         if form.is_valid():
#             form.save()
#             return redirect('website:other')
#     return render(request, 'update_other.html', {'form': form})


# =========== student ==========================================
def stddetail(request):
    check = StdModel.objects.all()
    can_show = 0
    for ck in check:
        if ck.user == request.user:
            can_show = 1
    if can_show == 1:
        show = StdModel.objects.filter(
            Q(fname=request.user.stdmodel.fname) & Q(lname=request.user.stdmodel.lname))
        context = {'show': show}
        return render(request, 'stddetail.html', context)
    else:
        messages.error(request, 'กรุณารอแอดมินอัพเดทข้อมูลนักศึกษา')
        return redirect('website:index')


def std(request):
    if request.method == "POST":
        form = StdModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = StdModelForm()
    show = StdModel.objects.all().order_by('major')

    context = {'form': form, 'show': show}
    return render(request, 'student.html', context)


def std_csv(request):
    show = StdModel.objects.all()
    if request.method == "GET":
        context = {'show': show}
        return render(request, 'std_csv.html', context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:std_csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = StdModel.objects.update_or_create(
            stdid=column[0],
            title=column[1],
            fname=column[2],
            lname=column[3],
            major=column[4],
            email=column[5],
            phone=column[6],

        )
    context = {
        'notify': 'CSV file is already upload', 'show': show
    }
    return render(request, 'std_csv.html', context)


def deletestd(request, pk):
    data = StdModel.objects.get(id=pk)
    data.delete()
    return redirect('website:std')


def updatestd(request, pk):
    list = StdModel.objects.get(id=pk)
    form = StdModelForm(instance=list)
    if request.method == 'POST':
        form = StdModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:std')
    return render(request, 'update_std.html', {'form': form})


# =========== PLAN for coordinator ==========================================

def coorplan(request):
    if request.method == "POST":
        form = CoorPlanModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = CoorPlanModelForm()
    show = CoorPlanModel.objects.all()

    context = {'form': form, 'show': show}
    return render(request, 'coorplan.html', context)


def coorplan_csv(request):
    show = CoorPlanModel.objects.all()
    if request.method == "GET":
        context = {'show': show}
        return render(request, 'coorplan_csv.html', context)

    if request.method == "POST":
        csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:coorplan_csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = CoorPlanModel.objects.update_or_create(
            date=column[0],
            list=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show': show
    }
    return render(request, 'coorplan_csv.html', context)


def deletecoorplan(request, pk):
    data = CoorPlanModel.objects.get(id=pk)
    data.delete()
    return redirect('website:coorplan')


def updatecoorplan(request, pk):
    list = CoorPlanModel.objects.get(id=pk)
    form = CoorPlanModelForm(instance=list)
    if request.method == 'POST':
        form = CoorPlanModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:coorplan')
    return render(request, 'update_coorplan.html', {'form': form})


# # =========== PLAN for committee ==========================================

# def complan(request):
#     if request.method == "POST":
#         form = ComPlanModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             print("Error", form.errors)
#     form = ComPlanModelForm()
#     show = ComPlanModel.objects.all()

#     context = {'form': form, 'show': show}
#     return render(request, 'complan.html', context)


# def complan_csv(request):
#     show = ComPlanModel.objects.all()
#     if request.method == "GET":
#         context = {'show': show}
#         return render(request, 'complan_csv.html', context)

#     if request.method == "POST":
#         csv_file = request.FILES['file']

#     if not csv_file.name.endswith('.csv'):
#         messages.error(request, 'Please upload only CSV file')
#         return redirect('website:complan_csv')

#     data_set = csv_file.read().decode('UTF-8')
#     io_string = io.StringIO(data_set)


#     for column in csv.reader(io_string, delimiter=',', quotechar='|'):
#         _, created = ComPlanModel.objects.update_or_create(
#             date=column[0],
#             list=column[1],
#         )
#     context = {
#         'notify': 'CSV file is already upload', 'show': show
#     }
#     return render(request, 'complan_csv.html', context)


# def deletecomplan(request, pk):
#     data = ComPlanModel.objects.get(id=pk)
#     data.delete()
#     return redirect('website:complan')


# def updatecomplan(request, pk):
#     list = ComPlanModel.objects.get(id=pk)
#     form = ComPlanModelForm(instance=list)
#     if request.method == 'POST':
#         form = ComPlanModelForm(request.POST, instance=list)
#         if form.is_valid():
#             form.save()
#             return redirect('website:complan')
#     return render(request, 'update_complan.html', {'form':form } )


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

    context = {'form': form, 'show': show}
    return render(request, 'profplan.html', context)


def profplan_csv(request):
    show = ProfPlanModel.objects.all()
    if request.method == "GET":
        context = {'show': show}
        return render(request, 'profplan_csv.html', context)

    if request.method == "POST":
        csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:profplan_csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = ProfPlanModel.objects.update_or_create(
            date=column[0],
            list=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show': show
    }
    return render(request, 'profplan_csv.html', context)


def deleteprofplan(request, pk):
    data = ProfPlanModel.objects.get(id=pk)
    data.delete()
    return redirect('website:profplan')


def updateprofplan(request, pk):
    list = ProfPlanModel.objects.get(id=pk)
    form = ProfPlanModelForm(instance=list)
    if request.method == 'POST':
        form = ProfPlanModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:profplan')
    return render(request, 'update_profplan.html', {'form': form})


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

    context = {'form': form, 'show': show}
    return render(request, 'stdplan.html', context)


def stdplan_csv(request):
    show = StdPlanModel.objects.all()
    if request.method == "GET":
        context = {'show': show}
        return render(request, 'stdplan_csv.html', context)

    if request.method == "POST":
        csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only CSV file')
        return redirect('website:stdplan_csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = StdPlanModel.objects.update_or_create(
            date=column[0],
            list=column[1],
        )
    context = {
        'notify': 'CSV file is already upload', 'show': show
    }
    return render(request, 'stdplan_csv.html', context)


def deletestdplan(request, pk):
    data = StdPlanModel.objects.get(id=pk)
    data.delete()
    return redirect('website:stdplan')


def updatestdplan(request, pk):
    list = StdPlanModel.objects.get(id=pk)
    form = StdPlanModelForm(instance=list)
    if request.method == 'POST':
        form = StdPlanModelForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('website:stdplan')
    return render(request, 'update_stdplan.html', {'form': form})


# =========== project ==========================================

def allproject(request):
    
    form = topicprojectForm(request.POST)
    proj = ProjectModel.objects.all()
    if request.method == "POST":
        if form.is_valid():
            check = SubjectModel.objects.all().order_by('-id')
            sc = SubjectModel.objects.all().order_by('-id')
            term = 1
            date_now = date.today()
            if sc[0].startterm < date_now < sc[0].endterm :
                term = 0
            if check:
                test = form.save(commit=False)
                test.save()
                for p in proj :
                    FileProject.objects.create(
                        topic = test,
                        project = p
                    )
                   
            else:
                messages.error(
                    request, 'กรุณารอแอดมินตั้งค่าวิชาและปีการศึกษา')
                return render(request, 'project.html')
        else:
            print("Error", form.errors)

    prof = ProfModel.objects.all()
    can_show = 0
    for ck in prof:
        if ck.user == request.user:
            can_show = 1
            
    if request.user.groups.filter(name='admin').exists():
        can_show = 1
    if can_show == 1:
        if request.user.groups.filter(name='admin').exists():
            show = ProjectModel.objects.all()
            con= ProjectModel.objects.all()
        elif request.user.profmodel.major == 'ไฟฟ้า' and request.user.groups.filter(name='coordinator'):
            show = ProjectModel.objects.filter(major = 'ไฟฟ้า')
            con = ProjectModel.objects.all()
        elif request.user.profmodel.major == 'คอมพิวเตอร์' and request.user.groups.filter(name='coordinator'):
            show = ProjectModel.objects.filter(major =  'คอมพิวเตอร์')
            con= ProjectModel.objects.all()
        else :
            show = ProjectModel.objects.all()
            con= ProjectModel.objects.all()
    file = Topicproject.objects.all()
    context = {'form': form, 'show': show, 'file': file, 'con' :con}
    return render(request, 'allproject.html', context)


def deletetopic(request, pk):
    data = Topicproject.objects.get(id=pk)
    data.delete()
    return redirect('website:allproject')

def project(request):
    form = projectModelForm(request.POST)
    forms = projectModelForm()
    prof = ProfModel.objects.all()
    can_show = 0
    for ck in prof:
        if ck.user == request.user:
            can_show = 1
    if request.user.groups.filter(name='admin').exists():
        can_show = 1
    if can_show == 1:
        if request.user.groups.filter(name='admin').exists():
            show = ProjectModel.objects.all()
            all = ProjectModel.objects.all()
        elif request.user.profmodel.major == 'ไฟฟ้า' and request.user.groups.filter(name='coordinator'):
            show = ProjectModel.objects.filter(major = 'ไฟฟ้า')
            all = ProjectModel.objects.all()
        elif request.user.profmodel.major == 'คอมพิวเตอร์' and request.user.groups.filter(name='coordinator'):
            show = ProjectModel.objects.filter(major =  'คอมพิวเตอร์')
            all= ProjectModel.objects.all()
        else :
            show = ProjectModel.objects.all()
            all= ProjectModel.objects.all()
        if request.method == "POST":
            if form.is_valid():
                check = SubjectModel.objects.all().order_by('-id')
                if check:
                    con = request.user.profmodel
                    test = form.save(commit=False)
                    test.consult = con
                    fin = test.save()
                    ScoreModel.objects.create(
                        subject =check[0],
                        project=test,
                        consult=con,            
                    )
                    ScoreModel.objects.create(
                        subject =check[1],
                        project=test,
                        consult=con,
                    )
                    ScoreConsult.objects.create(
                        subject =check[0],
                        project=test,
                        consult=con,
                    ) 
                    ScoreConsult.objects.create(
                        subject =check[1],
                        project=test,
                        consult=con,
                    ) 
                    ScoreCom1.objects.create(
                        subject =check[0],
                        project=test,
                        consult=con,
            
                    )
                    ScoreCom1.objects.create(
                        subject =check[1],
                        project=test,
                        consult=con,
                    )
                    ScoreCom2.objects.create(
                        subject =check[0],
                        project=test,
                        consult=con,
                    )
                    ScoreCom2.objects.create(
                        subject =check[1],
                        project=test,
                        consult=con,
                    )
                else:
                    messages.error(
                        request, 'กรุณารอแอดมินตั้งค่าวิชาและปีการศึกษา')
                    return redirect('website:index')
        else:
            print("Error", form.errors)
    else:
        messages.error(request, 'กรุณารอแอดมินอัพเดทข้อมูลอาจารย์')
        return redirect('website:index')
    
    context = {'form': forms, 'show': show , 'all': all}
    return render(request, 'project.html', context)



def reportproject(request, pk):
    temp = ProjectModel.objects.filter(id=pk).get()
    proj = ProjectModel.objects.filter(id=pk)
    show = FileProject.objects.exclude(file='').filter(project=temp)
    topic = Topicproject.objects.all()
    
    
    # form = scoretopicForm()
    # if request.method == "POST":
    #     form = scoretopicForm(request.POST)
    #     if form.is_valid():
    #         test = form.save(commit=False)
    #         FileProject.objects.filter(project=temp ,topic=test.topic).update(
    #             score = test.score
    #         )'form': form


    context = {'show': show, 'topic': topic,'proj': proj ,}
    return render(request, 'reportproject.html', context)


def deleteproject(request, pk):
    data = ProjectModel.objects.get(id=pk)
    data.delete()
    return redirect('website:project')


def updateproject(request, pk):
    list = ProjectModel.objects.get(id=pk)
    form = projectModelForm(instance=list)
    if request.method == 'POST':
        form = projectModelForm(request.POST, instance=list)
        if form.is_valid():
            con = request.user.profmodel
            test = form.save(commit=False)
            test.consult = con
            test = test.save()
            return redirect('website:project')
    return render(request, 'update_project.html', {'form': form})

    # form = projectForm()
    # if request.method == "POST":
    #     thainame = request.POST.get("thainame")
    #     engname = request.POST.get("engname")
    #     detail = request.POST.get("detail")
    #     proj = ProjectModel.objects.update(
    #         thainame =thainame,
    #         engname = engname,
    #         consult = request.user.first_name,
    #         detail = detail,
    #     )
    #     return redirect('website:project')

    # context = {list :'list'}
    # return render(request,'update_project.html' ,context)


def statusproject(request, pk):
    ProjectModel.objects.filter(id=pk).update(status='อนุมัติ')
    return redirect('website:project')

# =========== student project ==========================================


def stdproject(request):
    test = ProjectModel.objects.all()
    x = 0
    for test in test:
        if test.student1 == request.user.stdmodel or test.student2 == request.user.stdmodel:
            x = 1
    if x == 0:
        show = ProjectModel.objects.all()

    context = {'x': x, 'show': show}
    return render(request, 'stdproject.html', context)


def applyproject(request, pk):
    list = ProjectModel.objects.get(id=pk)
    form = applyprojectForm(instance=list)
    if request.method == 'POST':
        form = applyprojectForm(request.POST, instance=list)
        if form.is_valid():
            m = request.user.stdmodel.major
            test = form.save(commit=False)
            test.major = m
            test.status = 'รอการอนุมัติ'
            fin = test.save()
            ScoreModel.objects.filter(project=list).update(
                std1=list.student1,
                std2=list.student2,
                major = m
            )
            ScoreConsult.objects.filter(project=list).update(
                std1=list.student1,
                std2=list.student2,
            )
            ScoreCom1.objects.filter(project=list).update(
                std1=list.student1,
                std2=list.student2
            )
            ScoreCom2.objects.filter(project=list).update(
                std1=list.student1,
                std2=list.student2
            )
            return redirect('website:detailproject')
    return render(request, 'applyproject.html', {'form': form})


def detailproject(request):
    check = StdModel.objects.all()
    can_show = 0
    for ck in check:
        if ck.user == request.user:
            can_show = 1
    if request.user.groups.filter(name='admin').exists():
        can_show = 1
    if can_show == 1:
        show = ProjectModel.objects.filter(
            Q(student1=request.user.stdmodel) | Q(student2=request.user.stdmodel))
        if not show:
            return redirect('website:stdproject')
        else:
            test = ProjectModel.objects.get(
                Q(student1=request.user.stdmodel) | Q(student2=request.user.stdmodel))
            score = ScoreModel.objects.filter(project=test)
            context = {'show': show, 'score': score}
            return render(request, 'detailproject.html', context)
    else:
        messages.error(request, 'กรุณารอแอดมินอัพเดทข้อมูลนักศึกษา')
        return redirect('website:index')


def docproject(request):
    check = StdModel.objects.all()
    can_show = 0
    for ck in check:
        if ck.user == request.user:
            can_show = 1
    if request.user.groups.filter(name='admin').exists():
        can_show = 1
    if can_show == 1:
        temp = ProjectModel.objects.filter(
            Q(student1=request.user.stdmodel) | Q(student2=request.user.stdmodel))
        if temp:
            proj = ProjectModel.objects.filter(
                Q(student1=request.user.stdmodel) | Q(student2=request.user.stdmodel)).get()
            if proj.status == 'รอการอนุมัติ':
                messages.error(request, 'กรุณารอที่ปรึกษาอนุมัติโครงงาน')
                return render(request, 'docproject.html')
            else:
                form = fileprojectForm(instance=proj)
                if request.method == "POST":
                    form = fileprojectForm(request.POST, request.FILES)
                    if form.is_valid():
                        test = form.save(commit=False)
                        FileProject.objects.filter(project=proj ,topic = test.topic).update(
                            date = datetime.now(),
                            file = test.file
                        )

                    else:
                        print("Error", form.errors)
            form = fileprojectForm(initial={'project': proj})
            show = FileProject.objects.exclude(file='').filter(project=proj)
            topic = Topicproject.objects.all()
            context = {'form': form, 'show': show, 'topic': topic}
            return render(request, 'docproject.html', context)
        else:
            messages.error(request, 'กรุณาลงทะเบียนโครงงาน')
            return render(request, 'docproject.html')
    else:
        messages.error(request, 'กรุณารอแอดมินอัพเดทข้อมูลนักศึกษา')
        return redirect('website:index')


# ===========subject==========================================

def subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = SubjectForm()
    all = SubjectModel.objects.all().order_by("-id")
    context = {'form': form, 'all': all}
    return render(request, 'subject.html', context)


def deletesubject(request, pk):
    data = SubjectModel.objects.get(id=pk)
    data.delete()
    return redirect('website:subject')


# =========== grade score==========================================

def score(request, pk):
    list = ScoreConsult.objects.get(id=pk)
    t = ScoreConsult.objects.filter(id=pk)
    form = ScoreconsultForm(instance=list)
    sc = SubjectModel.objects.all().order_by('-id')
    term = 1
    date_now = date.today()
    if sc[0].startterm < date_now < sc[0].endterm :
        term = 2
    if request.method == 'POST':
        form = ScoreconsultForm(request.POST, instance=list)
        if form.is_valid():
            test = form.save(commit=False)
            if test.sc1 is None or test.sc2 is None or test.sc3 is None or test.sc4 is None or test.sc5 is None or test.sc6 is None or test.sc7 is None or test.sc8 is None :
                messages.error(request, 'กรุณากรอกคะแนนให้ครบทุกช่อง หากยังไม่ประสงค์ประเมินข้อใดกรุณาใส่ 0')
                return redirect('website:score' , pk)
            point = test.sc1 + test.sc2 + test.sc3 + test.sc4 + \
                test.sc5 + test.sc6 + test.sc7 + test.sc8
            test.score = point
            fin = test.save()
            if term == 1 :
                ScoreModel.objects.filter(project=test.project ,subject=sc[1]).update(
                    sccon = point
                )
            else:
                ScoreModel.objects.filter(project=test.project ,subject=sc[0]).update(
                    sccon = point
                )
        else:
            print("Error", form.errors)
    context = {'form': form,'t':t}
    return render(request, 'score.html', context)
    
def scorecom1(request, pk):
    list = ScoreCom1.objects.get(id=pk)
    t = ScoreCom1.objects.filter(id=pk)
    form = Scorecom1Form(instance=list)
    sc = SubjectModel.objects.all().order_by('-id')
    term = 1
    date_now = date.today()
    if sc[0].startterm < date_now < sc[0].endterm :
        term = 2
    if request.method == 'POST':
        form = Scorecom1Form(request.POST, instance=list)
        if form.is_valid():
            test = form.save(commit=False)
            if test.sc1 is None or test.sc2 is None or test.sc3 is None or test.sc4 is None or test.sc5 is None or test.sc6 is None :
                messages.error(request, 'กรุณากรอกคะแนนให้ครบทุกช่อง หากยังไม่ประสงค์ประเมินข้อใดกรุณาใส่ 0')
                return redirect('website:score' , pk)
            point = test.sc1 + test.sc2 + test.sc3 + test.sc4 + \
                test.sc5 + test.sc6 
            test.score = point
            fin = test.save()
            if term == 1 :
                ScoreModel.objects.filter(project=test.project ,subject=sc[1]).update(
                    sccom1 = point
                )
            else:
                ScoreModel.objects.filter(project=test.project ,subject=sc[0]).update(
                    sccom1 = point
                )
        else:
            print("Error", form.errors)
    context = {'form': form,'t':t}
    return render(request, 'score_com.html', context)
    
def scorecom2(request, pk):
    list = ScoreCom2.objects.get(id=pk)
    t = ScoreCom2.objects.filter(id=pk)
    form = Scorecom2Form(instance=list)
    sc = SubjectModel.objects.all().order_by('-id')
    term = 1
    date_now = date.today()
    if sc[0].startterm < date_now < sc[0].endterm :
        term = 2
    if request.method == 'POST':
        form = Scorecom2Form(request.POST, instance=list)
        if form.is_valid():
            test = form.save(commit=False)
            if test.sc1 is None or test.sc2 is None or test.sc3 is None or test.sc4 is None or test.sc5 is None or test.sc6 is None:
                messages.error(request, 'กรุณากรอกคะแนนให้ครบทุกช่อง หากยังไม่ประสงค์ประเมินข้อใดกรุณาใส่ 0')
                return redirect('website:score' , pk)
            point = test.sc1 + test.sc2 + test.sc3 + test.sc4 + \
                test.sc5 + test.sc6 
            test.score = point
            fin = test.save()
            if term == 1 :
                ScoreModel.objects.filter(project=test.project ,subject=sc[1]).update(
                    sccom2 = point
                )
            else:
                ScoreModel.objects.filter(project=test.project ,subject=sc[0]).update(
                    sccom2 = point
                )
        else:
            print("Error", form.errors)
    context = {'form': form,'t':t}
    return render(request, 'score_com.html', context)
    
def avgscore(request, pk):
    re = ScoreModel.objects.get(id=pk)
    if re.sccon is None or re.sccom1 is None or re.sccom2 is None :
        messages.error(request, 'กรุณารอกรรมการและที่ปรึกษาประเมินคะแนน')
        return redirect('website:reportscore')
    else :
        sc = re.sccon + (re.sccom1 + re.sccom2)/2
        ScoreModel.objects.filter(id=pk).update(
        score = sc
        )

    return redirect('website:reportscore')

def subscore(request, pk):
    re = FileProject.objects.get(id=pk)
    sc = SubjectModel.objects.all().order_by('-id')
    term = 1
    date_now = date.today()
    if sc[0].startterm < date_now < sc[0].endterm :
        term = 2
    if term == 1 :
        score = ScoreModel.objects.get(project = re.project,subject = sc[1])
        if score.score is None :
            messages.error(request, 'กรุณาสรุปคะแนนก่อน')
            return redirect('website:reportscore')
        else :
            fin  = score.score - (score.score* 5/100)
            FileProject.objects.filter(id=pk).update(
                subscore = True
                )
            score = ScoreModel.objects.filter(project = re.project,subject = sc[1]).update(
                score = fin
                )
    else:
        score = ScoreModel.objects.get(project = re.project,subject = sc[0])
        if score.score is None :
            messages.error(request, 'กรุณาสรุปคะแนนก่อน')
            return redirect('website:reportscore')
        else :
            fin  = score.score - (score.score* 5/100)
            FileProject.objects.filter(id=pk).update(
                subscore = True
                )
            score = ScoreModel.objects.filter(project = re.project,subject = sc[0]).update(
                score = fin
                )
    # if re.sccon is None or re.sccom1 is None or re.sccom2 is None :
    #     messages.error(request, 'กรุณาสรุปคะแนน')
    #     return redirect('website:reportscore')
    # else :
    # sc = re.score - (re.score* 5/100)
    # FileProject.objects.filter(id=pk).update(
    #     score = sc,
    #     subscore = True
    #     )
    return redirect('website:reportscore')


def evaluate(request):
    prof = ProfModel.objects.all()
    can_show = 0
    sc = SubjectModel.objects.all().order_by('-id')
    for ck in prof:
        if ck.user == request.user:
            can_show = 1
    if can_show == 1:
        show = ProjectModel.objects.filter(
            consult=request.user.profmodel, status='อนุมัติ')
        com = ProjectModel.objects.filter(
            Q(committee1=request.user.profmodel) | Q(committee2=request.user.profmodel), status='อนุมัติ')
        term = 1
        date_now = date.today()
        if sc[0].startterm < date_now < sc[0].endterm :
            term = 2
        if term == 1 :
            score = ScoreConsult.objects.filter(subject = sc[1])
            scorecom1 = ScoreCom1.objects.filter(subject = sc[1])
            scorecom2 = ScoreCom2.objects.filter(subject = sc[1])
        else:
            score = ScoreConsult.objects.filter(subject = sc[0]) 
            scorecom1 = ScoreCom1.objects.filter(subject = sc[0])
            scorecom2 = ScoreCom2.objects.filter(subject = sc[0])
            
        context = {'show': show, 'com': com, 'score': score, 'scorecom1': scorecom1, 'scorecom2': scorecom2}
        return render(request, 'evaluate.html', context)
    else:
        messages.error(request, 'กรุณารอแอดมินอัพเดทข้อมูลอาจารย์')
        return redirect('website:index')


def grade(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    form = GradeForm()
    show = GradeModel.objects.all().order_by("-id")
    context = {'form': form, 'show': show}
    return render(request, 'grade.html', context)

def deletegrade(request, pk):
    data = GradeModel.objects.get(id=pk)
    data.delete()
    return redirect('website:grade')

def updategrade(request, pk):
    list = GradeModel.objects.get(id=pk)
    form = GradeForm(instance=list)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    context = {'form': form}
    return render(request, 'updategrade.html', context)

def sumscore(request, pk):
    point = 0
    i = ScoreModel.objects.get(id=pk)
    print(i)
    sc = FileProject.objects.filter(project=i.project)
    print(sc)
    x = 0
    for sc in sc :
        x += 1
        point += sc.score
    final = point/x
    ScoreModel.objects.filter(id=pk).update(
            score = final
        )
    return redirect('website:reportscore')

def reportgrade(request, pk):
    i = ScoreModel.objects.get(id=pk)
    check = GradeModel.objects.filter(subject=i.subject).count()
    if check == 0:
        messages.error(request, 'กรุณากำหนดเกณฑ์การตัดเกรด')
    else:
        g = GradeModel.objects.get(subject=i.subject)
        if i.score >= g.A:
            ScoreModel.objects.filter(project=i.project,subject=i.subject).update(
                grade='A'
            )
        elif g.A >= i.score >= g.Bplus:
            ScoreModel.objects.filter(project=i.project,subject=i.subject).update(
                grade='B+'
            )
        elif g.Bplus >= i.score >= g.B:
            ScoreModel.objects.filter(project=i.project,subject=i.subject).update(
                grade='B'
            )
        elif g.B >= i.score >= g.Cplus:
            ScoreModel.objects.filter(project=i.project,subject=i.subject).update(
                grade='C+'
            )
        elif g.Cplus >= i.score >= g.C:
            ScoreModel.objects.filter(project=i.project,subject=i.subject).update(
                grade='C'
            )
        elif g.C >= i.score >= g.Dplus:
            ScoreModel.objects.filter(project=i.project,subject=i.subject).update(
                grade='D+'
            )
        elif g.Dplus >= i.score >= g.D:
            ScoreModel.objects.filter(project=i.project,subject=i.subject).update(
                grade='D'
            )
        else:
            ScoreModel.objects.filter(project=i.project,subject=i.subject).update(
                grade='F'
            )
        print(check)

    return redirect('website:reportscore')


def reportscore(request):
    report = FileProject.objects.all()
    sc = SubjectModel.objects.all().order_by('-id')
    temp = ScoreModel.objects.all()
    term = 1
    date_now = date.today()
    if sc[0].startterm < date_now < sc[0].endterm :
        term = 2
    if term == 1 :
        if request.user.groups.filter(name='admin').exists():
            show = ScoreModel.objects.all()
        elif request.user.profmodel.major == 'ไฟฟ้า':
            show = ScoreModel.objects.filter(subject = sc[1] ,major = 'ไฟฟ้า')
        elif request.user.profmodel.major == 'คอมพิวเตอร์':
            show = ScoreModel.objects.filter(subject = sc[1] ,major =  'คอมพิวเตอร์')
    else:
        if request.user.groups.filter(name='admin').exists():
            show = ScoreModel.objects.all()
        elif request.user.profmodel.major == 'ไฟฟ้า':
            show = ScoreModel.objects.filter(subject = sc[0] ,major = 'ไฟฟ้า') 
        elif request.user.profmodel.major == 'คอมพิวเตอร์':
            show = ScoreModel.objects.filter(subject = sc[0] ,major =  'คอมพิวเตอร์')

    context = {'show': show ,'re':report}
    return render(request, 'report_score.html', context)


# ################# commiteee ###########################

def committee(request, pk):
    list = ProjectModel.objects.get(id=pk)
    form = CommitteeForm(instance=list)
    if request.method == 'POST':
        form = CommitteeForm(request.POST, instance=list)
        if form.is_valid():
            test = form.save(commit=False)
            com1 = test.committee1
            com2 = test.committee2
            test = test.save()
            ScoreModel.objects.filter(project=list).update(
                committee1 = com1,
                committee2 = com2
            )
            return redirect('website:project')
    context = {'form': form, 'list': list}
    return render(request, 'committee.html', context)
