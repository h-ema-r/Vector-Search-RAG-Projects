import pymongo 
import requests

# Your MongoDB URI
client = pymongo.MongoClient("<Your MongoDB URI>")
db=client.sample_mflix
collection = db.movies

# items = collection.find().limit(5)

# for item in items:
#     print(item)


# your Hugging Face token
hf_token ="<Your Huggingface token>"
embedding_url ="https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generate_embedding(text: str)-> list[float]:

    response = requests.post(
        embedding_url,
        headers = {"Authorization": f"Bearer {hf_token}"},
        json ={"inputs":text}
    )

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()

# print(generate_embedding("Learning MongoDB is awesome."))

# for doc in collection.find({'plot': {"$exists": True}}).limit(50):
#     doc['plot_embedding_hf']=generate_embedding(doc['plot'])
#     collection.replace_one({'_id': doc['_id']},doc)

# This  code  to try out and use the embeddings.
#to perform vector search in mongodb space using aggregation pipeline

query = "imaginary characters from outer space at war"
results = collection.aggregate([
    {"$vectorSearch":{
        "queryVector": generate_embedding(query),
        "path":"plot_embedding_hf",
        "numCandidates":100,
        "limit":4,
        "index":"PlotSemanticSearch"
    }}
]);

for document in results:
    print(f'Movie Name: {document["title"]}, \nMovie Plot:{document["plot"]}\n')
