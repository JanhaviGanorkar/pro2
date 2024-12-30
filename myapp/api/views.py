from django.shortcuts import render
from .models import Task
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from django.http import HttpResponse
def ListTodo(request):
    tasks = Task.objects.all()
    return render(request, 'ListTodo.html', {'tasks' : tasks})
    # return HttpResponse("<h1>Welcome to Chai's Django Project: about page</h1>")
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets' : tweets})

def tweet_create(request):
    if request.method == "POST":
      form = TweetForm(request.POST, request.FILES, User)
      print(form, 'form value')
      if form.is_valid():

          tweet = form.save(commit=False)
          print(tweet)
          tweet.user = request.user
          tweet.save()
          return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

# Zahed75

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    print(request.user.username)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html',{'form': form})
    

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method == "POST":
        tweet.delete()
        
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})