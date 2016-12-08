from django.conf.urls import url, include
from django.contrib import admin
from Lab5.views import FightsView, FightView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fights/$', FightsView.as_view()),
    #url(r'^boxers/', admin.site.urls),
    url(r'^fight/(?P<id>\d+)$', FightView.as_view(), name='fight_url')
]
