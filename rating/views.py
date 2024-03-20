from typing import Any

from django.conf import settings
from django.core.cache import cache
from drf_spectacular.utils import extend_schema
from rest_framework.generics import get_object_or_404
from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


from rating.models import Comic
from rating.serializers import ComicSerializer, RatingSerializer


@extend_schema(
    tags=["ratings"],
    summary="creating a comic book rating",
)
class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=["comics"],
    summary="get rating for comic book",
)
class ComicRatingView(APIView):
    serializer_class = ComicSerializer

    def get(self, request, comic_id):

        cache_key = f"{settings.RATING_CACHE_NAME}{comic_id}"
        rating_chache = cache.get(cache_key)
        if not rating_chache:
            comic = get_object_or_404(Comic, id=comic_id)
            cache.set(cache_key, comic,  500)

        else:
            comic = rating_chache
        serializer = ComicSerializer(comic)
        return Response({'rating': serializer.data['rating']})
