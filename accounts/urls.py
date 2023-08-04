
from django.urls import path
from .views import CreateUser, home, login_view, publisher, logout_view, userslist, deleteView, articleCreation, viewArticles, articlesToBePublished, editArticle
urlpatterns = [
   path('create-user', CreateUser, name='create-user'),
   path('', home),
   path('login/', login_view, name="login"),
   path('home', home, name='home'),
   # path('author', author, name='author'),
   path('publisher', articlesToBePublished, name='publisher'),
   path('logout/', logout_view, name='logout'),
   path('userslist/', userslist, name='userslist'),
   path('delete', deleteView, name='delete'),                                                                                        
   # path('delete/<int:pk>',deleteView, name='delete')
   path('articles',articleCreation, name='articles' ),
   path('author',viewArticles, name='author'),
   path('editArticle/<int:article_id>/', editArticle, name='editArticle' )
]