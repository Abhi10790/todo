from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Task,Accounts

class TaskList(LoginRequiredMixin, ListView):
    model=Task
    context_object_name="task"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['task']=context['task'].filter(username=self.request.user)
        #context['count']=context['task'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model=Task 
    context_object_name="task"   

class TaskCreate(LoginRequiredMixin, CreateView):     

    model=Task
    fields=['username','title','description','complete']
    success_url=reverse_lazy('task') 

    def form_invalid(self,form):        
        obj = super(TaskCreate,self).save(form)
        if self.request:
           obj.instance.username = self.request.user
        obj.save()
        return obj





class TaskUpdate(LoginRequiredMixin, UpdateView):
    model=Task
    fields=fields=['title','description','complete']
    success_url=reverse_lazy('task') 

class TaskDelete(LoginRequiredMixin, DeleteView):
    model=Task
    
    success_url=reverse_lazy('task') 


class CustomLoginView(LoginView):
    template_name="app/login.html"
    fields="__all__"
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('task')   

class CustomSignUpView(CreateView):
    model=Accounts
    fields="__all__"
    template_name="app/registration.html"
    success_url = reverse_lazy('signup')

    def get_success_url(self):
        return reverse_lazy('task')   

   