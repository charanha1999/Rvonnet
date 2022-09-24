from django.shortcuts import render
from .models import Account

# Create your views here.
def check_is_superuser(user_id):
    user_obj = Account.objects.filter(
        id=user_id
    ).first()

    return user_obj.is_superuser


def check_is_staff(user_id):
    user_obj = Account.objects.filter(
        id=user_id
    ).first()

    return user_obj.is_staff


def check_is_admin(user_id):
    user_obj = Account.objects.filter(
        id=user_id
    ).first()

    return user_obj.is_admin