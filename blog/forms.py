from django import forms
from .models import Post1


class Postform(forms.ModelForm):
    class Meta :
        model = Post1
        fields = ('title', 'text',)