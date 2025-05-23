from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView
from .models import Post

def index_view(request):
    name='ali'
    posts=Post.objects.all()
    context={
        'name':name,
        'posts':posts,
    }
    return render(request,'index.html',context)

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='ali'
        context['posts']=Post.objects.all()
        return context

def redirect_view(request):
    return redirect('https://maktabkhooneh.com')

class Redirectview(RedirectView):
    url='https://maktabkhooneh.com'

    def get_redirect_url(self, *args, **kwargs):
        post=get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class PostList(ListView):
    #model=Post
    context_object_name='posts'
    queryset=Post.objects.all()
    ordering='-id'
    paginate_by=2
    '''
    def get_queryset(self):
        posts=Post.objects.filter(status=True)
        return posts
    '''