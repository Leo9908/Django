from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .forms import PostCreateForm
from .models import Post

# Create your views here.


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        # Para poder usar los objetos en html
        context = {
            'posts': posts
        }
        return render(request, 'blog_list.html', context)


class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                post, created = Post.objects.get_or_create(
                    title=title, content=content)
                post.save()

                return redirect('blog:home')

        context = {

        }
        return render(request, 'blog_create.html', context)


class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post
        }
        return render(request, 'blog_detail.html', context)
