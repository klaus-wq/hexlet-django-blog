from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

# Register your models here.
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )  # Перечисляем поля, отображаемые в таблице списка статей
    search_fields = ["name", "body"]
    list_filter = (
        ("created_at", DateFieldListFilter),
    )  # Перечисляем поля для фильтрации

#admin.site.register(Article, ArticleAdmin)