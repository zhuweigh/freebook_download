from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name
	
class E_book(models.Model):
	bname = models.CharField(max_length=20)
	published = models.DateTimeField(auto_now_add=True)
	isbn = models.CharField(max_length=10)
	pages = models.IntegerField()
	language = models.Field(max_length=20)
	year = models.CharField(max_length=20)
	filesize = models.CharField(max_length=10)
	fileformat = models.CharField(max_length=20)
	category = models.ForeignKey(Category,related_name="c_books")
	description = models.TextField()
	def __str__(self):
		return self.b_name
