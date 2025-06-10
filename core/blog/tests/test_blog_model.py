'''
from django.test import TestCase
from ..models import Post, Category
from accounts.models import User, Profile
from django.utils import timezone

class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test2@test2.com', password='mxgyuirt22ali')
        
        self.profile, created = Profile.objects.get_or_create(
            user=self.user,
            defaults={
                'first_name': 'ali',
                'last_name': 'saadat',
                'description': '...',
            }
        )

    def test_create_post_with_valid_data(self):

        post = Post.objects.create(
            author=self.profile,
            title='test',
            content='...',
            status=True,
            category=None,
            published_date=timezone.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
'''
