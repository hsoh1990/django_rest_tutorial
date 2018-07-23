from django.shortcuts import render


def post_list(request):
    # request = <WSGIRequest: GET '/'>
    return render(request, 'blog/post_list.html', {})
