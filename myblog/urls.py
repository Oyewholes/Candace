from django.urls import path, re_path
from .views import SubscribeView, SubscribeSuccessView
from myblog import views

app_name='myblog'

urlpatterns = [
    re_path(r'^$', views.Homepage.as_view(), name='home'),
    re_path(r'post_list', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('subscribe/success/', SubscribeSuccessView.as_view(), name='subscribe_success'),
    # path('post/<int:pk>/comment/', CommentView.as_view(), name='post_comment',)
]




# path('', PostListView.as_view(), name='post_list'),
#     path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),