# copy-indexes-from-elastic

This project is a Python application that interacts with Elasticsearch to copy data from a cloud-based Elasticsearch instance to a local Docker-based Elasticsearch instance. The project uses the dotenv library to load environment variables and the elasticsearch library to interact with Elasticsearch.

## Installation
1. Clone the repository: ```git clone https://github.com/ShmuelRob/copy-indexes-between-es.git```
2. Create and activate a virtual environment: ```python -m venv venv source venv/bin/activate```
  On Windows use ```venv\Scripts\activate```  
3. Install the required packages: ```pip install -r requirements.txt```
4. fill the .env file.

## Usage
Run the script to copy data from the cloud Elasticsearch instance to the local Docker-based Elasticsearch instance: ```python app/src/copy_indexes.py```

