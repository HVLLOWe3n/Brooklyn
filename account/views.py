from django.shortcuts import render


def some(request):
    return render(request, 'base/base.html')
