from django.forms import ModelForm
from bow.models import Restaurant



class ResForm(ModelForm):
	class Meta:
		model = Restaurant
		fields = ['res_name']