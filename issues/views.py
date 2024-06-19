from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import IssueForm, VoteForm
from .models import Issue

def issue_list_and_create(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("issue_list_and_create")
    else:
        form = IssueForm()

    issues_list = Issue.objects.all()
    paginator = Paginator(issues_list, 7)  # Show 10 issues per page
    page_number = request.GET.get("page")
    issues = paginator.get_page(page_number)

    vote_form = VoteForm()
    return render(
        request,
        "issues/issue_list_and_create.html",
        {"issues": issues, "form": form, "vote_form": vote_form},
    )


@login_required
def vote_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            # Ensure the current user is passed to the form's save method
            try:
                form.save(issue=issue, user=request.user)
            except Exception as e:
                print(f"Error saving vote: {e}")
            return redirect("issue_list_and_create")
    return redirect("issue_list_and_create")
