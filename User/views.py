from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    myposts= Post.objects.all()
    print(myposts)
    return render(request,'user/index.html',{'myposts':myposts})

def post(request,id):
    post= Post.objects.filter(user=id)[0]
    print(post)
    return render(request,'user/post.html',{'post':post})