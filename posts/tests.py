from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1=User.objects.create_user(
            username='testuser1',
            password='abc123'
        )
        testuser1.save()
        testpost=Post.objects.create(
            author=testuser1,
            title='blog title',
            body='blog content',
        )
        testpost.save()
    def test_blog_content(self):
        post=Post.objects.get(id=1)
        author=f'{post.author}'
        title=f'{post.title}'
        body=f'{post.body}'
        self.assertEqual(author,'testuser1')
        self.assertEqual(title,'blog title')
        self.assertEqual(body,'blog content')
        