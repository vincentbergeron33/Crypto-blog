from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('report_scam/', views.PostScam.as_view(), name='report_scam'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<str:category_name>/', views.CategoryPosts.as_view(),
         name='category_posts'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
