import fitz  # belongs to PyMuPDF

def extract_pdf_viewport(pdf_origin, txt_target, margins, page_range):
    
    # Open the PDF
    document = fitz.open(pdf_origin)

    extracted_text = ""

    # Define the margins
    top_margin = margins[0]
    right_margin = margins[1]
    bottom_margin = margins[2]
    left_margin = margins[3]

    # Check if the page range is valid
    if page_range[0] < 0 or page_range[1] > len(document):
        raise ValueError("Invalid page range")

    for page_num in range(page_range[0]-1, page_range[1]):
        # Get the page
        page = document.load_page(page_num)
        # Define the dimensions of the entire page
        rect = page.rect

        # Define your viewport excluding margins
        viewport = fitz.Rect(left_margin, top_margin, rect.width - right_margin, rect.height - bottom_margin)

        # Extract text within the viewport
        text = page.get_text("text", clip=viewport)

        # Remove line breaks and syllable breaks
        text = text.replace("-\n", "").replace("\n", " ")

        # Add the extracted text to the output string
        extracted_text += text

    document.close()

    with open(txt_target, "w") as f:
        f.write(extracted_text)

    return extracted_text

