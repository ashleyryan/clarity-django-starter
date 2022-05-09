from django.shortcuts import render


def index(request):
    return render(
        request,
        'index.html',
    )

def cdn(request):
    return render(
        request,
        'cdn.html',
    )