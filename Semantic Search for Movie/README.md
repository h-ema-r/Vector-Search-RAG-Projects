# Introduction
In this project "Semantic Search for movies",the mongodb atlas is used to to  create, store embedding  vector of  "plot" variable present in dataset "movie" which is  available in mongodb atlas.
<br>
The Huggingface based model "all-MiniLM-L6-v2" is used.This is a sentence-transformers model.It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.
<br>
The plot embedding is used to perform vector search in mongodb space using aggregation pipelins.
Dotproduct between vectors is used to measure the similarity.
# Packages installed
pip install pymongo
<br>
pip install requests
# Output 
![image](https://github.com/h-ema-r/Vector-Search-RAG-Projects/blob/main/Semantic%20Search%20for%20Movie/output-of-code.png)
