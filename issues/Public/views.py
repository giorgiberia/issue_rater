from django.shortcuts import render

def public_page(request):
    return render(request, 'issues/public/public_page.html')
