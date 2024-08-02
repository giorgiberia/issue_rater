from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from issues.forms import IssueForm, VoteForm
from issues.models import Issue, Vote
from .forms import UserRegistrationForm, UserLoginForm


def about(request):
    return render(request, "issues/about.html")


@login_required
def issue_list_and_create(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Issue created successfully.")
            return redirect("issue_list_and_create")
        else:
            messages.error(request, "Issue was not created.")
    else:
        form = IssueForm()

    if search_query := request.GET.get("search", ""):
        issues_qs = Issue.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )
    else:
        issues_qs = Issue.objects.all()

    all_issues_count = issues_qs.count()
    issues_qs = issues_qs.order_by("-rating")
    paginator = Paginator(issues_qs, 7)  # Show 7 issues per page
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
                issue.rating += (
                        vote_type - vote.vote_type
                )  # Adjust for the change in vote_type
                messages.success(request, "Your vote has been updated.")
            issue.save()
        else:
            messages.error(request, "Invalid form submission.")

    return redirect("issue_list_and_create")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if not form.is_valid():
            return render(request, 'registration/register.html', {'form': form})
        user = form.save()
        login(request, user)
        messages.success(request, 'Registration successful.')
        return redirect('issue_list_and_create')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'registration/login.html', {'form': form})
        user = form.get_user()
        login(request, user)
        messages.success(request, 'Login successful.')
        return redirect('issue_list_and_create')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')
