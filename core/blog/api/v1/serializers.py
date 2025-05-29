from rest_framework import serializers
from ...models import Post,Category

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model=Post
        fields=['id','author','status','title','content','created_date','published_date']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=['id','name']
