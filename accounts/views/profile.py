from django.views import View
from django.shortcuts import render
from accounts.forms import UserForm
from django.http import HttpResponse


class Profile(View):
    def insert_profile_image(self, request):
        if request.user.profile.image:
            request.user.profile.image_url = request.build_absolute_uri(request.user.profile.image.url)
        else:
            request.user.profile.image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'

    def get(self, request):
        self.insert_profile_image(request)
        user_form = UserForm(instance=request.user)

        return render(request, 'accounts/profile.html', {
            'user_form': user_form
        })

    def post(self, request):
        self.insert_profile_image(request)
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

        return render(request, 'accounts/profile.html', {
            'user_form': user_form
        })
