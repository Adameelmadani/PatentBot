"""
==========================================================
Espacenet CLI
Search Module
==========================================================

Envoie les requêtes vers l'API Open Patent Services (OPS).

Deux services sont utilisés :

- Patent Search
- Published Data (Bibliographic Data)
"""

import requests

from auth import get_access_token

from config import (
    SEARCH_URL,
    PUBLISHED_DATA_URL,
    REQUEST_TIMEOUT,
    ACCEPT_HEADER,
)


def search_patents(query, results=5):
    """
    Search patents using the OPS Search API.

    Parameters
    ----------
    query : str
        OPS query.

    results : int
        Number of search results.

    Returns
    -------
    dict
        JSON response.
    """

    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": ACCEPT_HEADER,
    }

    params = {
        "q": query,
        "Range": f"1-{results}",
    }

    response = requests.get(
        SEARCH_URL,
        headers=headers,
        params=params,
        timeout=REQUEST_TIMEOUT,
    )

    if response.status_code != 200:
        raise Exception(
            f"Search failed ({response.status_code})\n"
            f"{response.text}"
        )

    return response.json()


def get_biblio(publication_number):
    """
    Retrieve bibliographic data of one patent.

    Parameters
    ----------
    publication_number : str

        Example:
            EP4776409A1

    Returns
    -------
    dict
        JSON response.
    """

    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": ACCEPT_HEADER,
    }

    # -----------------------------------------------------
    # Convert EP4776409A1
    # -> EP4776409.A1
    # OPS requires a dot before the kind code.
    # -----------------------------------------------------

    country = publication_number[:2]

    kind = publication_number[-2:]

    number = publication_number[2:-2]

    epodoc = f"{country}{number}.{kind}"

    url = (
        f"{PUBLISHED_DATA_URL}"
        f"/publication/epodoc/"
        f"{epodoc}"
        f"/biblio"
    )

    response = requests.get(
        url,
        headers=headers,
        timeout=REQUEST_TIMEOUT,
    )

    if response.status_code != 200:

        raise Exception(
            f"Biblio failed ({response.status_code})\n"
            f"{response.text}"
        )

    return response.json()