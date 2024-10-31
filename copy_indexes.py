from dotenv import load_dotenv
load_dotenv()
import os
from elasticsearch import Elasticsearch, helpers


def get_clients():
    cloud_es_client = Elasticsearch(
        hosts=[{'host': os.getenv('CLOUD_ES_HOST'), 'port': int(os.getenv('CLOUD_ES_PORT')), 'scheme': os.getenv('CLOUD_ES_SCHEME')}],
        api_key=os.getenv('CLOUD_ES_API_KEY')
    )
    print("cloud_es_client connected")
    docker_es_client = Elasticsearch(
        os.getenv("DOCKER_ES_SCHEME") + "://" + os.getenv("DOCKER_ES_HOST") + ":" + os.getenv("DOCKER_ES_PORT")
    )
    print("docker_es_client connected")
    return cloud_es_client, docker_es_client


def copy_data():
    cloud, docker = get_clients()
    for i in range(0, 23):
        print(f'copy embedded_fusion_{i}')
        data = cloud.search(
            index=f'embedded_fusion_{i}'
        )
        for hit in data["hits"]["hits"]:
            docker.index(
                index=f'embedded_fusion_{i}',
                body=hit["_source"]
            )


copy_data()
print("Reindexing complete.")
