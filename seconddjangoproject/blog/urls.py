from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views 

urlpatterns=[
    path('',views.home,name ='blog-home'),
    path('about/',views.about,name ='blog-about'),
    path('test/',PostListView.as_view(),name='blog-home'),
    path('test/post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('test/post/create/',PostCreateView.as_view(),name='post-create'),
    path('test/post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('test/post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('test/<str:username>',UserPostListView.as_view(),name='user-post'),
]	

