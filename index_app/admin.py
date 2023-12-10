from django.contrib import admin
from index_app.models import MarkdownFilePool

# Register your models here.
class MarkdownFile(admin.ModelAdmin):
    pass


admin.site.register(MarkdownFilePool, MarkdownFile)