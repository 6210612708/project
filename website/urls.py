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

    # news
    path('news/', views.news ,name='news'),
    path('news_csv/', views.news_csv ,name='news_csv'),
    path('news/delete/<pk>', views.deletenews ,name='deletenews'),
    path('news/update/<pk>', views.updatenews ,name='updatenews'),
    path('news/<pk>', views.news_detail, name="news_detail"),

    # Document
    path('document/', views.document ,name='document'),
    # path('document/delete/<pk>', views.deletedoc ,name='deletenews'),
    path('document/<pk>', views.doc_detail, name="doc_detail"),


]
