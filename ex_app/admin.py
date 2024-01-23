from django.contrib import admin
from ex_app import models

# Register your models here.


admin.site.register(models.Type)
admin.site.register(models.Maker)

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
