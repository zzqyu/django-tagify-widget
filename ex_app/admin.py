from django.contrib import admin
from ex_app import models
from django import forms
from tagify_widget.widgets import TagSelect, TagSelectMultiple
from django.contrib.admin.views.main import ChangeList

# Register your models here.


admin.site.register(models.Type)
admin.site.register(models.Maker)

class MyModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
        widgets = {
            'gender': TagSelect(),
            'category': TagSelect(),
            'makers': TagSelectMultiple(),
        }

class MakerChangeList(ChangeList):

    def __init__(
        self,
        request,
        model,
        list_display,
        list_display_links,
        list_filter,
        date_hierarchy,
        search_fields,
        list_select_related,
        list_per_page,
        list_max_show_all,
        list_editable,
        model_admin,
        sortable_by,
        search_help_text,
    ):

        super().__init__(
            request,
            model,
            list_display,
            list_display_links,
            list_filter,
            date_hierarchy,
            search_fields,
            list_select_related,
            list_per_page,
            list_max_show_all,
            list_editable,
            model_admin,
            sortable_by,
            search_help_text
        )

        self.list_display = list(self.list_display) + ['makers']
        self.list_editable = list(self.list_editable) + ['makers']

class MakerChangeListForm(forms.ModelForm):
    makers = forms.ModelMultipleChoiceField(
        queryset=models.Maker.objects.all(), 
        required=True,
        widget=TagSelectMultiple()
    )


@admin.register(models.ProxyBook1)
class ProxyBook1Admin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'category')
    list_editable = ('gender', 'category')
    form = MyModelForm
    
    def get_changelist(self, request, **kwargs):
        return MakerChangeList

    def get_changelist_form(self, request, **kwargs):
        return MyModelForm
    
    def get_changelist_formset(self, request, **kwargs):
        from functools import partial
        from django.forms.models import modelformset_factory
        """
        Return a FormSet class for use on the changelist page if list_editable
        is used.
        """
        defaults = {
            "formfield_callback": partial(self.formfield_for_dbfield, request=request),
            **kwargs,
        }
        return modelformset_factory(
            self.model,
            self.get_changelist_form(request),
            extra=0,
            fields=self.get_changelist_instance(request).list_editable,
            **defaults,
        )
    

@admin.register(models.ProxyBook2)
class ProxyBook2Admin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'category')
    list_editable = ('gender', 'category')
    
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        form_field = super().formfield_for_choice_field(db_field, request, **kwargs)
        form_field.widget = TagSelect(choices=form_field.choices)
        return form_field

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        form_field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        form_field.widget = TagSelect()
        return form_field
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        form_field = super().formfield_for_manytomany(db_field, request, **kwargs)
        form_field.widget = TagSelectMultiple()
        form_field.help_text = ""
        return form_field
    
    def get_changelist(self, request, **kwargs):
        return MakerChangeList

    def get_changelist_form(self, request, **kwargs):
        return MakerChangeListForm
    
    def get_changelist_formset(self, request, **kwargs):
        from functools import partial
        from django.forms.models import modelformset_factory
        """
        Return a FormSet class for use on the changelist page if list_editable
        is used.
        """
        defaults = {
            "formfield_callback": partial(self.formfield_for_dbfield, request=request),
            **kwargs,
        }
        return modelformset_factory(
            self.model,
            self.get_changelist_form(request),
            extra=0,
            fields=self.get_changelist_instance(request).list_editable,
            **defaults,
        )
