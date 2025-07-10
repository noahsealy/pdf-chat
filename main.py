from PyPDF2 import PdfReader

from chunker import chunk

def main():
    reader = PdfReader('concurrency_and_threads.pdf')
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(number_of_pages)
    print(text)

if __name__ == '__main__':
    main()