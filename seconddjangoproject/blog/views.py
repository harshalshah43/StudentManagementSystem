from django.shortcuts import render,get_object_or_404
from .models import Post

from django.views.generic import (ListView,
                                DetailView,CreateView,
                                UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User 
'''data=[
    {
    'title':'post1',
    'author':'Harshal',
    'date_posted':'October 25th, 2019'
    },
    {
    'title':'post2',
    'author':'Saatvik',
    'date_posted':'October 26th, 2019'
    }

] '''

def home(request):
    #context = {'data':data}
    context = {
        'posts':Post.objects.all()
    }
    if(request.method=='GET'):
        query=request.GET.get("q")
        qs=Post.objects.all()
        if query is not None:
            qs=qs.filter(title__icontains=query)
            context={
                'posts':qs
            }
    return render(request,'blog/home.html',context)

#class based views 
class PostListView(ListView):  #default object name is object_list
    model=Post   
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=2

class UserPostListView(ListView):  #default object name is object_list
    model=Post   
    template_name='blog/home.html'
    context_object_name='posts'
    #ordering=['-date_posted']
    paginate_by=2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


#class based view post detail
class PostDetailView(DetailView): #default object name is object
    model=Post   
    #<app>/<model>_<viewType>.html

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    #template this class will be looking for is post_create

    def form_valid(self,form):
        form.instance.author=self.request.user 
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    #template this class will be looking for is post_create

    def form_valid(self,form):
        form.instance.author=self.request.user 
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if (self.request.user==post.author):
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/blog/test/'
    def test_func(self):
        post=self.get_object()
        if (self.request.user==post.author):
            return True
        else:
            return False

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

