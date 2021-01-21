from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'reddit/post_list.html',  {'posts': posts})
