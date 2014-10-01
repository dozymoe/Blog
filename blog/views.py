"""views for blog app"""

from django.shortcuts import render, get_object_or_404

from .models import Post


def detail(request, slug, *args, **kwargs):
    """
    Menampilkan isi dari blog post.
    """
    obj = get_object_or_404(Post, slug=slug)

    # variabel yang dilempar ke template
    context = {
        'object': obj,
    }
    # buat http response-nya
    return render(request, 'blog/detail.html', context)


def index(request, *args, **kwargs):
    """
    Menampilkan daftar blog post.
    """
    queryset = Post.objects.all()

    # variabel yang dilempar ke template
    context = {
        'object_list': queryset,
    }
    # buat http response-nya
    return render(request, 'blog/index.html', context)
