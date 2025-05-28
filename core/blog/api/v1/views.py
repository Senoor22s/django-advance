from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404,redirect

@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method=="GET":
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="GET":
        serialaizer=PostSerializer(post)
        return Response(serialaizer.data)
    elif request.method=="PUT":
        serializer=PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method=="DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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