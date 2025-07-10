class Chunker:
    def __init__(self, chunk_size=500, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def chunk(self, text:str) -> list[str]:
        words = text.split()
        chunks = []

        track = 0
        chunk = ''
        for i in range(len(words)):
            track += 1
            chunk += words[i]
            if track == (self.chunk_size + self.overlap):
                if i != len(words):
                    i -= self.overlap
                chunks.append(chunk)
                track = 0
                chunk = ''

        return chunks