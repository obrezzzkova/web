from django.contrib import admin
from .models import Post, Comment




# Register your models here.
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title','author')
    list_filter = ('title','author')
    date_hierarchy = ('published_date')
    ordering = ('published_date','author')

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('author_name', 'created_date' )
#     list_filter = ('author', 'createdd_date')
#
#
#
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
