from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'description', 'text', 'thumbnail', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
            # autocomplete - это заполнение браузером старыми значениями


class PostUpdateForm(PostCreateForm):
    class Meta:
        model = Post
        fields = PostCreateForm.Meta.fields + ('fixed', )
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2, "class": "form-control mb-1"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fixed'].widget.attrs.update({'class': 'form-check-input'})

