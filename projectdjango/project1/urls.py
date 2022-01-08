from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[path("",views.home,name='home'),
path("translate",views.translate,name="translate"),
path("trans",views.trans,name="trans"),
path("srans",views.srans,name="srans"),
path("speechtospeech",views.speechtospeech ,name="speechtospeech"),
path("imagetotext",views.imagetotext ,name="imagetotext"),
path("speech",views.speech,name='speech'),
] 
