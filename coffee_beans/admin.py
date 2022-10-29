from django.contrib import admin
from .models import Coffee


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('producer', 'slug', 'region',)
    search_fields = ['producer', 'flavournotes']
    list_filter = ('producer', 'region', 'variety', 'process', 'approved',)
    prepopulated_fields = {'slug': ('producer',)}
    actions = ['approve_coffee']

    def approve_coffee(self, request, coffee_entry):
        coffee_entry.update(approved=True)
