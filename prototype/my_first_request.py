# For reference only: a small script to test the API endpoint and understanding of documentation

import json
import os
import requests

from typing import Dict

APP_CLIENT_ID = os.environ.get("APP_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("APP_CLIENT_SECRET")
TEST_ARTIST_ID = "0hEurMDQu99nJRq8pTxO14"


def get_access_token(app_client_id: str, app_client_secret: str) -> Dict[str, str]:
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "client_credentials",
            "client_id": app_client_id,
            "client_secret": app_client_secret,
        },
    )

    response.raise_for_status()

    return response.json()


def get_artist(artist_url: str, access_token: str) -> Dict[str, str]:
    response = requests.get(
        f"https://api.spotify.com/v1/artists/{artist_url}",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    response.raise_for_status()

    return response.json()


print(
    "Access token response: {}".format(
        access_token_response := get_access_token(APP_CLIENT_ID, APP_CLIENT_SECRET)
    ),
    end="\n\n",
)

access_token = access_token_response["access_token"]
token_type = access_token_response["token_type"]
expires_in = access_token_response["expires_in"]

####################################
# Strictly for printing visibility #
####################################
print(json.dumps(access_token_response, indent=4), end="\n\n")

print(
    "Artist response: {}".format(
        artist_response := get_artist(TEST_ARTIST_ID, access_token)
    ),
    end="\n\n",
)

####################################
# Strictly for printing visibility #
####################################
print(json.dumps(artist_response, indent=4), end="\n\n")
