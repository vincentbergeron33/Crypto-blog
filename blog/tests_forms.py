from django.test import TestCase
from .forms import CommentForm, ScamForm

# Create your tests here.


class TestCommentForm(TestCase):
    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['body',])
