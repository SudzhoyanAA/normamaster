from django.contrib import admin

from .models import Order

from user.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_display_links = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_tags', 'author', 'cost', 'date')
    search_fields = ('cost', 'author__username')
    list_filter = ('author', 'tags')
    list_display_links = ('cost',)
    filter_horizontal = ('tags',)

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Тэг'
