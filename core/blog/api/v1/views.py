# from rest_framework.decorators import api_view, permission_classes, action
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework import status, mixins
'''from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)'''
# from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from .permissions import IsAuthorOrReadOnly
# from django.shortcuts import get_object_or_404, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination
from .filters import PostFilter


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author"]
    search_fields = ["title", "content"]
    filterset_class = PostFilter
    ordering_fields = ["created_date"]
    pagination_class = DefaultPagination


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


"""
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

class PostList(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer

    def get(self,request):
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostList(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk,status=True)
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
        return Response({"detail":"item successfully removed"},status=status.HTTP_204_NO_CONTENT)


class PostDetail(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer

    def get(self,request,pk):
        post=get_object_or_404(Post,pk=pk,status=True)
        serializer=PostSerializer(post)
        return Response(serializer.data)
    def put(self,request,pk):
        post=get_object_or_404(Post,pk=pk,status=True)
        serializer=PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,pk):
        post=get_object_or_404(Post,pk=pk,status=True)
        post.delete()
        return Response({"detail":"item successfully removed"},status=status.HTTP_204_NO_CONTENT)

class PostDetail(GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
"""
