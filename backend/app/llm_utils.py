import os
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.schema.document import Document

def answer_question(pdf_text: str, question: str) -> str:
    # Validate input
    if not pdf_text.strip():
        return "Document text is empty."
    if not question.strip():
        return "Question is empty."

    # Split PDF into chunks
    splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    chunks = splitter.split_text(pdf_text)

    if not chunks:
        return "Could not split document into valid chunks."

    # Wrap chunks in Document objects with required 'source' metadata
    documents = [Document(page_content=chunk, metadata={"source": f"chunk_{i}"}) for i, chunk in enumerate(chunks)]

    try:
        embeddings = OllamaEmbeddings(model="llama3")  # Or "mistral" if memory is limited
        vector_store = FAISS.from_documents(documents, embedding=embeddings)
    except Exception as e:
        return f"Error during embedding or vector store creation: {e}"

    try:
        llm = OllamaLLM(model="llama3")  # Or "mistral"
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(),
            return_source_documents=True
        )
        response = qa_chain.invoke({"query": question})
        return response.get("result", "No answer returned.")
    except Exception as e:
        return f"Error during QA processing: {e}"
