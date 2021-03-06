from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Post
from .forms import Search

POSTS_ON_ONE_PAGE = 4

def index(request):
	context = {}

	paginator = Paginator(Post.objects.all(), POSTS_ON_ONE_PAGE)
	page_number = 1

	try:
		page = paginator.page(1)

		context.update({'page': page.object_list})

		if paginator.page(page_number).has_next():
			context.update({'next_page': page_number + 1})
		else:
			context.update({'next_page': None})
	except:
		context.update({'page': None})

	return render(request, 'history_wiki/index.html', context)

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

	return render(request, 'history_wiki/posts-list.html', context)

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

def post(request, id):
	post = get_object_or_404(Post, id=id)

	context = {
		'post': post,
	}

	return render(request, 'history_wiki/opened-article.html', context)

def about(request):
	return render(request, 'history_wiki/about-us.html', {})

def search(request):
	context = {}
	output = None
	count_searched_posts = None

	if request.method == 'GET':
		form = Search(request.GET)

		if form.is_valid():
			result = Post.objects.filter(title__icontains=form.cleaned_data['query'])
			output = result
			count_searched_posts = len(result)
		else:
			form = Search()

		context.update({
			'form': form,
			'output': output,
			'count_searched_posts': count_searched_posts,
		})

	return render(request, 'history_wiki/search.html', context)
