from django.shortcuts import render
from pyexpat.errors import messages

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

# Create your views here.
class UserListApiview(APIView):

    Permission_classes =  [permissions.AllowAny]

    def submit_user_form (
            request,
            ):
        if request.method == "POST":
            username = request.POST.get("username")
            if User.objects.filter(username=username).exists():
                return render(request,"username allready exsist")
            else:
                frist_name = request.POST.get("frist_name")
                last_name = request.POST.get("last_name")
                username = request.POST.get("username")
                email = request.POST.get("email")
    
    def home(request):
        message = "Welcome to my Django project!"
        return render(request, 'home.html', {'message': message})
    

    def user_login(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page after successful login
            else:
                messages.error(request, 'Invalid username or password')
        return render(request, 'login.html')
    
    