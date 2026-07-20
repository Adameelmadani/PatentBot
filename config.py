"""
==========================================================
Espacenet CLI
Configuration File
==========================================================

Centralise toute la configuration du projet.
"""

# ==========================================================
# API CREDENTIALS
# ==========================================================

CONSUMER_KEY = "0SWogyTiZrttdLBnYHZN8ny66ns7VwWt2jOq6dOjBgkVDaBk"

CONSUMER_SECRET = "cMwMM9aiw5HsjjzxxHCjmWMf1mQJBn9eiO6IomD958hrsgzWQRucRHSLVhrAE0TJ"


# ==========================================================
# OPS ENDPOINTS
# ==========================================================

AUTH_URL = "https://ops.epo.org/3.2/auth/accesstoken"

SEARCH_URL = "https://ops.epo.org/3.2/rest-services/published-data/search"

PUBLISHED_DATA_URL = "https://ops.epo.org/3.2/rest-services/published-data"


# ==========================================================
# HTTP SETTINGS
# ==========================================================

REQUEST_TIMEOUT = 30

ACCEPT_HEADER = "application/json"


# ==========================================================
# CLI SETTINGS
# ==========================================================

APP_NAME = "Espacenet Patent Search CLI"

VERSION = "1.0.0"

DEFAULT_RESULTS = 5

PREFERRED_LANGUAGE = "en"

SEPARATOR = "=" * 80


# ==========================================================
# SUPPORTED SEARCH FIELDS
# ==========================================================

SEARCH_FIELDS = {
    "keyword": "",
    "title": "ti",
    "abstract": "ab",
    "title_abstract": "ta",
    "applicant": "pa",
    "inventor": "in",
    "ipc": "ipc",
    "cpc": "cpc",
    "publication_number": "pn",
    "application_number": "ap",
    "publication_date": "pd",
}