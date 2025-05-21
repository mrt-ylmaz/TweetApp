from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from TweetApp.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def listtweet(request):
    all_tweets= models.Tweet.objects.all()
    tweet_dict= {"tweets": all_tweets}
    return render(request,'TweetApp/listtweet.html', context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        massege = request.POST.get("massege", "")
        models.Tweet.objects.create(username=request.user, massege=massege)
        return redirect(reverse('TweetApp:listtweet')) #bağlanana urls atacak redirect ile
    else:
        return render(request, 'TweetApp/addtweet.html')

"""def addtweet(request):
        if request.POST:
              print(request.POST["nickname"])
              print(request.POST["massege"])
        return render(request,'TweetApp/addtweet.html')"""

def addtweetbyform(request):
    if request.method =="POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickkname_input"]
            massege = form.cleaned_data["massege_input"]
            models.Tweet.objects.create(nickname=nickname,massege=massege)
            return redirect(reverse("TweetApp:listtweet"))
        else:
            print("error in form!")
            return render(request,'TweetApp/addtweetbyform.html', context={"form":form})
    else:
        form = AddTweetForm()
        return render(request,'TweetApp/addtweetbyform.html', context={"form":form})
  
def addtweetbymodelform(request):
    if request.method =="POST":
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            massege = form.cleaned_data["massege"]
            models.Tweet.objects.create(nickname=nickname,massege=massege)
            return redirect(reverse("TweetApp:listtweet"))
        else:
            print("error in form!")
            return render(request,'TweetApp/addtweetbymodelform.html', context={"form":form})
    else:
        form = AddTweetModelForm()
        return render(request,'TweetApp/addtweetbymodelform.html', context={"form":form})
    
@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user==tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect('TweetApp:listtweet')

class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
