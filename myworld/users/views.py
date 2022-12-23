from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# def profile(request):
#     """render profilepage"""
#     return render(request, 'users/home.html')

class SignUp(CreateView):
    """render signuppage with built-in django registration form"""
    form_class = UserCreationForm
    success_url = "/users/login"
    template_name = "/members/templates/signup.html"