"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


app_name = "website" 
urlpatterns = [
    path('', views.index ,name='index' ),

    # todolist
    path('todolist/', views.todolist ,name='todolist'),
    path('todo_csv/', views.todo_csv ,name='todo_csv'),
    path('todolist/delete/<pk>', views.deletelist ,name='deletelist'),
    path('todolist/update/<pk>', views.updatelist ,name='updatelist'),

    # COOR plan
    path('coorplan/', views.coorplan ,name='coorplan'),
    path('coorplan_csv/', views.coorplan_csv ,name='coorplan_csv'),
    path('coorplan/delete/<pk>', views.deletecoorplan ,name='deletecoorplan'),
    path('coorplan/update/<pk>', views.updatecoorplan ,name='updatecoorplan'),

    # COM plan
    path('complan/', views.complan ,name='complan'),
    path('complan_csv/', views.complan_csv ,name='complan_csv'),
    path('complan/delete/<pk>', views.deletecomplan ,name='deletecomplan'),
    path('complan/update/<pk>', views.updatecomplan ,name='updatecomplan'),

    # CON plan
    path('profplan/', views.profplan ,name='profplan'),
    path('profplan_csv/', views.profplan_csv ,name='profplan_csv'),
    path('profplan/delete/<pk>', views.deleteprofplan ,name='deleteprofplan'),
    path('profplan/update/<pk>', views.updateprofplan ,name='updateprofplan'),

    # STD plan
    path('stdplan/', views.stdplan ,name='stdplan'),
    path('stdplan_csv/', views.stdplan_csv ,name='stdplan_csv'),
    path('stdplan/delete/<pk>', views.deletestdplan ,name='deletestdplan'),
    path('stdplan/update/<pk>', views.updatestdplan ,name='updatestdplan'),

    # news
    path('news/', views.news ,name='news'),
    path('news_csv/', views.news_csv ,name='news_csv'),
    path('news/delete/<pk>', views.deletenews ,name='deletenews'),
    path('news/update/<pk>', views.updatenews ,name='updatenews'),
    path('news/<pk>', views.news_detail, name="news_detail"),

    # Document
    path('document/', views.document ,name='document'),
    path('document/delete/<pk>', views.deletedoc ,name='deletedoc'),
    path('document/<pk>', views.doc_detail, name="doc_detail"),


    # Professor
    path('prof/', views.prof ,name='prof'),
    path('prof_csv/', views.prof_csv ,name='prof_csv'),
    path('prof/delete/<pk>', views.deleteprof ,name='deleteprof'),
    path('prof/update/<pk>', views.updateprof ,name='updateprof'),


    # OTHER
    path('other/', views.other ,name='other'),
    path('other_csv/', views.other_csv ,name='other_csv'),
    path('other/delete/<pk>', views.deleteother ,name='deleteother'),
    path('other/update/<pk>', views.updateother ,name='updateother'),


    # Student
    path('std/', views.std ,name='std'),
    path('std_csv/', views.std_csv ,name='std_csv'),
    path('std/delete/<pk>', views.deletestd ,name='deletestd'),
    path('std/update/<pk>', views.updatestd ,name='updatestd'),


]
