"""
==========================================================
Espacenet CLI
Patent Service
==========================================================

Responsabilités :

- Télécharger un brevet complet
- Télécharger les métadonnées
- Télécharger l'abstract
- (plus tard : claims, description, images...)

Aucun parsing n'est effectué ici.
"""

import requests

from cli.auth import OPSAuthenticator
from cli.config import REQUEST_TIMEOUT


class PatentService:

    BASE_URL = "https://ops.epo.org/3.2/rest-services/published-data"

    def __init__(self):
        self.auth = OPSAuthenticator()

    # ==========================================================
    # PRIVATE
    # ==========================================================

    def _headers(self):

        token = self.auth.get_token()

        return {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }

    # ==========================================================
    # PUBLIC
    # ==========================================================

    def get_biblio(self, publication_number):
        """
        Retourne toutes les métadonnées d'un brevet.

        Exemple :
            EP4776409A1
        """

        url = (
            f"{self.BASE_URL}/publication/"
            f"epodoc/{publication_number}/biblio"
        )

        response = requests.get(
            url,
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================

    def get_abstract(self, publication_number):
        """
        Retourne uniquement l'abstract.
        """

        url = (
            f"{self.BASE_URL}/publication/"
            f"epodoc/{publication_number}/abstract"
        )

        response = requests.get(
            url,
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================

    def get_claims(self, publication_number):
        """
        Retourne les claims (si disponibles).
        """

        url = (
            f"{self.BASE_URL}/publication/"
            f"epodoc/{publication_number}/claims"
        )

        response = requests.get(
            url,
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================

    def get_description(self, publication_number):
        """
        Retourne la description complète.
        """

        url = (
            f"{self.BASE_URL}/publication/"
            f"epodoc/{publication_number}/description"
        )

        response = requests.get(
            url,
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()