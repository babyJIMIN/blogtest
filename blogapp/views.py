from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    form = BlogForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            blog = form.save(commit=False)
            blog = timezone.now()
            blog.save()
            return redirect('home')
        else:
            form = BlogForm()
    return render(request, 'new.html', {'form' : form})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    blog_detail.delete()
    return redirect('home')

def edit(request, blog_id):
    if(request.method == 'POST'):
        blog_detail = get_object_or_404(Blog, pk = blog_id)
        return render(request, 'edit.html', {'blog' : blog_detail})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if(request.method == 'POST'):
         blog.title = request.POST['title']
         blog.body = request.POST['body']
         blog.save()
         return redirect('/blog/' + str(blog.id))


def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('/blog/' + str(blog.id))
        else:
            form = CommentForm()
        return render(request, 'add_comment.html', {'form' : form})

def edit_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('/blog/' + str(blog.id))
        else:
            form = CommentForm(instance=comment)
        return render(request, 'add_comment.html', {'form' : form})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('home')