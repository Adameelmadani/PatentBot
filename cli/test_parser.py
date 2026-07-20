from cli.search import search_patents
from cli.parser import parse_search_results
from cli.config import SEPARATOR

print(SEPARATOR)
print("PARSER TEST")
print(SEPARATOR)

data = search_patents("battery", 3)

patents = parse_search_results(data)

for patent in patents:

    print(patent)