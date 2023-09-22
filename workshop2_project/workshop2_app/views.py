from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.http import Http404


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveAPIView):
    serializer_class = MovieSerializer

    def get_object(self):
        movie_name = self.request.query_params.get('movie_name', None)
        if movie_name is not None:
            try:
                return Movie.objects.get(name=movie_name)
            except Movie.DoesNotExist:
                raise Http404("Movie not found")
        else:
            raise Http404("Movie name parameter not provided")
