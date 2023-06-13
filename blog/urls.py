from . import views
from django.urls import path
from blog.views import add_scam, edit_scam


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('scam/', views.ScamList.as_view(), name='scam'),
    path('report_scam/', views.PostScam.as_view(), name='report_scam'),
    path('report_scam/add', add_scam, name='add'),
    path('edit/<slug:slug>', edit_scam, name='edit'),
    path('<slug:slug>/', views.ScamDetail.as_view(), name='scam_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<str:category_name>/', views.CategoryPosts.as_view(),
         name='category_posts'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
