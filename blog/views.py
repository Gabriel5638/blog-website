from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Post
from django.http import JsonResponse
from .forms import CommentForm, CreationForm


class PostList(generic.ListView):
    """
    Display a list of published posts ordered by the number of likes and date.
    """
    model = Post
    queryset = Post.objects.filter(status=1).annotate(
        like_count=Count('likes')).order_by("-like_count", "-created_on")
    template_name = "index.html"
    paginate_by = 6


class UserPosts(LoginRequiredMixin, generic.ListView):
    """
    Display a list of posts created by the current user.
    """
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'user_posts'
    paginate_by = 10

    def get_queryset(self):
        # Retrieve the posts created by the current user
        queryset = Post.objects.filter(
            author=self.request.user).order_by('-created_on')
        return queryset


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        # Add success message based on the like action
        if liked:
            messages.success(request, 'Post liked successfully!')
        else:
            messages.success(request, 'Post unliked successfully!')

        # Redirect back to the post detail page
        return redirect('post_detail', post_slug=slug)


class TrendingPosts(generic.ListView):
    """
    Display a list of posts ordered by the number of likes received.
    """
    model = Post
    template_name = "trending_posts.html"
    context_object_name = "trending_posts"
    paginate_by = 6

    def get_queryset(self):
        # Retrieve the posts ordered by the number of likes they have received
        queryset = Post.objects.annotate(num_likes=Count('likes')).filter(
            num_likes__gt=0).order_by('-num_likes')
        return queryset


class PostDetail(View):
    """
    Display a post and its details, along with comments and like status.
    Allow users to post comments on the current post.
    """

    def get(self, request, post_slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=post_slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = post.likes.filter(id=request.user.id).exists()
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
        liked = post.likes.filter(id=request.user.id).exists()
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.info(request, "Your comment has been submitted and is awaiting approval.")

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


def edit_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if request.method == 'POST':
        form = CreationForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post edited successfully!')
            return redirect('post_detail', post_slug=post.slug)
    else:
        form = CreationForm(instance=post)

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'edit_post.html', context)


class DeletePost(DeleteView):
    """
    Delete a post.
    """
    model = Post
    template_name = 'user_posts.html'
    success_message = 'Post has been successfully deleted.'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER') or reverse('home')

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)


def create_posts(request):
    if request.method == 'POST':
        postitem_form = CreationForm(request.POST, request.FILES)
        if postitem_form.is_valid():
            post = postitem_form.save(commit=False)
            post.author_id = request.user.id
            post.status = 1  # Set the default status to represent published
            post.save()
            messages.success(request, 'You have successfully posted an item!')
            category = post.category
            if category == 'sports':
                return redirect('sports')
            elif category == 'music':
                return redirect('music')
            elif category == 'art':
                return redirect('art')
            elif category == 'gaming':
                return redirect('gaming')
    else:
        postitem_form = CreationForm()

    context = {
        'postitem_form': postitem_form
    }

    return render(request, "create_posts.html", context)


def sports_view(request):
    sports_posts = Post.objects.filter(
        category='sports',
        status=1
    ).order_by('-created_on')

    paginator = Paginator(sports_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sports.html', {'page_obj': page_obj})


def music_view(request):
    music_posts = Post.objects.filter(
        category='music',
        status=1
    ).order_by('-created_on')

    paginator = Paginator(music_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'music.html', {'page_obj': page_obj})


def art_view(request):
    art_posts = Post.objects.filter(
        category='art',
        status=1
    ).order_by('-created_on')

    paginator = Paginator(art_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'art.html', {'page_obj': page_obj})


def gaming_view(request):
    gaming_posts = Post.objects.filter(
        category='gaming',
        status=1
    ).order_by('-created_on')

    paginator = Paginator(gaming_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gaming.html', {'page_obj': page_obj})
