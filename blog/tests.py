from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_post_creation(self):
        # Test creating a post with various attributes
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            image_caption='Test Image Caption',
            image_credit='Test Image Credit',
            author=self.user,
            excerpt='Test Excerpt',
            content='Test Content',
            status=1,
            category='sports'
        )
        # Verify that the post's fields match the provided values
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(post.image_caption, 'Test Image Caption')
        self.assertEqual(post.image_credit, 'Test Image Credit')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.excerpt, 'Test Excerpt')
        self.assertEqual(post.content, 'Test Content')
        self.assertEqual(post.status, 1)
        self.assertEqual(post.category, 'sports')

    def test_number_of_likes(self):
        # Test the number_of_likes method
        post = Post.objects.create(title='Test Post', author=self.user)
        # Verify that the initial number of likes is 0
        self.assertEqual(post.number_of_likes(), 0)

    def test_save_method(self):
        # Test the save method
        post = Post(title='Test Post', author=self.user)
        post.save()
        # Verify that the slug is generated correctly and created_on/updated_on are set
        self.assertEqual(post.slug, 'test-post')
        self.assertIsNotNone(post.created_on)
        self.assertIsNotNone(post.updated_on)

