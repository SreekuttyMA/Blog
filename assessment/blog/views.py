from django.http import request
from django.shortcuts import render, redirect
from django.template import context
from .models import PostModel , Like
from .forms import PostModelForm, PostUpdateForm,CommentForm

# from django.http import HttpResponse
# Create your views here.


def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
        return redirect('blog-index')
    else:
        form = PostModelForm()
    context = {
        'posts' : posts,
        'form' : form 
    }
    return render(request, 'blog/index.html', context)

def post_detail(request ,pk):
    post = PostModel.objects.get(id = pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
           instance =  c_form.save(commit=False)
           instance.user = request.user
           instance.post = post
           instance.save()
        return redirect ('blog-post-detail', pk=post.id)

    else:
        c_form = CommentForm()

    context ={
        'post':post,
        'c_form':c_form,
    }
    return render(request, 'blog/post_detail.html',context)



def like_post(request ,pk):
    user = request.user
    if request.method == 'POST':
        pk = request.POST.get('post.id')
        post_obj = PostModel.objects.get(id=pk)
        
        if user in post_obj.liked.all():
            pk.liked.remove(user)
        else:
            pk.liked.add(user)
            
        like , created =Like.objects.get_or_create(user=user, pk=pk)
        if not created:
            if like.value == 'Like':
                instance =  like.value.save(commit=False)
                instance.user = request.user
            instance.save()     
        else:
            like.value = 'Unlike'
        #         like.value = 'Unlike'
        #     else:
        #         like.value == 'Like'  
        # like.save()
        return redirect(' blog-post-detail', )



def post_edit(request , pk):
    post = PostModel.objects.get(id = pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail' , pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context={
        'post':post,
        'form':form,
    }
    return render(request, 'blog/post_edit.html' , context)

def post_delete(request, pk):
    post = PostModel.objects.get(id = pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')

    context ={
        'post':post,
    }
    return render(request, 'blog/post_delete.html',context)


