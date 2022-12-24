import sys

import environ
from django.conf import settings
from django.core.management import execute_from_command_line
from django.core.management.utils import get_random_secret_key  
from django.http import HttpResponse
from django.urls import path


env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)
environ.Env.read_env()

settings.configure(
    DEBUG=env("DEBUG"),
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=env("ALLOWED_HOSTS"),
)


def index(request):
    return HttpResponse(
        "<h2>New secret key:</h2>"
        f"<h3>{get_random_secret_key()}</h3>"
    )


urlpatterns = [
    path("", index),
]


if __name__ == "__main__":
    execute_from_command_line(sys.argv)
