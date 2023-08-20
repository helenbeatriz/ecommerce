from django.shortcuts import render, get_object_or_404
from django.contrib import messages


from .models import UserProfile
from .forms import UserProfileForm


def users(request):
    """ Display the user's profile. """
    users = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=users)
    orders = users.orders.all()

    template = 'users/users.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)