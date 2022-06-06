from django.contrib import admin
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('producer', 'slug', 'region',)
    search_fields = ['producer', 'flavournotes']
    list_filter = ('producer','region', 'variety','process')
    prepopulated_fields = {'slug': ('producer',)}
