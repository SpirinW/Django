from django.http import HttpResponse


from django.shortcuts import render


def main_page(request) -> HttpResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def second_view(request) -> HttpResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def third_view(request) -> HttpResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def fourth_view(request) -> HttpResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def fifth_view(request) -> HttpResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def sixth_view(request) -> HttpResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')

def about_view(request):
    return HttpResponse("About Page")