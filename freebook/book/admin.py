from django.contrib import admin
from book.models import E_book,Category
# Register your models here.
class EbookAdmin(admin.ModelAdmin):
	list_display = ['b_name','category','published']
	list_filter = ['b_name','category','published']
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(E_book,EbookAdmin)
admin.site.register(Category,CategoryAdmin)

