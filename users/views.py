from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def users(request):
    """ Display the user's profile. """
    users = get_object_or_404(UserProfile, user=request.user)

    template = 'users/users.html'
    context = {
        'users': users,
    }

    return render(request, template, context)