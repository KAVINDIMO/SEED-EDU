from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Onlinecourses(models.Model):
	name=models.CharField(max_length=150)
	description=models.CharField(max_length=1500)
	rating=models.FloatField(default=5,validators=[MaxValueValidator(5), MinValueValidator(0)])
	price=models.CharField(max_length=100)
	image=models.ImageField(upload_to='images',default='images/tst2.jpg')
	link=models.CharField(max_length=1000)

class Videos(models.Model):
	name=models.CharField(max_length=300)
	link=models.CharField(max_length=1000)
	grade=models.CharField(max_length=150)
	description=models.CharField(max_length=1500,blank=True)
	thumbnail=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Tips(models.Model):
	name=models.CharField(max_length=300)
	thumbnail=models.ImageField(upload_to='images',default='images/tst2.jpg')
	grade=models.IntegerField(default=12)
	link=models.CharField(max_length=1000,blank=True)
	isvideo=models.BooleanField(default=False)
	description=models.CharField(max_length=1500,blank=True)
	istext=models.BooleanField(default=False)
	tipfile=models.FileField(blank=True)
	isfile=models.BooleanField(default=False)

class Notes(models.Model):
	title=models.CharField(max_length=300)
	sub = models.CharField(max_length=100,default="maths")
	thumbnail=models.ImageField(upload_to='images',default='images/tst2.jpg')
	grade=models.IntegerField(default=10,validators=[MaxValueValidator(12), MinValueValidator(10)])
	file=models.FileField(upload_to='images',default="images/default.pdf")
