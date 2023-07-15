from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm
from .forms import CreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Count


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).annotate(like_count=Count('likes')).order_by("-like_count", "-created_on")
    template_name = "index.html"
    paginate_by = 6


class TrendingPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-likes')[:5]  
    template_name = 'trending_posts.html' 
    context_object_name = 'trending_posts' 


class PostDetail(View):
    def get(self, request, post_slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=post_slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Get the absolute URL of the current post
        post_url = request.build_absolute_uri(reverse('post_detail', args=[post.slug]))

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "post_url": post_url
            },
        )

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

        # Get the absolute URL of the current post
        post_url = request.build_absolute_uri(reverse('post_detail', args=[post.slug]))

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "post_url": post_url
            },
        )


def create_posts(request):
    if request.method == 'POST':
        postitem_form = CreationForm(request.POST, request.FILES)
        if postitem_form.is_valid():
            post = postitem_form.save(commit=False)
            post.author_id = request.user.id  
            post.status = 1  # Set the default status to represent published
            post.save()
            messages.success(request, 'You have successfully posted an item!')
            return redirect('home')
    else:
        postitem_form = CreationForm()

    context = {
        'postitem_form': postitem_form
    }

    return render(request, "create_posts.html", context)


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def about(request):
    return render(request, "about.html")


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


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