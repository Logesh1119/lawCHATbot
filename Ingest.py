import pandas as pd
from langchain_community.document_loaders import DataFrameLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
 
df = pd.read_csv("crime_dataset_india.csv")
print(f"CSV loaded. Total rows: {len(df)}")
 
df["combined_text"] = df.astype(str).apply(lambda row: " | ".join(row.values), axis=1)
 
TEXT_COLUMN = "combined_text"
 
loader = DataFrameLoader(df, page_content_column=TEXT_COLUMN)
documents = loader.load()
print(f"Loaded {len(documents)} combined documents from CSV.")
 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=200)
texts = text_splitter.split_documents(documents)
print(f"Split into {len(texts)} text chunks.")
 
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
 
faiss_db = FAISS.from_documents(texts, embeddings)
print("FAISS vector database created.")
 
faiss_db.save_local("ipc_vector_db")
print("✅ Vector database saved in folder: ipc_vector_db")
