import decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Comic(models.Model):
    title: str
    autor: User
    rating: decimal
    total_rating: int
    num_ratings: int

    title = models.CharField(max_length=150, unique=True, verbose_name="Название комикса")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="autor", db_index=True,
                               verbose_name="Автор комикса")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, db_index=True,
                                 verbose_name="Рейтинг комикса")
    total_rating = models.PositiveIntegerField(default=0)
    num_ratings = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return self.title


class Rating(models.Model):
    comic: Comic
    user: User
    value: int

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                             verbose_name="оценка пользователя")

    class Meta:
        unique_together = ('comic', 'user')

    def __str__(self):
        return f"{self.user.username} rated {self.comic.title} with {self.value}"
