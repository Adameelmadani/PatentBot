"""
==========================================================
Document Benchmark
Docling Extractor
==========================================================

Extract text from documents using IBM Docling.

Supported formats include:
- PDF
- DOCX
- PPTX
- HTML
- Markdown
- TXT
- ...

The extracted content is converted into Markdown.
"""

from pathlib import Path
import time

from docling.document_converter import DocumentConverter

def save_output(file_path, text, extension="txt"):
    """
    Save extracted text into the output folder.
    """

    output_dir = Path("../output/docling")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{Path(file_path).stem}.{extension}"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

# ==========================================================
# Initialize converter
# ==========================================================

converter = DocumentConverter()


# ==========================================================
# Extract document
# ==========================================================

def extract_document(file_path):
    """
    Extract a document using Docling.

    Parameters
    ----------
    file_path : str | Path

    Returns
    -------
    dict
    """

    start = time.time()

    result = converter.convert(file_path)

    processing_time = round(time.time() - start, 3)

    document = result.document

    text = document.export_to_markdown()
    save_output(file_path, text)

    return {

        "tool": "Docling",

        "file_name": Path(file_path).name,

        "file_type": Path(file_path).suffix.lower()[1:],

        "processing_time": processing_time,

        "page_count": None,

        "text": text

    }