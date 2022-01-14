from django.contrib import admin
from .models import Category, Product, Ratings
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name','Image')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Category', 'Title', 'Description', 'Model', 'Image')
class RatingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review', 'rating', 'posted_on')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Ratings, RatingsAdmin)
