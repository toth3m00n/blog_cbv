from ckeditor.widgets import CKEditorWidget
from django import forms
from django_recaptcha.fields import ReCaptchaField

from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))

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


class CommentCreateForm(forms.ModelForm):
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={"rows": 5, "cols": 30, "placeholder": "Комментарий",
                                                           "class": "form-control"}))

    class Meta:
        model = Comment
        fields = ('content',)
