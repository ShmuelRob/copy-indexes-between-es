from dotenv import load_dotenv
load_dotenv()
import os
from elasticsearch import Elasticsearch


def get_clients():
    cloud_es_client = Elasticsearch(
        cloud_id=os.getenv('CLOUD_ES_ID'),
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
        try:
            print(f'copy embedded_fusion_{i}')
            data = cloud.search(
                index=f'stage_embedded_fusion_{i}'
            )
            for hit in data["hits"]["hits"]:
                docker.index(
                    index=f'local_embedded_fusion_{i}',
                    body=hit["_source"]
                )
        except Exception as e:
            print(e)
            continue


copy_data()
print("Reindexing complete.")
