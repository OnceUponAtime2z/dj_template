from django.contrib import admin
from web.models import Reporter, Article

@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['head_line', 'pub_date', 'reporter']
    


    


    

    
