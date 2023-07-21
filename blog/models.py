from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

CATEGORIES = (
    ("sports", "Sports"),
    ("music", "Music"),
    ("art", "Art"),
    ("gaming", "Gaming"),
)


class Post(models.Model):
    """
    Represents a blog post.

    Fields:
    - title: The title of the post.
    - slug: The unique slug for the post's URL.
    - author: The author of the post (a foreign key to the User model).
    - featured_image: The featured image of the post.
    - excerpt: A brief summary or excerpt of the post.
    - updated_on: The date and time when the post was last updated.
    - content: The main content of the post.
    - created_on: The date and time when the post was created.
    - status: The status of the post (draft or published).
    - category: The category of the post.
    - likes: Users who liked the post.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image_caption = models.CharField(max_length=200, default='')
    image_credit = models.CharField(max_length=200, default=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    category = models.CharField(
        max_length=20, choices=CATEGORIES, default='sections'
    )
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Fields:
    - post: The related post (foreign key to the Post model).
    - name: The name of the commenter.
    - email: The email address of the commenter.
    - body: The content of the comment.
    - created_on: The date and time when the comment was created.
    - approved: Indicates whether the comment has been approved or not.
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
