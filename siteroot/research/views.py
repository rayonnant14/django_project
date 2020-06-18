from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Researcher, Post
from django.template import loader
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='/research/login')
def index(request):
    context = {'username': request.user.username}
    return HttpResponse(render(request, 'research/index.html', context))

@login_required(login_url='/research/login')
def log_out(request):
    logout(request)
    redirect_url = request.GET['next'] or reverse('index')
    return redirect(redirect_url)

def log_in(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            check_user_exist = Researcher.objects.filter(author=username).count()
            if check_user_exist == 0:
                Researcher.objects.create(author=username)
            return redirect(request.GET['next'])
        else:
            error = 'Invalid credentials!'
    else:
        error = None
    return HttpResponse(render(request, 'research/login.html', {'error' : error}))

@login_required(login_url='/research/login')
def render_researcher(request, researcher_id):
    researcher = get_object_or_404(Researcher, pk=researcher_id)
    #researcher = Researcher.objects.filter(id=researcher_id)
    posts = Post.objects.filter(author_id=researcher_id).order_by('-created_at')
    #posts = researcher.post_set.order_by('-created_at')
    context = {'researcher': researcher, 'posts': posts}
    return HttpResponse(render(request, 'research/researcher.html', context))

def get_researcher(request, researcher_id):
    return render_researcher(request, researcher_id)

def get_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return HttpResponse(render(request, 'research/post.html', context))

def get_all_posts(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return HttpResponse(render(request, 'research/posts.html', context))

def get_all_researchers(request):
    researchers = Researcher.objects.all()
    context = {'researchers' : researchers}
    return HttpResponse(render(request, 'research/researchers.html', context))

def render_creation_page(request, additional_context={}):
    context = {**additional_context}
    return HttpResponse(render(request, 'research/post_creation.html', context))

@login_required(login_url='/research/login')
def create_post(request):
    #researcher = request.user.username
    researcher = Researcher.objects.filter(author=request.user.username)
    subject = request.POST.get('subject')
    text = request.POST.get('text')

    error_message = None

    if not subject or subject.isspace():
        error_message = 'Please provide non-empty subject!'
    elif not text or text.isspace():
        error_message = 'Please provide non-empty text!'
    if error_message:
        context = {'error':error_message, 'subject':subject, 'text': text}
        return render_creation_page(request, additional_context=context)
    else:
        Post.objects.create(post=researcher[0], author_id=researcher[0].id, subject=subject, text=text)
        return HttpResponse('<body style="background-color:#cccfff"><h1> Your post created successfully!</h1></body>')
