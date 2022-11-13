from .models import Director, Movie, Review
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, director):
        return director.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars movie'.split()


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = 'id title description duration'.split()


class MovieReviewsSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()


class MovieValidateAbstractSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=100)
    description = serializers.CharField()
    duration = serializers.TimeField()
    director = serializers.CharField()


class MovieValidateCreateSerializer(MovieValidateAbstractSerializer):
    def validate_title(self, title):
        try:
            Movie.objects.get(title=title)
        except Movie.DoesNotExist:
            return title
        raise ValidationError(f'Movie with title({title}) already exists')


class MovieValidateUpdateSerializer(MovieValidateAbstractSerializer):
    def validate_title(self, title):
        if Movie.objects.exclude(id=self.context['movie_id']).filter(title=title).count() > 0:
            raise ValidationError(f'Movie with title({title}) already exists')
        return title


class DirectorCreateValidate(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, name):
        try:
            Director.objects.get(name=name)
        except Director.DoesNotExist:
            return name
        raise ValidationError(f"Director with name {name} already exists")


class DirectorUpdateValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, name):
        if Director.objects.exclude(id=self.context['director_id']).filter(name=name).count() > 0:
            raise ValidationError(f'Director with name {name} already exists')
        return name


class ReviewAbstractValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    movie_id = serializers.IntegerField()

    def validate_text(self, text):
        if len(text) > 50:
            raise ValidationError(f'NE NADA TY CHE POET')
        return text

    def validate_stars(self, stars):
        if stars > 5:
            raise ValidationError('NE BOLSHE 5')
        return stars


class ReviewCreateValidateSerializer(ReviewAbstractValidateSerializer):
    pass


class ReviewUpdateSerializer(ReviewAbstractValidateSerializer):
    def validate_movie_id(self, movie_id):
        if Movie.objects.filter(id=movie_id).count() == 0:
            raise ValidationError(f'Movie with id {movie_id} not found')
        return movie_id
