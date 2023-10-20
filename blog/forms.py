from django import forms
from mailling.forms import StyleFormMixin
from blog.models import Blog


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('slug', 'is_published', 'views')
