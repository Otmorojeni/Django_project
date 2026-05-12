from django.contrib import admin
from .models import Theme, Brand, Kit, Review


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = (
        'article',
        'name',
        'theme',
        'details_count',
        'release_year',
        'price'
    )
    list_filter = ('theme', 'details_count')
    search_fields = ('name', 'article')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'kit',
        'reviewer_name',
        'rating',
        'comment',
        'created_at'
    )
    list_filter = ('rating', 'created_at')
    search_fields = ('reviewer_name', 'kit__name')