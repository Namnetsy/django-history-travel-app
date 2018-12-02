from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group

from . import forms

def sign_up(request):
	context = {}
	form = None

	if request.method == 'POST':
		form = forms.SignUp(request.POST)

		if form.is_valid(): # TODO: check if the user exist
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			password_again = form.cleaned_data['password_again']

			if password == password_again:
				user = User.objects.create_user(username, email, password)
				user.first_name = first_name
				user.last_name = last_name

				try:
					group = Group.objects.get(name='Users')
				except Group.DoesNotExist:
					group = None

				if group != None:
					group.user_set.add(user)

					user.save()

					return HttpResponseRedirect('/account/sign_in/')
				else:
					context.update({'error': 'We\'re sorry. Server doesn\'t register your account, try later.'})
			else:
				context.update({'error': 'Passwords do not match!'})
	else:
		form = forms.SignUp()

	context.update({'form': form})

	return render(request, 'auth_wiki/sign_up.html', context)

def sign_in(request):
	return render(request, 'auth_wiki/sign_in.html', {})
