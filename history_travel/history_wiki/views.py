from django.shortcuts import render

def index(request):
	return render(request, 'history_wiki/index.html', {})
