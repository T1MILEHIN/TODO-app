from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from .forms import Django_Created_Form
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class Registration_Form(FormView):
    form_class = Django_Created_Form
    template_name = 'user/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo:home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registration_Form, self).form_valid(form)



class Log_in_Form(LoginView):
    redirect_authenticated_user = True
    fields = '__all__'
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('todo:home')
    