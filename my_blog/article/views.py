from django.shortcuts import render
from django.http import HttpResponse

from .models import ArticlePost

def hello_world(request):
	return HttpResponse("Hello World!")

def hello_world2(request):
	return HttpResponse("Hello World 2!")

def article_list(request):
	articles = ArticlePost.objects.all()	# 所有博客文章
	context = { 'articles': articles }	# context: 需要传递给templates的对象
	return render(request, 'article/list.html', context)	#模板: templates/article/list.html
