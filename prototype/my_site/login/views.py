from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect

import base64
import json
import os
import requests

from my_package.env_config import APP_CLIENT_ID, APP_CLIENT_SECRET, URI_DEFAULT


# Sample from the getting-started examples
def index(request):
    return HttpResponse("Hello, world. You're at the login index.")


def authenticate(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return redirect(
            (
                f"https://accounts.spotify.com/authorize"
                f"?client_id={APP_CLIENT_ID}&response_type=code&redirect_uri={URI_DEFAULT}/login/callback"
                f"&scope=user-read-recently-played user-top-read"
            )
        )
    else:
        raise ValueError


def callback(request: HttpRequest) -> HttpResponse:
    response: requests.Response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "content-type": "application/x-www-form-urlencoded",
            "Authorization": ("Basic " + base64.b64encode((APP_CLIENT_ID + ":" + APP_CLIENT_SECRET).encode()).decode('utf-8')),
        },
        data={
            "code": request.GET["code"],
            "redirect_uri": "http://localhost:8080/login/callback",
            "grant_type": "authorization_code",
        },
    )

    return HttpResponse(json.dumps(response.json(), indent=4))

