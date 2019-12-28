from django.contrib import admin

from .models import *


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher']


class CatalogInline(admin.TabularInline):
    model = Catalog
    extra = 1


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = (CatalogInline,)


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Shop, ShopAdmin)
