from django.test import TestCase
from .models import Post, Comment, Scam
from django.contrib.auth.models import User


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(
            password='vince', username='gonnabuypie@outlook.com')

    def test_post_string_method_returns_title(self):
        test_user = self.user1
        self.client.force_login(test_user)
        post = Post.objects.create(
            slug='Test', title='Test', author=test_user, status=1)
        self.assertEqual(str(post), post.title)

    def test_comment_string_method_returns_body_name(self):
        test_user = self.user1
        self.client.force_login(test_user)
        post = Post.objects.create(
            slug='Test', title='Test', author=test_user, status=1)
        comment = Comment.objects.create(
            post=post, name='Tester', email='Tester@gmail.com',
            body='Test', approved=True)
        self.assertEqual(
            str(comment), f"Comment {comment.body} by {comment.name}")
    
    def test_scam_string_method_returns_title(self):
        test_user = self.user1
        self.client.force_login(test_user)
        scam = Scam.objects.create(
            title='test', slug='testing', name='Tester',
            email='test@gmail.com', media='tester', excerpt='description',
            content='details', approved=True)
        self.assertEqual(str(scam), scam.title)