from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404,redirect

@api_view()
def post_list(request):
    posts=Post.objects.filter(status=True)
    serializer=PostSerializer(posts,many=True)
    return Response(serializer.data)


'''
@api_view()
def post_detail(request,pk):
    try:
        post=Post.objects.get(pk=pk)
        serialaizer=PostSerializer(post)
        return Response(serialaizer.data)
    except Post.DoesNotExist:
        return Response({"detail":"post does not exist"},status=status.HTTP_404_NOT_FOUND)
'''

@api_view()
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    serialaizer=PostSerializer(post)
    return Response(serialaizer.data)