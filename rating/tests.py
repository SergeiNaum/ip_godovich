from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rating.models import Comic, Rating


class RatingTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass')
        self.comic = Comic.objects.create(title='Test Comic', author=self.user)

    def test_create_rating(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/api/ratings/', {'comic': self.comic.id, 'user': self.user.id, 'value': 5})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Rating.objects.count(), 1)
        self.assertEqual(Rating.objects.get().value, 5)

    def test_update_rating(self):
        self.client.force_login(self.user)
        self.client.post('/api/ratings/', {'comic': self.comic.id,  'value': 5})
        self.client.login(username='testuser', password='testpass')
        self.client.force_login(self.user2)
        response = self.client.post('/api/ratings/', {'comic': self.comic.id, 'value': 2})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Rating.objects.count(), 2)
        self.assertEqual(Comic.objects.get(pk=self.comic.id).rating, 3.5)

    def test_get_comic_rating(self):
        self.client.login(username='testuser', password='testpass')
        self.client.post('/api/ratings/', {'comic': self.comic.id, 'user': self.user.id, 'value': 5})
        response = self.client.get(f'/api/comics/{self.comic.id}/rating/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['rating'], '5.00')
