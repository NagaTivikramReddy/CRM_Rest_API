
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.contrib.auth import login


def index(request):
    return render(request, 'CRM/index.html')


class CustomLoginView(LoginView):
    template_name = 'CRM/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class CustomRegister(CreateView):
    template_name = 'CRM/register.html'
    form_class = UserCreateForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')
