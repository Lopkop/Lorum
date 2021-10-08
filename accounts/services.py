from django.contrib.auth.models import User


def get_user(user_pk):
    return User.objects.get(pk=user_pk)
