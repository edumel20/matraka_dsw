from django.shortcuts import get_object_or_404, redirect
from posts.models import Post

from .forms import CommentForm

def add_comment(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.alias = request.user.username
            comment.post = post
            comment.save()
            return redirect(getattr(post, 'get_absolute_url', lambda: f'/posts/{post.slug}'))
