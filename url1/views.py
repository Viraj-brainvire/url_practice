
from django.http import HttpResponse 
from django.shortcuts import render
from django.urls import reverse

from django.shortcuts import redirect
 
def my_view(request):
    return redirect(reverse('home'))

# Create your views here.
def home(request):
    return HttpResponse("welcome to our website")

def blog(request):
    return HttpResponse("Blog")

def blog_detail(request, blog_id):
    blog_post = {'id': blog_id, 'title': 'Sample Blog Post', 'content': 'This is the content of the blog post.'}
    context = {'blog_post': blog_post}
    return render(request, 'static_page/index.html', context)

def aboutus(request):
    return HttpResponse("About Us")

def aboutdetails(request,aboutusid):
    return HttpResponse(aboutusid)

def add(request,a,b):
    return HttpResponse(int (a) + int (b))


  