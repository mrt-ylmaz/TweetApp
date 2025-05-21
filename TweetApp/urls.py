from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'TweetApp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'),
    path('addtweet/', views.addtweet, name='addtweet'),
    path('addtweetbyform', views.addtweetbyform, name="addtweetbyform"),
    path('addtweetbymodelform', views.addtweetbymodelform, name="addtweetbymodelform"),
    path('signup/',views.SingUpView.as_view(),name="signup"),
    path('deletetweet/<int:id>',views.deletetweet,name="deletetweet")
]
