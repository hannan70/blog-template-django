from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post, Comment, Category
from .forms import CommentForm
from django.views import View
from django.db.models import Count
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def home_page(request):
    posts = Post.objects.annotate(total_comment=Count('comments'))

    # paginator
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    categories = Category.objects.all()
    popular_posts = Post.objects.filter(is_featured=True)
    resented_posts = Post.objects.order_by('-id')[:3]

    return render(request, 'pages/index.html',{
        'posts': posts,
        'categories': categories,
        'resented_posts': resented_posts,
        'popular_posts': popular_posts
    })


def about_page(request):
    return render(request, 'pages/about.html')


def category_page(request):
    posts = Post.objects.annotate(total_comment=Count('comments'))
    context = {
        'posts': posts
    }
    return render(request, 'pages/category.html', context)


class SinglePostView(View):

    def get_comments(self, post):
        comments = post.comments.all().order_by("-id")
        return comments

    def get_related_post(self, post, slug):
         related_posts = Post.objects.filter(category=post.category).exclude(slug=slug).distinct()[:3]
         return related_posts

    def get_post(self, slug):
         post = get_object_or_404(Post, slug=slug)
         return post

    def is_stored_post(self, request, post_id):
        stored_post = request.session.get("stored_posts")
        if stored_post is not None:
            is_save_for_later = post_id in stored_post
        else:
            is_save_for_later = False

        return is_save_for_later

    def get(self, request, slug):
        post = self.get_post(slug)
        form = CommentForm()
        context = {
            'post': post,
            'related_posts': self.get_related_post(post, slug),
            'comments': self.get_comments(post),
            "form": form,
            "save_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, 'pages/single-post.html', context)

    def post(self, request, slug):
        post = self.get_post(slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.post = post
            comment_form.save()
            messages.success(request, "Comment Success")
            return redirect(reverse('single-post', args=[slug]))

        context = {
            'post': post,
            'related_posts': self.get_related_post(post, slug),
            'comments': self.get_comments(post),
            "form": form,
            "save_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, 'pages/single-post.html', context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'pages/stored-posts.html', context)

    def post(self, request):

        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session['stored_posts'] = stored_posts

        return redirect('home')


def error_page(request):
     return HttpResponse("This is error page")
