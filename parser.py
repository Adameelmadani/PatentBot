"""
==========================================================
Espacenet CLI
Parser Module
==========================================================

Transforme les réponses JSON de l'API OPS
en objets Python simples.
"""


def parse_search_results(data):
    """
    Parse search results.

    Parameters
    ----------
    data : dict
        JSON returned by the OPS Search API.

    Returns
    -------
    list
        List of patents.
    """

    patents = []

    world = data.get("ops:world-patent-data", {})

    search = world.get("ops:biblio-search", {})

    publications = (
        search
        .get("ops:search-result", {})
        .get("ops:publication-reference", [])
    )

    if not isinstance(publications, list):
        publications = [publications]

    for patent in publications:

        doc = patent.get("document-id", {})

        patents.append({

            "publication_number":
                f"{doc.get('country', {}).get('$', '')}"
                f"{doc.get('doc-number', {}).get('$', '')}"
                f"{doc.get('kind', {}).get('$', '')}",

            "family_id":
                patent.get("@family-id", "N/A")

        })

    return patents


def parse_biblio(data):
    """
    Parse bibliographic data.
    """

    world = data.get("ops:world-patent-data", {})

    exchange = world.get("exchange-documents", {}).get("exchange-document", {})

    # Certaines réponses retournent une liste
    if isinstance(exchange, list):
        exchange = exchange[0]

    biblio = exchange.get("bibliographic-data", {})

    # ----------------------------------------------------
    # Publication Number
    # ----------------------------------------------------

    publication = (
        exchange.get("@country", "")
        + exchange.get("@doc-number", "")
        + exchange.get("@kind", "")
    )

    # ----------------------------------------------------
    # Family ID
    # ----------------------------------------------------

    family = exchange.get("@family-id", "N/A")

    # ----------------------------------------------------
    # Title
    # ----------------------------------------------------

    title = "N/A"

    titles = biblio.get("invention-title", [])

    if not isinstance(titles, list):
        titles = [titles]

    # priorité : anglais

    for t in titles:

        if t.get("@lang") == "en":

            title = t.get("$", "N/A")

            break

    # sinon premier titre disponible

    if title == "N/A" and len(titles) > 0:

        title = titles[0].get("$", "N/A")

    # ----------------------------------------------------
    # Abstract
    # ----------------------------------------------------

    abstract = "N/A"

    abstract_data = exchange.get("abstract")

    if abstract_data:

        p = abstract_data.get("p")

        if isinstance(p, dict):

            abstract = p.get("$", "N/A")

        elif isinstance(p, list):

            abstract = " ".join(

                paragraph.get("$", "")

                for paragraph in p

            )

    # ----------------------------------------------------
    # Applicants
    # ----------------------------------------------------

    applicants = []

    app = (
        biblio
        .get("parties", {})
        .get("applicants", {})
        .get("applicant", [])
    )

    if isinstance(app, dict):
        app = [app]

    for a in app:

        name = (
            a.get("applicant-name", {})
             .get("name", {})
             .get("$")
        )

        if name:
            applicants.append(name)

    # ----------------------------------------------------
    # Inventors
    # ----------------------------------------------------

    inventors = []

    inv = (
        biblio
        .get("parties", {})
        .get("inventors", {})
        .get("inventor", [])
    )

    if isinstance(inv, dict):
        inv = [inv]

    for i in inv:

        name = (
            i.get("inventor-name", {})
             .get("name", {})
             .get("$")
        )

        if name:
            inventors.append(name)

    # ----------------------------------------------------

    return {

        "publication_number": publication,

        "family_id": family,

        "title": title,

        "abstract": abstract,

        "applicants": applicants,

        "inventors": inventors

    }