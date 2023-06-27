from django.test import TestCase, Client
from .models import Post, Comment, Scam
from django.contrib.auth.models import User
from django.shortcuts import reverse


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(
            password='vince', username='gonnabuypie@outlook.com')

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
        post = Post.objects.create(
            slug='Test', title='Test', author=test_user, status=1)
        response = self.client.get(reverse('post_detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_scam(self):
        response = self.client.get('/report_scam/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report_scam.html')

    def test_can_add_scam(self):
        test_user = self.user1
        self.client.force_login(test_user)
        response = self.client.post('/report_scam/add', {
            'scam_title': 'Testing', 'scam_slug': 'Test',
            'name': test_user.username, 'email': test_user.username,
            'scam_media': 'testcase', 'scam_excerpt': 'description',
            'scam_content': 'Testing'})
        self.assertRedirects(response, '/scam/')

    def test_can_edit_scam(self):
        test_user = self.user1
        self.client.force_login(test_user)
        scam = Scam.objects.create(
            title='test', slug='testing', name='Tester',
            email='test@gmail.com', media='tester', excerpt='description',
            content='details', approved=True)
        response = self.client.post(
            f'/edit/{scam.slug}', {
                'title': 'Updated Title', 'slug': 'Test',
                'name': test_user.username, 'email': test_user.username,
                'media': 'testcase', 'excerpt': 'description',
                'content': 'Testing'})
        self.assertRedirects(response, '/scam/')
        updated_scam = Scam.objects.get(slug=scam.slug)
        self.assertEqual(updated_scam.title, 'Updated Title')

    def test_delete_confirmation(self):
        test_user = self.user1
        self.client.force_login(test_user)
        scam = Scam.objects.create(
            title='test', slug='testing', name='Tester',
            email='test@gmail.com', media='tester', excerpt='description',
            content='details', approved=True)
        response = self.client.get(reverse('confirmation', args=(scam.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirmation.html')

    def test_can_delete_scam(self):
        test_user = self.user1
        self.client.force_login(test_user)
        scam = Scam.objects.create(
            title='test', slug='testing', name='Tester',
            email='test@gmail.com', media='tester', excerpt='description',
            content='details', approved=True)
        response = self.client.get(reverse('delete', args=(scam.slug,)))
        self.assertRedirects(response, '/scam/')
        existing_scam = Scam.objects.filter(slug=scam.slug)
        self.assertEqual(len(existing_scam), 0)

    def test_scam_detail_get(self):
        test_user = self.user1
        self.client.force_login(test_user)
        scam = Scam.objects.create(
            title='test', slug='last test', name='Tester',
            email='test@gmail.com', media='tester', excerpt='description',
            content='details', approved=True)
        response = self.client.get(reverse('scam_detail', args=(scam.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scam_detail.html')
