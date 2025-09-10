from django.urls import path
from . import views


urlpatterns = [
    path('',views.LandingPage.as_view(), name="landing-page"),
    path('posts',views.AllPosts.as_view(),name="posts-page"),
    path('/<slug:slug>',views.PostDetail.as_view(),name="post-detail-page"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")

]