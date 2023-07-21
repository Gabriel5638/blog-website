from .models import Comment
from django import forms
from .models import Post


class CommentForm(forms.ModelForm):
    """
    Form for adding comments to a post.
    """
    class Meta:
        model = Comment
        fields = ("body",)


class CreationForm(forms.ModelForm):
    """
    Form for creating or editing a post.
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'featured_image',
            'content',
            'category',
        )

    def __init__(self, *args, **kwargs):
        """
        Initialize the CreationForm instance.
        """
        super(CreationForm, self).__init__(*args, **kwargs)
