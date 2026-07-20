from search import (
    search_patents,
    get_biblio,
)

from parser import (
    parse_search_results,
    parse_biblio,
)

from config import SEPARATOR


print(SEPARATOR)
print("SEARCH TEST")
print(SEPARATOR)

# ----------------------------------------------------
# Search
# ----------------------------------------------------

data = search_patents("battery", 3)

patents = parse_search_results(data)

print("\nSearch Results\n")

for patent in patents:

    print(patent)

# ----------------------------------------------------
# Bibliographic Data
# ----------------------------------------------------

print("\n")
print(SEPARATOR)
print("BIBLIO TEST")
print(SEPARATOR)

publication = patents[0]["publication_number"]

print(f"\nRetrieving : {publication}\n")

data = get_biblio(publication)

patent = parse_biblio(data)

print("Publication :", patent["publication_number"])
print("Family      :", patent["family_id"])
print("Title       :", patent["title"])

print("\nApplicants")

for applicant in patent["applicants"]:
    print("-", applicant)

print("\nInventors")

for inventor in patent["inventors"]:
    print("-", inventor)

print("\nAbstract\n")

print(patent["abstract"])