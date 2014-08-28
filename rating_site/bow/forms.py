from django.forms import ModelForm
from bow.models import Restaurant,User


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['name','email']


class ResForm(ModelForm):
	class Meta:
		model = Restaurant
		fields = ['res_name']