from django.http import HttpResponse
from django.shortcuts import render 
from .models import *

def index(request, parent_or_child = None, pk = None):
    
   categories = Category.objects.filter(parent = None)

   if parent_or_child is None:

      posts = Post.objects.all()

   elif parent_or_child == 'child':
      sub_cat = SubCategory.objects.get(pk = pk)
      posts = sub_cat.objects.post_set.all()

   elif parent_or_child == 'parent':
      posts = []
      sub_cats = SubCategory.objects.get(pk = pk).children.all()

      for sub_cat in sub_cats:
         po = sub_cat.post_set.all()
         posts += po
   else:
      posts = []






   context = {
       'categories': categories,
       'posts': posts
    }
  
   return render(request, 'post/index.html', context)
