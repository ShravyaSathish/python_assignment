from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, LoginForm, ArticleCreationForm, ArticleEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from .models import User, ArticlesModel, StatusChoices
from django.http import JsonResponse
import json
def home(request):
    articles = ArticlesModel.objects.filter(status=StatusChoices.PUBLISHED.value)
    return render(request, 'home.html', {'articles':articles})


# def author(request):
#     return render(request, 'author.html')

def publisher(request):
    return render(request, 'publisher.html')

@login_required
@user_passes_test(lambda user: user.is_superuser)
def CreateUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('userslist')
    else:
        form = UserForm()
    return render(request, 'addUser.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            # print(user.role=='author')
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('userslist')
            
            if user.role == 'author':
                login(request, user)
                return redirect('author')
            if user.role == 'publisher':
                login(request, user)
                return redirect('publisher')
            else:
                messages.error(request, 'Invalid Credentials')

        else:
            messages.error(request, 'error form validation')
    form = LoginForm()
    return render(request, 'login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('home')


def userslist(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'userslist.html', {'users':users})


def deleteView(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        User.objects.filter(email=email).delete()
    


@login_required
@user_passes_test(lambda user: user.role == 'author') 
def articleCreation(request):
    if request.method == 'POST':
        form = ArticleCreationForm(request.POST, request.FILES)
        print(request.user)
        print(form.is_valid())
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user 
            article.status = 'draft'
            article.save()
            return redirect('author')
        else:
            print(form.errors)
    else:
        form = ArticleCreationForm()
    return render(request, 'articles.html', {'form': form})


@login_required
@user_passes_test(lambda user: user.role == 'author') 
def viewArticles(request):
    articles = ArticlesModel.objects.filter(user_id =request.user)
    return render(request, 'author.html', {'articles':articles})




@login_required
@user_passes_test(lambda user: user.role == 'publisher') 
def articlesToBePublished(request):
    articles = ArticlesModel.objects.exclude(status=StatusChoices.PUBLISHED.value)
    return render(request, 'publisher.html', {'articles':articles})


@login_required
@user_passes_test(lambda user: user.role == 'publisher')
def editArticle(request, article_id):
        print(article_id)
        article = ArticlesModel.objects.get(id=article_id)
        form = ArticleEditForm(request.POST, request.FILES ,instance=article)
        print(form.is_valid())   
        if form.is_valid():
                print(form.is_valid())
                data = form.save()
                print("fff", data)
                data.publisher = request.user
                data.is_editted = True
                data.status = 'published'
                data.save()
                return redirect('home')
        else:
                print(form.errors)
        form = ArticleEditForm(instance=article)
        return render(request, 'edit.html', {'form': form, 'article':article})






    











