from PyPDF2 import PdfReader

from chunker import Chunker

def main():
    reader = PdfReader('concurrency_and_threads.pdf')
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(number_of_pages)
    print(text)

    c = Chunker(chunk_size=500, overlap=50)
    chunks = c.chunk(text)
    print(chunks)

if __name__ == '__main__':
    main()