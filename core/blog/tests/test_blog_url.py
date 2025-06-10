'''
from django.test import TestCase
from django.urls import reverse,resolve
from .. import views

class TestUrl(TestCase):
    def test_blog_index_url_resolver(self):
        url=reverse('blog:cbv-index')
        self.assertEqual(resolve(url).func.view_class,views.IndexView)

    def test_blog_post_detail_url_resolver(self):
        url=reverse('blog:post-detail',kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class,views.PostDetail)
    
    def test_blog_post_list_url_resolver(self):
        url=reverse('blog:post-list')
        self.assertEqual(resolve(url).func.view_class,views.PostList)
'''
