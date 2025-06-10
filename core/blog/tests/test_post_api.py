import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User
from django.utils import timezone

@pytest.fixture
def api_client():
    client=APIClient()
    return client

@pytest.fixture
def common_user():
    user=User.objects.create_user(email='test2@test2.com', password='mxgyuirt22ali')
    return user

@pytest.mark.django_db
class TestPostAPI:
    def test_create_post_response_201_status(self,common_user,api_client):
        url=reverse('blog:api-v1:post-list')
        data={
            'title':'test',
            'content':'...',
            'status':True,
            'published_date':timezone.now(),
        }
        user=common_user
        api_client.force_authenticate(user=user)
        response=api_client.post(url,data)
        assert response.status_code == 201
    
    def test_get_post_response_201_status(self,api_client):
        url=reverse('blog:api-v1:post-list')
        response=api_client.get(url)
        assert response.status_code == 200