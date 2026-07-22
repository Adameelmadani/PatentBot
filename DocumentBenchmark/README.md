# Document Extraction Benchmark for Patent Search System

> A comparative evaluation of document extraction tools to identify the optimal solution for a RAG-based patent search pipeline.

---

## 📋 Table of Contents
- [1. Objective](#1-objective)
- [2. Approaches Evaluated](#2-approaches-evaluated)
- [3. Benchmark Architecture](#3-benchmark-architecture)
- [4. Test Documents](#4-test-documents)
- [5. Evaluation Metrics](#5-evaluation-metrics)
- [6. Results](#6-results)
- [7. Overall Comparison](#7-overall-comparison)
- [8. Decision & Next Steps](#8-decision--next-steps)
- [9. Improvements](#9-improvements)

---

## 1. Objective

Before building the RAG pipeline, we needed to determine the most suitable document extraction tool for processing technical documents submitted by users.

**Key evaluation criteria:**
- ✅ Extraction quality
- ✅ Structural preservation
- ✅ Execution speed
- ✅ Resource consumption
- ✅ Integration ease

**Supported document formats:**
- PDF
- DOCX
- PPTX
- TXT

---

## 2. Approaches Evaluated

Three independent extraction approaches were implemented and tested.

### Approach 1: Classic Parsers

**Libraries used:**
- `PyMuPDF` (PDF)
- `python-docx` (DOCX)
- `python-pptx` (PPTX)

**Principle:** Each document type is processed by its specialized library.

**Goal:** Fast plain-text extraction.

---

### Approach 2: MarkItDown

**Library:** Microsoft's MarkItDown

**Principle:** Automatic conversion of all documents to Markdown format.

**Benefits:**
- Preserves headings
- Maintains lists
- Converts tables
- Keeps logical structure
- Directly usable in RAG pipeline

---

### Approach 3: Docling

**Library:** IBM's Docling

**Features:**
- Built-in OCR
- Layout understanding
- Table detection
- Figure detection
- Structured Markdown generation

**Goal:** Test an advanced solution for complex documents.

---

## 3. Benchmark Architecture

Each approach has its own independent module:

```
DocumentBenchmark/
├── input/
├── classic_parser/
├── markitdown/
├── docling/
├── output/
│   ├── classic/
│   ├── markitdown/
│   └── docling/
├── compare.py
└── metrics.py
```

**Workflow:** Each extractor:
1. Reads documents from `input/`
2. Extracts text
3. Displays statistics
4. Saves results to `output/`

---

## 4. Test Documents

The benchmark used real-world documents:

| Document | Type | Description |
|----------|------|-------------|
| Presentation | PPTX | Standard business presentation |
| Word Document | DOCX | Technical report |
| Patent PDF | PDF | Standard patent document |
| Large Patent PDF | PDF | Heavy, complex patent |

---

## 5. Evaluation Metrics

For each document, we measured:

| Metric | Description |
|--------|-------------|
| ⏱️ Execution Time | Processing duration |
| 📝 Character Count | Total characters extracted |
| 📊 Word Count | Total words extracted |
| 📄 Line Count | Number of lines |
| 📑 Paragraph Count | Number of paragraphs |
| #️⃣ Headings Detected | Structure preservation |
| 📋 Lists Detected | Structure preservation |
| 📊 Tables Detected | Structure preservation |

Extracted text is saved for visual comparison with originals.

---

## 6. Results

### Classic Parser

| Pros | Cons |
|------|------|
| ⚡ Extremely fast (< 0.2s) | ❌ No structure preservation |
| 🛡️ Very stable | ❌ No heading detection |
| 💾 Low memory usage | ❌ Poor table handling |
| ✅ Reliable text extraction | ❌ Plain text only |

---

### MarkItDown

| Pros | Cons |
|------|------|
| ✅ Excellent overall quality | ⚠️ No built-in OCR |
| ✅ Great structure preservation | |
| ✅ Proper heading detection | |
| ✅ Lists preserved | |
| ✅ Tables converted | |
| ✅ Markdown output ready | |

**Performance:**
| Document | Time |
|----------|------|
| DOCX | ~0.5s |
| PPTX | ~0.6s |
| PDF | 3-6s |

**Conclusion:** Excellent balance between quality and performance.

---

### Docling

| Pros | Cons |
|------|------|
| ✅ Best structural understanding | 🐌 **Very slow** (~210s per PDF) |
| ✅ Built-in OCR | 💥 Memory issues (`std::bad_alloc`) |
| ✅ Excellent table detection | ⚠️ Unstable on large documents |
| ✅ High-quality Markdown output | |

**Performance:**
- First PDF: ~210 seconds
- Second PDF: Failed (std::bad_alloc)

**Cause:** High memory consumption from AI models.

---

## 7. Overall Comparison

| Criteria | Classic Parser | MarkItDown | Docling |
|----------|:-------------:|:----------:|:-------:|
| ⚡ Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ | ⭐☆☆☆☆ |
| 🏗️ Structure | ⭐☆☆☆☆ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 📊 Tables | ⭐☆☆☆☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐⭐ |
| 💾 Memory | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ | ⭐☆☆☆☆ |
| 🛡️ Robustness | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐☆☆☆ |
| 🔍 OCR | ❌ | ❌ | ✅ |
| 📝 Markdown Output | ❌ | ✅ | ✅ |

---

## 8. Decision & Next Steps

### Current Decision

| Tool | Status | Rationale |
|------|--------|-----------|
| **Classic Parser** | ⚡ Backup | Good for simple documents needing fast extraction |
| **MarkItDown** | 🏆 **Primary Choice** | Best compromise: quality + speed + stability + integration |
| **Docling** | 🔧 Fallback | Reserved for scanned/complex PDFs only |

**Why MarkItDown?**
- ✅ Excellent structural preservation
- ✅ Fast enough for production
- ✅ Stable and memory-efficient
- ✅ Markdown output ready for RAG
- ✅ Easy integration

### Next Phase: Preprocessing Pipeline

```
1. 📤 Document Upload
2. 📝 Text Extraction (MarkItDown)
3. 🔍 Scanned Document Detection
4. 🖼️ OCR (if needed)
5. 🧹 Text Cleaning
6. 🏷️ Automatic Keyword Extraction
7. ✏️ User Keyword Validation
8. 🔗 Search Query Construction
9. 🌐 Patent Platform Search
10. 🧠 RAG Pipeline & Vectorization
```

---

## 9. Improvements

The benchmark was enhanced with automatic result saving:

```
output/
├── classic/
├── markitdown/
└── docling/
```

This enables:
- 📋 Manual comparison with original documents
- 🔄 Cross-tool comparison
- 🔍 Qualitative analysis
- 📊 Justification for final decision

---

## 📊 Conclusion

This benchmark objectively compared three document extraction approaches on real-world patent documents. **MarkItDown** emerged as the optimal choice, offering the best balance of:

- 🎯 Extraction quality
- 🏗️ Structure preservation
- ⚡ Performance
- 💾 Resource efficiency
- 🔧 Integration simplicity

This makes it the preferred solution for the patent search system's RAG pipeline development.

---

## 🛠️ Technologies Used

| Component | Technology |
|-----------|------------|
| PDF Parsing | PyMuPDF |
| DOCX Parsing | python-docx |
| PPTX Parsing | python-pptx |
| Universal Converter | MarkItDown (Microsoft) |
| Advanced Extraction | Docling (IBM) |
| Language | Python 3.x |

---



