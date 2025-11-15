from django import forms
from .models import Post, Comment



# class PostForm(forms.Form):
#     title = forms.CharField(label='Заголовок', max_length=255)
#     content = forms.CharField(label='Содержимое', widget=forms.Textarea)
#     rate = forms.IntegerField(label='Рейтинг', min_value=0, initial=0)
#     image = forms.ImageField(label='Изображение', required=False)



class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rate', 'image', 'category', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
            'tags': forms.CheckboxSelectMultiple(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2}),
        }
