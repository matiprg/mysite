from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from blog.models import Post


def blog_view(request,cat_name=None):
        posts=Post.objects.filter(status=1)
        if cat_name:
                posts=posts.filter(category__name=cat_name)
        #current_time = timezone.now()  
        #posts = Post.objects.filter(published_date__lte=current_time)
        context={'posts': posts}
        return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts=Post.objects.filter(status=1)
    post=get_object_or_404(posts,pk=pid)
    previous_post=Post.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    next_post=Post.objects.filter(pk__gt=post.pk).order_by('pk').first()
    post.counted_views+=1
    post.save()
    #context={'post':post}
    return render(request,'blog/blog-single.html',{'post':post,'previous_post':previous_post, 'next_post': next_post})

def blog_category(request,cat_name):
        posts=Post.objects.filter(status=1)
        posts=posts.filter(category__name=cat_name)  
        context={'posts': posts}
        return render(request,'blog/blog-home.html',context) 

def test(request):
      return render(request,'test.html')

    # posts=Post.objects.filter(status=1)
    # post=Post.objects.get(id=pid)
    # post=get_object_or_404(Post,pk=pid)
    # context={'post':post}
  

   