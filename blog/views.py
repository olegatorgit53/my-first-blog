from django.shortcuts import render, HttpResponse


def index_controller(request):
    return HttpResponse('<h1>PRIVET KOLLEGI</h1>')