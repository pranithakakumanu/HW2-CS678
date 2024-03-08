import PyPDF2
from collections import Counter
import re

def extract_text(pdf_path):
    """Extract text from each page of the PDF."""
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text() + ' '
    return text

def basic_summarize(text, summary_length=100):
    """Summarize the text into a paragraph of about summary_length words."""
    # Simplistic approach: split the text into words, then take the most common words.
    words = re.findall(r'\w+', text.lower())  # Extract words
    word_counts = Counter(words)
    common_words = [word for word, count in word_counts.most_common(20)]  # Adjust as needed
    
    # Split text into sentences
    sentences = re.split(r' [\.\?!][\'"\)\]] *', text)
    scored_sentences = [(sum(word in sentence.lower() for word in common_words), sentence) for sentence in sentences]
    scored_sentences.sort(reverse=True)
    
    # Join top sentences until reaching summary_length
    summary_sentences = []
    total_words = 0
    for score, sentence in scored_sentences:
        if total_words < summary_length:
            summary_sentences.append(sentence)
            total_words += len(sentence.split())
        else:
            break
    
    return ' '.join(summary_sentences)

# Path to your PDF file
pdf_path = 'NLP-Paper.pdf'
text = extract_text(pdf_path)
summary = basic_summarize(text)

print("Summary:\n", summary) 
