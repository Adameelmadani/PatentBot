"""
==========================================================
Espacenet Patent Search CLI
==========================================================

Mini client en ligne de commande utilisant
l'API Open Patent Services (OPS).

Auteur : Nouaaman Chaaibi
"""

from config import (
    APP_NAME,
    VERSION,
    DEFAULT_RESULTS,
    SEPARATOR,
)

from search import (
    search_patents,
    get_biblio,
)

from parser import (
    parse_search_results,
    parse_biblio,
)


# ==========================================================
# SEARCH TYPES
# ==========================================================

SEARCH_TYPES = {

    "1": ("Keyword Search", ""),

    "2": ("Title Search", "ti"),

    "3": ("Abstract Search", "ab"),

    "4": ("Title or Abstract", "ta"),

    "5": ("Applicant Search", "pa"),

    "6": ("Inventor Search", "in"),

    "7": ("IPC Search", "ipc"),

    "8": ("CPC Search", "cpc"),

    "9": ("Publication Number", "pn"),

    "10": ("Application Number", "ap"),

}


# ==========================================================
# DISPLAY FUNCTIONS
# ==========================================================

def print_separator():

    print(SEPARATOR)


def print_header():

    print_separator()

    print(APP_NAME)

    print(f"Version {VERSION}")

    print_separator()


def print_menu():

    print("\nSearch Types\n")

    for key, value in SEARCH_TYPES.items():

        print(f"{key:>2} - {value[0]}")

    print("\n 0 - Exit")


# ==========================================================
# QUERY BUILDER
# ==========================================================

def build_query(field, value):
    """
    Build an OPS query.

    Examples
    --------
    battery

    ti="battery"

    pa=Samsung
    """

    value = value.strip()

    if field == "":

        return value

    if " " in value:

        return f'{field}="{value}"'

    return f"{field}={value}"


# ==========================================================
# USER INPUT
# ==========================================================

def ask_search():

    while True:

        print_menu()

        choice = input("\nChoice : ").strip()

        if choice == "0":

            return None

        if choice not in SEARCH_TYPES:

            print("\nInvalid choice.\n")

            continue

        search_name, field = SEARCH_TYPES[choice]

        print(f"\n{search_name}")

        query = input("Query : ").strip()

        if not query:

            print("\nQuery cannot be empty.\n")

            continue

        results = input(
            f"Number of results [{DEFAULT_RESULTS}] : "
        ).strip()

        if results == "":

            results = DEFAULT_RESULTS

        else:

            results = int(results)

        return {

            "query": build_query(field, query),

            "results": results,

            "name": search_name,

        }
    
# ==========================================================
# DISPLAY PATENT
# ==========================================================

def display_patent(patent, index):
    """
    Display one patent.
    """

    print()
    print_separator()
    print(f"PATENT #{index}")
    print_separator()

    print(f"Publication Number : {patent['publication_number']}")
    print(f"Family ID          : {patent['family_id']}")

    print("\nTitle")
    print("-" * 60)
    print(patent["title"])

    print("\nApplicants")
    print("-" * 60)

    if patent["applicants"]:

        for applicant in patent["applicants"]:
            print(f"• {applicant}")

    else:
        print("N/A")

    print("\nInventors")
    print("-" * 60)

    if patent["inventors"]:

        for inventor in patent["inventors"]:
            print(f"• {inventor}")

    else:
        print("N/A")

    print("\nAbstract")
    print("-" * 60)
    print(patent["abstract"])


# ==========================================================
# SEARCH WORKFLOW
# ==========================================================

def run_search():
    """
    Complete search workflow.
    """

    request = ask_search()

    if request is None:
        return False

    print()
    print_separator()
    print("SEARCHING...")
    print_separator()

    try:

        # -----------------------------------------
        # Search
        # -----------------------------------------

        data = search_patents(
            request["query"],
            request["results"],
        )

        patents = parse_search_results(data)

        if len(patents) == 0:

            print("\nNo patent found.\n")

            return True

        print(f"\n{len(patents)} patent(s) found.\n")

        # -----------------------------------------
        # Retrieve detailed information
        # -----------------------------------------

        for index, result in enumerate(patents, start=1):

            print(
                f"Loading patent {index}/{len(patents)}..."
            )

            biblio = get_biblio(
                result["publication_number"]
            )

            patent = parse_biblio(biblio)

            display_patent(
                patent,
                index,
            )

    except Exception as error:

        print()
        print_separator()
        print("ERROR")
        print_separator()

        print(error)

    return True

# ==========================================================
# MAIN
# ==========================================================

def main():
    """
    Main program.
    """

    print_header()

    while True:

        continue_program = run_search()

        if not continue_program:
            break

        answer = input(
            "\nDo you want to perform another search? (y/n): "
        ).strip().lower()

        if answer not in ("y", "yes"):

            break

    print()
    print_separator()
    print("Thank you for using Espacenet Patent Search CLI.")
    print_separator()


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    main()