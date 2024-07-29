import json
import os
from openai import OpenAI
import pandas as pd
import numpy as np
from getpass import getpass
import time
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SimpleField, SearchFieldDataType, SearchIndex
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.data.tables import TableServiceClient, TableClient
from azure.core.credentials import AzureNamedKeyCredential

load_dotenv()
account_url = "https://sabarishmnblob.blob.core.windows.net"
default_credential = DefaultAzureCredential()
credential = AzureKeyCredential(str(os.getenv("AZURE_KEY_CREDENTIAL")))
blob_service_client = BlobServiceClient(account_url, credential=default_credential)
search_svc_endpoint = os.getenv("SEARCH_SERVICE_ENDPOINT")
rec_endpoint = os.getenv("RECOGNIZER_ENDPOINT")
rec_key = os.getenv("RECOGNIZER_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
data_account_key = os.getenv("DATA_ACCOUNT_KEY")



def get_embedding(x, engine='text-embedding-ada-002'):
    response = client.embeddings.create(
        input=x,
        model=engine
    )
    return response.data[0].embedding
def writeToBlob(filename):
    blob_client = blob_service_client.get_blob_client(container="mt-intership-us-sabarish", blob=filename)

    print("\nUploading to Azure Storage as blob:\n\t" + filename)

    # Upload the created file
    with open(file=filename, mode="rb") as data:
        blob_client.upload_blob(data, overwrite=True)

def vector_search(query_vector, index_name, top_k=5):
    search_client = SearchClient(endpoint=search_svc_endpoint, index_name=index_name, credential=credential)
    index_client = SearchIndexClient(endpoint=search_svc_endpoint, credential=credential)
    vector_query = VectorizedQuery(vector=query_vector, k_nearest_neighbors=top_k, fields="content_vector",
                                   exhaustive=True)
    results = search_client.search(
        search_text="*",
        vector_queries=[vector_query],
        select=["id", "content"],
        top=top_k,
        filter="invoice_id eq '#000023'"

    )
    return results

def aiSearch(index_name, top_k):
    user_query = input("How can I help you ? ")
    user_query_term_vector = get_embedding(user_query, engine="text-embedding-ada-002")
    results = vector_search(user_query_term_vector,index_name, top_k)
    data_to_search = []
    for result in results:
        print(result['id'])
        print(result['content'])
        data_to_search.append(result['content'])
        # print(f"Score: {result['@search.score']}")
        print("----")
    print(" ##############  ")
    prompt = "Users Question : " + user_query + "Documents provided:"
    for index, value in enumerate(data_to_search, 1):
        prompt += (f"document {index}: \"value of row {index}\" {value}")
    print(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant designed to answer users question based on the documents provided. If you don't find the answer based on the documents provided, please respond you couldn't find any information based on the documents provided."},
            {"role": "user", "content": "" + prompt + ""}
        ]
    )
    print(response.choices[0].message.content)

def generate_sample(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant designed to answer users question based on the data provided. Please dont repeat your responses."},
            {"role": "user", "content": "" + prompt + ""}
        ],
        response_format={ "type": "json_object" }
    )
    return response.choices[0].message.content

def putDataToTable(data, data_storage_name, table_name):
    credential = AzureNamedKeyCredential(data_storage_name, data_account_key)
    table_service = TableServiceClient(endpoint=f"https://{data_storage_name}.table.core.windows.net/",
                                       credential=credential)

    # table_name = "aptitude1"
    # Create the table if it doesn't exist
    table_service.create_table_if_not_exists(table_name)

    # Get a reference to the table
    table_client = table_service.get_table_client(table_name)
    # Your JSON data
    for item in data:
        json_data = {
            "category": item["category"],
            "question": item["question"],
            "options": json.dumps(item['options']) if json.dumps(item['options']) else item['options'],
            "answer": item["answer"],
            "difficulty": item["difficulty"]
        }
        entity = {
            "PartitionKey": json_data["category"],
            "RowKey": str(hash(json_data["question"]))  # Using a hash of the question as a unique identifier
        }
        entity.update(json_data)  # Add the JSON data to the entity
        print(entity)
        table_client.create_entity(entity)
        print("Data inserted successfully.")

def getDataFromTable(data_storage_name, table_name):
    credential = AzureNamedKeyCredential(data_storage_name, data_account_key)
    table_service = TableServiceClient(endpoint=f"https://{data_storage_name}.table.core.windows.net/",
                                       credential=credential)
    # table_service.create_table_if_not_exists(table_name)
    table_client = table_service.get_table_client(table_name)
    entities = table_client.query_entities("")

    return entities
