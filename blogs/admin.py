from django.contrib import admin
from blogs.models import Category, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'created_on')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)