from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['region', 'producer', 'process', 'variety', 'flavournotes']
    prepopulated_fields = {'slug': ('producer',)}
    list_filter = ('region', 'producer', 'process', 'variety', 'flavournotes')
    summernote_fields = ('region', 'producer', 'process', 'variety', 'flavournotes')
