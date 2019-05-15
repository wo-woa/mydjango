from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from django.http import Http404
from .forms import NewTopicForm


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    # board = get_object_or_404(Board, pk=pk)
    # user = User.objects.first()#  get the currently logged in user
    # if request.method == 'POST':
    #     form = NewTopicForm(request.POST)
    #     if form.is_valid():
    #         topic = form.save()
    #         return redirect('board_topics', pk=board.pk)
    # else:
    #     form = NewTopicForm()
    # return render(request, 'new_topic.html', {'form': form})
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()  # 临时使⽤⼀个账号作为登录⽤户
        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )
        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        return redirect('board_topics', pk=board.pk)  # redirect to the created topic page
    return render(request, 'new_topic.html', {'board': board})
