import chromadb
import ollama

file_name = "sample.txt"

with open(file_name, "r") as file:
    text = file.read()

chunks = []
chunk_size = 100
chunk_overlap =20
step = chunk_size - chunk_overlap

for i in range(0, len(text), step):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)