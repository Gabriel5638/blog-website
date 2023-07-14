from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, CreationForm
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, post_slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=post_slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')


def post(self, request, post_slug, *args, **kwargs):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=post_slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    liked = False
    if post.likes.filter(id=self.request.user.id).exists():
        liked = True

    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "comments": comments,
            "commented": True,
            "comment_form": comment_form,
            "liked": liked,
        },
    )


@login_required
def create_posts(request):
    if request.method == 'POST':
        postitem_form = CreationForm(request.POST, request.FILES)
        if postitem_form.is_valid():
            post = postitem_form.save(commit=False)
            post.author_id = request.user.id
            post.status = 1
            post.save()
            messages.success(request, 'You have successfully posted an item!')
            return redirect('home')
    else:
        postitem_form = CreationForm()

    context = {
        'postitem_form': postitem_form
    }

    return render(request, "create_posts.html", context)


class PostLike(View):
    def post(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=post_slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[post_slug]))


def sports_view(request):
    sports_posts = Post.objects.filter(
        category='sports',
        status=1
    ).order_by('-created_on')
    return render(request, 'sports.html', {'posts': sports_posts})


def music_view(request):
    music_posts = Post.objects.filter(
        category='music',
        status=1
    ).order_by('-created_on')
    return render(request, 'music.html', {'posts': music_posts})


def art_view(request):
    art_posts = Post.objects.filter(
        category='art',
        status=1
    ).order_by('-created_on')
    return render(request, 'art.html', {'posts': art_posts})


def gaming_view(request):
    gaming_posts = Post.objects.filter(
        category='gaming',
        status=1
    ).order_by('-created_on')
    return render(request, 'gaming.html', {'posts': gaming_posts})