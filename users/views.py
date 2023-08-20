from django.shortcuts import render


def users(request):
    """ Display the user's profile. """

    template = 'users/users.html'
    context = {}

    return render(request, template, context)