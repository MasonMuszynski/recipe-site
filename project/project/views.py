"""
Generic views for website
"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm

def home(request):
    """
    The homepage of the recipe site

    :param request:
    :return:
    """
    # TODO: site name pagetitle
    return render(request, 'home.html', {'request': request, 'page_title': 'Site Name'})


def about(request):
    """
    The about page of the recipes site

    :param request:
    :return:
    """
    return render(request, 'under_construction.html', {'request': request, 'page_title': 'About'})


# TODO: restrict to users not logged in
def loginUser(request):
    """
    logs in a user
    login form redirects to this view (/login/)

    :param request: POST obtained from navbar form on base.html
    :return: redirects to the page they were viewing
            (because users can login from anwhere b/c login is in navbar)
    """

    # TODO: Instead of 404 response, instead have a notification pop up on current page

    try:
        username = request.POST['username']
        password = request.POST['password']
        nextPage = request.POST['next'] # Path of the page the user was at when they logged in
    except Exception:
        raise Http404("Login Unsuccessful.")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(nextPage)
    else:
        messages.error(request, 'Login unsuccessful. Please try again.')
        return HttpResponseRedirect(nextPage)
        # raise Http404("Login Unsuccessful.")


# TODO: restrict to logged in users only
def logoutUser(request):
    """
    logs out the user

    :param request: the user
    :return: a goodbye page confirming that the user has logged out.
    """

    # TODO: use try/except.

    logout(request)
    return render(request, 'logout.html', {'page_title':'Logout'})


def register(request):
    """
    Register a user

    :param request: The user to be registered
    :return: user registration form
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm
    return render(request, 'register.html', {'form': form})

