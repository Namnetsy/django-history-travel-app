from django.shortcuts import render, get_object_or_404
from .models import Category, Post

def index(request):
	return render(request, 'history_wiki/index.html', {})

def categories(request):
	categories = Category.objects.values()
	context = {
		'categories': categories,
	}

	return render(request, 'history_wiki/categories.html', context)

def category(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	posts = {}

	for post in Post.objects.all():
		if post.category == category:
			posts.update({post.id: post})

	context = {
		'category_name': category.name,
		'posts': posts,
	}

	return render(request, 'history_wiki/category.html', context)
