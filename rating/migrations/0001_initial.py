# Generated by Django 4.2 on 2024-03-19 11:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comic",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=150, unique=True, verbose_name="Название комикса")),
                (
                    "rating",
                    models.DecimalField(
                        db_index=True, decimal_places=2, default=0.0, max_digits=3, verbose_name="Рейтинг комикса"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="autor",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор комикса",
                    ),
                ),
            ],
            options={
                "ordering": ["-rating"],
            },
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "value",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="оценка пользователя",
                    ),
                ),
                (
                    "comic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="ratings", to="rating.comic"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="ratings", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "unique_together": {("comic", "user")},
            },
        ),
    ]
