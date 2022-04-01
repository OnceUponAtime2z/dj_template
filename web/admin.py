from django.contrib import admin
from web.models import Blog, Author

# Register your models here.
# admin.site.register(Blog)
# admin.site.register(Author)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_created']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['prefix', 'first_name', 'last_name', 'dateofbirth']

    

    
