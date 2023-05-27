from django.urls import path,include
from music_app.views import *
urlpatterns = [
   
    path('', home, name='home'),
    path('upload/', upload_music, name='upload_music'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/',custom_logout, name='logout'),
    path('myPlayList/',my_playlist,name='myPlayList'),
    path('shared_with_me',shared_with_me,name='shared_with_me'),
    path("check_email/",check_email),
    path('delete-music/', delete_music, name='delete_music'),
    

]