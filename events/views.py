from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Event
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def Events(request):
    keyword = request.GET.get("keyword")

    if keyword:
        events = Event.objects.filter(title__contains = keyword)
        return render(request,"Events.html",{"events":events})
    events = Event.objects.all()

    return render(request,"Events.html",{"events":events})
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def Publications(request):
    return render(request,"Publications.html")

def Projects(request):
    return render(request,"Projects.html")

def IPD(request):
    return render(request,"IPD.html")

def News(request):
    return render(request,"News.html")

def Collaborators(request):
    return render(request,"Collaborators.html")

def Conferences(request):
    return render(request,"Conferences.html")

def RuTAG_Club(request):
    return render(request,"RuTAG_Club.html")

@login_required(login_url = "user:login")
def dashboard(request):
    events = Event.objects.filter(author = request.user)
    context = {
        "events":events
    }
    return render(request,"dashboard2.html",context)
@login_required(login_url = "user:login")
def addEvent(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        event = form.save(commit=False)
        
        event.author = request.user
        event.save()

        messages.success(request,"Event Created Successfully!!!")
        return redirect("events:dashboard")
    return render(request,"addEvent.html",{"form":form})

@login_required(login_url = "user:login")
def updateArticle(request,id):

    events = get_object_or_404(Event,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = events)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Event Successfully Updated")
        return redirect("events:dashboard")


    return render(request,"update.html",{"form":form})
