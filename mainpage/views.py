from django.shortcuts import render, get_object_or_404, reverse, redirect

# Create your views here.


def index(request):
    """A view to return the index page"""

    return render(request, "mainpage/index.html")


def error_404(request, exception):
    return render(request, "404.html", status=404)


def error_403(request, exception):
    return render(request, "403.html", status=403)


def server_error(request, template_name="500.html"):
    return render(request, template_name, status=500)


def bad_request(request, exception):
    return render(request, "400.html", status=400)
