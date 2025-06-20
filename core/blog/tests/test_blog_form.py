'''
from django.test import TestCase
from datetime import datetime
from ..forms import PostForm
from ..models import Category

class TestPostForm(TestCase):
    def test_blog_form_with_valid_data(self):
        category_obj=Category.objects.create(name='hello')
        form=PostForm(data={
            'title':'test',
            'content':'...',
            'status':True,
            'category':category_obj,
            'published_date':datetime.now(),
        })
        self.assertTrue(form.is_valid())
'''