#Intoduction
<br>
In This project Semantic Search for movies, 
I have used mongodb atlas to  create, store embedding  vector of  "plot" variable present in dataset "movie" which is  available in mongodb atlas.
I have used Huggingface based model "all-MiniLM-L6-v2".This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.
The plot embedding is used to perform vector search in mongodb space using aggregation pipelins.
# Packages installed
pip install pymongo
<br>
pip install requests
# Output 
![image](https://github.com/h-ema-r/Vector-Search-RAG-Projects/blob/main/Semantic%20Search%20for%20Movie/output-of-code.png)
