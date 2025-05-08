from PyPDF2 import PdfReader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import os

# Set up API key
os.environ["OPENAI_API_KEY"] = "openai_key"

# Agents Definitions
class PDFReaderAgent:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def read_pdf(self):
        try:
            if not os.path.exists(self.pdf_path):
                print(f"File {self.pdf_path} does not exist. Please check the file path.")
                return ""

            # Reading the PDF file
            pdfreader = PdfReader(self.pdf_path)
            raw_text = ''
            for page in pdfreader.pages:
                content = page.extract_text()
                if content:
                    raw_text += content
            return raw_text
        except Exception as e:
            print(f"An error occurred while reading the PDF: {e}")
            return ""

class TextSplitterAgent:
    def __init__(self, chunk_size, chunk_overlap):
        self.text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )

    def split_text(self, raw_text):
        return self.text_splitter.split_text(raw_text)

class EmbeddingAgent:
    def __init__(self):
        self.openai_embeddings = OpenAIEmbeddings()
        self.sentence_transformer = SentenceTransformer('all-MiniLM-L6-v2')

    def get_openai_embedding(self, texts):
        return self.openai_embeddings

    def get_sentence_transformer_embedding(self, text):
        return self.sentence_transformer.encode(text)

class DocumentSearchAgent:
    def __init__(self, texts, embeddings, embedding_agent):
        self.faiss_index = FAISS.from_texts(texts, embeddings)
        self.embedding_agent = embedding_agent

    def similarity_search(self, query_embedding):
        docs_with_scores = []
        for doc in self.faiss_index.similarity_search(query):
            doc_embedding = self.embedding_agent.get_sentence_transformer_embedding(doc.page_content)
            score = cosine_similarity([query_embedding], [doc_embedding])[0][0]
            docs_with_scores.append((doc, score))
        return docs_with_scores

# Testing Orchestrator and PDF reading functionality
pdf_path = 'awsgsg-intro.pdf'  # Specify your PDF file path here
orchestrator = PDFReaderAgent(pdf_path=pdf_path)

# Test response generation
query = "How do I make a file public in Amazon S3?"
response = orchestrator.read_pdf()

# Output the response for the query
print(f"Response: {response}")
