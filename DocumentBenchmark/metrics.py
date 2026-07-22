"""
==========================================================
Document Benchmark
Metrics Module
==========================================================

Compute simple metrics on extracted text.
"""

import re


# ==========================================================
# Compute metrics
# ==========================================================

def compute_metrics(result):
    """
    Compute metrics from an extraction result.

    Parameters
    ----------
    result : dict

    Returns
    -------
    dict
    """

    text = result["text"]

    lines = text.splitlines()

    words = text.split()

    paragraphs = [x for x in lines if x.strip()]

    markdown_titles = 0

    markdown_lists = 0

    markdown_tables = 0

    for line in lines:

        line = line.strip()

        if line.startswith("#"):
            markdown_titles += 1

        if line.startswith("-") or line.startswith("*"):
            markdown_lists += 1

        if "|" in line:
            markdown_tables += 1

    metrics = {

        "tool": result["tool"],

        "file_name": result["file_name"],

        "processing_time": result["processing_time"],

        "characters": len(text),

        "words": len(words),

        "lines": len(lines),

        "paragraphs": len(paragraphs),

        "titles": markdown_titles,

        "lists": markdown_lists,

        "tables": markdown_tables

    }

    return metrics