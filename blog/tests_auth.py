from django.test import TestCase
from .models import Post, Comment, Scam
from django.contrib.auth.models import User


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(
            'vince', 'gonnabuypie@outlook.com')

    def test_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_scam_list(self):
        response = self.client.get('/scam/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scam.html')

    def test_category_post(self):
        response = self.client.get('/category/<str:category_name>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_posts.html')

    def test_post_detail_get(self):
        test_user = self.user1
        self.client.force_login(test_user)
        post = Post.objects.create(slug='Test', author=test_user)
        response = self.client.get('/<slug:slug>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
