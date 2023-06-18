from django.test import TestCase
from .forms import CommentForm, ScamForm

# Create your tests here.


class TestCommentForm(TestCase):
    def test_fields_are_explicit_in_comment_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestScamForm(TestCase):
    def test_fields_are_explicit_in_scam_form_metaclass(self):
        form = ScamForm()
        self.assertEqual(form.Meta.fields, (
            'title', 'media', 'excerpt', 'content'))
