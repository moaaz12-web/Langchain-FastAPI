from dotenv import load_dotenv
import os
from langchain.memory import VectorStoreRetrieverMemory
from langchain_community.vectorstores.redis import Redis
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_core.runnables import ConfigurableField

load_dotenv()

redis_url = os.getenv("REDIS_URL")
openai_key = os.getenv("OPENAI_API_KEY")
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")


embedding_fn = OpenAIEmbeddings(openai_api_key=openai_key)


#! Alternatively, can use Hugging Face embeddings if you don't have one
# modelPath = "HuggingFaceH4/zephyr-7b-beta"
# model_kwargs = {'device':'cpu'}
# encode_kwargs = {'normalize_embeddings':False}
# embedding_fn = HuggingFaceEmbeddings(
#   model_name = modelPath,  
#   model_kwargs = model_kwargs,
#   encode_kwargs=encode_kwargs
# )

schema = {'text': [{'name': 'content',
   'weight': 1,
   'no_stem': False,
   'withsuffixtrie': False,
   'no_index': False,
   'sortable': False}],
 'vector': [{'name': 'content_vector',
   'dims': 1536,
   'algorithm': 'FLAT',
   'datatype': 'FLOAT32',
   'distance_metric': 'COSINE'}]}

def vectorstore_as_memory(username):
    try:
        new_rds = Redis.from_existing_index(
            embedding=embedding_fn,
            index_name=username,
            redis_url=redis_url,
            # schema=rds.schema,
            schema=schema,
        )

        retriever = new_rds.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        memory = VectorStoreRetrieverMemory(retriever=retriever)
        return memory

    except ValueError:
        rds = Redis.from_texts(
            texts=["Hi there"],
            embedding=embedding_fn,
            redis_url=redis_url,
            index_name=username
        )

        retriever = rds.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        memory = VectorStoreRetrieverMemory(retriever=retriever)
        return memory

