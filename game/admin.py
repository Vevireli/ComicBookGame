from django.contrib import admin
from .models import Panel, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    fk_name = "from_panel"
    extra = 2
    autocomplete_fields = ["to_panel"]


@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    list_display = ["number", "title", "is_start", "is_end", "image"]
    list_filter = ["is_start", "is_end"]
    search_fields = ["number", "title", "description"]
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["from_panel", "to_panel", "text", "condition"]
    list_filter = ["from_panel"]
    search_fields = ["text", "condition"]
    autocomplete_fields = ["from_panel", "to_panel"]