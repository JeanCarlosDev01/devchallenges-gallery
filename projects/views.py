from django.shortcuts import render

# Device Shop Checkout project view


def dsc_project(request):
    return render(request, 'dsc_project.html')

# Pricing Table project view


def pt_project(request):
    return render(request, 'pt_project.html')

# Meet the Team Section project view


def mtts_project(request):
    return render(request, 'mtts_project.html')

# Simple Feature Section project view


def sfs_project(request):
    return render(request, 'sfs_project.html')

# Simple Article Listing project view


def sal_project(request):
    return render(request, 'sal_project.html')

# Join Our Newsletter project view


def jon_project(request):
    return render(request, 'jon_project.html')
