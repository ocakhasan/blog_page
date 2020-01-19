from django.views import generic
from .models import Post, Contact
from .forms import CommentForm, ContactForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def PostList(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    latest = Post.objects.filter(status=1).order_by('-created_on')[:4]
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    post_list =  paginator.get_page(page)
    """try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)"""
    return render(request,
                  'blog/index.html',
                  {'page': page,
                  'latest': latest,
                   'post_list': post_list})


    

def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    title = post.title
    posts = Post.objects.filter(status=1).order_by('-created_on')
    latest = Post.objects.filter(status=1).order_by('-created_on')[:4]
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                            'title': title,
                                            'latest': latest,
                                            'posts': posts,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    template_name = 'blog/contact.html'
    new_contact = None
    contact_form = ContactForm(request.POST)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        
        contact_form.name = name
        contact_form.email = email
        contact_form.body = body

        new_contact = contact_form.save(commit=False)
        new_contact.save()

    return render(request, template_name, {
                                           'new_contact': new_contact,
                                           'contact_form': contact_form})
    
