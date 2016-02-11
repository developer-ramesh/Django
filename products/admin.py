from django.contrib import admin

from .models import Product , Menu

class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_text','product_desc','pub_date']

admin.site.register(Product,ProductAdmin)

class MenuAdmin(admin.ModelAdmin):
	list_display = ['menu_name','menu_price','user','image','pub_date']

	search_fields = ['menu_name','user',]

	list_filter = ['menu_name','user',]

admin.site.register(Menu,MenuAdmin)
