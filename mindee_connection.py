import os
from dotenv import load_dotenv
from mindee import Client, AsyncPredictResponse, product

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

MINDEE_API_KEY = os.getenv('MINDEE_API_KEY')

mindee_client = Client(api_key=MINDEE_API_KEY)

my_endpoint = mindee_client.create_endpoint(
    account_name="matiasbarbieri",
    endpoint_name="new_christmas",
    version="1"
)

def process_file(file_path):
    input_doc = mindee_client.source_from_path(file_path)

    result: AsyncPredictResponse = mindee_client.enqueue_and_parse(
        product.GeneratedV1,
        input_doc,
        endpoint=my_endpoint
    )

    return result.document.inference.prediction.fields
