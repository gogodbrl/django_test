# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post1
from django.utils import timezone
from .forms import Postform
from django.http import JsonResponse
import json
import numpy as np
from django.contrib.auth.decorators import login_required
import os



# Create your views here.
def post_list(request):
    posts = Post1.objects.filter().order_by('id').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post1, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request) :
    if request.method == "POST" :
        form = Postform(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :
        form = Postform()
    return render(request, 'blog/post_edit.html', {'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post1, pk=pk)
    if request.method =="POST" :
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :
        form = Postform(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def data(request):
    x = np.array(['20170710', '20170711', '20170712', '20170713', '20170714'])
    y = np.array([58.13, 53.98, 67.00, 89.70, 99.00])
    
    myData = json.dumps([{"date":x[i], "close":y[i]} for i in range(5)])    
    return JsonResponse(myData, safe=False)

def countries(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_data = open(os.path.join(BASE_DIR,'blog','static','json','countries.json')).read()
    data = json.loads(json_data)
    return JsonResponse(data, safe=False)

def d3sample(request):
    return render(request, 'blog/d3sample.html', {})
    
def d3test(request):
    return render(request, 'blog/d3test.html', {})

def post_draft_list(request):
    posts = Post1.objects.filter(publish_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

def post_publish(request, pk):
    post = get_object_or_404(Post1, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()
    
def post_remove(request, pk):
    post = get_object_or_404(Post1, pk=pk)
    post.delete()
    return redirect('post_list')    
    