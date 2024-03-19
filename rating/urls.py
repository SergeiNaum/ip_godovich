from django.urls import path
from .views import RatingCreateView, ComicRatingView

urlpatterns = [
    path('ratings/', RatingCreateView.as_view()),
    path('comics/<int:comic_id>/rating/', ComicRatingView.as_view()),
]
