from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddPostForm, EditPostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    print(f'{request.user=}')
    return render(request, 'posts/post/list.html', {'posts': posts})


@login_required
def post_detail(request, post_slug: str):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return HttpResponse(f'Post with slug "{post_slug}" does not exist!')
    return render(request, 'posts/post/detail.html', {'post': post})


def add_post(request):
    if request.method == 'POST':
        if (form := AddPostForm(request.POST)).is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            form.save()
            return redirect('posts:post-list')

    else:
        form = AddPostForm()

    return render(request, 'posts/post/add.html', dict(form=form))


def edit_post(request, post_slug):
    post = Post.objects.get(slug=post_slug)

    if request.method == 'POST':
        if (form := EditPostForm(request.POST, instance=post)).is_valid():
            post = form.save(commit=False)

            post.slug = slugify(post.title)

            post.save()

            return redirect('posts:post-list')

    else:
        form = EditPostForm(instance=post)

    return render(request, 'posts/edit_post.html', dict(post=post, form=form))
