from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})
def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})   


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"     
