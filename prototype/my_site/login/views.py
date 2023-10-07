from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect

import os

"""
# Sample from the getting-started examples
def index(request):
    return HttpResponse("Hello, world. You're at the login index.")
"""


def log_all(request: HttpRequest) -> None:
    info = {
        "scheme": request.scheme,
        "body": request.body,
        "path": request.path,
        "path_info": request.path_info,
        "method": request.method,
        "encoding": request.encoding,
        "content_type": request.content_type,
        "content_params": request.content_params,
        "GET": request.GET,
        "POST": request.POST,
        "COOKIES": request.COOKIES,
        "FILES": request.FILES,
        "META": request.META,
        "headers": request.headers,
        "resolver_match": request.resolver_match,
    }
    for k, v in info.items():
        print(f"{k}: {v}\n")


def login_redirect(request: HttpRequest) -> HttpResponse:
    client_id = os.environ.get("APP_CLIENT_ID")
    redirect_uri = os.environ.get("URI_DEFAULT")
    if request.method == "GET":
        if "authorized" in request.GET:
            return redirect(
                (
                    f"https://accounts.spotify.com/authorize"
                    f"?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}/login"
                )
            )
        else:
            log_all(request)
            return HttpResponse("Nice test.")
