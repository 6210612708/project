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

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('website:index')

    news = NewsModel.objects.all()
    context = {'news': news}
    return render(request, 'user/index.html', context)


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
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
                    if username.isnumeric():    
                        pull_api = requests.get(
                            'https://restapi.tu.ac.th/api/v2/profile/std/info/?id='+str(username), headers=header)
                        data_student = json.loads(pull_api.content).get("data")
                        first_name, surname = (
                            data_student["displayname_th"]).split(" ")
                        email = data_student["email"]
                        all_users = User.objects.values_list('username', flat=True)

                        if username not in list(all_users):
                            user = User.objects.create_user(username=username,
                                                            password=password,
                                                            first_name=first_name,
                                                            last_name=surname,
                                                            email=email
                                                            )
                            user.save()
                        group = Group.objects.get(name='student')
                        user.groups.add(group)
                        StdModel.objects.filter(stdid = user.username).update(
                            user=user
                        )
                    else:
                        pull_api = requests.get(
                            'https://restapi.tu.ac.th/api/v2/profile/emp/info/?username='+str(username), headers=header)
                        data = json.loads(pull_api.content).get("data")
                        first_name, surname = (
                            data["displayname_th"]).split(" ")
                        email = data_student["email"]
                        all_users = User.objects.values_list('username', flat=True)

                        if username not in list(all_users):
                            user = User.objects.create_user(username=username,
                                                            password=password,
                                                            first_name=first_name,
                                                            last_name=surname,
                                                            email=email
                                                            )
                            user.save()
                        group = Group.objects.get(name='consultant')
                        user.groups.add(group)
                        OtherModel.objects.filter(stdid = user.username).update(
                            user=user
                        )
                
                
                if user is not None:
                    login(request, user)
                    return redirect("/")

            else:
                login_status = login_engr(username, password)

                if login_status.status_code == 200:
                    
                    all_users = User.objects.values_list('username', flat=True)
                    if username not in list(all_users):
                        user = User.objects.create_user(username=username,
                                                        password=password,
                                                        )
                        user.save()
                        
                    if user.username.isnumeric():
                        group = Group.objects.get(name='student')
                        user.groups.add(group)
                        StdModel.objects.filter(stdid = user.username).update(
                            user=user
                        )
                            
                    else:
                        group = Group.objects.get(name='consultant')
                        user.groups.add(group)                        

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


def login_engr(username, password):

    body = {"username": username, "password": password}

    res = requests.post(
        "https://restapi.engr.tu.ac.th/api/v1/authentication/", json=body)
    # print(res)

    return res