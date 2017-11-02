from django.contrib import admin

# Register your models here.

from blog.models import Article,Category,Tag

class ArticleAdmin (admin.ModelAdmin):
    list_display = ['title','uid','category','status','views','likes','topped','created_time','updated_time']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'pid','status','created_time','updated_time']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
