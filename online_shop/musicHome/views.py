from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegisterUserForm
from .models import *
from .utils import DataMixin

menu = [
    {'mtitle': 'MusicHome | Авторизация', 'url_name': 'log_in'},
    {'mtitle': '', 'url_name': 'home'},
    {'mtitle': 'Личный кабинет', 'url_name': 'admin_account'},
    {'mtitle': 'Личный кабинет', 'url_name': 'personal_account'},
    {'mtitle': 'Товары', 'url_name': 'products'},
    {'mtitle': 'Регистрация', 'url_name': 'registrate'},
    {'mtitle': 'Корзина', 'url_name': 'to_buy'}
]


#def log_in(request):
#    data = Users.objects.all()
 #   context1 = {
  #      'data': data,
  #      'title': 'MusicHome | Авторизация'
  #  }
  #  return render(request, 'musicHome/log_in.html', context=context1)


def home(request):
    context2 = {
        'title': 'MusicHome | Главная'
    }
    return render(request, 'musicHome/home.html', context=context2)


def admin_account(request):
    context3 = {
        'title': 'MusicHome | Личный кабинет админа'
    }
    return render(request, 'musicHome/admin_account.html', context=context3)


def personal_account(request):
    context4 = {
        'title': 'MusicHome | Личный кабинет покупателя'
    }
    return render(request, 'musicHome/personal_account.html', context=context4)


def products(request):
    context5 = {
        'title': 'MusicHome | Товары'
    }
    return render(request, 'musicHome/products.html', context=context5)


# def registrate(request):
#    context6 = {
#        'title': 'MusicHome | Регистрация'
#    }
#    return render(request, 'musicHome/registrate.html', context=context6)

def to_buy(request):
    context7 = {
        'title': 'MusicHome | Корзина'
    }
    return render(request, 'musicHome/to_buy.html', context=context7)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'musicHome/registrate.html'
    success_url = reverse_lazy('log_in/')

    def get_context_data(self, *, object_list=None, **kwards):
        context = super().get_context_data(**kwards)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('log_in')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'musicHome/log_in.html'

    def get_context_data(self, *, object_list=None, **kwards):
        context = super().get_context_data(**kwards)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')