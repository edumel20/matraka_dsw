from posts.models import Post


def last_post(request) -> dict:
    try:
        return {'last_post': Post.objects.last()}
    except Post.DoesNotExist:
        return {}
