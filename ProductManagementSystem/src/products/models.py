from django.db import models

# Create your models here.

class ProductType(models.Model):
	product_type = models.CharField(max_length=100, unique=True)
	unit_price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.product_type

class Order(models.Model):
	buyer_name = models.CharField(max_length=100)
	company_name = models.CharField(max_length=200)
	company_address = models.TextField()
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	height = models.DecimalField(max_digits=5, decimal_places=2)
	wighth = models.DecimalField(max_digits=5, decimal_places=2)
	style = models.CharField(max_length=100, null=True, blank=True)
	color = models.CharField(max_length=100)
	amount = models.PositiveIntegerField()
	cotton = models.PositiveIntegerField(null=True, blank=True)
	asking_price = models.PositiveIntegerField()
	order_date = models.DateField()
	delivery_date = models.DateField(null=True, blank=True)

	def __str__(self):
		return str(self.id)


class Costing(models.Model):
	invoic_number = models.OneToOneField(Order, on_delete=models.CASCADE)
	collar = models.PositiveIntegerField(default=0)
	cutting = models.PositiveIntegerField(default=0)
	dying = models.PositiveIntegerField(default=0)
	washing = models.PositiveIntegerField(default=0)
	others = models.PositiveIntegerField(default=0)
	collar_unit_price = models.PositiveIntegerField(default=0)
	cutting_unit_price = models.PositiveIntegerField(default=0)
	dying_unit_price = models.PositiveIntegerField(default=0)
	washing_unit_price = models.PositiveIntegerField(default=0)
	others_price = models.PositiveIntegerField(default=0)
	total_price = models.PositiveIntegerField(default=0)
	total_profit = models.IntegerField(default=0)


	def __str__(self):
		return str(self.invoic_number)


YEAR_CHOICE = (
	("2018","2018"),
	("2019","2019"),
	("2020","2020")
	)


class YearlyProfit(models.Model):
	year = models.CharField(max_length=10,choices=YEAR_CHOICE)
	january = models.IntegerField(default=0)
	february = models.IntegerField(default=0)
	march = models.IntegerField(default=0)
	april = models.IntegerField(default=0)
	may = models.IntegerField(default=0)
	june = models.IntegerField(default=0)
	july = models.IntegerField(default=0)
	august = models.IntegerField(default=0)
	september = models.IntegerField(default=0)
	october = models.IntegerField(default=0)
	november = models.IntegerField(default=0)
	december = models.IntegerField(default=0)
	total_month = models.IntegerField(default=0)

	def __str__(self):
		return str(self.year)