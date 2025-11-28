from django import forms

from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

        def clean_title(self):
            if (title := self.cleaned_data.get('title')).isupper():
                raise forms.ValidationError('Title cannot be all uppercase.')
            return title


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
