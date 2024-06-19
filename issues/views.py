from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Issue, Vote
from .forms import IssueForm, VoteForm


# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Issue, Vote
from .forms import IssueForm, VoteForm


@login_required
def issue_list_and_create(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.rating = 0  # Ensure the rating is set to 0 by default
            issue.save()
            return redirect("issue_list_and_create")
    else:
        form = IssueForm()

    issues = Issue.objects.all()
    vote_form = VoteForm()
    return render(
        request,
        "issues/issue_list_and_create.html",
        {"issues": issues, "form": form, "vote_form": vote_form},
    )


@login_required
def vote_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            # Ensure the current user is passed to the form's save method
            try:
                form.save(issue=issue, user=request.user)
            except Exception as e:
                print(f"Error saving vote: {e}")
            return redirect('issue_list_and_create')
    return redirect('issue_list_and_create')
