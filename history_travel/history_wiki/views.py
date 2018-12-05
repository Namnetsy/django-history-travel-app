from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Post

POSTS_ON_ONE_PAGE = 2

def index(request):
	return render(request, 'history_wiki/index.html', {})

def posts_list(request, page_number):
	context = {}
	paginator = Paginator(Post.objects.all(), POSTS_ON_ONE_PAGE)

	try:
		page = paginator.page(page_number)
		context.update({'page': page.object_list})

		if paginator.page(page_number).has_next():
			context.update({'next_page': page_number + 1})
		else:
			context.update({'next_page': None})

		if paginator.page(page_number).has_previous():
			context.update({'previous_page': page_number - 1})
		else:
			context.update({'previous_page': None})
	except:
		context.update({'page': None})

	return render(request, 'history_wiki/posts_list.html', context)

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
