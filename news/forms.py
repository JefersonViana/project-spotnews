from django import forms
from .models import News


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Nome'
        self.fields['title'].widget = forms.TextInput(
            attrs={'type': 'text', 'name': 'name', 'maxlength': '200'}
        )
        self.fields['created_at'].widget = forms.DateInput(
            attrs={'type': 'date', 'name': 'created_at'}
        )
