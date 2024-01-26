
# Django Tagify Widget

This is a Django widget that integrates with `tagify.js` to provide tagging functionality in Django forms.

## Features

- Integrates seamlessly with Django forms.
- Uses `tagify.js` for a sleek, modern UI.

## Installation

You can install `django-tagify-widget` using pip:

```bash
pip install django-tagify-widget
```
# Requirements
- Django 2.0.0 or higher
- Python 3 or higher

# Usage

To use the ```django-tagify-widget``` in your Django project, simply import it in your forms and use it as you would any standard Django form widget.Example

Here's a simple example of how to use it in a Django form:python
```python
from django import forms
from django.db import models
from tagify_widget.widgets import TagSelect, TagSelectMultiple


# ex_app/models.py of this repogitory
class Book(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    name = models.CharField(max_length=50);
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES);
    category = models.ForeignKey(
        Type,
        on_delete=models.CASCADE
    )
    makers = models.ManyToManyField(Maker)

    def __str__(self) -> str:
        return self.name


# ex_app/admin.py of this repogitory
class MyModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'gender': TagSelect(),
            'category': TagSelect(),
            'makers': TagSelectMultiple(),
        }
```

# Contributing

Contributions to ```django-tagify-widget``` are welcome! Please refer to the [GitHub repository](https://github.com/zzqyu/django-tagify-widget) for more details.Author
- zzqyu
- Email: [wjdrb0626@naver.com]()

# License

This project is licensed under the MIT License 