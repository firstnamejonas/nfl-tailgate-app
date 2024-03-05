from django import forms
from .models import Profile
from chatrooms.models import Team

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']

class FavoriteTeamForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['favorite_team']

    def __init__(self, *args, **kwargs):
        super(FavoriteTeamForm, self).__init__(*args, **kwargs)
        self.fields['favorite_team'].queryset = Team.objects.all()
