from django.urls import path
from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('movie_list/', MovieListView.as_view(), name='movie-list'),
    path('movie_detail/', MovieDetailView.as_view(), name='movie-detail-by-name'),
]
