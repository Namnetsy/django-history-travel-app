from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib import auth

from . import forms
from .models import Folk

MSG_USERNAME_ALREADY_EXIST = 'The username already exist!'
MSG_USER_GROUP_DOES_NOT_EXIST = 'We\'re sorry. Server cannot register your account, try later.'
MSG_PASSWORDS_DO_NOT_MATCH = 'Passwords do not match!'
MSG_LOGIN_ERROR = 'Login or password wrong!'

USER_GROUP_NAME = 'Newbies'
REDIRECT_AFTER_SIGNUP = '/account/sign_in/'
REDIRECT_AFTER_LOGIN = '/'
REDIRECT_IF_AUTHORIZED = '/'
REDIRECT_AFTER_LOGOUT = '/account/sign_in/'

def sign_up(request):
	context = {}
	form = None

	if request.user.is_authenticated:
		return HttpResponseRedirect(REDIRECT_IF_AUTHORIZED)

	if request.method == 'POST':
		form = forms.SignUp(request.POST)

		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			password_again = form.cleaned_data['password_again']

			try:
				if User.objects.get(username=username) != None:
					context.update({'error': MSG_USERNAME_ALREADY_EXIST})
			except User.DoesNotExist:
				if password == password_again:
					user = User.objects.create_user(username, email, password)
					user.first_name = first_name
					user.last_name = last_name

					try:
						group = Group.objects.get(name=USER_GROUP_NAME)
						group.user_set.add(user)
						user.save()

						Folk.objects.create(instance_user=user, avatar=None)

						return HttpResponseRedirect(REDIRECT_AFTER_SIGNUP)
					except Group.DoesNotExist:
						context.update({'error': MSG_USER_GROUP_DOES_NOT_EXIST})
				else:
					context.update({'error': MSG_PASSWORDS_DO_NOT_MATCH})
	else:
		form = forms.SignUp()

	context.update({'form': form})

	return render(request, 'auth_wiki/sign_up.html', context)

def sign_in(request):
	context = {}
	form = None

	if request.user.is_authenticated:
		return HttpResponseRedirect(REDIRECT_IF_AUTHORIZED)

	if request.method == 'POST':
		form = forms.SignIn(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			try:
				user = User.objects.get(email=email)

				if user.check_password(password):
					auth.login(request, user)

					return HttpResponseRedirect(REDIRECT_AFTER_LOGIN)
				else:
					context.update({'error': MSG_LOGIN_ERROR})
			except User.DoesNotExist:
				context.update({'error': MSG_LOGIN_ERROR })
	else:
		form = forms.SignIn()

	context.update({'form': form})

	return render(request, 'auth_wiki/sign_in.html', context)

def logout(request):
	auth.logout(request)

	return HttpResponseRedirect(REDIRECT_AFTER_LOGOUT)
