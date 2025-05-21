from django.contrib import admin
from TweetApp.models import Tweet
# Register your models here.


class Tweetadmin(admin.ModelAdmin):     #admin özelleştirme bağlantısı
    fieldsets= [
        ('massege Group',{"fields":["massege"]}),
        ('Nickname Group',{"fields":["nickname"]})
    ]

admin.site.register(Tweet,Tweetadmin)
#admin özelliklerini ayarlama büyüsü
