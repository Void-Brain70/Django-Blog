from django.core import paginator
from django.shortcuts import get_object_or_404, render,redirect
from .models import Post
from .forms import PostForm,LoginForm,UserCreateForm
from datetime import datetime
from django.template.defaultfilters import slugify, title
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def home(request):
    return redirect('blog/showPost')


def showPost(request):
    posts = Post.published.all()
    paginator = Paginator(posts,3)
    page =request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)        
    context = {
            'posts':posts,
            'page':page
            }
    return render(request,'blog/showPost.html',context)

def postDetails(request,year,month,day,hour,minute,second,slug):
    posts = get_object_or_404(Post, slug = slug,
                            status = 'published',
                            publish__year = year,
                            publish__month = month,
                            publish__day = day,
                            publish__hour =hour,
                            publish__minute = minute,
                            publish__second =second)
    context={
            'post':posts
    }
    return render(request,'blog/postDetails.html',context)
        
def postCreate(request):
    if request.method=='POST':
      form = PostForm(request.POST)
      if form.is_valid():
        title = form.cleaned_data['title']
        slug = slugify(title)
        body = form.cleaned_data['body']
        status = form.cleaned_data['status']
        author = request.user
        publish = datetime.now()
        created = publish
        updated = publish
        post = Post(title=title,slug=slug,author=author,body=body,status=status,publish=publish,created=created,updated=updated)
        post.save()
        return redirect('/blog/showPost')
    else:
        form = PostForm()
    context ={
        'form':form
    }        
    return render(request, "blog/createPost.html",context)        

def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/blog/showPost')
            else :
                return redirect('/blog/showPost')
        else :
            return redirect('/blog/showPost')
    else :
        form = LoginForm()
        return render(request, 'blog/userLogin.html', context={'form': form})


def userCreate(request):
    if request.method=='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            passwordagain = form.cleaned_data['passwordagain']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            if password == passwordagain:
                user = authenticate(request,username=username, password=password)
                if user is None:
                    user = User(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    login(request,user)
                    return redirect('/blog/showPost')
                else:
                    return redirect('/blog/showPost')
            else:
                return redirect("/blog/showPost")
        else:
            return redirect("/blog/showPost")
    else:
        form = UserCreateForm()
    return render(request,'blog/userCreate.html',context={'form':form})                        

def userLogout(request):
    logout(request)
    return redirect('/blog/showPost')




