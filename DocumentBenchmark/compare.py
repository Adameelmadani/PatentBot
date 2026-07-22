"""
==========================================================
Document Benchmark
Comparison Script
==========================================================

Compare:

- Classic Parser
- MarkItDown
- Docling
"""

from pathlib import Path

from metrics import compute_metrics

from parser_extractor.extractor import extract_document as parser_extract
from markitdown_extractor.extractor import extract_document as markitdown_extract
from docling_extractor.extractor import extract_document as docling_extract


INPUT_FOLDER = Path("input")


TOOLS = [

    ("Classic Parser", parser_extract),

    ("MarkItDown", markitdown_extract),

    ("Docling", docling_extract)

]


def print_metrics(metrics):

    print(f"Tool          : {metrics['tool']}")

    print(f"Time          : {metrics['processing_time']} s")

    print(f"Characters    : {metrics['characters']}")

    print(f"Words         : {metrics['words']}")

    print(f"Lines         : {metrics['lines']}")

    print(f"Paragraphs    : {metrics['paragraphs']}")

    print(f"Titles        : {metrics['titles']}")

    print(f"Lists         : {metrics['lists']}")

    print(f"Tables        : {metrics['tables']}")


def main():

    files = list(INPUT_FOLDER.iterdir())

    if not files:

        print("No documents found.")

        return

    print("=" * 90)

    print("DOCUMENT EXTRACTION BENCHMARK")

    print("=" * 90)

    for file in files:

        print("\n")

        print("=" * 90)

        print(file.name)

        print("=" * 90)

        for tool_name, extractor in TOOLS:

            print()

            print("-" * 70)

            print(tool_name)

            print("-" * 70)

            try:

                result = extractor(file)

                metrics = compute_metrics(result)

                print_metrics(metrics)

            except Exception as e:

                print("ERROR")

                print(e)


if __name__ == "__main__":

    main()