
# Django
from django.urls import path

# Views
from workshops import views

urlpatterns = [

    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create'
    ),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),


    path(
        route='search/',
        view=views.PostsSearchView.as_view(),
        name='search',

    )
]