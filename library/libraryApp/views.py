from django.shortcuts import HttpResponse


def about(request):
    return HttpResponse('Hello, world')
