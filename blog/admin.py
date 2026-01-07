from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at',)


