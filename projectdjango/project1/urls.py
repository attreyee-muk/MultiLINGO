from django.urls import path
from . import views 



urlpatterns=[path("",views.home,name='home'),
path("translate",views.translate,name="translate"),
path("trans",views.trans,name="trans"),
path("srans",views.srans,name="srans"),
path("speechtospeech",views.speechtospeech ,name="speechtospeech"),
path("imagetotext",views.imagetotext,name="imagetotext"),
path("speech",views.speech,name='speech'),
path("video_feed",views.video_feed,name="video_feed")]