from django.db import models

# Create your models here.
#category
#subcategory
#ads 
#slidder
#product
#brand 

class Category(models.Model):
	name=models.CharField(max_length=300)
	slug=models.TextField()
	status=models.CharField(max_length=500,blank = True,choices=(('active','Active'),('','Default')))
    

	def __str__(self):
		return self.name




class SubCategory(models.Model):
	name=models.CharField(max_length=300)
	category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
	slug=models.TextField()


	def __str__(self):
		return self.name
		


class Ads(models.Model):
	name=models.CharField(max_length=300)
	image=models.ImageField(upload_to='media')
	link=models.URLField(max_length=500,blank=True)
	rank=models.IntegerField()


	def __str__(self):
		return self.name
		

class Slidder(models.Model):
	name=models.CharField(max_length=300)
	image=models.ImageField(upload_to = 'media')
	status=models.CharField(max_length=500,blank = True,choices=(('active','Active'),('','Default')))
	rank=models.IntegerField()


	def __str__(self):
		return self.name
		

LABELS=(('offer','offer'),('new','new'),('hot','hot'),('','default'))
class Products(models.Model):
	name=models.CharField(max_length=300)
	image=models.ImageField(upload_to='media')
	discounted_price=models.IntegerField(default=0)
	price=models.IntegerField()
	category=models.ForeignKey(Category,on_delete=models.CASCADE,default=0)
	SubCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,default=0)
	description=models.TextField(blank=True)
	status=models.CharField(max_length=500,choices=(('active','Active'),('','Default')),default=0)
	labels=models.CharField(max_length=500,choices=LABELS,blank=True)
	slug=models.TextField(default=0)


	def __str__(self):
		return self.name
		

class Cart(models.Model):
	username=models.CharField(max_length=400)
	slug=models.TextField(max_length=400)
	items=models.ForeignKey(Products,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=1)
	checkout=models.BooleanField(default=False)
	total=models.IntegerField(default=0)

	def __str__(self):
		return self.username





	

	