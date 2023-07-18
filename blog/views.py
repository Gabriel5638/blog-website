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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).annotate(like_count=Count('likes')).order_by("-like_count", "-created_on")
    template_name = "index.html"
    paginate_by = 6


class UserPosts(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'user_posts'
    paginate_by = 10

    def get_queryset(self):
        # Retrieve the posts created by the current user
        queryset = Post.objects.filter(author=self.request.user).order_by('-created_on')
        return queryset


class TrendingPosts(generic.ListView):
    model = Post
    template_name = "trending_posts.html"
    context_object_name = "trending_posts"
    paginate_by = 6

    def get_queryset(self):
        # Retrieve the posts ordered by the number of likes they have received
        queryset = Post.objects.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by('-num_likes')

        return queryset


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

            # Determine the category of the posted item
            category = post.category

            # Redirect to the respective category
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


class DeletePost(DeleteView):
    model = Post
    template_name = 'user_posts.html' 
    success_message = 'Post has been successfully deleted.'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER') or reverse('home')

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)


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

    paginator = Paginator(sports_posts, 6)  # Display 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sports.html', {'page_obj': page_obj})


def music_view(request):
    music_posts = Post.objects.filter(
        category='music',
        status=1
    ).order_by('-created_on')

    paginator = Paginator(music_posts, 6)  # Display 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'music.html', {'page_obj': page_obj})


def art_view(request):
    art_posts = Post.objects.filter(
        category='art',
        status=1
    ).order_by('-created_on')

    paginator = Paginator(art_posts, 6)  # Display 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'art.html', {'page_obj': page_obj})


def gaming_view(request):
    gaming_posts = Post.objects.filter(
        category='gaming',
        status=1
    ).order_by('-created_on')

    paginator = Paginator(gaming_posts, 6)  # Display 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gaming.html', {'page_obj': page_obj})