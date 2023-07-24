from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.

class Home_Page(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'app/index.html'
    context_object_name = 'todos'

    
    def get(self, request):
        search_query = request.GET.get('todo')

        if search_query:
            todos = self.model.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        else:
            todos = self.model.objects.filter(user=self.request.user)

        context = {
            'todos': todos,
        }

        return render(request, self.template_name, context)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["todos"] = context["todos"].filter(user=self.request.user)
    #     return context
    
class Todo_Create_view(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'content', 'complete']
    template_name = "app/create-todo.html"
    success_url = reverse_lazy('todo:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Todo_Create_view, self).form_valid(form)

class Todo_Update_View(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'content', 'complete']
    template_name = "app/update-todo.html"
    success_url = reverse_lazy('todo:home')

class Todo_Delete_View(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'item'
    template_name = "app/confirm-delete.html"
    success_url = reverse_lazy('todo:home')    