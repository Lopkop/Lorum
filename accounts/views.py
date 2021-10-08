from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core import exceptions

from .services import get_user


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def user_page_view(request, pk):
    try:
        user = get_user(pk)
    except exceptions.ObjectDoesNotExist:
        return HttpResponse('User not found.')
    return render(request, 'registration/user.html', {'user': user})
