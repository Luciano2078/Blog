from django.contrib import admin

from .models import Post

from .formulario import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'author', 'created')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'author', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ['name', 'email', 'body']
    

admin.site.register(Post, PostAdmin)


