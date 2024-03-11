from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfilePictureForm, FavoriteTeamForm
from .models import Profile

@login_required
def user_profile(request):
    """
    Summary:
    Renders the user profile page and handles profile updates.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The HTTP response object containing the rendered user profile page.
    """
    profile = request.user.profile
    if request.method == 'POST':
        if 'change_picture' in request.POST:
            picture_form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
            if picture_form.is_valid():
                picture_form.save()
                return redirect('userprofile')
        elif 'save_favorite_team' in request.POST:
            team_form = FavoriteTeamForm(request.POST, instance=profile)
            if team_form.is_valid():
                team_form.save()
                return redirect('userprofile')
    else:
        picture_form = ProfilePictureForm(instance=profile)
        team_form = FavoriteTeamForm(instance=profile)
    return render(request, 'user_profile.html', {'picture_form': picture_form, 'team_form': team_form, 'profile': profile})
