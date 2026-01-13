import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from users.decorators import auth_required

from .forms import EditPostForm
from .models import Post
from .serializers import PostSerializer


@csrf_exempt
@require_GET
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts)
    return serializer.json_response()


@csrf_exempt
@require_GET
def post_detail(request, post_slug: str):
    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    serializer = PostSerializer(post)
    return serializer.json_response()


@csrf_exempt
@require_POST
@auth_required
def add_post(request):
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON body'}, status=400)
    post = Post.objects.create(
        title=payload['title'],
        slug=slugify(payload['title']),
        content=payload['content'],
    )
    return JsonResponse({'id': post.pk})


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


def delete_post(request, post_slug: str):
    try:
        post = Post.objects.get(slug=post_slug)
        messages.success(request, 'Post deleted successfully')

    except Post.DoesNotExist:
        messages.error(request, 'Post does not exist')

    posts = Post.objects.all()
    return render(request, 'posts/post/list.html', {'posts': posts})
