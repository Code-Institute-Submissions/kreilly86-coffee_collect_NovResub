from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['region', 'producer', 'process', 'variety', 'flavournotes']
    prepopulated_fields = {'slug': ('producer',)}
    list_filter = ('region', 'producer', 'process', 'variety', 'flavournotes')
    summernote_fields = ('region', 'producer', 'process', 'variety', 'flavournotes')
