from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


@login_required
def createpost(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid:
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.author = request.user
            post.image = 'images/' + request.POST.get('image')
            post.save()
            allposts = Post.objects.all()

            context = {'allposts': allposts}
            return render(request, 'home.html', context)

    else:
        form = PostForm()
        return render(request, 'create.html', {'form':form})
    

def home(request):
    allposts = Post.objects.all()

    context = {'allposts': allposts}

    return render(request, 'home.html', context)


def detail_post_view(request, id=None):
    eachpost = get_object_or_404(Post, id=id)
    print(eachpost.image.url)
    context = {'eachpost': eachpost}

    return render(request, 'detail.html', context)

