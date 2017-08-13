"""
Generic views for website
"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
    return render(request, 'logout.html')