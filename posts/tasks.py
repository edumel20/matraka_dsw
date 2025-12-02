from django_rq import job

import posts.models as pm


@job
def post_stats() -> None:
    posts = pm.Post.objects.all()
    num_posts = posts.count()
    tot_content_length = sum(len(post.content) for post in posts)
    avg_content_length = tot_content_length / num_posts if num_posts > 0 else 0
    print(f'Total Posts: {num_posts}')
    print(f'Average Content Length: {avg_content_length:.2f} characters')
