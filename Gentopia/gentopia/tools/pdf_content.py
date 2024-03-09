import PyPDF2

class PDFTextSummarizer:
    def _init_(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        text = ''
        with open(self.pdf_path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            for page in pdf.pages:
                text += page.extract_text() + ' '
        return text

    def basic_summarize(self, text):
        sentences = text.split('.')
        summary = '. '.join(sentences[:3]) + '.'
        return summary

if __name__ == "__main__":
    # Path to your PDF file
    pdf_path = 'NLP-Paper.pdf'
    summarizer = PDFTextSummarizer(pdf_path)
    text = summarizer.extract_text()
    summary = summarizer.basic_summarize(text)

    print("Summary:\n", summary)
