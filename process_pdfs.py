import os
import fitz  # PyMuPDF
import json


def is_probable_heading(span, y_position):
    """
    Heuristic: Combine font size, boldness (flags), and vertical position (Y coordinate).
    Larger font size + boldness + upper page position = more likely a heading.
    """
    font_size = span["size"]
    is_bold = span["flags"] == 20  # Commonly 20 = bold in PyMuPDF
    y_threshold = 300  # Upper part of the page, adjust if needed

    if font_size >= 20 and y_position < y_threshold:
        return "H1"
    elif 16 <= font_size < 20 and (is_bold or y_position < y_threshold):
        return "H2"
    elif 13 <= font_size < 16 and is_bold:
        return "H3"
    else:
        return None


def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get('title', os.path.splitext(os.path.basename(pdf_path))[0])

    headings = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    text_spans = [span for span in line["spans"] if span["text"].strip()]
                    if not text_spans:
                        continue

                    for span in text_spans:
                        text = span["text"].strip()
                        if len(text) < 3:
                            continue  # Skip noise like single letters

                        heading_level = is_probable_heading(span, block["bbox"][1])

                        if heading_level:
                            headings.append({
                                "level": heading_level,
                                "text": text,
                                "page": page_num + 1
                            })

    return {
        "title": title,
        "outline": headings
    }


def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            output_json = extract_outline_from_pdf(pdf_path)

            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output_json, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
