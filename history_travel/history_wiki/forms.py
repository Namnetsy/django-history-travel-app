from django import forms

class Search(forms.Form):
	query = forms.CharField(
		max_length=300,
		widget=forms.TextInput(attrs={'placeholder':'Введіть пошуковий запит'})
	)
