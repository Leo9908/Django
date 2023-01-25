from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    UpdateView,
    DeleteView,
    ListView,
    CreateView,
    DetailView)
from .models import Post, Blog
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound

# Create your views here.

# Así es fácil crear las vistas porque ya Django viene con estas vistas genéricas
# pero mas abajo hay algunos ejemplos sin usar estas vistas genericas para las operaciones CRUD

# Estas son vistas de clase


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ['name', 'tagline', 'image']
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    # Estoy reutilizando el template de confirmación de los Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:blog_list')


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_create.html'
    success_url = reverse_lazy('blog:home')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk': pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:home')


# Esta es una vista de funcion
def status_code_view(request, exception):
    return HttpResponseNotFound('Pagina Web no encontrada, error 404')


# Así se haría sin usar las vistas genericas para las operaciones CRUD
# Habría que retornar el contexto para poder usarlo en el html
# pero con las vistas genéricas ya eso se hace por detrás
"""
class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        # Para poder usar los objetos en html
        context = {
            'posts': posts
        }
        return render(request, 'post_list.html', context)


class PostCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'post_create.html', context)

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
        return render(request, 'post_create.html', context)


class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post
        }
        return render(request, 'post_detail.html', context)

"""
