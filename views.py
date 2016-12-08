from django.shortcuts import render
#from django.conf.urls import url
#from django.http import HttpResponse
from django.views.generic import View
from Lab5.data import fights, fights_dict

class FightsView(View):
    def get(self, request):
        return render(request, 'main_page.html', {'fights': fights})

class FightView(View):
    def get(self, request, id):
        fight = fights_dict.get(int(id))
        return render(request, 'fight.html', {'fight': fight})