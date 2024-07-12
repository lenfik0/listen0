from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import UserSignUpForm
from django.urls import reverse_lazy

class UserCreationView(CreateView):
    form_class = UserSignUpForm #Какую форму использовать в представлении(Views).
    success_url = reverse_lazy('login') #После отправки формы перенаправить на страницу логина.
    template_name = 'accounts/signup.html' #Меняем страндартный путь шаблона.


































