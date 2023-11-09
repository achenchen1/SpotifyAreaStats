# For reference only: a small script to test the API endpoint and understanding of documentation

import json
import os
import requests

from typing import Dict

APP_CLIENT_ID = os.environ.get("APP_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("APP_CLIENT_SECRET")
TEST_ARTIST_ID = "0hEurMDQu99nJRq8pTxO14"


def get_access_token(app_client_id: str, app_client_secret: str) -> Dict[str, str]:
    # The most basic access token
    #    response = requests.post(
    #        "https://accounts.spotify.com/api/token",
    #        headers={"Content-Type": "application/x-www-form-urlencoded"},
    #        data={
    #            "grant_type": "client_credentials",
    #            "client_id": app_client_id,
    #            "client_secret": app_client_secret,
    #        },
    #    )
    import base64

    print(
        "Basic "
        + base64.b64encode((APP_CLIENT_ID + ":" + APP_CLIENT_SECRET).encode()).decode(
            "utf-8"
        )
    )
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "content-type": "application/x-www-form-urlencoded",
            "Authorization": (
                "Basic "
                + base64.b64encode(
                    (APP_CLIENT_ID + ":" + APP_CLIENT_SECRET).encode()
                ).decode("utf-8")
            ),
        },
        data={
            "code": "",  # Get code from using the authenticate endpoint on the Django server
            "redirect_uri": "http://localhost:8080/login",
            "grant_type": "authorization_code",
        },
    )
    print(response.request.method, response.request.url, response.request.headers)

    response.raise_for_status()

    return response.json()


def get_artist(artist_url: str, access_token: str) -> Dict[str, str]:
    response = requests.get(
        f"https://api.spotify.com/v1/artists/{artist_url}",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    response.raise_for_status()

    return response.json()


def get_me(user_url: str, access_token: str) -> Dict[str, str]:
    response = requests.get(
        f"https://api.spotify.com/v1/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    response.raise_for_status()

    return response.json()


def _utility_printer(json_response: Dict[str, str], function_name: str = "") -> None:
    if function_name:
        print(f"{function_name} response:")
    print(json.dumps(json_response, indent=4))
    # Pad with an extra two linebreaks for visibility
    print("\n")


# r = get_access_token(APP_CLIENT_ID, APP_CLIENT_SECRET)

# print(r)
# _utility_printer(r)
import time

response = requests.get(
    f"https://api.spotify.com/v1/me/player/recently-played?limit=50&before={int(time.time()*1000)}",
    headers={
        "Authorization": f"Bearer "  # Add auth token here, obtained from login app flow
    },
)

response.raise_for_status()
_utility_printer(response.json())
with open("test.txt", "w+") as f:
    f.write(json.dumps(response.json(), indent=4))
