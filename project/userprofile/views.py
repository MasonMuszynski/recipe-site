from django.shortcuts import render

def profileindex(request):
    """
    A user's profile page

    :param request:
    :return:
    """

    return render(request, 'under_construction.html', {'page_title':'Profile'})