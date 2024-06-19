from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from issues.forms import IssueForm, VoteForm
from issues.models import Issue, Vote


@login_required
def issue_list_and_create(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Issue created successfully.")
            return redirect("issue_list_and_create")
    else:
        form = IssueForm()

    issues_list = Issue.objects.all().order_by('-rating')
    all_issues_count = issues_list.count()
    paginator = Paginator(issues_list, 7)  # Show 10 issues per page
    page_number = request.GET.get("page")
    issues = paginator.get_page(page_number)
    messages.success(request, f"Your venue has {all_issues_count} issues.")
    vote_form = VoteForm()
    return render(
        request,
        "issues/issue_list_and_create.html",
        {"issues": issues, "form": form, "vote_form": vote_form},
    )


@login_required
def vote_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    user = request.user

    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            vote_type = form.cleaned_data["vote_type"]
            vote, created = Vote.objects.get_or_create(user=user, issue=issue)

            if created:
                vote.vote_type = vote_type
                vote.save()
                issue.rating += vote_type
                messages.success(request, "Your vote has been counted.")
            elif vote.vote_type == vote_type:
                messages.error(request, "You have already voted on this issue.")
            else:
                issue.rating -= vote.vote_type  # Remove previous vote
                vote.vote_type = vote_type
                vote.save()
                issue.rating += (vote_type - vote.vote_type) # Adjust for the change in vote_type
                messages.success(request, "Your vote has been updated.")
            issue.save()
        else:
            messages.error(request, "Invalid form submission.")

    return redirect("issue_list_and_create")
