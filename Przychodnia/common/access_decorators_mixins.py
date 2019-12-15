from functools import wraps

from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def uprawniania_rejestratorka_wymagane(function):
    def wrap(request, *args, **kwargs):
        conditions = [
            request.user.role == 'REJ',
            request.user.is_superuser
        ]
        if any(conditions):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def uprawniania_lekarz_wymagane(function):
    def wrap(request, *args, **kwargs):
        conditions = [
            request.user.role == 'LEK',
            request.user.is_superuser
        ]
        if any(conditions):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def uprawniania_przegladanie_listy_pacjentow(function):
    def wrap(request, *args, **kwargs):
        conditions = [
            request.user.role == 'REJ',
            request.user.role == 'LEK',
            request.user.is_superuser
        ]
        if any(conditions):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
