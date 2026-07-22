"""
==========================================================
Classic Parser Test
==========================================================

Test the classic parser extractor.

Usage

python test_parser.py
"""

from pathlib import Path

from extractor import extract_document


INPUT_FOLDER = Path("../input")


def main():

    files = list(INPUT_FOLDER.iterdir())

    if not files:
        print("No files found.")
        return

    print("=" * 80)
    print("CLASSIC PARSER TEST")
    print("=" * 80)

    for file in files:

        print("\n" + "=" * 80)
        print(file.name)
        print("=" * 80)

        try:

            result = extract_document(file)

            print("Tool :", result["tool"])
            print("Type :", result["file_type"])
            print("Pages :", result["page_count"])
            print("Time :", result["processing_time"], "seconds")

            print("\nTEXT PREVIEW\n")

            preview = result["text"][:1000]

            print(preview)

            if len(result["text"]) > 1000:
                print("\n...")

            print("\nCharacters :", len(result["text"]))
            print("Words :", len(result["text"].split()))

        except Exception as e:

            print("ERROR :", e)


if __name__ == "__main__":
    main()