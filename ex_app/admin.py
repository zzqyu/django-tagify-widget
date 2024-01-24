from django.contrib import admin
from ex_app import models
from django import forms
from tagify_widget.widgets import TagSelect

# Register your models here.


admin.site.register(models.Type)
admin.site.register(models.Maker)

class MyModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
        widgets = {
            'category': TagSelect(),
        }


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    form = MyModelForm
