from django import forms
from .models import News


class CategoryForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=200)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets = {
            'categories': forms.CheckboxSelectMultiple(
                attrs={'class': 'category-checkbox'}
            ),
            'created_at': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control',
                       'placeholder': 'Selecione a data'}
            ),
            'author': forms.Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione o autor'}
            ),
        }
