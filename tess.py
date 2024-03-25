from pdfquery import PDFQuery

def extract_text_from_region(pdf, bbox):
    region = pdf.pq(':in_bbox("{},{},{},{}")'.format(*bbox))
    return region.text()

def extract_text_after_pattern(pdf, pattern, page_index=0):
    pattern_position = pdf.pq(':contains("{}")'.format(pattern)).bbox()

    if pattern_position:
        x, y = pattern_position[2], pattern_position[3]
        text_after_pattern = pdf.extract([
            ('with_parent', 'LTPage[page_index="{}"]'.format(page_index)),
            ('text', ':in_bbox("{},{},{},{}")'.format(x, y, 600, 700))
        ])
        return ' '.join(text_after_pattern).strip()
    else:
        return ''

def extract_article_information(pdf_path, page_index=0):
    pdf = PDFQuery(pdf_path)
    pdf.load()

    # Extract title
    title = extract_text_from_region(pdf, bbox=(0, 500, 600, 700))

    # Extract authors
    authors = extract_text_from_region(pdf, bbox=(0, 450, 600, 500))

    # Extract abstract
    abstract = extract_text_from_region(pdf, bbox=(0, 300, 600, 450))

    # Extract keywords (assuming keywords are present on the first page)
    keywords = extract_text_from_region(pdf, bbox=(0, 0, 600, 50))

    # Extract references (assuming references start with "References")
    references = extract_text_after_pattern(pdf, pattern="References", page_index=page_index)

    # Extract date (assuming date is in a specific region)
    date = extract_text_from_region(pdf, bbox=(500, 0, 600, 50))

    # Clean up extracted text
    title = title.strip() if title else ''
    authors = authors.strip() if authors else ''
    abstract = abstract.strip() if abstract else ''
    keywords = keywords.strip() if keywords else ''
    references = references.strip() if references else ''
    date = date.strip() if date else ''

    print("Title:", title)
    print("Authors:", authors)
    print("Abstract:", abstract)
    print("Keywords:", keywords)
    print("References:", references)
    print("Date:", date)

    return {
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "keywords": keywords,
        "references": references,
        "date": date,
    }

# Example usage:
pdf_path = 'C:\\Users\\dell\\PycharmProjects\\pyfad\\publications-08-00038.pdf'
result = extract_article_information(pdf_path)
print(result)
