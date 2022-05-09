from django.shortcuts import render


def index(request):
    return render(
        request,
        'index.html',
    )

def webpack(request):
    return render(
        request,
        'webpack.html',
    )