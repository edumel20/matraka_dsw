from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('add/', views.add_post, name='add-post'),
    path('<post_slug>/', views.post_detail, name='post-detail'),
    path(_('<slug:post_slug>/edit/'), views.edit_post, name='edit-post'),
]
