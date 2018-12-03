from django import forms

class SignUp(forms.Form):
	first_name = forms.CharField(required=True, max_length=30)
	last_name = forms.CharField(required=True, max_length=50)
	username = forms.CharField(required=True, max_length=20)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput, max_length=30, min_length=8)
	password_again = forms.CharField(widget=forms.PasswordInput, max_length=30, min_length=8)

class SignIn(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput, max_length=30, min_length=8)
