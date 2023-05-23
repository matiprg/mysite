from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from blog.models import Post

def blog_view(request):
        posts=Post.objects.filter(status=1)
        # زمان فعلی
        current_time = timezone.now()  
        # فیلتر کردن پست‌ها بر اساس زمان
        posts = Post.objects.filter(published_date__lte=current_time)
        context={'posts': posts}
        return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts=Post.objects.filter(status=1)
    post=get_object_or_404(posts,pk=pid)
    post.counted_views+=1
    post.save()
    context={'post':post}
    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    #posts=Post.objects.filter(status=1)
    #post=Post.objects.get(id=pid)
    post=get_object_or_404(Post,pk=pid)
    context={'post':post}
    return render(request,'test.html',context)


   