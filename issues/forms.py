from django import forms

from issues.models import Issue, Vote


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["title", "description", "rating"]

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('vote_type',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vote_type'].widget = forms.HiddenInput()  # Hide the select dropdown

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
