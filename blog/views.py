from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (ListView,DetailView,UpdateView,
                                    CreateView,DeleteView,TemplateView)

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Post,Comment
from .forms import PostForm,CommentForm

# Create your views here.

class PasswordChangeViewPage(PasswordChangeView):
    template_name = 'blog/password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('blog:about')


class AboutUs(TemplateView):
    template_name = 'blog/about.html'


class ListPageView(LoginRequiredMixin,ListView):
    login_url ="/"
    redirect_field_name ="blog/index.html"
    model = Post
    ordering = ["-id"]
    template_name = 'blog/index.html'
    context_object_name = 'lists'

class DetailPageView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'posts'

class CreatePageView(LoginRequiredMixin,CreateView):
    login_url ="/"
    redirect_field_name ="blog/index.html"
    model = Post
    fields = ('title','author','body')

class UpdatePageView(UpdateView):
    model = Post
    fields = ('title','body')

class DeletePageView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk = post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

class Register(CreateView):
    form_class = UserCreationForm
    model = User

    success_url = reverse_lazy('blog:index')
