from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
from .forms import PostForm


class PostListAPIView(TemplateView):
    template_name='blog/post_list_api.html'

def index_view(request):
    return render(request, "index.html")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


def redirect_view(request):
    return redirect("https://maktabkhooneh.com")


class Redirectview(RedirectView):
    url = "https://maktabkhooneh.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostList(LoginRequiredMixin, ListView):
    # model=Post
    context_object_name = "posts"
    queryset = Post.objects.all()
    ordering = "-id"
    paginate_by = 2

    def get_queryset(self):
        posts = Post.objects.filter(author=self.request.user.profile).order_by("-id")
        return posts


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post

    def get_queryset(self):
        posts = Post.objects.filter(author=self.request.user.profile)
        return posts


class PostCreate(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.save()
        return super().form_valid(form)

    def get_queryset(self):
        posts = Post.objects.filter(author=self.request.user.profile)
        return posts


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    success_url = "/blog/post/"
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_queryset(self):
        posts = Post.objects.filter(author=self.request.user.profile)
        return posts


class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

    def get_queryset(self):
        posts = Post.objects.filter(author=self.request.user.profile)
        return posts


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"

    def get_queryset(self):
        posts = Post.objects.filter(author=self.request.user.profile)
        return posts
