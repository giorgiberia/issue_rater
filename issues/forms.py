from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from issues.models import Issue, Vote


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["title", "description"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_description'}),
        }


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ("vote_type",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["vote_type"].widget = (
            forms.HiddenInput()
        )  # Hide the select dropdown

    def as_button_choice(self):
        return '<button type="submit" name="vote_type" value="1" class="vote-button upvote">Upvote</button> \
                <button type="submit" name="vote_type" value="-1" class="vote-button downvote">Downvote</button>'

    def save(self, issue, user, commit=True):
        vote = super().save(commit=False)
        vote.issue = issue
        vote.user = user
        if vote.vote_type == 1:
            issue.rating += 1
        elif vote.vote_type == -1:
            issue.rating -= 1
        issue.save()
        if commit:
            vote.save()
        return vote


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput)
