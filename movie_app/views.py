from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import Director, Movie, Review
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


@api_view(['GET', "POST"])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    else:
        serializer = DirectorCreateValidate(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = request.data.get('name', '')
        director = Director()
        director.name = name
        director.save()
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)


class DirectorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def director_details_views(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': '404'})
    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(data=serializer.data)
    elif request.method == "PUT":
        serializer = DirectorUpdateValidateSerializer(data=request.data,
                                                      context={'director_id': id})
        serializer.is_valid(raise_exception=True)
        director.name = request.data.get('name', '')
        director.save()
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        director.delete()
        return Response(data={'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@api_view(['GET', 'POST'])
def movie(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    else:
        serializer = MovieValidateCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = request.data.get('title', '')
        description = request.data.get('description', '')
        duration = request.data.get('duration', '1:00:00')
        director_id = request.data.get('director')
        movie_ = Movie()
        movie_.title = title
        movie_.description = description
        movie_.duration = duration
        movie_.director_id = director_id
        movie_.save()
        return Response(data=MovieSerializer(movie_).data, status=status.HTTP_201_CREATED)


class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details_views(request, id):
    try:
        movie_ = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': '404'})
    if request.method == 'GET':
        serializer = MovieSerializer(movie_)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = MovieValidateUpdateSerializer(data=request.data,
                                                   context={'movie_id': id})
        serializer.is_valid(raise_exception=True)
        movie_.title = request.data.get('title', '')
        movie_.description = request.data.get('description', '')
        movie_.duration = request.data.get('duration', '')
        movie_.director_id = request.data.get('director_id', '')
        movie_.save()
        return Response(data=MovieSerializer(movie_).data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        movie_.delete()
        return Response(data={'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@api_view(['GET', 'POST'])
def review(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    else:
        serializer = ReviewCreateValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie')
        review_ = Review()
        review_.text = text
        review_.stars = stars
        review_.movie_id = movie_id
        review_.save()
        return Response(ReviewSerializer(review_).data, status=status.HTTP_201_CREATED)


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@api_view(['GET', "PUT", "DELETE"])
def review_details_views(request, id):
    try:
        review_ = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': '404'})
    if request.method == "GET":
        serializer = ReviewSerializer(review_)
        return Response(data=serializer.data)
    elif request.method == "PUT":
        serializer = ReviewUpdateSerializer(data=request.data,
                                            context={'movie_id': id})
        serializer.is_valid(raise_exception=True)
        review_.text = request.data.get('text', '')
        review_.stars = request.data.get('stars', '')
        review_.movie_id = request.data.get('movie_id', '')
        review_.save()
        return Response(data=ReviewSerializer(review_).data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        review_.delete()
        return Response(data={'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class MoviesReviewListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewsSerializers


@api_view(['GET'])
def movies_review_views(request):
    movie_ = Movie.objects.all()
    serializer = MovieReviewsSerializers(movie_, many=True)
    return Response(data=serializer.data)
