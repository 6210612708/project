import email
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import json
import requests
from website.models import *
from website.decorator import *

from .models import Student
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('website:index')

    news = NewsModel.objects.all()
    context = {'news':news}
    return render(request, 'user/index.html' ,context)

@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('website:index')

        else:

            login_status = login_api(username, password)

            if login_status == 200:
                user = authenticate(
                    request, username=username, password=password)

                if not request.user.is_authenticated:
                    header = {
                        'Content-Type': 'application/json',
                        'Application-Key': 'TU240a80e5357e5d9279be402378381dfdfe126518202b4a6f5b30a4fb6218476b5ed6436d7a53ba7cc8009994e1ced28e'
                    }
                    pull_api = requests.get(
                        'https://restapi.tu.ac.th/api/v2/profile/std/info/?id='+str(username), headers=header)
                    data_student = json.loads(pull_api.content).get("data")
                    first_name, surname = (
                        data_student["displayname_th"]).split(" ")
                    email = data_student["email"]
                    # print(User.objects.all().username)
                    all_users = User.objects.values_list('username', flat=True)
                    print(username in list(all_users))
                    # print(all_users[]['username'])
                    if username not in list(all_users):
                        user = User.objects.create_user(username=username,
                                                        password=password,
                                                        first_name=first_name,
                                                        last_name=surname,
                                                        email=email)
                    user.save()

                if user is not None:
                    login(request, user)
                    return redirect("/")

            else:
                messages.info(request, "invalid Student ID or password")
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return redirect('user:index')


# login with tu api
def login_api(username, password):
    header = {
        'Content-Type': 'application/json',
        'Application-Key': 'TU240a80e5357e5d9279be402378381dfdfe126518202b4a6f5b30a4fb6218476b5ed6436d7a53ba7cc8009994e1ced28e'
    }

    body = {"UserName": username, "PassWord": password}

    res = requests.post(
        "https://restapi.tu.ac.th/api/v1/auth/Ad/verify", headers=header, json=body)

    return res.status_code