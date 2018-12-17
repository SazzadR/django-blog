from django.http import HttpResponse
from django.shortcuts import render


def profile(request):
    if request.user.profile.image:
        request.user.profile.image_url = request.build_absolute_uri(request.user.profile.image.url)
    else:
        request.user.profile.image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'

    return render(request, 'accounts/profile.html')
