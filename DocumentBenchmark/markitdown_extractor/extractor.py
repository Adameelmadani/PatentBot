"""
==========================================================
Document Benchmark
MarkItDown Extractor
==========================================================

Extract text from documents using Microsoft's
MarkItDown library.

Supported formats include:

- PDF
- DOCX
- PPTX
- XLSX
- HTML
- Markdown
- TXT
- ...

The extracted content is converted into Markdown.
"""

from pathlib import Path
import time

from markitdown import MarkItDown

def save_output(file_path, text, extension="txt"):
    """
    Save extracted text into the output folder.
    """

    output_dir = Path("../output/markitdown")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{Path(file_path).stem}.{extension}"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

# ==========================================================
# Extract Document
# ==========================================================

def extract_document(file_path):
    """
    Extract document content using MarkItDown.

    Parameters
    ----------
    file_path : str | Path

    Returns
    -------
    dict
    """

    start = time.time()

    md = MarkItDown()

    result = md.convert(file_path)

    processing_time = round(time.time() - start, 3)

    text = result.text_content
    save_output(file_path, text)

    return {

        "tool": "MarkItDown",

        "file_name": Path(file_path).name,

        "file_type": Path(file_path).suffix.lower()[1:],

        "processing_time": processing_time,

        "page_count": None,

        "text": text

    }