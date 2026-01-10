from django.contrib import admin
from .models import Article

# Register your models
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'author')
    ordering = ('-date_posted',)


admin.site.register(Article, ArticleAdmin)


