from .models import Comment
from django import forms
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


class CreationForm(forms.ModelForm):
    image_caption = forms.CharField(max_length=200)
    
    class Meta:
        model = Post
        fields = (
            'title',
            'featured_image',
            'content',
            'category',
        )

    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)