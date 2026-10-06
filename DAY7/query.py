from sentence_transformers import SentenceTransformer
import chromadb, ollama,streamlit as st
st.title("Welcome To My App")
model=SentenceTransformer('all-MiniLM-L6-v2')
file_name="sample.txt"
with open("sample.txt", "r") as file:
    text = file.read()
chunks=[]
chunk_size = 100
chunk_overlap= 20
step = chunk_size - chunk_overlap
for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)
embeddings = model.encode(chunks)
print(embeddings[0])
client = chromadb.Client()
collection = client.get_or_create_collection(name="My_documents")
ids = []
for i in range(len(chunks)):
    ids.append(f"{file_name}_{i}")
collection.add(
    ids = ids,
    documents = chunks,
    embeddings = embeddings.tolist()
)
question = "who founded Nexora Labs?"
question_embedding = model.encode(question)
results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=3
)
retrieved_results = results['documents'][0]
retrieved_ids = results['ids'][0]

# #prompting
context = '\n'.join(retrieved_results)
print(retrieved_results)
print(context)

prompt = f'''
# Answer the question using the context provided below.
# Question : (question)
# Context : (context)
# Answer:
# '''

# Connecting to Local Model
response = ollama.chat(
           model="llama3.2:3b",
           messages=[{
                "role":"user",
                "context":prompt
           }]
 )