import decimal

from django.contrib.auth.models import User
from rest_framework import serializers


from rating.models import Comic, Rating


class RatingSerializer(serializers.ModelSerializer):

    comic: Comic
    value: int

    class Meta:
        model = Rating
        fields = ['comic', 'value']

    def create(self, validated_data: dict) -> Rating:
        rating: Rating
        created: bool

        rating, created = Rating.objects.get_or_create(
            comic=validated_data['comic'], user=self.context['request'].user, defaults={'value': validated_data['value']}
        )
        if not created:
            raise serializers.ValidationError("Вы уже голосовали за этот комикс!")

        self.update_comic_retings(validated_data['value'], rating)
        return rating

    def update_comic_retings(self, value: int, rating: Rating) -> None:

        comic = rating.comic
        comic.total_rating += value
        comic.num_ratings += 1
        comic.rating = comic.total_rating / comic.num_ratings
        rating.comic.save()


class ComicSerializer(serializers.ModelSerializer):
    title: str
    autor: User
    rating: decimal

    class Meta:
        model = Comic
        fields = ['title', 'author', 'rating']
