from django.contrib import admin
from .models import Person, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'information', 'date']
    list_filter = ['date', 'name']
    search_fields = ['id']
    inlines = [CommentInline]
admin.site.register(Person, PersonAdmin)
