"""views for blog app"""

from django.shortcuts import render

from .models import Post


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
