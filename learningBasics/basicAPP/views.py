from cv2 import ml_ParamGrid
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return(HttpResponse("Sasappa is cool"))
    data={'insert_me':'This is from views.py','Thenga':'Kola'}

    return(render(request,"basicAPP/index.html",context=data))


def help(request):
    help={"help":"THIS IS THE HELP PAGE from template tags"}
    return(render(request,"basicAPP/help.html",context=help))