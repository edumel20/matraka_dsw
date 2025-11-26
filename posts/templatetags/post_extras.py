from django import template
from django.utils.html import format_html

from posts.models import Post

register = template.Library()


@register.inclusion_tag('templates/posts/post/list.html')
def post_list(min_rating: int = 0):
    posts = Post.objects.filter(rating__gte=min_rating)
    return {'posts': posts}


@register.filter
def post_size(post: Post, metric: str = 'by-words') -> int:
    match metric:
        case 'by-words':
            size = len(post.content.split())
        case 'by-chars':
            size = len(post.content)
        case _:
            size = 0
    return size


@register.filter
def post_link(post: Post) -> str:
    return format_html('<a href="{}">{}</a>', post.get_absolute_url, post.title)
