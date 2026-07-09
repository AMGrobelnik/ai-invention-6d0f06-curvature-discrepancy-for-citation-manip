#!/usr/bin/env python3
"""
Convert PDF pages to PNG images for visual review.
"""
import sys
import os

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF not installed. Install with: pip install pymupdf")
    sys.exit(1)

def pdf_to_images(pdf_path, output_dir, dpi=150):
    """
    Convert PDF pages to PNG images.

    Args:
        pdf_path: Path to PDF file
        output_dir: Directory to save images
        dpi: Resolution in DPI (150 is good for review)
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Open PDF
    doc = fitz.open(pdf_path)
    print(f"PDF has {len(doc)} pages")

    # Convert each page
    for page_num in range(len(doc)):
        page = doc[page_num]

        # Calculate zoom factor from DPI
        # 72 DPI is the base PDF resolution
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)

        # Render page to pixmap
        pix = page.get_pixmap(matrix=mat)

        # Save as PNG
        output_path = os.path.join(output_dir, f"page_{page_num + 1:02d}.png")
        pix.save(output_path)
        print(f"Saved page {page_num + 1} to {output_path}")

    doc.close()
    print(f"\nConverted {len(doc)} pages to PNG images at {dpi} DPI")

if __name__ == "__main__":
    pdf_path = "paper.pdf"
    output_dir = "page_images"

    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]

    pdf_to_images(pdf_path, output_dir)
