from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import  PostModelForm, CommentForm

def home(request):
    return render(request, 'base.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'myapp/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'myapp/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

@login_required(login_url='/login/')
def posts_list_view(request):
    posts = Post.objects.all()
    form = SearchForm()
    if request.methon == "GET":
        query_params = request.GET
        search = query_params.get("search")
        category_id = query_params.get("category_id")
        
        

# def post_create_form(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             Post.objects.create(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 rate=form.cleaned_data['rate'],
#                 image=form.cleaned_data['image']
#             )
#             return redirect('post_list')
#     else:
#         form = PostForm()
#     return render(request, 'myapp/post_create.html', {'form': form, 'title': 'Создание поста (Form)'})



def post_create_modelform(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm()
    return render(request, 'myapp/post_create.html', {'form': form, 'title': 'Создание поста'' (ModelForm)'})
    