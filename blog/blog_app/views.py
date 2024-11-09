from django.shortcuts import render, HttpResponse, redirect
from .models import (
    Category,
    FAQ,
    Slider,
    Post,
    PostGallery,
    Comment,
    PostViews,
    Like,
    Dislike
)
from .forms import LoginForm, RegistrationForm, CommentForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView

def home_page(request):
    # categories = Category.objects.all()
    faqs = FAQ.objects.all()
    slides = Slider.objects.all()
    posts = Post.objects.all()
    context = {
        # 'categories': categories
        'faqs': faqs,
        'slides': slides,
        'posts': posts
    }
    return render(request, 'blog_app/index.html', context)

def contacts_page(request):
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'blog_app/contacts.html', context)

def about_page(request):
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'blog_app/about.html', context)

# pk - primary key = ID
def category_page(request, pk):
    sort_query = request.GET.get('sort')
    category = Category.objects.get(pk=pk)
    posts = Post.objects.filter(category=category)

    if sort_query:
        posts = posts.order_by(sort_query)

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog_app/category.html', context)

def post_detail(request, pk):
    if pk == 'all':
        posts = Post.objects.all()
        return render(request, 'blog_app/posts.html', {'posts': posts})
    post = Post.objects.get(pk=pk)
    gallery = PostGallery.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.post = post
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm

    comments = Comment.objects.filter(post=post)

    if not  request.session.session_key:
        request.session.save()

    session_key = request.session.session_key

    post_viewed = PostViews.objects.filter(post=post, session_id=session_key).count()
    if post_viewed == 0 and session_key != 'None':
        obj = PostViews(post=post, session_id=session_key)
        obj.save()

        post.views += 1
        post.save()

    try:
        post.likes
    except Exception as e:
        Like.objects.create(post=post)

    try:
        post.dislikes
    except Exception as e:
        Dislike.objects.create(post=post)

    total_likes = post.likes.user.all().count()
    total_dislikes = post.dislikes.user.all().count()

    context = {
        'post': post,
        'gallery': gallery,
        'form': form,
        'comments': comments,
        'total_likes': total_likes,
        'total_dislikes': total_dislikes,
    }
    return render(request, 'blog_app/post_detail.html', context)

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'blog_app/login.html', context)

def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'blog_app/registration.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')


def create_article_view(request):
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            for item in request.FILES.getlist('photos'):
                new_obj = PostGallery(
                    post=form,
                    photo=item
                )
                new_obj.save()
            return redirect('post_detail', pk=form.pk)

    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'blog_app/article_form.html', context)

def delete_post(requests, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')

class PostUpdateView(UpdateView):
    model = Post
    success_url = '/'
    form_class = PostForm
    template_name = 'blog_app/article_form.html'


def Search(request):
    query = request.GET.get('q')
    posts = []
    if query:
        posts = Post.objects.filter(title__iregex=query)
    context = {
        'posts': posts,
        'query': query
    }
    return render(request, 'blog_app/search_page.html', context)

def add_vote(request, post_id, action):
    post = Post.objects.get(pk=post_id)

    if action == 'add_like':
        if request.user in post.likes.user.all():
            post.likes.user.remove(request.user.pk)
        else:
            post.likes.user.add(request.user.pk)
            post.dislikes.user.remove(request.user.pk)
    elif action == 'add_dislike':
        if request.user in post.dislikes.user.all():
            post.dislikes.user.remove(request.user.pk)
        else:
            post.dislikes.user.add(request.user.pk)
            post.likes.user.remove(request.user.pk)
    return redirect('post_detail', pk=post_id)