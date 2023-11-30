from django import forms
from .models import News, Category, User


class CreateCategoriesModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Nome'
        self.fields['name'].widget = forms.TextInput(
            attrs={'type': 'text', 'maxlength': '200'}
        )


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        exclude = ['categories']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Título'
        self.fields['title'].widget = forms.TextInput(
            attrs={'type': 'text', 'name': 'title', 'maxlength': '200'}
        )
        self.fields['content'].label = 'Conteúdo'
        self.fields['content'].widget = forms.Textarea(
            attrs={'type': 'text', 'name': 'content', 'maxlength': '200'}
        )
        self.fields['author'].label = 'Autoria'
        self.fields['author'].widget = forms.Select(
            attrs={'type': 'text', 'name': 'author', 'maxlength': '200'},
            choices=[(user.id, user.name) for user in User.objects.all()]
        )
        self.fields['created_at'].label = 'Criado em'
        self.fields['created_at'].widget = forms.DateInput(
            attrs={'type': 'date', 'name': 'created_at', 'maxlength': '200'}
        )
        self.fields['image'].label = 'URL da Imagem'
        self.fields['image'].widget = forms.FileInput(
            attrs={'type': 'file', 'name': 'image', 'maxlength': '200'}
        )

        self.fields['categories'] = forms.ModelMultipleChoiceField(
            label='categories',
            queryset=Category.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=True,
        )
