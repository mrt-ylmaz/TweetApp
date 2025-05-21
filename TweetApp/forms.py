#burası opsiyoneldir
from django import forms
from django.forms import ModelForm
from TweetApp.models import Tweet

class AddTweetForm(forms.Form):
    nickkname_input = forms.CharField(label="username",max_length=50)
    massege_input = forms.CharField(label="massege",max_length=100,
                                 widget=forms.Textarea(attrs={"class": 'AddTweetForm'}))

class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username","massege"]
