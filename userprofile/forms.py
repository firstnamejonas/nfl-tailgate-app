from django import forms
from .models import Profile
from chatrooms.models import Team

class ProfilePictureForm(forms.ModelForm):
    """
    Summary:
    Form for updating profile picture.
    """
    class Meta:
        model = Profile
        fields = ['picture']

class FavoriteTeamForm(forms.ModelForm):
    """
    Summary:
    Form for selecting favorite team in profile.
    """
    class Meta:
        model = Profile
        fields = ['favorite_team']

    def __init__(self, *args, **kwargs):
        super(FavoriteTeamForm, self).__init__(*args, **kwargs)
        self.fields['favorite_team'].queryset = Team.objects.all()
