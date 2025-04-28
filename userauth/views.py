from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . models import Profile, Post, LikePost

# Create your views here.
def signup(request):
    try:
        if request.method=='POST':
            fname = request.POST.get('fname')
            emailid = request.POST.get('emailid')
            pwd = request.POST.get('pwd')
            my_user = User.objects.create_user(fname, emailid, pwd)
            my_user.save()
            user_model = User.objects.get(username=fname)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            if my_user is not None:
                login(request,my_user)
                return redirect('/') 
            return redirect('/login')
    except:
        invalid="User Already Exists"
        return render(request, 'signup.html', {'invalid': invalid}) 
    return render(request, 'signup.html') 

def login(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/')
        invalid="Invalid Credentials"
        return render(request, 'login.html', {'invalid': invalid}) 
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('/login')

def upload(request):
    if request.method=='POST':
        user = request.user.username
        image = request.files.get('image-upload')
        caption = request.POST.get('caption')
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return render('/')
    
   

def home(request):
    post=Post.objects.all().order_by('-created_at')
    profile = Profile.objects.all()
    context = {
        'post': post,
        # 'profile': profile
    } 
    return render(request, 'main.html',context)

def likes(request, id):
    if request.method == 'GET':
        username = request.user.username
        post = get_object_or_404(Post, id=id)

        like_filter = LikePost.objects.filter(post_id=id, username=username).first()
        if like_filter is None:
            new_like = LikePost.objects.create(post_id=id, username=username)
            post.no_of_likes += 1
        else:
            like_filter.delete()
            post.no_of_likes -= 1 
    post.save()  
    return redirect('/#'+id)

def home_posts(request, id):
    post = Post.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)
    context = {
        'post': post,
        'profile': profile
    } 
    return render(request, 'main.html',context)     

