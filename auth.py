"""
==========================================================
Espacenet CLI
Authentication Module
==========================================================

Gère l'authentification OAuth2 auprès de l'API
Open Patent Services (OPS).

Auteur : Nouaaman Chaaibi
"""

import base64
import requests

from config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    AUTH_URL,
    REQUEST_TIMEOUT,
)


def get_access_token():
    """
    Authenticate with the OPS API.

    Returns
    -------
    str
        OAuth2 access token.

    Raises
    ------
    Exception
        If authentication fails.
    """

    credentials = f"{CONSUMER_KEY}:{CONSUMER_SECRET}"

    encoded_credentials = base64.b64encode(
        credentials.encode()
    ).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    payload = {
        "grant_type": "client_credentials"
    }

    response = requests.post(
        AUTH_URL,
        headers=headers,
        data=payload,
        timeout=REQUEST_TIMEOUT,
    )

    if response.status_code != 200:
        raise Exception(
            f"Authentication failed ({response.status_code})\n"
            f"{response.text}"
        )

    return response.json()["access_token"]