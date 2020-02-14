from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
from .models import Book, Hero


class HeroInline(admin.StackedInline):
    model = Hero
    extra = 5


class HeroAdmin(ModelAdmin):
    list_display = ('name', 'gender', 'content', 'book')


admin.site.register(Hero, HeroAdmin)


class BookAdmin(ModelAdmin):
    list_display = ('title', 'price', 'pub_date')
    # list_per_page = 1
    search_fields = ('title', 'price')
    list_filter = ('title', 'price')
    inlines = [HeroInline]


admin.site.register(Book, BookAdmin)
