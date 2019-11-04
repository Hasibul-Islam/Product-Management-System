from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

from .models import Order, ProductType, Costing, YearlyProfit
from .forms import OrderForm


def home(request):
	return render(request, "home.html")


def product_analysis(request):
	data = {}
	products = ProductType.objects.all()
	total_amount = 0
	total_amount_li = []
	final_amount = 0
	final_amount_p = 0
	final_amount_px = []
	products_list = []
	for pro in products:
		products_list.append(pro.product_type)
		orders = Order.objects.filter(product_type=pro)
		for amount in orders:
			total_amount = total_amount + amount.amount
		total_amount_li.append(total_amount)
		total_amount = 0

	final_amount_p = sum(total_amount_li)

	for pp in total_amount_li:
		per = pp / final_amount_p * 100
		final_amount_px.append(per)


	data['product'] = products_list
	data['per'] = final_amount_px

	for pr in products:
		for p in final_amount_px:
			data[pr] = p

	context = {
		"products":products,
		"data":data
	}
	return render(request, "product/product_analysis.html", context)



def order_list(request):
	orders = Order.objects.all()
	context = {
		"orders":orders
	}
	return render(request, "order/list.html", context)



def product_list(request):
	products = ProductType.objects.all()
	context = {
		"products":products
	}
	return render(request, "product/list.html", context)


class ProductCreate(CreateView):
	model = ProductType
	template_name = 'product/create.html'
	fields = ['product_type','unit_price']
	success_url = '/products/list/'

	def form_valid(self,form):
		super(ProductCreate,self).form_valid(form)
		messages.success(self.request, 'Product successfully Created')
		return HttpResponseRedirect(self.get_success_url())

class OrderCreate(CreateView):
	model = Order
	template_name = 'order/create.html'
	form_class = OrderForm
	success_url = '/orders/list/'

	def form_valid(self,form):
		super(OrderCreate,self).form_valid(form)
		messages.success(self.request, 'Order successfully Created')
		return HttpResponseRedirect(self.get_success_url())

class Productupdate(UpdateView):
	model = ProductType
	template_name = 'product/create.html'
	fields = ['product_type','unit_price']
	success_url = '/products/list/'

	def form_valid(self,form):
		super(Productupdate,self).form_valid(form)
		messages.success(self.request, 'Product successfully Updated')
		return HttpResponseRedirect(self.get_success_url())

class Orderupdate(UpdateView):
	model = Order
	template_name = 'order/create.html'
	form_class = OrderForm
	success_url = '/orders/list/'

	def form_valid(self,form):
		super(Orderupdate,self).form_valid(form)
		messages.success(self.request, 'Order successfully Updated')
		return HttpResponseRedirect(self.get_success_url())

def product_delete(request,id):
	product = ProductType.objects.get(id=id)
	product.delete()
	messages.success(request, 'Successfully Deleted')
	return redirect("/products/list/")

def order_delete(request,id):
	order = Order.objects.get(id=id)
	order.delete()
	messages.success(request, 'Successfully Deleted')
	return redirect("/orders/list/")


def order_update_list(request):
	orders = Order.objects.all()
	context = {
		"orders":orders
	}
	return render(request, "order/list_edit.html", context)



def product_update_list(request):
	products = ProductType.objects.all()
	context = {
		"products":products
	}
	return render(request, "product/list_edit.html", context)


def order_delete_list(request):
	orders = Order.objects.all()
	context = {
		"orders":orders
	}
	return render(request, "order/list_delete.html", context)



def product_delete_list(request):
	products = ProductType.objects.all()
	context = {
		"products":products
	}
	return render(request, "product/list_delete.html", context)


def costing_list_update(request):
	costings = Costing.objects.all()
	context = {
		"costings":costings
	}
	return render(request, "costing/list.html", context)





class CostingCreate(CreateView):
	model = Costing
	template_name = 'costing/create.html'
	fields = [
		'invoic_number',
		'collar',
		'cutting',
		'dying',
		'washing',
		'others',
		'collar_unit_price',
		'cutting_unit_price',
		'dying_unit_price',
		'washing_unit_price',
		'others_price'
		]
	success_url = '/costing/update/'

	def form_valid(self,form):
		super(CostingCreate,self).form_valid(form)
		inv = Order.objects.get(id=int(form.instance.invoic_number.id))
		collar_price = form.instance.collar * form.instance.collar_unit_price
		cutting_price = form.instance.cutting * form.instance.cutting_unit_price
		dying_price = form.instance.dying * form.instance.dying_unit_price
		washing_price = form.instance.washing * form.instance.washing_unit_price
		others_price = form.instance.others * form.instance.others_price

		costing_price = collar_price + cutting_price + dying_price + washing_price + others_price
		product_unit_price = inv.product_type.unit_price
		order_price = inv.height * inv.wighth * inv.amount * product_unit_price

		profit = inv.amount * inv.asking_price
		total_cost = costing_price + order_price
		total_profit = profit - total_cost


		form.instance.total_price = total_cost
		form.instance.total_profit = total_profit
		form.instance.save()

		delevary_date = str(inv.delivery_date)[5:7]
		yp = YearlyProfit.objects.get(year="2018")
		print(yp)
		if int(delevary_date) == 1:
			yp.january = yp.january + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 2:
			yp.february = yp.february + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 3:
			yp.march = yp.march + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 4:
			yp.april = yp.april + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 5:
			yp.may = yp.may + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 6:
			yp.june = yp.june + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 7:
			yp.july = yp.july + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 8:
			yp.august = yp.august + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 9:
			yp.september = yp.september + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 10:
			yp.october = yp.october + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 11:
			yp.november = yp.november + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()
		elif int(delevary_date) == 12:
			yp.december = yp.december + total_profit
			yp.total_month = yp.total_month + total_profit
			yp.save()


		messages.success(self.request, 'Costing successfully Created')
		rurl = self.get_success_url() + str(form.instance.id) + "/"
		return HttpResponseRedirect(rurl)


class CostingUpdate(UpdateView):
	model = Costing
	template_name = 'costing/update.html'
	fields = '__all__'
	success_url = '/costing/update/'

	def form_valid(self,form):
		super(CostingUpdate,self).form_valid(form)
		inv = Order.objects.get(id=int(form.instance.invoic_number.id))
		collar_price = form.instance.collar * form.instance.collar_unit_price
		cutting_price = form.instance.cutting * form.instance.cutting_unit_price
		dying_price = form.instance.dying * form.instance.dying_unit_price
		washing_price = form.instance.washing * form.instance.washing_unit_price
		others_price = form.instance.others * form.instance.others_price

		costing_price = collar_price + cutting_price + dying_price + washing_price + others_price
		product_unit_price = inv.product_type.unit_price
		order_price = inv.height * inv.wighth * inv.amount * product_unit_price

		profit = inv.amount * inv.asking_price
		total_cost = costing_price + order_price
		total_profit = profit - total_cost

		form.instance.total_price = total_cost
		form.instance.total_profit = total_profit
		form.instance.save()

		messages.success(self.request, 'Costing successfully Updated')
		rurl = self.get_success_url() + str(form.instance.id) + "/"
		return HttpResponseRedirect(rurl)


def profit_list(request):
	profit = YearlyProfit.objects.get(year="2018")
	total = profit.total_month
	january = profit.january/total*100
	february = profit.february/total*100
	march = profit.march/total*100
	april = profit.april/total*100
	may = profit.may/total*100
	june = profit.june/total*100
	july = profit.july/total*100
	august = profit.august/total*100
	september = profit.september/total*100
	october = profit.october/total*100
	november = profit.november/total*100
	december = profit.december/total*100
	context = {
		"profit":profit,
		"january":january,
		"february":february,
		"march":march,
		"april":april,
		"may":may,
		"june":june,
		"july":july,
		"august":august,
		"september":september,
		"october":october,
		"november":november,
		"december":december,

	}
	return render(request, "profit/list.html", context)