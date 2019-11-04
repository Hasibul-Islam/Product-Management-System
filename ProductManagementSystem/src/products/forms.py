from django.forms import ModelForm, TextInput
from .models import Order


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = "__all__"
		widgets ={
			'color':TextInput(attrs={'type':'color'}),
			'order_date':TextInput(attrs={'type':'date'}),
			'delivery_date':TextInput(attrs={'type':'date'}),
		}