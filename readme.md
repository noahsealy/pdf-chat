Project Flow

1. Extract input PDF with pdfreader (PyPDF2)
2. Chunk the extracted text
3. Embedding the chunks into vectors (OpenAI)
4. Store in postgresql (pgvector)
5. Query
6. Embed Query + Similarity Search
7. Send relevant chunks to LLM
8. Answer!