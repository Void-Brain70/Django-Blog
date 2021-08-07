from django.contrib import admin
from django.urls import path
from .views import postDetails, showPost,postCreate,userLogin,userCreate,userLogout 

urlpatterns = [
    path('showPost', showPost ,name='showPost'),
    path('postDetails/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<int:second>/<slug:slug>', postDetails ,name='postDetails'),
    path('createPost', postCreate ,name="createPost"),
    path('userLogin', userLogin ,name="userLogin"),
    path('userLogout', userLogout ,name="userLogout"),
    path('userCreate', userCreate ,name="userCreate")
]