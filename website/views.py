from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date, datetime
from django.contrib import messages
import csv
import io
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from .decorator import *
from django.db.models import Q
from django.contrib.auth.models import Group


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


# =========== consultant coordinator ==========================================

def deletecoor(request, pk):
    data = CoordinatorModel.objects.get(id=pk)
    data.delete()
    username = User.objects.get(username=data.user)
    group = Group.objects.get(name='coordinator')
    username.groups.remove(group)
    return redirect('website:prof')


def addcoor(request, pk):
    name = ProfModel.objects.get(id=pk)
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
    show = ProfModel.objects.all()
    coor = CoordinatorModel.objects.all()

    context = {'form': form, 'show': show, 'coor': coor}
    return render(request, 'professor.html', context)


def prof_csv(request):
    show = ProfModel.objects.all()
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
    show = StdModel.objects.all()

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
            email=column[4],
            phone=column[5],

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
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            print("Error", form.errors)
    show = ProjectModel.objects.all()
    file = Topicproject.objects.all()
    context = {'form': form, 'show': show, 'file': file}
    return render(request, 'allproject.html', context)


def project(request):
    form = projectModelForm(request.POST)
    forms = projectModelForm()
    prof = ProfModel.objects.all()
    show = ProjectModel.objects.all()
    can_show = 0
    for ck in prof:
        if ck.user == request.user:
            can_show = 1
    if request.user.groups.filter(name='admin').exists():
        can_show = 1
    if can_show == 1:
        # if request.user.profmodel.major == 'ไฟฟ้า':
        #     p = ProfModel.objects.filter(major = 'ไฟฟ้า')
        #     show = ProjectModel.objects.filter(consult = p)
        # else:
        #     p = ProfModel.objects.filter(major = 'คอมพิวเตอร์')
        #     show = ProjectModel.objects.filter(consult = p)
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
                        consult=con
                    )
                    ScoreModel.objects.create(
                        subject =check[1],
                        project=test,
                        consult=con
                    )
                    ScoreConsult.objects.create(
                        subject =check[0],
                        project=test,
                        consult=con
                    )
                    ScoreConsult.objects.create(
                        subject =check[1],
                        project=test,
                        consult=con
                    )
                    ScoreCom1.objects.create(
                        subject =check[0],
                        project=test,
                        consult=con
                    )
                    ScoreCom1.objects.create(
                        subject =check[1],
                        project=test,
                        consult=con
                    )
                    ScoreCom2.objects.create(
                        subject =check[0],
                        project=test,
                        consult=con
                    )
                    ScoreCom2.objects.create(
                        subject =check[1],
                        project=test,
                        consult=con
                    )
                else:
                    messages.error(
                        request, 'กรุณารอแอดมินตั้งค่าวิชาและปีการศึกษา')
                    return render(request, 'project.html')
        else:
            print("Error", form.errors)

    else:
        messages.error(request, 'กรุณารอแอดมินอัพเดทข้อมูลอาจารย์')
        return redirect('website:index')
    context = {'form': forms, 'show': show}
    return render(request, 'project.html', context)


def reportproject(request, pk):
    temp = ProjectModel.objects.filter(id=pk).get()
    show = Fileproject.objects.filter(project=temp).order_by("-id")
    topic = Topicproject.objects.all()
    context = {'show': show, 'topic': topic}
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
            list.status = 'รอการอนุมัติ'
            form.save()
            ScoreModel.objects.filter(project=list).update(
                std1=list.student1,
                std2=list.student2
            )
            ScoreConsult.objects.filter(project=list).update(
                std1=list.student1,
                std2=list.student2
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
                        test.date = datetime.now()
                        test = test.save()
                    else:
                        print("Error", form.errors)
            form = fileprojectForm(initial={'project': proj})
            show = Fileproject.objects.filter(project=proj).order_by("-id")
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

def score2(request, pk):
    con = ProjectModel.objects.filter(
        consult=request.user.profmodel, status='อนุมัติ')
    com1 = ProjectModel.objects.filter(
        committee1=request.user.profmodel, status='อนุมัติ')
    check = SubjectModel.objects.all().order_by('-id')
    if con:
        con = ProjectModel.objects.filter(
            consult=request.user.profmodel, status='อนุมัติ').get()
        list = ScoreConsult.objects.filter(project=con,subject=check[0]).get()
        show = ScoreConsult.objects.filter(project=con,subject=check[0])
        form = ScoreconsultForm(instance=list)
        if request.method == 'POST':
            form = ScoreconsultForm(request.POST, instance=list)
            if form.is_valid():
                test = form.save(commit=False)
                point = test.sc1 + test.sc2 + test.sc3 + test.sc4 + \
                    test.sc5 + test.sc6 + test.sc7 + test.sc8
                test.score = point
                fin = test.save()
                ScoreModel.objects.filter(project=test.project,subject = test.subject).update(
                    consc=point
                )
            else:
                print("Error", form.errors)
        context = {'form': form, 'show': show}
    elif com1:
        com1 = ProjectModel.objects.filter(
            committee1=request.user.profmodel, status='อนุมัติ')
        list = ScoreCom1.objects.filter(project=com1,subject=check[0]).get()
        show = ScoreCom1.objects.filter(project=com1,subject=check[0])
        form = Scorecom1Form(instance=list)
        if request.method == 'POST':
            form = Scorecom1Form(request.POST, instance=list)
            if form.is_valid():
                test = form.save(commit=False)
                point = test.sc1 + test.sc2 + test.sc3 + test.sc4 + \
                    test.sc5 + test.sc6 + test.sc7 + test.sc8
                test.score = point
                fin = test.save()
                ScoreModel.objects.filter(project=test.project,subject = test.subject).update(
                    com1sc=point
                )
            else:
                print("Error", form.errors)
        context = {'form': form, 'show': show}
    else:
        com2 = ProjectModel.objects.filter(
            committee2=request.user.profmodel, status='อนุมัติ')
        list = ScoreCom2.objects.filter(project=com2,subject=check[0]).get()
        show = ScoreCom2.objects.filter(project=com2,subject=check[0])
        form = Scorecom2Form(instance=list)
        if request.method == 'POST':
            form = Scorecom2Form(request.POST, instance=list)
            if form.is_valid():
                test = form.save(commit=False)
                point = test.sc1 + test.sc2 + test.sc3 + test.sc4 + \
                    test.sc5 + test.sc6 + test.sc7 + test.sc8
                test.score = point
                fin = test.save()
                ScoreModel.objects.filter(project=test.project,subject = test.subject).update(
                    com2sc=point
                )
            else:
                print("Error", form.errors)
        context = {'form': form, 'show': show}

    return render(request, 'score.html', context)

def score1(request, pk):
    con = ProjectModel.objects.filter(
        consult=request.user.profmodel, status='อนุมัติ')
    com1 = ProjectModel.objects.filter(
        committee1=request.user.profmodel, status='อนุมัติ')
    check = SubjectModel.objects.all().order_by('-id')
    if con:
        con = ProjectModel.objects.filter(
            consult=request.user.profmodel, status='อนุมัติ').get()
        list = ScoreConsult.objects.filter(project=con,subject=check[1]).get()
        show = ScoreConsult.objects.filter(project=con,subject=check[1])
        form = ScoreconsultForm(instance=list)
        if request.method == 'POST':
            form = ScoreconsultForm(request.POST, instance=list)
            if form.is_valid():
                test = form.save(commit=False)
                point = test.sc1 + test.sc2 + test.sc3 + test.sc4 + \
                    test.sc5 + test.sc6 + test.sc7 + test.sc8
                test.score = point
                fin = test.save()
                ScoreModel.objects.filter(project=test.project,subject = test.subject).update(
                    consc=point
                )
            else:
                print("Error", form.errors)
        context = {'form': form, 'show': show}
    elif com1:
        com1 = ProjectModel.objects.filter(
            committee1=request.user.profmodel, status='อนุมัติ')
        list = ScoreCom1.objects.filter(project=com1,subject=check[1]).get()
        show = ScoreCom1.objects.filter(project=com1,subject=check[1])
        form = Scorecom1Form(instance=list)
        if request.method == 'POST':
            form = Scorecom1Form(request.POST, instance=list)
            if form.is_valid():
                test = form.save(commit=False)
                point = test.sc1 + test.sc2 + test.sc3 + test.sc4 + \
                    test.sc5 + test.sc6 + test.sc7 + test.sc8
                test.score = point
                fin = test.save()
                ScoreModel.objects.filter(project=test.project,subject = test.subject).update(
                    com1sc=point
                )
            else:
                print("Error", form.errors)
        context = {'form': form, 'show': show}
    else:
        com2 = ProjectModel.objects.filter(
            committee2=request.user.profmodel, status='อนุมัติ')
        list = ScoreCom2.objects.filter(project=com2,subject=check[1]).get()
        show = ScoreCom2.objects.filter(project=com2,subject=check[1])
        form = Scorecom2Form(instance=list)
        if request.method == 'POST':
            form = Scorecom2Form(request.POST, instance=list)
            if form.is_valid():
                test = form.save(commit=False)
                point = test.sc1 + test.sc2 + test.sc3 + test.sc4 + \
                    test.sc5 + test.sc6 + test.sc7 + test.sc8
                test.score = point
                fin = test.save()
                ScoreModel.objects.filter(project=test.project,subject = test.subject).update(
                    com2sc=point
                )
            else:
                print("Error", form.errors)
        context = {'form': form, 'show': show}

    return render(request, 'score.html', context)

def evaluate(request):
    sc = SubjectModel.objects.all().order_by('-id')
    prof = ProfModel.objects.all()
    can_show = 0
    term = 1
    date_now = date.today()
    if sc[0].startterm < date_now < sc[0].endterm :
        term = 2
    for ck in prof:
        if ck.user == request.user:
            can_show = 1
    if can_show == 1:
        show = ProjectModel.objects.filter(
            consult=request.user.profmodel, status='อนุมัติ')
        com = ProjectModel.objects.filter(
            Q(committee1=request.user.profmodel) | Q(committee2=request.user.profmodel), status='อนุมัติ')
        context = {'show': show, 'com': com, 'term':term}
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


def report_grade(request, pk):
    show = ScoreModel.objects.filter(std1=not None)
    i = ScoreModel.objects.get(id=pk)
    g = GradeModel.objects.get(subject=i.subject)
    if i.score > g.A:
        ScoreModel.objects.filter(project=i.project).update(
            grade='A'
        )
    elif g.A > i.score > g.Bplus:
        ScoreModel.objects.filter(project=i.project).update(
            grade='B+'
        )
    elif g.Bplus > i.score > g.B:
        ScoreModel.objects.filter(project=i.project).update(
            grade='B'
        )
    elif g.B > i.score > g.Cplus:
        ScoreModel.objects.filter(project=i.project).update(
            grade='C+'
        )
    elif g.Cplus > i.score > g.C:
        ScoreModel.objects.filter(project=i.project).update(
            grade='C'
        )
    elif g.C > i.score > g.Dplus:
        ScoreModel.objects.filter(project=i.project).update(
            grade='D+'
        )
    elif g.Dplus > i.score > g.D:
        ScoreModel.objects.filter(project=i.project).update(
            grade='D'
        )
    else:
        ScoreModel.objects.filter(project=i.project).update(
            grade='F'
        )

    return redirect('website:report_score')


def report_score(request):
    sc = SubjectModel.objects.all().order_by('-id')
    temp = ScoreModel.objects.all()
    term = 1
    date_now = date.today()
    if sc[0].startterm < date_now < sc[0].endterm :
        term = 2
    if term == 1 :
        show = ScoreModel.objects.filter(subject = sc[1])
    else:
        show = ScoreModel.objects.filter(subject = sc[0])
    for i in temp:
        sc = (i.consc + i.com1sc + i.com2sc)/3
        ScoreModel.objects.filter(project=i.project).update(
            score=sc
        )
    context = {'show': show}
    return render(request, 'report_score.html', context)


# ################# commiteee ###########################

def committee(request, pk):
    list = ProjectModel.objects.get(id=pk)
    form = CommitteeForm(instance=list)
    if request.method == 'POST':
        form = CommitteeForm(request.POST, instance=list)
        if form.is_valid():
            test = form.save(commit=False)
            test = test.save()
            return redirect('website:project')
    context = {'form': form, 'list': list}
    return render(request, 'committee.html', context)
