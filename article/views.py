from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def Article_list(request):
    article="Voice of Indium"
    return render(request,'article.html',{'articles':article})

def get_all_article(request):
    article_list=Article.objects.all().order_by('-published')
    return render(request,'getarticle.html',{'article_lists':article_list})

def article_details(request,slug):
    article=get_object_or_404(Article, slug=slug)
    return render (request,'details.html',{'article':article})

def register(request):
    if request.method=='POST':
        user_form=RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            return render(request,'account/register_done.html',{'user_form':user_form})
        
    else:
        user_form=RegistrationForm()
    return render (request,'account/register.html',{'user_form':user_form})

@login_required
def article_form(request):
    article_form=ArticleAddingForm(request.POST)
    if request.method=="POST":
        if article_form.is_valid():
            article=article_form.save(commit=False)
            article.author=request.user
            article=article_form.save()
            return redirect('articlelist')
    else:
        article_form=ArticleAddingForm()
        return render(request,'account/add_article.html',{'article_form':article_form})
@login_required
def update_article(request,slug):
    article=get_object_or_404(Article,slug=slug)
    form=ArticleUpdateForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articlelist')
    return render(request,'account/update.html',{'form':form})
@login_required
def delete_article(request,slug):
    article=get_object_or_404(Article,slug=slug)
    article.delete()
    return redirect('getarticle')










