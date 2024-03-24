from django.urls import path

from apps.blog.views import PostListView, PostDetailView, PostFromCategoryView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<str:slug>', PostFromCategoryView.as_view(), name='post_by_category')
]
