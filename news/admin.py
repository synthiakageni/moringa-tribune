from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Editor,Article,tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)


admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)


