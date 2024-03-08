import PyPDF2

def extract_text(pdf_path):
    """Extract text from each page of the PDF."""
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text() + ' '
    return text

def basic_summarize(text):
    """Generate a basic summary of the given text."""
    # Perform summarization logic here
    # For example, you can split the text into sentences and return the first few sentences as a summary
    sentences = text.split('.')
    summary = '. '.join(sentences[:3])  # Return the first three sentences as a basic summary
    return summary

# Path to your PDF file
pdf_path = 'NLP-Paper.pdf'
text = extract_text(pdf_path)
summary = basic_summarize(text)

print("Summary:\n", summary)



