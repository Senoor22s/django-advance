'''
from django.test import TestCase,Client
from django.urls import reverse
from ..models import Post,Category
from accounts.models import User,Profile
from django.utils import timezone

class TestBlogView(TestCase):
    def setUp(self):
        self.client=Client()
        self.user = User.objects.create_user(email='test2@test2.com', password='mxgyuirt22ali')
        
        self.profile, created = Profile.objects.get_or_create(
            user=self.user,
            defaults={
                'first_name': 'ali',
                'last_name': 'saadat',
                'description': '...',
            }
        )
        self.post = Post.objects.create(
            author=self.profile,
            title='test',
            content='...',
            status=True,
            category=None,
            published_date=timezone.now(),
        )
    
    def test_blog_index_url_successful_response(self):
        url=reverse('blog:cbv-index')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,template_name='index.html')
    
    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url=reverse('blog:post-detail',kwargs={'pk':self.post.id})
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

'''
