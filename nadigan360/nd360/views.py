from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpRequest
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from models import *

def home(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'starter-template.html', context)
	#return render("starter-template.html","Succes")
