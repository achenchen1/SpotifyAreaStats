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


def get_me(user_url: str, access_token: str) -> Dict[str, str]:
    response = requests.get(f"https://api.spotify.com/v1/me",
                            headers={"Authorization": f"Bearer {access_token}"})

    response.raise_for_status()

    return response.json()


def _utility_printer(json_response: Dict[str, str], function_name: str = "") -> None:
    if function_name:
        print(f"{function_name} response:")
    print(json.dumps(json_response, indent=4))
    # Pad with an extra two linebreaks for visibility
    print("\n")


