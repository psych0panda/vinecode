from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ('date_create', 'date', 'score', 'price')
    search_fields = ('wine', 'owner')
    prepopulated_fields = {'slug': ('wine',)}
    raw_id_fields = ('owner',)
    date_hierarchy = 'date_create'

