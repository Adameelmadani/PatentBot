from cli.patent import PatentService
import json

service = PatentService()

publication = "EP4776409A1"

print("=" * 80)
print("BIBLIO TEST")
print("=" * 80)

data = service.get_biblio(publication)

print(json.dumps(data, indent=2)[:2500])

print("\n")

print("=" * 80)
print("ABSTRACT TEST")
print("=" * 80)

data = service.get_abstract(publication)

print(json.dumps(data, indent=2)[:1500])