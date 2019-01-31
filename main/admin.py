from django.contrib import admin
from .models import Recipe
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title & Date", {
            "fields": ["title", "published"]
        }),
        ("Content", {
            "fields": ["content"]
        })
    ]

    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE()
        }
    }


admin.site.register(Recipe, RecipeAdmin)
