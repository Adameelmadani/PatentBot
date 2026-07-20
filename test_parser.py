from search import search_patents
from parser import parse_search_results
from config import SEPARATOR

print(SEPARATOR)
print("PARSER TEST")
print(SEPARATOR)

data = search_patents("battery", 3)

patents = parse_search_results(data)

for patent in patents:

    print(patent)